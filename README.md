# BOL-LISTING

> BOL.com 荷兰站商品 Listing 审核与优化工作空间

本项目用于管理 BOL.com 荷兰站（bol.com）商品 Listing 的合规审核、标题评分、荷兰语本地化重写以及可直接上架的 HTML 描述生成。由 AI 运营分析师（SHOKO）协助完成，所有产出均基于已确认的产品事实，遵循 BOL 平台规则与欧盟合规要求。

---

## 项目结构

```
BOL-LISTING/
├── README.md                          # 项目说明（本文件）
├── AGENTS.md                          # 工作空间与 Agent 框架说明
├── SOUL.md                            # Agent 角色定位：跨境电商运营分析师
├── IDENTITY.md                        # Agent 身份信息
├── USER.md                            # 用户信息模板
├── TOOLS.md                           # 工具本地配置模板
├── HEARTBEAT.md                       # 定期任务模板
├── BOL-跨境产品需求清单.md              # 选品方向、痛点分析与行动清单
├── bol-review-batch_*.md              # 按批次归档的 Listing 审核记录
├── task-summary_*.md                  # 单品任务总结
├── zonvanger-review_*.md              # 特定产品审核
├── airco-raamafdichting_*.md         # 特定产品审核
├── Nachtlampje标题词频分析_*.md        # 夜灯品类标题词频分析
├── Nachtlampje系列Listing优化审核_*.md # 夜灯系列优化审核
├── analyze_nightlight_titles*.py      # 标题词频分析脚本（Python）
├── outputs/                           # 已生成的 BOL HTML 描述成品
│   ├── *.html
└── .gitignore
```

> **注意：** `MEMORY.md`、`memory/`、`.workbuddy/`、`sessions/` 等包含个人上下文与工作日志的文件已在 `.gitignore` 中排除，不会提交到仓库。

---

## 核心工作流程

### 1. 产品信息输入

用户提供产品的标题、描述、规格、包装清单等原始信息（荷兰语或英文），以及中文处理说明。

### 2. 合规审核

对标题与描述逐项审查，识别并处理以下高风险宣称：

| 风险类别 | 示例 | 处理方式 |
|---------|------|---------|
| 耐久性宣称 | `duurzaam`、`langdurig gebruik`、`bestand tegen intensief gebruik` | 删除或改为客观材质描述 |
| 安全/无毒宣称 | `veilig`、`niet-giftig`、`BPA-vrij`、`FDA-goedgekeurd` | 无检测依据时删除 |
| 医疗/健康效果 | `artritis`、`pijn verlichten`、`gezonde houding` | 删除 |
| 效果保证 | `perfect`、`ideaal`、`voorkomt`、`altijd` | 改为中性描述 |
| 绝对化适配 | `geschikt voor alle`、`past op vrijwel elke` | 改为 `geschikt voor` + 核对提示 |
| 防水/耐候 | `waterdicht`、`UV-bestendig`、`weerbestendig` | 无 IP 等级或测试依据时删除 |
| 品质主观词 | `hoogwaardig`、`premium`、`topkwaliteit` | 删除 |

### 3. 标题评分与优化

对原标题进行 10 分制评分，输出优化后的荷兰语标题。评分维度包括：
- 关键词覆盖（产品类型、数量、尺寸、颜色、用途）
- 荷兰语表达自然度与语序
- BOL 类目词匹配
- 合规性

### 4. HTML 描述生成

输出可直接复制到 BOL 后台的完整 HTML，仅使用 BOL 支持的标签：

```html
<h3>Productomschrijving</h3>
<p>产品概述段落。</p>

<h3>Belangrijkste kenmerken</h3>
<ul>
<li><strong>卖点标题：</strong> 客观事实描述。</li>
</ul>

<h3>Specificaties</h3>
<ul>
<li>属性：值</li>
</ul>

<h3>Inhoud van de verpakking</h3>
<ul>
<li>1x 产品名称</li>
</ul>
```

**BOL 支持的 HTML 标签：** `h3`、`strong`、普通文本段落、`ul`/`li`。不使用复杂 HTML。

### 5. 数量与规格一致性核对

每次输出前核对标题、描述、规格表与包装清单之间的数量、尺寸、颜色是否一致。例如：标题写 19 件，包装清单各件相加必须等于 19。

---

## 合规规则要点

1. **只使用已确认的事实** — 不编造产品参数，不凭空生成产品。
2. **公制优先** — 英制单位换算为公制；除非实物刻度确实为英寸，此时双单位并注明。
3. **材质必须真实** — 如 `eikenhout`（橡木）曾改为实际的 `rubberhout`（橡胶木）；`engineered wood` 改为 `samengestelde houtplaat`。
4. **适配产品提醒核对尺寸** — 凡涉及适配其他产品（如粉碗、门框、镜面），必须提示购买前核对实际尺寸。
5. **变体由变体系统承载** — 其他尺寸和颜色不在单品描述中列举。
6. **户外使用保守表述** — 无耐候测试依据时，写 `binnen en beschut buitengebruik`（室内及有遮挡的户外），不写 `waterdicht`/`weerbestendig`。
7. **洗护说明以洗标为准** — 不推定洗护方式，需与厂家说明一致。
8. **品牌名兼容性声明有风险** — 保守版本删除品牌兼容性声明。

---

## 标题词频分析脚本

`analyze_nightlight_titles.py` 系列脚本用于分析 BOL 荷兰站夜灯品类的竞品标题，提取高频关键词，辅助标题优化。

### 运行方式

```bash
python analyze_nightlight_titles.py
```

> 脚本内置了竞品标题数据，无需额外输入文件。需要 Python 3 环境。

---

## 在另一台电脑上使用

1. **克隆仓库：**

   ```bash
   git clone https://github.com/xiaoyang717/BOL-LISTING.git
   cd BOL-LISTING
   ```

2. **浏览审核记录：** 查看 `bol-review-batch_*.md` 和 `task-summary_*.md` 了解已完成产品的审核过程与结论。

3. **使用 HTML 成品：** `outputs/` 目录下的 `.html` 文件可直接复制到 BOL 后台的描述字段。

4. **运行分析脚本：** 安装 Python 3 后可直接运行标题词频分析脚本。

5. **参考合规规则：** 本 README 的「合规规则要点」章节总结了 Listing 审核的核心规则，可直接用于新产品审核。

---

## 已审核产品类别（部分）

- 窗帘、纱门、收纳用品、清洁用品、工具
- 宠物用品（鸟玩具、宠物碗、狗服）
- 厨房用品（摩卡壶、咖啡配件、定时器、沙漏）
- 旅行用品（颈枕）
- 空气炸锅配件
- 文具、日程本、白板笔
- 节日装饰（圣诞蝴蝶结、枫叶藤、雪松藤、雪松装饰）
- 美容个护（去角质手套、腿套）
- 家居用品（鞋架、门挂、沙发罩、挡风条）
- 汽车用品（盲区镜）
- 体育训练用品（足球训练套装、敏捷锥）

---

## 版本说明

- 本仓库仅保存业务产出（审核记录、需求清单、分析脚本、HTML 成品）。
- 个人记忆与工作日志不纳入版本控制。
- 如需新增产品审核，参考已有批次文件的格式创建新的审核记录。

---

*本项目基于 BOL.com 荷兰站运营实践整理，合规规则需结合平台政策更新与欧盟法规变化持续校准。*
