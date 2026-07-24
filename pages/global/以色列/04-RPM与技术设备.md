---
type: entity
tags: [israel, tier-3, country, digital-health, RPM, telemedicine, startup-nation]
created: 2026-07-24
updated: 2026-07-24
aliases: [以色列数字健康, RPM Israel, Startup Nation]
---

# 🇮🇱 以色列 远程患者监测（RPM）与技术设备

## 核心数据速览

| 指标 | 数据 | 来源 |
|:---|:---|:---|
| 数字健康初创企业数量 | **400+家** | Startup Nation Central |
| 健康科技领域融资 (2023) | **~20亿美元** | Startup Nation Central |
| 电子病历数据积累 | **30年以上**（四大HMO整合数据） | 行业共识 |
| 国家级HIE平台 | **Ofek**（连接所有医院+健康基金） | IDB |
| 远程医疗法律基础 | 《医疗信息调动法》(2024) | ICLG 2026 |
| **Maccabi远程疾病管理** | **MOMA多学科呼叫中心** | Maccabi |
| **Clalit远程医疗平台** | **Vitalon（与Essence SmartCare合作）** | PRNewswire 2022 |
| 全球健康科技投资排名 | 全球前5-10位（per capita） | IVC/Startup Nation Central |

---

## 一、"Start-Up Nation" 数字健康生态

### 为什么以色列成为全球数字健康强国？

以色列之所以被称为"Start-Up Nation"并成为全球数字健康创新的核心枢纽，有以下结构性因素：

| 驱动因素 | 详细说明 |
|:---|:---|
| **全民电子病历数据** | 四大健康基金覆盖~100%人口，各自拥有数十年纵向EMR数据。Clalit一家覆盖~478万患者，数据元丰富程度全球领先 |
| **军事技术外溢** | IDF（以色列国防军）的精英技术部队（如8200信号情报部队）每年输出数千名技术人才进入创业生态 |
| **紧密的产学研合作** | 魏茨曼研究所、Technion、特拉维夫大学、Ben-Gurion大学与产业界高度联动 |
| **"Chutzpah"创业文化** | 敢于挑战权威、快速试错、扁平化组织结构 |
| **紧迫的国内需求** | 护士/医生短缺、老龄化加速、地理安全挑战（远程医疗可减少非必要出行） |
| **强力政府支持** | 以色列创新局（IIA）、MoH数字健康计划、多国双边创新合作（如与美国、阿联酋、摩洛哥） |

### 数字健康细分领域格局

```text
以色列数字健康创新版图（~400+初创企业）：

AI辅助诊断与影像
  ├── Zebra Medical Vision（AI放射影像分析，已被Nanox收购）
  ├── Aidoc（AI放射科工作流，获FDA批准，估值超10亿美元）
  └── Viz.ai（AI卒中检测）

远程监测与慢性病管理
  ├── BioBeat（可穿戴连续生命体征监测）
  ├── TytoCare（家用远程检查设备，已获FDA批准）
  ├── Oxitone（腕戴式血氧监测）
  └── EarlySense（无接触床旁监测，2021年被Hillrom/Baxter收购）

数字疗法（DTx）
  ├── DarioHealth（糖尿病/慢性病数字管理，纳斯达克上市）
  ├── Kaia Health（MSK数字疗法，德国总部但以色列技术团队）
  └── Happify Health（心理健康数字疗法）

老年护理/居家护理科技
  ├── Essence SmartCare（老年人远程安全监测，与Clalit合作Vitalon平台）
  ├── Intuition Robotics（ElliQ社交机器人，老年陪伴）
  ├── Sensi.AI（AI音频分析监测居家老人状态）
  ├── Uniper Care（老年人数字社交健康平台）
  └── iSavta（在线护工匹配平台，详见03-头部机构/iSavta.md）

健康数据分析与AI
  ├── MDClone（合成数据平台，加速临床研究）
  ├── K Health（AI初级保健分诊，基于Maccabi数据训练）
  └── Sweetch（AI行为改变平台，慢性病预防）

远程医疗平台
  ├── Healthy.io（智能手机尿液分析，FDA批准）
  └── TytoCare（已列入，远程检查+视频问诊一体化）
```

---

## 二、国家级远程医疗基础设施

### Ofek — 国家健康信息交换平台

**Ofek**（אופק，意为"视野/地平线"）是以色列的国家级健康信息交换（HIE）平台，由Clalit开发并推广至全国：

