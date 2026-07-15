---
tags: [国家, 美国, RPM, 技术设备]
created: 2026-07-05
updated: 2026-07-12
aliases: [美国 RPM, 美国 远程监测]
---

# 美国 — RPM 与技术设备

> 本页面覆盖美国远程患者监测（RPM）设备市场规模、CMS 报销码、主要供应商、FDA 监管框架及 EHR 互操作性标准。

---

## 市场规模

美国是全球最大的 RPM 市场。根据 MarketsandMarkets 2025 年报告：

- **2024 年市场规模：** 141.5 亿美元
- **2025 年市场规模：** 160.9 亿美元
- **2030 年预测规模：** 291.3 亿美元
- **年复合增长率（CAGR）：** 12.6%–12.8%（2025–2030）

**来源：** MarketsandMarkets, "US Remote Patient Monitoring Market Report 2025–2030"

全球 RPM 市场在 2024 年约为 277.2 亿美元，预计到 2030 年达到 569.4 亿美元（CAGR 12.7%）。美国市场约占全球市场的 50% 以上。

**来源：** MarketsandMarkets, "Remote Patient Monitoring Market Global Forecast to 2030" (2025)

---

## CMS RPM 报销码（Billing Codes）

CMS 自 2018 年起将 RPM 纳入 Medicare Physician Fee Schedule。以下为截至 2025 年的核心 CPT 码及其平均报销金额：

| CPT 码 | 服务描述 | 2025 平均报销 |
|--------|----------|--------------|
| **99453** | 初始设备设置与患者教育（一次性） | $19.73 |
| **99454** | 设备月供 — 每日数据记录/警报传输，每 30 天 | $43.02 |
| **99457** | 首个 20 分钟 RPM 管理（需交互沟通），每日历月 | $47.87 |
| **99458** | 每额外 20 分钟管理（99457 附加码） | $38.49 |

**报销潜力示意：** 按 2025 年费率，100 名患者使用最低月度服务，年报销额约 **$110,000**。

**来源：** CMS Physician Fee Schedule 2025 Final Rule; Prevounce Quick Guide (2025)

### 2026 年新增 CPT 码

2026 年 Medicare Physician Fee Schedule 最终法规新增两个 RPM 码：

- **99445** — 设备供应（患者 30 天内有 2–15 天数据）
- **99470** — 首个 10 分钟 RPM 管理时间（需患者互动）

**来源：** CMS CY 2026 Physician Fee Schedule Final Rule

### 关键编码规则

1. **99454** — 每患者每 30 天只可开单一次，不限设备数量
2. **99457** — 每月至少 20 分钟管理时间，可由医生、QHCP 或临床人员执行
3. **99458** — 每月最多附加两次（40 分钟、60 分钟）
4. **数据采集要求：** 患者必须在 30 天内至少使用设备 **16 天** 并传输数据
5. 可与 CCM、TCM、BHI 等护理管理码**同时开单**

**来源：** CMS 2025 Final Rule; Smart Meter 2025 RPM Billing Summary

---

## 主要 RPM 设备与平台供应商

| 供应商 | 核心产品 / 平台 | 重点领域 |
|--------|----------------|----------|
| **Biofourmis** | Biovitals® 预测分析平台 — FDA 批准算法预测心衰恶化 | 心衰、慢性病预测分析 |
| **Cadence** | Cadence Care — 远程监测 + 护理协调平台 | 高血压、糖尿病、心衰 |
| **Current Health (Best Buy Health)** | 一体化 RPM 平台 — 可穿戴监测 + 虚拟护理 | HaH 急性期监测、慢病管理 |
| **HealthSnap** | 多参数 RPM 平台 + 护理管理 | 慢病管理、COPD、心衰 |
| **Athelas** | 血液监测 + RPM 集成平台 | 慢性病远程血液监测 |
| **Health Recovery Solutions (HRS)** | RPM 设备套件 + 患者教育平台 | 术后恢复、心衰、COPD |
| **Accuhealth** | RPM 平台 + 蓝牙设备集成 | 慢病管理、Medicare 人群 |
| **Optimize Health** | RPM 白标平台 + 临床服务 | 糖尿病、高血压 |

**来源：** HealthSnap "Top 7 RPM Companies 2025"; RPM Leadership Council (2025); Elion RPM Product Database

