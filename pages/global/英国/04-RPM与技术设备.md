---
tags: [国家, 英国, RPM, 技术设备]
created: 2026-07-04
updated: 2026-07-05
aliases: [英国 RPM, 英国 远程监测]
---

# 英国 — RPM 与技术设备

## 一、NHS Virtual Ward 技术栈全景

英国 NHS 虚拟病房（Virtual Ward）的技术服务市场呈「多供应商 + 全托管」格局。主要供应商包括：

| 供应商 | 总部 | 服务模式 | NHS 渗透 | 关键特征 |
|--------|------|----------|----------|----------|
| **Doccla** | 伦敦 | 全托管（Fully Managed） | **>60% ICB** | 自建 CQC 注册临床团队；40+ 护理路径；400 万+ 患者日；G-Cloud 14 框架定价 £550/天 |
| **Current Health** | 爱丁堡/波士顿 | 技术平台 | 较低（美国重心） | 2021 年被 Best Buy 收购；自研可穿戴贴片硬件 |
| **Spirit Health** | 英国 | 技术平台 | NHS 部署 | CliniTouch Vie 远程监测平台；COVID-19 虚拟病房经验 |
| **Lenus Health** | 英国 | 技术平台 | NHS 部署 | 虚拟病房数字化平台；呼吸/心衰路径 |
| **Isansys Lifecare** | 英国 | 硬件+平台 | NHS 部署 | 自研可穿戴传感器（Lifetouch 患者监测平台） |

**Doccla 为英国虚拟病房最大供应商**，覆盖超 60% 的 NHS Integrated Care Board（ICB），服务 11 个欧洲国家，2024 年 9 月完成 £35M Series B（Lakestar 领投）。[^1]

其他主要供应商还包括 Inhealthcare、Kinetik Wellbeing、Florence（Generated Health）、Access Group 等。[^2]

---

## 二、NHS England 远程监测框架

NHS 远程患者监测（RPM）的技术基础设施以三大数字服务为核心：

### 2.1 NHS App
- 英国居民访问 NHS 服务的统一移动入口（≥13 岁可注册）
- 提供查看检测结果、预约管理、GP 通信等功能
- 2025 年用户约 3,500 万注册用户 [^3]
- 远程监测数据可集成至 NHS App 供患者查看

### 2.2 NHS Login
- 统一身份认证系统，是 NHS App 和第三方数字健康服务的底层认证层
- 被 NHS 委托的第三方数字健康服务广泛使用 [^4]
- 支持患者通过单一账户访问多个数字健康应用

### 2.3 GP Connect
- 允许授权的卫生和社会护理工作者跨机构访问患者 GP 记录
- 为虚拟病房团队提供实时的患者诊疗信息共享能力 [^5]
- 支持 FHIR 标准，是 NHS 互操作性战略的核心组成部分

### 2.4 EMIS Health 集成
- Doccla 等供应商与 EMIS Health（英国最大 GP 系统供应商）集成
- 实现虚拟病房数据与 NHS EHR 系统的双向流动

---

## 三、NHS 数字健康安全标准（NHSX / NHS England）

### 3.1 DCB0129 与 DCB0160
- **DCB0129**：制造商临床风险管理标准，适用于健康 IT 系统生产的临床风险管控 [^6]
- **DCB0160**：部署和使用方的临床风险管理标准，适用于医疗机构对健康 IT 系统的安全管理 [^6]
- 两类标准均为 **NHS 强制要求**，所有在 NHS 中使用的数字健康技术（DHT）必须合规
- 2024 年 12 月，NHS England 启动对 DCB0129 和 DCB0160 的全面审查（含 AI、网络安全等新维度）[^7]
- **2025 年大规模调查发现**：239 家 NHS 组织中共使用约 14,747 个数字健康系统，其中约 70% 无文档化的安全保证记录（首个系统量级全国横断面研究）[^8]

### 3.2 DTAC（Digital Technology Assessment Criteria）
- NHS 数字技术评估标准，是 NHS 数字健康采购的基准网关 [^9]
- 涵盖五大维度：**临床安全、数据保护、技术保障、互操作性、可用性和可及性**
- 供应商必须证明符合 DTAC 要求方可进入 NHS 采购市场
- 与 DCB0129、NHS DSPT（Data Security and Protection Toolkit）、Cyber Essentials、UK GDPR 互为补充

### 3.3 NHS DSP Toolkit
- 数据安全与保护工具包，是 NHS 所有组织及其技术供应商的强制安全合规要求
- 每年评估，覆盖数据治理、网络安全、信息治理等维度

---

## 四、NICE 对 RPM 技术的评估指南

### 4.1 NICE Evidence Standards Framework（ESF）for Digital Health Technologies
- 2018 年初版发布，**2022 年 8 月更新**，是 NICE 对 DHT 的官方证据标准框架 [^10]
- **目的**：为 NHS 和社会照护系统的采购决策者提供统一的证据评估标准；帮助 DHT 公司理解 NHS 如何评估技术价值
- **三级分类**：
  - **A 类**：非临床直接影响的 DHT（如健康生活方式记录）
  - **B 类**：改变临床路径但非医疗器械的 DHT
  - **C 类**：行使医疗器械功能的 DHT（需符合 UKCA/CE 标志要求）
- 每个类别对应不同的证据标准（安全、有效性、经济性）
- **非强制性**，但被 NHS 采购广泛参考

### 4.2 NICE 对其他 RPM 技术的评估
- NICE 对具体 RPM 产品（如心衰远程监测、COPD 远程监测）进行单项技术评估（Technology Appraisal）
- NICE 指南（NG系列）涵盖远程监测在多个疾病路径中的应用推荐