| 功能维度 | 描述 |
|:---|:---|
| **连接范围** | 连接所有以色列医院 + 四大健康基金 + 社区诊所 |
| **数据内容** | 患者病历、检验结果、影像报告、用药记录、过敏史、就诊历史 |
| **访问权限** | 临床医生在患者同意下实时查询，提供完整的纵向医疗史 |
| **技术标准** | 基于HL7 FHIR标准，支持跨机构互操作 |
| **对HaH的意义** | HaH医生在患者家中可通过移动端访问Ofek，获取医院检验结果、影像报告等，无需重复检查 |

（来源：IDB, The Implementation of a National HIE Platform in Israel, 2023）

### Maccabi MOMA — 多学科远程协调中心

**MOMA**（Multi-Disciplinary Call Center）是Maccabi Healthcare Services的核心远程医疗基础设施：

- **定位**：不只是呼叫中心，而是**临床信息系统+远程疾病管理+护理协调**的综合平台
- **功能**：
  - 整合Maccabi EMR数据，实时显示患者病历
  - 远程慢性病管理（糖尿病、心衰、COPD等）
  - 医疗资源的GPS式调度（最近可用诊所/医生/护理站）
  - 24小时护士热线分诊
  - 为CBHH（社区居家住院）提供远程支持
- **覆盖**：服务Maccabi的~260万会员

### Clalit-Essence Vitalon 远程医疗平台

- **合作伙伴**：Clalit Health Services + Essence SmartCare（以色列老年人远程安全监测公司）
- **试点内容**：为老年慢性病患者提供居家远程监测+AI风险预警
- **目标**：降低可避免的住院率，延迟或避免机构化
- **技术栈**：IoT传感器（门磁、运动感应、跌倒检测）+ AI分析平台 + 护理协调

---

## 三、主要RPM技术供应商（以色列籍）

### 面向居家/老年护理

| 公司 | 核心产品 | 技术特点 | 市场状态 |
|:---|:---|:---|:---|
| **Essence SmartCare** | Vitalon / Care@Home | 多传感器老年安全监测，AI行为模式分析，跌倒检测 | 与Clalit合作试点；国际扩张（欧洲/美国） |
| **Sensi.AI** | 音频AI监测 | 仅用一个麦克风设备，通过环境音频分析检测异常（跌倒、呼救、异常作息）；无需摄像头、无需穿戴 | 2023年获$14M A轮融资；获多个国际奖项 |
| **Intuition Robotics** | ElliQ | 主动式AI老年陪伴机器人；通过自然语言交互减少孤独感、提醒用药、促进身体活动 | 与纽约州老龄化办公室合作部署800+台；获Toyota AI Ventures等投资 |
| **Uniper Care** | 老年数字平台 | 电视端社交+健康内容+远程医疗入口，降低老年人数字化门槛 | 与多家美国Medicare Advantage计划合作 |
| **BioBeat** | 可穿戴监测 | 腕戴式/胸贴式连续生命体征监测（HR、BP、SpO2、RR、体温），获FDA/CE批准 | 全球多中心临床研究；与Mayo Clinic合作 |

### 面向远程检查/远程问诊

| 公司 | 核心产品 | 技术特点 | 市场状态 |
|:---|:---|:---|:---|
| **TytoCare** | 家用远程检查套件 | 手持设备集成听诊器、耳镜、喉镜、皮肤镜、温度计，患者自操作→医生远程解读。获FDA批准 | 融资超$200M；与多家美国大型医疗系统合作（Sanford、Sentara等） |
| **Healthy.io** | 智能手机尿液分析 | 利用手机摄像头+AI分析尿液试纸条，获FDA批准（首个此类产品） | 与英国NHS合作部署（50万+测试）；与美国Walgreens合作 |

---

## 四、远程医疗法规与数字健康政策

### 法规里程碑

| 年份 | 法规/政策 | 核心意义 |
|:---|:---|:---|
| 2020 | MoH远程医疗服务操作标准 | COVID-19加速了远程医疗法规制定，为远程诊疗提供标准化框架 |
| 2024 | **《医疗信息调动法》**（חוק הנעת מידע רפואי） | 里程碑式法律，打破机构间数据壁垒，促进健康数据共享 |
| 2025（待定） | 数字健康解决方案定价与报销机制 | 正在制定中，将决定RPM/DTx能否进入基本服务包 |

### 数据隐私框架

- **《隐私保护法》**（Protection of Privacy Law, 5741-1981）：个人健康数据保护的基础法律
- **以色列隐私保护局（PPA）**：监管数据隐私合规
- **GDPR充分性认定**：以色列已获得欧盟的GDPR数据保护充分性认定，为跨境数字健康合作提供法律基础

### 数字健康报销现状

目前以色列尚未建立统一的数字健康/远程监测国家报销体系。实际运作模式为：