> 2025 年，Cadence、Best Buy Health、Biofourmis 等七家 RPM 公司联合成立 **RPM Leadership Council**，推动 RPM 行业标准与政策倡导。

**来源：** RPM Leadership Council Public Announcement (2025)

---

## FDA 监管框架

FDA 将 RPM 设备作为**医疗器械**进行监管，根据风险水平分类：

| 类别 | 描述 | 上市路径 |
|------|------|----------|
| **Class I** | 低风险（如电子体温计） | 一般控制 — 大多免 510(k) |
| **Class II** | 中风险（如血压监测仪、脉搏血氧仪、心电监护贴片） | **510(k) 清关** — 需证明与已上市器械实质性等同 |
| **Class III** | 高风险（如可植入心脏监测器） | PMA（上市前批准） |

**关键要点：**
- 大多数 RPM 设备为 **Class II**，需通过 **510(k)** 路径上市
- RPM 软件即医疗设备（SaMD）需符合 FDA 的数字健康指南
- FDA CDRH 的 **Breakthrough Devices Program** 已授权 77+ 台具有突破性认定的设备上市
- 后疫情时代，FDA 发布了针对**非侵入式远程监测设备**的永久性执法政策

**来源：** FDA "Medical Device Safety and the 510(k) Clearance Process"; Tenovi "FDA Language Around RPM Devices" (2023); FDA CDRH Breakthrough Devices Data

---

## EHR 互操作性与 FHIR

美国在 EHR 互操作性方面处于全球领先地位，核心驱动力是 **21st Century Cures Act** 和 **CMS 互操作性与患者接入最终规则**。

### FHIR 采用现状

- **HL7 FHIR R4** 是美国联邦政府强制采用的互操作性标准
- ONC **HTI-1 规则**要求 2025 年起支持 **USCDI v3** 和 **SMART on FHIR 2.0**
- 2025 年 FHIR 全球采用调查：71% 的受访者报告 FHIR 至少用于几种场景（2024 年为 66%）
- CMS 要求所有 Medicare Advantage、Medicaid、CHIP、QHP 计划通过 **Patient Access API**（FHIR 标准）向患者提供数据

**来源：** ONC HTI-1 Final Rule (2024); HL7/Firely "State of FHIR 2025"; CMS Interoperability and Patient Access Final Rule

### Apple Health Records

Apple Health Records 是 FHIR 互操作性在消费者端的重要实践：
- 基于 **SMART on FHIR** 框架，从支持 FHIR 的 EHR 系统中获取数据
- 覆盖美国 600+ 医院和卫生系统
- 患者可在 iPhone 上统一查看来自不同医疗机构的健康数据
- 支持近 500 家医疗机构的病历整合

**来源：** Apple Health Records Product Page; ONC Interoperability Standards Advisory

### 对 HaH/RPM 的意义

FHIR 互操作性使 RPM 数据（血压、血氧、体重、心率等）能够无缝流入主流 EHR 系统（Epic、Cerner/Oracle Health、Meditech），实现：
- 远程监测数据与临床工作流集成
- 跨机构数据共享
- 实时临床决策支持（CDS Hooks）
- 质量指标自动上报（如 CMS AHCAH 要求的数据报告）

---

## 最新动态

- **2026-07-05:** 本页面首次填充 — 覆盖市场规模、CMS 报销码、供应商全景、FDA 监管及 FHIR 互操作性标准。
- 2026-07-12: **Vega Health and Baptist Health Bring Actionable AI to Hospital at Home**——Vega Health与Baptist Health合作将AI引入居家医院模式，为长期协作奠定基础，提升患者监测和临床决策效率（来源：[Yahoo Finance](https://news.google.com/rss/articles/CBMimAFBVV95cUxPQnpTNGtCX2xuemtFcE1nR0hrbk9STnhydHREVFU3bnFfcEp0cEFYTVAtb0JJUEtNUUZ3TlRXZ3lpMEh0cTlCVkVObms2dFp5Y1FGei03VWRzMFMxaVJaSDFSZEE2ZmpLeDVUM095dFpwVTdBZ0dUVUk4Ti04Z2ZzYl9mNjRwMG43WjdySVVyTHVjdWdSOEhvTQ?oc=5)）

本页面最后更新：**2026-07-05**
