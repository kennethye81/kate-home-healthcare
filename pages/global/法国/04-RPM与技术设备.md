---
tags: [国家, 法国, RPM, 技术设备]
created: 2026-07-04
updated: 2026-07-05
aliases: [法国 RPM, 法国 远程监测]
---

# 法国 — RPM 与技术设备

## 一、法国远程医疗（Télémédecine）市场概况

法国远程医疗生态系统在近十年经历了显著扩张。与德国或美国不同，法国 HAD（Hospitalisation à Domicile）体系的远程监测渗透率**相对较低**——历史上以人工巡诊为主——但近年来政策推动和技术采纳正在加速。

### 1.1 市场规模与增长

- 法国数字健康市场（含远程医疗、eHealth、mHealth）2024 年估值约 **69 亿欧元**，预计 2024–2030 年以约 **11% CAGR** 增长（ResearchAndMarkets 估计）。
- **Télémédecine**（远程医疗）是增长最快的子领域之一，2024 年市场规模约 **4.5 亿欧元**。
- 2020 年 COVID-19 疫情后，法国远程咨询（Téléconsultation）数量从 2019 年的约 **60 万次/年** 飙升至 2020 年的 **2,000 万次/年**，此后稳定在约 **1,200–1,500 万次/年**（Assurance Maladie 数据）。
- **Télésurveillance médicale**（远程患者监测）自 2023 年起纳入法国法定医保（Assurance Maladie）的 **标准报销框架**（ETAPES 计划扩展）。

> **来源：** ResearchAndMarkets, "France Digital Health Market Report 2024"; Assurance Maladie, "Téléconsultation: chiffres clés 2023–2024"

### 1.2 HAD 中的技术需求

法国 HAD 的法定技术要求由《公共卫生法典》（CSP）Articles **D. 6124-194 à D. 6124-201** 规定：

| 技术要求 | 内容 |
|---------|------|
| **24/7 远程通信** | HAD 机构必须建立远程通信系统确保患者与医疗团队 24 小时联络 |
| **医疗项目** | 必须覆盖特定的照护领域包括姑息治疗、复杂伤口、呼吸辅助、疼痛管理等 |
| **药物管理** | 与 PUI（药房）合作为患者提供药物配送和管理 |
| **感染控制** | 必须建立居家感染控制和质量安全体系 |
| **认证** | 每 4 年接受 HAS（Haute Autorité de Santé）认证，标准等同传统医院 |

法国 HAD 以**高触达、低技术**模式为特征——强调护士每日上门巡诊（1–3 次/日），而非依赖远程监测设备。这是法国 HAD 与美国 HaH（大量使用 RPM + AI 风险预测）的关键差异。

> **来源：** Legifrance, CSP Articles D. 6124-194 à D. 6124-201; FNEHAD, "Hospital Care at Home in France"

## 二、主要 RPM 与医疗技术供应商

### 2.1 Fondation Santé Service

- 法国 HAD 市场的领导者，日服务 **2,000+ 患者**。
- 覆盖肿瘤、姑息、复杂伤口、康复、围产期、老年医学等全部主要 GHT（同质费率组）类别。
- 2024 年 5 月收购 Clariane（前 Korian）的 HAD 业务，进一步巩固市场主导地位。
- 使用 DMP（Dossier Médical Partagé，共享医疗档案）作为与医院和社区医师的数据交换平台。

### 2.2 AP-HP HAD（巴黎公立医院系统）

- 全球历史最悠久的 HAD 机构（1957 年创立）。
- 巴黎大区主导服务商，服务覆盖肿瘤、姑息、产后护理等。
- 依托 AP-HP 的医院信息系统（ORBIS / CGM）进行数据管理，与 PMSI-HAD 数据库对接。

### 2.3 Orange Healthcare / La Poste Santé

- Orange（法国电信巨头）通过子公司 **Orange Healthcare** 进入远程医疗市场，提供 **Télésurveillance** 平台。
- 与法国多家 HAD 机构合作试点远程监测项目（如心衰和 COPD 远程随访）。
- La Poste（法国邮政）旗下 **La Poste Santé** 推出 **Veiller sur mes parents** 等远程照护服务，但尚未大规模进入 HAD 市场。

### 2.4 Withings (Nokia Health)

- 法国本土 RPM 硬件制造商（总部 Issy-les-Moulineaux），以智能体重秤、血压计、体温计闻名。
- 产品在欧洲 CE 认证体系下广泛用于慢性病家庭管理，但非 HAD 专用设备。
- 2023 年推出 **BPM Connect Pro**（医用级血压仪）和 **ScanWatch**（混合智能手表），面向远程患者监测场景。

### 2.5 Doctolib

- 法国最大的远程医疗平台（1,200 万月活用户），主营 Téléconsultation（视频问诊）。
- 2023 年收购 **Monsu**（远程护理排班 SaaS），开始渗透居家护理市场。
- 与 HAD 机构的 EHR 整合有限，但正在通过 **Doctolib Cabinet** 连接社区医师与 HAD 协调团队。

### 2.6 Dedalus (法国分部)

- 意大利医疗 IT 巨头，法国分部提供 **Dedalus HAD** 模块，专门用于 HAD 机构的患者管理、用药追踪和 PMSI 数据上报。
- 这是法国 HAD 机构最广泛使用的专业信息系统之一，直接对接 ATIH 的 PMSI-HAD 数据库。

