---
tags: [国家, 德国, RPM, 技术设备]
created: 2026-07-05
updated: 2026-07-05
aliases: [德国 RPM, 德国 远程监测]
---

# 德国 — RPM 与技术设备

## 一、远程医疗与 RPM 市场概况

德国数字健康市场在 2024 年估值约为 **149 亿欧元（约 USD 14.6B）**，预计 2024–2030 年以 **~15.8% CAGR** 增长，2030 年达 **~227 亿美元**（ResearchAndMarkets, 2024）。其中远程医疗（Telemedizin）和远程患者监测（RPM）是增长最快的细分领域之一。

- **Telemedizin** 在德国的法律障碍已于 2020 年大幅放宽，新冠疫情进一步加速了采纳。
- **远程监测（Telemonitoring）** 在德国已从研究工具演变为**标准医保服务**：2021 年 3 月起，高风险的慢性心力衰竭（CHF, LVEF ≤ 35%）患者可享受 Telemonitoring 作为法定医疗保险（GKV）的标准给付项目（G-BA 2020 年决定，基于 TIM-HF2 和 IN-TIME 等关键研究）。
- 在德国，每天约 **1,250 名患者**因心功能失代偿住院，远程监测被视作减少再入院的核心手段（JMIR 2024;26:e63391）。

## 二、主要供应商与产品

### 2.1 Vitaphone GmbH

- 总部位于德国曼海姆，是德国历史最悠久、规模最大的远程医疗企业之一。
- 核心产品包括 **EKG-Monitoring-Card（Vitaphone 100 IR）** 等心电远程监测设备，以及 24/7 远程医疗中心服务（Telemedizinisches Zentrum）。
- 在德国心脏远程监测市场中占据领先地位，与多家保险公司（如 AOK）和企业客户合作开展 Telemonitoring 项目。
- 提供 **Curaplan Herz Plus**（AOK Nordost）等疾病管理项目中的远程监护服务。

### 2.2 CompuGroup Medical SE & Co. KGaA (CGM)

- 总部位于科布伦茨，德国最大的医疗 IT 公司之一，全球拥有超过 7,000 名员工。
- RPM 产品线为 **ARIA Population Health**，提供实时远程患者监测解决方案，与 CGM 的 EHR（如 CGM APRIMA、CGM eMDs）深度集成。
- 支持慢性病管理，可监测血压、血糖、血氧、体重等生理参数，数据自动录入 EHR。
- CGM 还提供 **CGM ELVI** 远程会诊平台（HIPAA 兼容，在德国符合 DSGVO 要求）。

### 2.3 Philips Deutschland GmbH

- 荷兰皇家飞利浦在德国的子公司，是全球 RPM 市场的领导者之一（与 Medtronic、GE HealthCare 并列前三）。
- 在德国提供 **Philips Remote Patient Monitoring** 平台——通过 eCareCoordinator 和 eCareCompanion 实现慢性病患者的居家远程监测。
- 产品线涵盖从 **IntelliVue 床边监护**到**家庭远程监测**的全链条解决方案。
- Philips 的 RPM 平台在德国医院和居家护理场景中均有部署，特别是在心力衰竭、COPD 和高血压管理领域。

## 三、技术标准与互操作性

- 德国远程医疗系统须接入 **Telematikinfrastruktur (TI)**——即德国医疗服务的统一数字基础设施（gematik 运营）。
- 数据交换标准采用 **HL7 FHIR**（德国 Patientendaten-Schutz-Gesetz 推动的互操作路线图）。
- 远程监测设备需符合 **CE 医疗认证（MDR 2017/745）**，医疗软件须为 **Medizinprodukt (MPG)** 或按 DiGA（Digitale Gesundheitsanwendungen）审批。
- BfArM（德国联邦药品和医疗器械研究所）负责数字健康应用（DiGA）的审批与评估。

## 四、DSGVO 对 RPM 的影响

德国对健康数据的保护执行欧盟 **DSGVO（GDPR）** 的最严格标准，健康数据属于第 9 条下的**特殊类别数据**，原则上禁止处理，除非获得**明确知情同意**或基于**重大公共健康利益**等豁免。

**关键合规要求：**
1. **知情同意（§ 4 Abs. 3 DSGVO i.V.m. Art. 9 Abs. 2 lit. a）**：患者必须明确、具体地同意数据的远程采集与传输。
2. **数据最小化（Art. 5 Abs. 1 lit. c DSGVO）**：仅采集治疗所绝对必要的生理参数。
3. **传输加密**：患者数据须通过端到端加密传输（TI 安全标准）。
4. **数据处理记录（Verarbeitungsverzeichnis）**：RPM 提供者须建立完整的数据处理记录。
5. **云端限制**：健康数据原则上不得传输至非欧盟/欧洲经济区国家，除非存在 Adequacy Decision 或 Standard Contractual Clauses (SCCs)。

德国各州数据保护机构（Datenschutzbehörden）对远程医疗应用保持严格监管态势。2020 年通过的 **Patientendaten-Schutz-Gesetz (PDSG)** 进一步收紧了 ePA（电子病历）和 TI 中的数据处理规则。

> **来源：** DSGVO (EU) 2016/679; Patientendaten-Schutz-Gesetz (PDSG) 2020; gematik TI-Sicherheitsrichtlinien

## 五、SGB V 远程医疗 Reimbursement 框架

德国远程医疗的报销基于《社会法典第五卷》（SGB V），主要包括以下路径：

### 5.1 标准给付（Regelversorgung）

- **Herzinsuffizienz-Telemonitoring**：自 2021 年 3 月起纳入 GKV 标准给付，适用于 LVEF ≤ 35% 且近期有心衰住院史的高风险患者。G-BA 在 2020 年 11 月的 Beschluss 中将其列为标准干预措施。
- **Videosprechstunde（视频问诊）**：EBM（Einheitlicher Bewertungsmaßstab）编码，自 2017 年起逐步纳入，2020 年进一步扩围。每次视频问诊约 €4.55–€9.28（取决于类型和时长）。

### 5.2 选择性合同（Selektivverträge, § 140a SGB V）

- 多数远程监测项目（包括 Vitaphone 和 Philips 的项目）通过 **§ 140a SGB V** 的选择性合同与保险公司签订。
- 例如 AOK Nordost 的 **Curaplan Herz Plus** 即属此类条款下的项目。
- 报销金额和条件由合同双方（保险公司与医疗服务提供者）协商确定。

### 5.3 创新基金（Innovationsfonds, § 92a SGB V）

- G-BA 管理的创新基金为远程医疗/远程监测的随机对照试验提供资金（如 PASSPORT-HF 研究，纳入 554 名患者，结果预计 2026 年公布）。
- 成功项目可通过 G-BA 评估后转为标准给付。

### 5.4 主要局限

- RPM 在除心衰外的适应证（如 COPD、糖尿病、高血压）尚未普遍纳入标准报销——多数仍需通过选择性合同或项目形式。
- DiGA（数字健康应用，如处方 App）有独立的报销路径（§ 33a SGB V），但对硬件型 RPM 设备兼容性有限。
- 2023–2024 年 G-BA 正在评估 COPD 和糖尿病远程监测项目的纳入可能性。

> **来源：** G-BA Beschluss 2020 (Herzinsuffizienz-Telemonitoring); § 140a SGB V; EBM-Katalog 2024; JMIR 2024;26:e63391

---

> 📎 相关专题报告：[[Topics/RPM设备商全景.md]]

**本页面最后更新：2026-07-05**
