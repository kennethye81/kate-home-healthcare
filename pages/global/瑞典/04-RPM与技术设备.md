---
tags: [国家, 瑞典, RPM, 技术设备]
created: 2026-07-04
updated: 2026-07-05
aliases: [瑞典 RPM, 瑞典 远程监测]
---

# 瑞典 — RPM 与技术设备

## 一、瑞典远程医疗市场概况

瑞典是全球数字化程度最高的医疗市场之一。2025 年瑞典的 eHealth 战略（Vision e-hälsa 2025）已基本实现预期目标，远程患者监测（RPM）和虚拟病房进入大规模扩张阶段。[^1][^2]

### 1.1 市场规模

| 指标 | 数据 | 年份/来源 |
|------|------|----------|
| 医疗卫生 GDP 占比 | **11.2%**（约 7,190 亿 SEK） | 2024 (SCB) |
| RPM/虚拟病房市场 | 早期阶段（约 0.01–0.04% 总支出），**年增长率 >20%** | 2024–25 估算 |
| 远程监测设备渗透率（居家护理） | 约 60–70% 接受者使用基本警报系统 | 2024 (Socialstyrelsen) |
| 1177.se 年访问量 | 近 **1,500 万次** | 2024–25 |
| BankID 数字身份覆盖率 | >95% 成年人口 | 2025 |

### 1.2 增长驱动因素

1. **人口老龄化**：≥80 岁人口预计从 2025 年约 58 万增至 2035 年约 80 万 [^3]
2. **医院床位紧张**：瑞典每 10 万人口仅约 **190 张病床**（欧盟最低之一），倒逼服务居家化 [^4]
3. **数字基础设施成熟**：全国电子健康记录（EHR）、1177.se 门户、BankID 数字身份全覆盖
4. **政治意愿**：SKR（瑞典市县联合会）将居家医疗列为首要战略方向 [^5]
5. **成本压力**：住院日成本约 10,000–15,000 SEK vs 居家医疗约 3,000–5,000 SEK/天 [^6]

---

## 二、Välfärdsteknik（福祉技术）政策框架

瑞典的 **Välfärdsteknik**（福祉技术）政策框架是国家应对老龄化社会的核心战略之一，由 Socialstyrelsen 和 SKR 联合推动。[^5]

### 2.1 政策沿革

| 年份 | 里程碑 |
|------|--------|
| **2006** | 首次将 IT 在医疗中的应用写入国家卫生政策 |
| **2016** | Vision e-hälsa 2025 发布——政府与 SKR 联合制定 |
| **2017** | 成立 E-hälsomyndigheten（电子健康局，国家 eHealth 协调机构） |
| **2018** | 协调出院法实施，推动出院后居家数字化监测 |
| **2020** | COVID-19 大幅加速远程医疗采纳 |
| **2022** | 卫生和社会事务监察局（IVO）发布居家数字监测安全指南 |
| **2025** | Vision e-hälsa 2025 基本完成，进入下一阶段规划 |

### 2.2 Välfärdsteknik 的核心技术类别

| 技术类别 | 瑞典语 | 应用场景 | 渗透率 |
|---------|--------|---------|--------|
| 社交警报/应急呼叫系统 | trygghetslarm | 跌倒检测、日常求助 | 高（约 60–70%） |
| 远程药物分配器 | påminnelsedispenser | 多重用药患者用药管理 | 中 |
| 智能环境传感器 | sensorteknik (rörelse, dörr, säng) | 活动监测、认知障碍预警 | 中度增长 |
| 视频访视系统 | videobesök | 远程护理、GP 视频问诊 | 高增长（COVID 后加速） |
| 可穿戴监测设备 | bärbar teknik för vitalparametrar | 心率、血压、血氧、体温 | 早期阶段 |
| 远程居家透析监测 | Peritonealdialys med fjärrövervakning | 腹膜透析患者管理 | 特定人群 |
| 跌倒预防可穿戴 | fallpreventionsenheter | 高风险老年人警示 | 早期阶段 |

### 2.3 数字健康基础设施

**1177.se 国家健康门户**：
- 瑞典最广泛使用的健康平台（年访问量近 1,500 万次）
- 功能：在线预约、处方续方、健康信息、电子病历查询、视频问诊
- 所有居民可通过 **BankID** 登录访问个人电子健康记录 [^2]

**全国电子健康记录（EHR）互操作性**：
- **Nationell Patientöversikt (NPÖ)**：允许跨 Region 医疗卫生人员查看患者信息
- 瑞典在 EHR 互操作性方面走在欧盟前列
- 但 Kommun/Region 间的数据共享仍是瓶颈

**国家质量登记系统**：
- 全球最完备体系之一，居家医疗领域包括：Svenska Palliativregistret（安宁疗护）、Senior Alert（老年预防）、Swedevox（氧疗）、Riksstroke（卒中）等
- 这些登记系统与 RPM 设备数据对接，形成闭环质量改进 [^7]

---

## 三、主要 RPM 设备与技术供应商

### 3.1 公共部门主导