1. **健康基金内部采用**：各HMO自主决定是否将该数字健康方案纳入自身预算
2. **创新局（IIA）试点资助**：政府提供研发资助但不负责常规运营报销
3. **私人支付/保险覆盖**：部分数字健康产品（如TytoCare）通过消费者自购进入家庭
4. **国际收入为主**：多数以色列数字健康公司的商业收入来自美国/欧洲市场，而非本国报销

---

## 五、AI与大数据在居家护理中的应用

### 临床预测模型

各健康基金利用30+年纵向EMR数据开发AI模型：

| 模型应用 | 目的 | 代表性工作 |
|:---|:---|:---|
| **再入院风险预测** | 筛选适合HaH的低风险患者，排除高风险者 | Clalit/Maccabi内部模型 |
| **功能衰退预测** | 识别尚能独立生活但即将失能的老年人，提前干预 | 学界活跃研究方向 |
| **跌倒风险分层** | 基于电子病历标记高风险居家老人 | — |
| **护理需求预测** | 优化护理人力资源调度 | 起步阶段 |
| **败血症早筛** | 居家患者早期预警 | 与远程监测设备联动 |

### MDClone — 合成数据加速研究

**MDClone**是以色列健康数据分析领域的代表性公司。其**合成数据引擎**允许研究人员在不暴露真实患者隐私的情况下访问与分析临床数据，大幅加速了临床研究流程。该平台已获多个国家医疗系统采用。

---

## 六、数字健康与HaH的融合

以色列数字健康生态与HaH体系形成了良性循环：

```
数字健康工具
  ├── TytoCare远程检查 → HaH医生居家访问时可进行听诊/耳镜等检查
  ├── Essence Vitalon → 持续监测HaH患者居家状态
  ├── BioBeat可穿戴 → 连续生命体征监测替代每天多次手动测量
  ├── Sensi.AI音频 → 检测跌倒/异常行为
  ├── Ofek HIE → HaH团队实时访问医院检验影像报告
  └── AI预测模型 → 优化患者筛选，降低再入院风险
  
    ↓
  
HaH项目
  → 为数字健康产品提供真实世界验证场景
  → 产出高质量临床证据（如Lustman et al., 2025）
  → 吸引更多创业公司进入居家医疗赛道
```

---

## 七、关键趋势

### 趋势1：从"创业输出"到"本土应用"

历史上以色列数字健康公司的收入70%+来自海外。近年来，在MoH推动和HaH扩展背景下，**本土部署正在加速**。Clalit与Essence合作、Maccabi的MOMA系统是典型代表。

### 趋势2：AI Agent进入老年护理

Intuition Robotics（ElliQ）、Sensi.AI等代表了从"被动监测"到"主动交互"的转变——AI不仅能检测异常，还能主动与老年人对话、提供陪伴和提醒。

### 趋势3：数据整合加速

《医疗信息调动法》(2024) + Ofek平台 + MDClone合成数据 = 正在形成一个全球独有的数据驱动研究基础设施。未来5年可能产出大量基于真实世界数据的居家护理证据。

### 趋势4：数字疗法（DTx）纳入报销

JMIR 2023年综述指出，以色列正在制定数字健康解决方案的定价和报销机制。DTx（尤其是心理健康、慢性病管理类）可能率先进入基本服务包。

### 趋势5：跨境合作新模式

《亚伯拉罕协议》（2020）后，以色列与阿联酋、摩洛哥、巴林等国的数字健康合作快速增长。以色列技术+海湾资本+非美欧市场验证的三角模式正在形成。

---

## 相关页面

- 00-概览.md|以色列长护险市场全景
- 05-临床证据.md|以色列居家护理临床证据
- 03-头部机构/B-Lev Shalem.md|B'Lev Shalem
- 03-头部机构/iSavta.md|iSavta 护工匹配平台

## 参考文献

1. Startup Nation Central. (2024). Global Health Challenges, Meet Israeli Health Tech Solutions. [T3-行业]
2. IDB. (2023). The Implementation of a National Health Information Exchange Platform in Israel. [T2-国际组织]
3. PRNewswire Israel. (2022). Essence SmartCare & Clalit Health Services: Vitalon Telehealth Platform Pilot. [T3-新闻]
4. ICLG. (2026). Digital Health Laws and Regulations Report 2026: Israel. [T2-法律]
5. JMIR. (2023). Digital Health Reimbursement Strategies of 8 European Countries and Israel. [T2-学术]
6. Lustman, A., et al. (2025). Hospital at home program. *IJHPR*. [T2-学术]
7. Israel Innovation Authority. (2024). Digital Health Sector Report. [T1-政府]
8. IVC Research Center. (2024). Israeli Health Tech Funding Report. [T3-行业]

**本页面最后更新：2026-07-24**