---

## 五、NHS Long Term Plan 对数字化居家医疗的投资

- 2019 年发布的 NHS Long Term Plan 明确将数字化和居家照护作为核心战略方向 [^11]
- 承诺向数字健康投资，推动「医院向社区转移」的模式变革
- 2023 年更新：设定虚拟病房床位目标为 **40–50 床/10 万人**（2030 年前），2025 年 3 月已达成 20 床/10 万人 [^12]
- NHS 2024/25 运营规划指南要求维持虚拟病房容量、优化占用率至 **80% 以上** [^13]
- 英国政府 2025 年宣布七项 NHS 数字项目共享 **£7.4 亿** 投资 [^14]
- 2025 年 1 月，卫生大臣 Wes Streeting 提出三大改革方向：「从医院到社区、从治疗到预防、从模拟到数字」[^15]

---

## 六、5G 远程医疗试验

### 6.1 West Midlands 5G Testbed
- 英国首个 5G 医疗试验床，始于 2018 年
- **5G 连接救护车**：University Hospitals Birmingham NHS Foundation Trust 与 BT、WM5G 合作，展示英国首个在公网 5G 上的远程超声操作——救护车内超声传感器由远程医生操控 [^16]
- 评估 5G 在急救转运、远程诊断中的价值

### 6.2 Liverpool 5G Health & Social Care Testbed
- 利物浦 5G 健康与社会照护试验床，获 £148 万额外资助延展一年 [^17]
- 测试 5G 在社区护理、远程生命体征监测、社会照护协调中的应用

### 6.3 其他 5G 医疗试验
- 英国 5G Testbeds and Trials Programme（2018–至今）覆盖医疗、交通、制造等多个领域 [^18]
- Rural Connected Communities 项目投资 £3,000 万用于农村 5G 研发（含远程医疗应用）
- 5G 被视为 NHS 远程监测的底层连接基础设施，尤其适合农村和移动医疗场景

---

## 七、NHS 采购框架

- **G-Cloud 14**：Doccla 上架 NHS 官方云采购框架，定价透明化
- **NHS England Virtual Ward Operational Framework**：2024 年发布，定义虚拟病房的核心服务组件、质量标准、数据采集要求，要求各 ICB 统一执行 [^13]

---

## 参考资料

[^1]: Doccla 27 维度深度尽调报告（报告日期：2026-07-03）. /Users/kennethye/workspace/kate-knowledge-base/reports/2026-07-03-doccla-27dim/report.md
[^2]: Best Virtual Ward Providers in the UK — The Access Group. https://www.theaccessgroup.com/en-gb/blog/hsc-best-virtual-ward-providers-in-the-uk
[^3]: NHS App — Google Play / NHS England. https://www.nhs.uk/nhs-app/
[^4]: NHS Login — Websites and apps you can access. https://www.nhs.uk/nhs-services/nhs-login/websites-and-apps-you-can-access-with-nhs-login
[^5]: GP Connect — NHS England Digital. https://digital.nhs.uk/services/gp-connect
[^6]: NHS England — Digital Clinical Safety Assurance. https://www.england.nhs.uk/long-read/digital-clinical-safety-assurance
[^7]: NHS England Launches Digital Clinical Safety Standards Review — Digital Health (2024-12). https://www.digitalhealth.net/2024/12/nhs-england-launches-digital-clinical-safety-standards-review
[^8]: Digital Health Technology Compliance With Clinical Safety Standards In the NHS — PMC (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12619009
[^9]: Digital Technology Assessment Criteria (DTAC) — ORCHA. https://www.orchahealth.com/resources/assessment-frameworks/dtac
[^10]: NICE Evidence Standards Framework for Digital Health Technologies. https://www.nice.org.uk/corporate/ecd7/resources/evidence-standards-framework-for-digital-health-technologies-pdf-1124017457605
[^11]: NHS Long Term Plan — Digital Transformation. https://www.longtermplan.nhs.uk/areas-of-work/digital-transformation
[^12]: POST-PN-0744 — Virtual Wards and Hospital at Home, UK Parliament (2025). https://researchbriefings.files.parliament.uk/documents/POST-PN-0744/POST-PN-0744.pdf
[^13]: NHS England — Virtual Wards Operational Framework. https://www.england.nhs.uk/long-read/virtual-wards-operational-framework
[^14]: Seven NHS Digital Programmes to Share £7.4 Billion New Investment — LinkedIn (2025). https://www.linkedin.com/pulse/seven-nhs-digital-programmes-share-74-billion-new-jon-hoeksma-yo8ge
[^15]: Digital Health Rewired 2025 — A Critical Moment for the NHS's Transformation. https://digitalhealthrewired.com/2024/12/17/digital-health-rewired-2025-a-critical-moment-for-the-nhss-transformation
[^16]: Connected Ambulance: BT Demonstrates UK's First Remote Ultrasound Over 5G — Mobile Europe. https://www.mobileeurope.co.uk/connected-ambulance-bt-demonstrates-uk-s-first-remote-ultrasound-over-5g
[^17]: Liverpool 5G Health & Social Care Testbed Extended — Blu Wireless. https://www.bluwireless.com/insight/news/liverpool-5g-health-social-care-testbed-extended-for-a-year-with-1-48m-in-extra-funding
[^18]: 5G Testbeds and Trials Programme: Complete List of 5G Projects — GOV.UK. https://www.gov.uk/guidance/5g-testbeds-and-trials-programme-complete-list-of-5g-projects

> 📎 相关专题报告：[[Topics/RPM设备商全景.md]]

本页面最后更新：2026-07-05