> **来源：** FNEHAD 会员目录 2024; Dedalus France HAD Solutions; Doctolib 2024 年报; Withings 官网

## 三、技术标准与互操作性

### 3.1 DMP（Dossier Médical Partagé）

- 法国国家级共享医疗档案，含 HAD 患者的摘要信息。
- HAD 机构与社区医师通过 DMP 交换患者数据。
- 截至 2024 年底，DMP 已覆盖 **2,800 万+** 法国居民，但实际在 HAD 场景中的使用率仍有限——多数 HAD 机构仍以电话/纸质 + 内部 EHR 为主。

### 3.2 PMSI-HAD（医疗信息系统项目）

- **ATIH**（Agence Technique de l'Information sur l'Hospitalisation）维护的全国 HAD 数据库。
- 覆盖 **100%** 法国 HAD 住院记录，是支付（T2A）、质量评估和政策制定的数据基础。
- 数据通过标准化编码（GHM/GHT 分类）统一上报。
- 学术研究者可通过 **SNDS（Système National des Données de Santé）** 申请使用 PMSI-HAD 微数据。

### 3.3 监管合规要求

- **CE 医疗认证（MDR 2017/745）**：所有 RPM 设备须符合欧盟医疗器械法规。
- **RGPD（GDPR）**：法国 CNIL（国家信息与自由委员会）对健康数据执行最严格标准。
- **Hébergeur de Données de Santé (HDS)** 认证：健康数据托管服务商须取得法国卫生部认可的 HDS 认证。
- **Sécurité Numérique en Santé (SNS)**：法国卫生部 2023 年发布的数字健康安全框架，要求 HAD 机构进行安全评估。

> **来源：** ATIH, PMSI-HAD 技术文档; CNIL, "Santé et RGPD" 指南 (2023); ANS, SNS 框架

## 四、医保覆盖与支付

### 4.1 T2A 按日付费框架下的技术支出

法国 HAD 支付体系主要通过 **T2A（Tarification à l'Activité）** 的 **GHT（Groupement Homogène de Tarifs）** 按日费率运行：

- **GHT 费率跨度为 €150–€350/日**（取决于照护模式的强度）。
- 常规药品和耗材含在 GHT 日费率内。
- **"Liste en sus"** 昂贵药品和植入式器械额外结算。
- 远程监测/远程医疗费用**尚未单独纳入 GHT 费率**——多数 HAD 机构通过自有预算或选择性项目提供。

### 4.2 ETAPES 计划（远程监测报销）

- **ETAPES**（Expérimentations de Télémédecine pour l'Amélioration des Parcours en Santé，2018–2022）是法国卫生部的远程医疗试点项目。
- 2023 年起转为**标准报销**（droit commun）。
- 覆盖领域：心衰、糖尿病、肾衰竭、COPD、透析。
- **费率**：约 **€30–€50/患者/月**（远程监测），由 Assurance Maladie 按固定拨款支付。
- **局限性**：ETAPES 主要覆盖慢病管理，尚未与 HAD 的 GHT 支付体系整合——HAD 患者如同时接受远程监测，需走两条独立的报销通道。

### 4.3 对比：法国 vs 美国 vs 德国

| 维度 | 法国 HAD | 美国 CMS HaH | 德国 |
|------|---------|-------------|------|
| 支付模式 | T2A GHT 按日付费 (€150–€350) | DRG 按次 + 日附加费 | SGB V 标准给付 + 选择性合同 |
| RPM 独立报销 | ETAPES (€30–€50/月) | CMS RPM CPT 代码 (~$50–$120/月) | 心衰 Telemonitoring 标准报销 |
| 数据基础设施 | PMSI-HAD (100% 覆盖) | 碎片化 EHR | TI (Telematikinfrastruktur) |
| 远程监测渗透 | 低（人工巡诊为主） | 高（RPM 为核心） | 中等（心衰领先, 其他逐步推广） |

> **来源：** ATIH, AAH 2024; Assurance Maladie, ETAPES 评估报告 (2023); CSP L. 6125-2

---

## 五、关键判断与技术趋势

1. **法国 HAD 的"低技术"特征是制度选择而非技术落后**——高密度上门巡诊模式是基于数十年的实践优化，替代远程监测并非优势。
2. **ETAPES→ droit commun 的转化**是法国 RPM 报销的标志性里程碑，但 HAD 与 RPM 的支付整合仍需政策推动。
3. **DMP + PMSI-HAD 的数据基础设施**是法国相较英美的重要优势——一旦 RPM 设备大规模进入 HAD，现有数据体系可快速生成真实世界证据。
4. **Withings 等法国本土硬件厂商**在全球消费者健康设备市场有影响力，但在 HAD B2B 市场尚未形成规模。
5. **Clariane 退出、Santé Service 收购整合**表明法国 HAD 正在经历行业集中化，这可能成为技术投入的催化剂——大机构更有能力部署数字化基础设施。

---

> 📎 相关专题报告：[[Topics/RPM设备商全景.md]]

**本页面最后更新：2026-07-05**

**主要来源：** reports/2026-07-03-france-had-analysis.md; ATIH AAH 2024; FNEHAD; Legifrance CSP; Assurance Maladie ETAPES
