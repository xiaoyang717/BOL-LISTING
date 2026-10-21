# BOL 产品标题描述审查批次 2026-08-10

## 目标
用户持续提供 BOL 荷兰站产品标题和描述，SHOKO 负责审查、评分、修正并输出符合 BOL 规则的 HTML 描述。

## 本批次审查产品清单

1. **Airfryer 烤串架 28 签 + 圆形 24 签变体**
   - 标题：Airfryer Grillrek - BBQ Spieshouder - Verticaal Grillen - 28 roestvrijstalen spiesen – Verticaal & opvouwbaar – Geschikt voor 4,5L+
   - 主要修正：
     - 删除 `360°` / `perfect resultaat` / `gaat jaren mee` / `in 2 minuten schoon` 等绝对化/无依据宣称
     - 删除 `Voedselveilig`、`hittebestendig tot 260°C`、`Rookvrij en gezond`、`Ook als dehydrator` 等需检测或功能依据的表述
     - 英制 `6 inch` 转公制 `ca. 15,2 cm`
     - 标题加 `Incl. Uitneemtang` 作为差异化卖点
     - 补 `<h3>` / `<strong>` / `<ul>` 标准格式
   - 圆形变体：24 签 / Ø16,3 x 10 cm，结构照搬，仅改数量和尺寸

2. **床单固定夹 4 件装**
   - 标题：Bedlakenhouders voor hoeken – 4 stuks met stevige kliksluiting – eenmalig monteren onder matras – geschikt voor alle maten
   - 主要修正：
     - `geschikt voor alle maten` → `Voor De Meeste Matrasmaten`
     - 删除 `tot het verleden behoren` 夸张表达
     - 删除 `de hele nacht strak` 效果承诺
     - 加 `Controleer de afmetingen voor aanschaf` 免责声明
     - 补 `<h3>` / `<strong>` / `<ul>` 标准格式

## 关键修正模式

| 修正类型 | 代表 |
|---------|------|
| 绝对化宣称 → 中性化 | alle maten → meeste matrasmaten |
| 效果承诺 → 功能描述 | perfect resultaat → kan rondom circuleren |
| 英制转公制 | 6 inch → ca. 15,2 cm |
| 无依据宣称删除 | voedselveilig / 260°C / rookvrij en gezond |
| HTML格式补全 | h3/strong/ul |

## BOL属性配置经验新增

- Airfryer 烤串架：
  - 类目：Koken & Bakken / Keukenaccessoires / Airfryer accessoires
  - Materiaal: Roestvrij staal type 304
  - 变体1 方形：Afmetingen 15,5 x 15,5 x 10 cm / 28 spiesen
  - 变体2 圆形：Afmetingen Ø16,3 x 10 cm / 24 spiesen
  - Kenmerken: Verticaal hangend, Opvouwbaar, Incl. uitneemtang, Vaatwasmachinebestendig（已确认）

- 床单固定夹：
  - 类目：Wonen / Slaapkamer / Beddengoedaccessoires / Bedlakenhouders
  - Materiaal: Kunststof
  - Aantal: 4 stuks
  - Kenmerken: Met kliksluiting, Eenmalige installatie, Onder matras
