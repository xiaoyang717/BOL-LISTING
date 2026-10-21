# BOL 产品标题描述审查批次 2026-08-06

## 目标
用户持续提供 BOL 荷兰站产品标题和描述，SHOKO 负责审查、评分、修正并输出符合 BOL 规则的 HTML 描述。

## 本批次审查产品清单

1. **厨房水槽沥水架（In-Sink dish rack）**
   - 标题：In-Sink afdruiprek van roestvrij staal – Compact formaat – 8 kopbeugels – Afneembare bestekhouder – Antislip voetjes
   - 主要修正：
     - `In-Sink` 英文改 `Voor In De Gootsteen`
     - 标题补尺寸 `33x37x13,5 cm`
     - 删比较级宣称 `sterker en duurzamer dan ijzeren varianten`
     - 删除颜色选择引导 `Kies uit zwart of wit`（BOL变体系统管理）
     - 补 `<h3>` / `<strong>` / `<ul>` 标准格式

## 关键修正模式

| 修正类型 | 代表 |
|---------|------|
| Denglish→荷兰语 | In-Sink → Voor in de gootsteen |
| 删无依据比较宣称 | sterker en duurzamer dan ijzeren |
| 颜色引导删除 | Kies uit zwart of wit → 由BOL变体管理 |
| HTML格式补全 | h3/strong/ul |

## BOL属性配置经验新增

- 水槽沥水架类目：Wonen/Keuken/Keukenaccessoires/Afdruiprekken
- Materiaal: Roestvrij staal (RVS) + siliconen
- Afmetingen: 33,3 x 36,6 x 13,5 cm
- Geschikt voor: Standaard dubbele spoelbakken ca. 35,5 x 40,6 cm
- Kenmerken: In de gootsteen, 8 kopbeugels, Afneembare bestekhouder, Antislip voetjes