| 提供者 | Region | 居家医疗/RPM 项目 |
|--------|--------|------------------|
| **Karolinska 大学医院** | Stockholm | Karolinska@home（数字+实体混合虚拟病房，2024 启动） |
| **Sahlgrenska 大学医院** | Västra Götaland | 规模较大的 ASIH 和居家监测项目 |
| **Skåne 大学医院** | Skåne | 南部最大居家医疗服务提供者 |
| **Norrlands 大学医院** | Västerbotten | 北部偏远地区远程居家医疗创新方案 |

### 3.2 主要私营供应商

| 供应商 | 业务领域 | 市场地位 |
|--------|---------|---------|
| **Capio**（Ramsay Santé 旗下） | 居家医护、ASIH 服务 | 在多个 Region 运营 |
| **Aleris** | 居家医疗、安宁疗护 | 中大型私营提供者 |
| **Attendo** | 养老和居家护理 | 北欧最大养老/居家护理集团之一（主要在 Kommun 层面） |
| **Cura** | 安宁疗护、高级居家医疗 | 专业化私营提供者 |
| **Humana** | 个人援助、居家护理 | 多 Region 运营 |
| **Vardaga** | 居家护理、特别住宅 | 聚焦老年人服务 |

### 3.3 提供者结构

| 类型 | 占比（估） | 特点 |
|------|-----------|------|
| Region 自营 | ~70–75% | 通过医院 ASIH 团队直接提供服务 |
| 私营（签约/受委托） | ~20–25% | 通过 LOV（自由选择制度）或传统采购签约 |
| 私营（纯自费补充） | <5% | 主要是补充性私人医疗服务 |

> 初级保健中私营比例约 35–40%（大城市如斯德哥尔摩可达 60%），但居家医疗/ASIH 中的私营比例较低。急性期 HaH 由于需要与医院信息系统深度整合，目前仍以 Region 自营为主。[^8]

---

## 四、RPM 互操作性与技术标准

### 4.1 国家互操作性框架

瑞典的医疗 IT 互操作性由 **E-hälsomyndigheten** 协调，遵循以下标准：

| 标准/框架 | 说明 |
|-----------|------|
| **HL7 FHIR** | 瑞典国家 eHealth 战略推荐的互操作性标准 |
| **NPÖ**（Nationell Patientöversikt） | 跨 Region 患者信息共享平台 |
| **1177.se API** | 开放数字健康服务接口 |
| **BankID 集成** | 全国统一的患者身份认证 |
| **Socialstyrelsen 编码标准** | ICD-10-SE、KVÅ（医疗操作编码）、SNOMED CT 部分采纳 |

### 4.2 远程监测领域的主要挑战

- Kommun/Region 间的数据共享仍存在接口障碍
- 护士需要登录多个不互联的系统——增加了行政负担 [^6]
- 缺乏统一的 RPM 设备数据标准——各 Region 采购不同品牌设备
- IVO 2023–24 年报告特别指出：数字监测中的数据保护和知情同意需要加强 [^9]

---

## 五、Karolinska@home 技术方案

Karolinska@home 是瑞典最具标志性的虚拟病房项目，也是 RPM 技术在急性期 HaH 中应用的成功案例。[^10]

**技术栈**：
- **患者端**：集成可穿戴生命体征监测设备（心率、血压、血氧、体温） + 移动应用
- **传输层**：4G/5G（瑞典 5G 基础设施正加速铺设）
- **中心监控站**：Karolinska 医院内 24/7 实时数据监控
- **医生远程查房**：通过视频系统每日 1–2 次
- **护士上门**：每日 1–2 次嵌入式家访

**研发合作**：Karolinska 大学医院与 **皇家理工学院（KTH）** 合作开发 [^10]

---

## 参考资料

[^1]: Vision e-hälsa 2025 — Swedish Government / SKR. https://ehalsa2025.se/
[^2]: 1177.se — Sveriges sjukvårdsinformation på webben. https://www.1177.se/
[^3]: SCB — Sveriges framtida befolkning 2024–2060. https://www.scb.se/
[^4]: OECD Health at a Glance 2025 — Hospital beds indicators.
[^5]: SKR — Välfärdsteknik och e-hälsa. https://skr.se/
[^6]: 瑞典/北欧 居家医疗体系深度分析（2026-07-04）. /Users/kennethye/workspace/kate-knowledge-base/reports/2026-07-04-sweden-hah-analysis.md
[^7]: Svenska Palliativregistret. https://palliativregistret.se/
[^8]: WHO European Health Observatory — Sweden: Health System Review 2023. https://eurohealthobservatory.who.int/publications/i/sweden-health-system-review-2023
[^9]: IVO — Inspektionen för vård och omsorg. https://www.ivo.se/
[^10]: Karolinska University Hospital — Hospital@home. https://www.karolinskahospital.com/care-at-karolinska/tomorrows-healthcare/hospitalhome

> 📎 相关专题报告：[[Topics/RPM设备商全景.md]]

本页面最后更新：2026-07-05
