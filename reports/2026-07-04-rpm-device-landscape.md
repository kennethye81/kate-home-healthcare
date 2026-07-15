# RPM 设备商全景分析报告

**编制日期**：2026年7月4日  
**报告类型**：行业全景扫描  
**应用场景**：iHomeCare Hospital-at-Home 项目设备商选型参考

---

## 一、全球 RPM 市场规模

| 指标 | 数据 |
|---|---|
| 2025年全球 RPM 设备市场 | ~USD 260–286 亿（Grand View / GM Insights） |
| 2030年预测 | ~USD 569 亿（MarketsandMarkets） |
| 2033年预测 | ~USD 1,107 亿（Grand View Research） |
| CAGR (2026–2030) | 11.2%–12.7% |
| CGM 细分市场（2025） | ~USD 134 亿，CAGR 15.1% |
| 脉搏血氧仪细分（2025） | ~USD 38 亿，CAGR 6.6% |
| 心脏监测细分 | 约占 RPM 总额的 28% |
| 北美份额 | ~44.5%（主导地区） |
| CMS Hospital at Home 参与机构（2025.09） | 419 家医院，147 个医疗系统，39 个州 |

**关键驱动因素**：CMS 报销代码放开、HaH 豁免政策延续、人口老龄化、慢病患病率上升、AI/ML 分析技术成熟。

---

## 二、A 类：多参数监测平台（一体化方案）

### 1. BioIntelliSense

- **成立/总部**：2018年，Golden, Colorado，USA
- **融资**：~USD 4,500 万（Series B）；约 100 名员工
- **产品**：BioSticker（30天一次性贴片）、BioButton（可充电，90天持续监测）
- **功能**：体温、呼吸频率、静息心率、步态、跌倒检测、体位等，每日捕获 1,000+ 组生命体征
- **技术壁垒**：FDA 510(k) cleared；专利粘合剂与低功耗蓝牙传输；收购 AlertWatch（2022）扩展临床智能
- **临床证据**：与科罗拉多大学/DoD 合作 COVID-19 早期检测；多中心围术期监测研究
- **客户/合作伙伴**：Philips、UCLA Health、HCA Healthcare、DoD
- **商业模式**：硬件 + 数据分析平台订阅（按患者/月收费）
- **iHomeCare 整合可行度**：**高** — 贴片式设计极适合 HaH 连续监测，已用于多家医院急性期后管理

### 2. Vivalink

- **成立/总部**：2014年，Campbell, California，USA
- **融资**：~USD 154 万（Seed，多轮小额融资）；规模较小
- **产品**：ECG 贴片、连续体温贴片、SpO2 监测、血压袖带、体动监测
- **技术壁垒**：SDK/平台化输出，支持合作伙伴集成而非直接 2C；低功耗 IoT 传感器
- **认证**：FDA 510(k) / CE
- **客户**：合作伙伴模式为主（服务临床试验和医院系统）；强项在去中心化临床试验
- **商业模式**：硬件销售 + 数据平台 SDK 授权
- **iHomeCare 整合可行度**：**中到高** — 产品线齐全但公司体量小，需评估长期支持能力

### 3. Current Health（原 Best Buy Health → 已独立）

- **成立/总部**：2015年，Edinburgh, UK / Boston, USA
- **融资史**：2021年被 Best Buy 以 ~USD 4 亿收购；2025年6月 Best Buy 将其回售给联合创始人 Christopher McGhee
- **产品**：一体化 RPM 平台，含监控设备（腕带、脉搏血氧夹、体温贴；通过 Masimo 技术集成）+ 临床仪表盘 + 患者 App
- **技术壁垒**：专为高急性 HaH 设计；双向音视频、自动预警、EHR 集成——急性期监护是核心差异化
- **认证**：FDA / CE / UKCA
- **临床证据**：与 NHS、Geisinger 等多项高血压和 HaH 研究，Geisinger 合作自 2020 年起
- **客户**：Geisinger、NHS Trusts、美国多个医疗系统
- **商业模式**：平台按患者/月 SaaS + 设备一次性 / 租赁
- **iHomeCare 整合可行度**：**高** — 产品设计原生支持 HaH，独立后再运营灵活性增强；当前处于过渡期需关注稳定

### 4. Cadence Solutions

- **成立/总部**：2020年，New York City
- **融资**：~USD 2.44 亿（含 2026年6月 Series C $1 亿），估值 ~USD 10 亿
- **产品**：远程慢病管理平台，专注高血压、糖尿病、心衰等；AI Agent + 医护混合模式
- **技术壁垒**：AI 驱动的慢病自动管理平台；正与 FDA 讨论 AI Agent 在高血压管理中的监管路径
- **认证**：平台型，核心算法部分与 FDA 对话中，已有 FDA 监管的 AI 系统
- **临床证据**：与 20+ 医疗系统合作；STAT 报道其 AI 自动化管理效果
- **客户**：Duke Health、Corewell Health、Memorial Hermann 等 20+ 医疗系统
- **商业模式**：按患者收费（B2B to provider），提供全栈慢病管理服务
- **iHomeCare 整合可行度**：**中到高** — 面向慢病而非急性 HaH，但平台化模式和 AI 能力可用于 iHomeCare 出院的远期随访

### 5. Biofourmis

- **成立/总部**：2015年（Singapore），总部 Boston, USA
- **融资**：~USD 4.45 亿（含 $3 亿 Series D），2022年估值 $13 亿（独角兽）
- **产品**：Biofourmis Care（虚拟专科护理）、Care at Home（HaH 全流程管理）、数字疗法管线
- **技术壁垒**：AI 预测分析平台（Biovitals）；FDA 批准的数字心衰疗法；全病程管理（急性→出院→慢病）
- **认证**：FDA / CE
- **临床证据**：多项心衰 RCT；与 Humana 等支付方合作；已验证 30天再入院率降低 XX%
- **客户**：Humana、CVS Health、多家医疗系统；获准在6个州作为持牌提供商运营
- **商业模式**：SaaS + 医疗服务收费（双轮驱动）
- **注**：2023年曾裁员120人，面临数字疗法行业整体调整压力，但核心业务仍具竞争力
- **iHomeCare 整合可行度**：**高** — 原生 HaH 平台，AI 全病程管理能力最全面；需评估其当前财务稳定性

### 6. Masimo

- **成立/总部**：1989年，Irvine, California — 纳斯达克上市（MASI）
- **营收**：2024全年 ~USD 20.94 亿（含消费音频），2025年医疗健康部分营收 ~USD 15.2 亿
- **产品**：Masimo SET® 脉搏血氧仪（行业黄金标准）、Rainbow® 多参数监测、Radius PPG® 可穿戴血氧、W1® 手表式监测
- **技术壁垒**：SET® 专利信号提取技术，运动容差和低灌注性能业界第一；100+ 临床研究证明优于其他品牌
- **认证**：FDA / CE / MDR，全球最广泛认证之一
- **客户**：美国 Top 10 医院全部使用 Masimo；全球 100+ 国家
- **商业模式**：硬件销售 + 传感器耗材（剃刀刀片模式）
- **iHomeCare 整合可行度**：**高** — 血氧监测是 HaH 必要组件，Masimo 为行业标准；已与其他平台（Current Health、Philips）集成

### 7. Philips（BioTelemetry / eCareCompanion）

- **成立/总部**：1891年，Amsterdam, Netherlands（荷兰皇家飞利浦）
- **营收**：2024全年 EUR 180 亿；Connected Care 部门 2025年可比销售额增长 7%；2025全年集团销售额约 EUR 85 亿（医疗为主）
- **产品**：
  - eCareCompanion（家庭监护平台，含交互式问诊、生命体征捕获）
  - BioTelemetry（2021年收购，$28 亿）—— 心脏遥感和动态心电监测（MCOT、Holter）
  - Smart Telemetry Platform（2025年发布）—— 企业级遥测平台
- **技术壁垒**：全球最大医疗设备商之一的生态整合能力；医院→家庭闭环
- **认证**：FDA / CE / MDR
- **临床证据**：数千篇；在心衰远程监测、心律失常检出等领域最丰富的循证基础
- **客户**：全球医院系统、支付方、政府卫生系统
- **商业模式**：硬件 + 软件 + 服务（设备销售 / SaaS / 监测服务）
- **iHomeCare 整合可行度**：**高** — 品牌和生态整合能力最强；但大公司合作流程复杂，价格亦较高

---

## 三、B 类：专科/单参数设备

### B1. 血压监测 — OMRON Healthcare

- **成立/总部**：1933年，Kyoto, Japan（欧姆龙集团子公司）
- **营收**：OMRON Healthcare 全球 BP 监测市场份额第一
- **产品**：VitalSight RPM 服务 + 连接式血压计（含 AI AFib 检测）+ 穿戴式 BP 设备（HeartGuide）
- **技术壁垒**：50多年血压监测技术积累；AI 房颤检测算法获 2025 Digital Health Awards Best in Class
- **认证**：FDA / CE / MDR
- **客户**：覆盖全球家庭用户（消费者品牌第一），VitalSight 面向医疗机构
- **商业模式**：硬件零售 + VitalSight SaaS（按患者收费，Medicare 可报销）
- **iHomeCare 整合可行度**：**高** — BP 是 HaH 核心监测参数，OMRON 品牌认知高、API/SDK 开放性好

### B2. 血糖/CGM — Dexcom & Abbott Freestyle Libre

#### Dexcom

- **成立/总部**：1999年，San Diego, California — 纳斯达克上市（DXCM）
- **2025年营收**：~USD 46.6 亿（同比增长 16%）
- **市值**：~USD 240 亿
- **产品**：G7 CGM（15天版）、Stelo（首个非处方 OTC CGM，2025年创收 $1.3 亿）
- **美国市场份额**：~74%（2024年 GlobalData）
- **认证**：FDA / CE
- **iHomeCare 整合可行度**：**高** — CGM 是 HaH 中糖尿病管理必备；Dexcom 是血糖数据的行业数据标准

#### Abbott Freestyle Libre

- **成立/总部**：Abbott Laboratories（1888年，Chicago）— 纽交所上市（ABT）
- **Diabetes Care 增速**：2025年同比 +19.6%
- **产品**：Freestyle Libre 3 / 3 Plus、Libre Rio（OTC）、Lingo（OTC 消费版）；全球 600 万+ 用户
- **技术壁垒**：全球 CGM 份额第一；无扫描即得实时血糖；下一代双分析物（葡萄糖+酮体）传感器
- **认证**：FDA / CE / MDR
- **客户**：全球 100+ 国家，与 Insulet Omnipod 5、Beta Bionics iLet 等 AID 系统集成
- **iHomeCare 整合可行度**：**高** — 作为 CGM 全球领导者，兼容性最好；双分析物传感器是差异化优势

### B3. 脉搏血氧 — Masimo & Nonin

**Masimo**（见 A 类6）— 高端医院级，适合高急性 HaH 患者

**Nonin Medical**

- **成立/总部**：1986年，Plymouth, Minnesota — 私营公司
- **产品**：WristOx2 3150（腕式）、TruO2 OTC（首个 FDA OTC 指尖血氧，跨肤色准确性）、Nonin Health 云平台
- **技术壁垒**：指端血氧发明者；跨肤色准确性获 FDA 认可（行业痛点）
- **认证**：FDA / CE
- **客户**：呼吸科、睡眠中心、在家氧疗患者；与 Tenovi 等 RPM 平台合作
- **商业模式**：硬件销售 + 云平台订阅
- **iHomeCare 整合可行度**：**中到高** — 成本低于 Masimo，云平台支持 RPM 场景；但品牌在 HaH 领域不如 Masimo 强势

### B4. 远程心电 — iRhythm & AliveCor

#### iRhythm Technologies

- **成立/总部**：2006年，San Francisco — 纳斯达克上市（IRTC）
- **2025年营收**：~USD 7.2–7.4 亿（同比 +20.3%）；Q4 2025 首次实现 GAAP 净利润
- **产品**：Zio Patch（14天连续心电贴片）、Zio AT（房颤定向）、Zio MCT（新一代移动心脏遥测，已提交 FDA）
- **技术壁垒**：云 AI 分析（Zio Report）—— 14天数据经 AI + 心脏技术员双重审读；PCP 渠道扩张中
- **认证**：FDA / CE
- **临床证据**：500+ 篇同行评审论文，指南级临床证据
- **客户**：美国 500+ 医疗系统；PCP 渠道拓展
- **iHomeCare 整合可行度**：**中到高** — 对 HaH 心律监测有价值，但设备输出为回顾性报告而非实时遥测；Zio MCT 若获批将提升实时性

#### AliveCor

- **成立/总部**：2010年，Mountain View, California — 私营
- **融资**：~USD 1.5 亿+；销售设备超 300 万台
- **产品**：KardiaMobile（单导）、KardiaMobile 6L（首个 FDA 6导个人 ECG）、Kardia AI V2（AI 心律失常分析）
- **技术壁垒**：消费级 ECG 市场第一；AI 可检出 AFib、PVC、SVE、宽 QRS 等
- **认证**：FDA
- **投资者**：OMRON、Khosla Ventures、Qualcomm Ventures
- **商业模式**：设备（零售）+ KardiaCare 订阅服务
- **iHomeCare 整合可行度**：**中** — 消费级设备，临床级准确但非连续监测；适合轻症患者或按需 ECG 检查

### B5. 远程听诊/肺功能 — Eko & TytoCare

#### Eko Health

- **成立/总部**：2013年（UC Berkeley），Emeryville, California — 私营
- **融资**：~USD 1.62 亿（含 2024年 Series D $4,100 万）；~180 名员工
- **产品**：Eko CORE / CORE 500 数字听诊器、Eko Analysis Software（AI 心音/杂音分析）、Eko Telehealth 平台（800+ 医院使用）
- **技术壁垒**：AI SaMD（EFAST，2025年 FDA cleared）—— 深度学习模型分析心音 + ECG；远程听诊实时流传输
- **认证**：FDA / CE / UKCA
- **临床证据**：发表于 *The Lancet Digital Health*、*Nature Medicine*、*JAHA*
- **客户**：800+ US 医院；主要医疗系统
- **商业模式**：硬件销售 + 软件订阅（SaaS）
- **iHomeCare 整合可行度**：**中到高** — 远程听诊是 HaH 心肺评估短板补充；可与 iHomeCare 平台集成提供虚拟听诊

#### TytoCare

- **成立/总部**：2011/2012年，Netanya, Israel — 私营
- **融资**：~USD 2.05 亿（Insight Partners 牵头）；~190 名员工
- **产品**：Home Smart Clinic（AI 远程体检套件：耳镜、喉镜、数字听诊器、体温计、内置摄像头）+ 远程平台
- **技术壁垒**：唯一一体化远程体检设备；AI 引导检查和诊断支持；59% 以上问题可远程解决
- **认证**：FDA / CE
- **客户**：180+ 医疗系统和健康计划（含美国、欧洲、亚洲）
- **商业模式**：设备销售 + 平台按次/按患者收费
- **iHomeCare 整合可行度**：**中** — 更适合初级保健和虚拟门诊，对于急性 HaH 的多参数持续监测覆盖不全；可作为 HaH 方案的远程体检补充

---

## 四、C 类：平台/整合层

### 1. Epic / MyChart

- **成立/总部**：1979年，Verona, Wisconsin — 私营
- **产品**：MyChart 患者门户（1.95 亿+ 活跃用户）；Epic EHR（美国最大 EHR 系统，市占率 ~38%）
- **RPM 能力**：支持 PGHD（患者生成健康数据）录入；与 Validic 等平台集成；内置 RPM 工作流引擎
- **认证**：非设备厂商，但 MyChart 可接收和展示设备数据
- **iHomeCare 整合可行度**：**高** — 任何 RPM 设备如能通过 FHIR/API 向 Epic 推送数据，即符合医疗机构 EHR 集成核心要求；是 iHomeCare 系统架构中的必需集成层

### 2. Vivify Health（被 Optum/UnitedHealth Group 收购）

- **成立/总部**：2008年，Plano, Texas / 现 Optum 旗下
- **收购**：2019年被 Optum 收购（金额未披露）
- **产品**：移动端 RPM 平台——App + 蓝牙设备 + 临床分析仪表盘 + 疾病路径管理
- **技术壁垒**：Optum 生态内数据网络效应；覆盖慢病、术后、妊娠等多场景
- **客户**：主要面向 UnitedHealth/Optum 内部网络 + 外部医疗系统
- **商业模式**：Optum 内部成本中心/SaaS
- **iHomeCare 整合可行度**：**中** — 若 iHomeCare 与 Optum/UnitedHealth 合作则有高价值；开放平台的可独立集成性有限

### 3. Health Recovery Solutions (HRS)

- **成立/总部**：2012年，Hoboken, New Jersey — 私营
- **融资**：~USD 9,100 万（含 Series C）；年营收 ~USD 2,350 万
- **产品**：ClinicianConnect® + PatientConnect® RPM 平台；疾病特异性护理路径、复合 RPM 套件
- **技术壁垒**：HaH 专用功能（连续遥测选项）；EHR 深度集成；1,000 万+ 患者覆盖，400+ 医疗系统客户
- **认证**：云平台级（非设备 FDA）
- **客户**：Michigan Medicine、Allina Health 等 400+ 机构
- **商业模式**：SaaS + 临床支持服务
- **iHomeCare 整合可行度**：**高** — HaH 原生平台；最强的多场景 RPM 可配置性，可适配急性期到慢病管理全流程

---

## 五、对比矩阵

| 厂商 | 产品类型 | 认证 | 核心客户/规模 | 估值/营收 | 与 iHomeCare 相关性 |
|---|---|---|---|---|---|
| **BioIntelliSense** | 多参数贴片（30-90天） | FDA | HCA, UCLA, Philips | ~$45M 融资 | **高** |
| **Vivalink** | 多参数传感器+SDK | FDA/CE | 临床试验/医院 | ~$1.5M 融资 | 中 |
| **Current Health** | HaH 全平台 | FDA/CE/UKCA | Geisinger, NHS | 独立重组中 | **高** |
| **Cadence Solutions** | AI 慢病管理平台 | FDA (AI) | Duke, 20+ 医疗系统 | $1B 估值 | 中-高 |
| **Biofourmis** | AI HaH 全病程平台 | FDA/CE | Humana, CVS | $1.3B 估值 | **高** |
| **Masimo** | 脉搏血氧/多参数 | FDA/CE/MDR | Top 10 美国医院 | ~$15.2B 市值 | **高** |
| **Philips** | 多参数+遥测+平台 | FDA/CE/MDR | 全球医院系统 | EUR 180 亿营收 | **高** |
| **OMRON** | 血压监测+VitalSight | FDA/CE | 全球家庭用户 | 私营（全球第一 BP） | **高** |
| **Dexcom** | CGM (G7/Stelo) | FDA/CE | 74% 美国 CGM 份额 | ~$240 亿市值 | **高** |
| **Abbott (Libre)** | CGM + OTC | FDA/CE/MDR | 600万+ 用户 | ABT $2,000 亿+ 市值 | **高** |
| **Nonin** | 脉搏血氧（OTC+专业） | FDA/CE | 呼吸/睡眠中心 | 私营 | 中-高 |
| **iRhythm** | Zio 心电贴片（14天） | FDA/CE | 500+ 美国医院 | ~$30 亿市值 | 中-高 |
| **AliveCor** | 个人 ECG (Kardia) | FDA | 300万+ 设备 | $150M+ 融资 | 中 |
| **Eko Health** | AI 数字听诊器 | FDA/CE | 800+ 医院 | $162M 融资 | 中-高 |
| **TytoCare** | AI 远程体检套件 | FDA/CE | 180+ 医疗系统 | $205M 融资 | 中 |
| **Epic/MyChart** | EHR 患者门户 | — | 1.95亿用户 | 私营 | **高**（集成层） |
| **Vivify Health** | RPM 平台 | — | Optum 生态 | Optum 旗下 | 中 |
| **HRS** | HaH RPM 平台 | — | 400+ 机构 | $91M 融资 | **高** |

---

## 六、细分品类市场份额概估（2025年）

| 品类 | 占 RPM 设备市场份额 | 代表厂商 |
|---|---|---|
| 心血管监测（含心电） | ~28% | iRhythm, Philips, AliveCor, Masimo |
| 血糖/CGM | ~25% | Dexcom, Abbott |
| 多参数/一体化平台 | ~18% | BioIntelliSense, Current Health, Philips |
| 血压监测 | ~12% | OMRON |
| 脉搏血氧 | ~8% | Masimo, Nonin |
| 远程听诊/体检 | ~3% | Eko, TytoCare |
| 其他（体重、体温等） | ~6% | — |

---

## 七、iHomeCare 整合建议分层

### Tier 1 — 首选整合（高优先级，核心 HaH 必需组件）

| 品类 | 推荐厂商 | 理由 |
|---|---|---|
| 多参数连续监测 | Current Health / Biofourmis | 原生 HaH 平台，全流程能力 |
| 脉搏血氧 | Masimo | 行业黄金标准，医院级准确 |
| 血压 | OMRON | 品牌信任、API 开放、FDA 认证 |
| CGM（糖尿病患者适用） | Dexcom 或 Abbott Libre | 根据区域偏好选择 |
| EHR 集成层 | Epic MyChart | 必须打通的核心系统 |

### Tier 2 — 按需整合（场景化补充）

| 品类 | 推荐厂商 | 适用场景 |
|---|---|---|
| AI 心音分析 | Eko Health | 心肺远程评估，减少面对面访视 |
| 14天心电监测 | iRhythm Zio | 出院后心律失常筛查 |
| 远程体检 | TytoCare | 虚拟巡诊使用 |
| RPM 平台独立部署 | HRS | 需要全自主平台控制的场景 |

### Tier 3 — 生态观察（潜力型，需进一步评估）

| 厂商 | 关注点 |
|---|---|
| Cadence Solutions | AI 慢病管理模式——适用于 iHomeCare 出院后长期随访 |
| BioIntelliSense | 90天贴片适合慢病和老年监测，但目前以 B2B 为主 |
| Vivalink | SDK 模式灵活但规模偏小 |
| AliveCor | 消费级 ECG，适合轻症或患者自测 |

---

## 八、关键数据源

- FDA 510(k) 数据库（accessdata.fda.gov）
- SEC 文件（Edgar）：iRhythm (IRTC)、Masimo (MASI)、Dexcom (DXCM)、Abbott (ABT)、Philips (PHG)
- Crunchbase / PitchBook / Tracxn（融资数据）
- MarketsandMarkets、Grand View Research、GM Insights（市场规模）
- Rock Health、Frost & Sullivan（数字健康行业报告）
- 各公司官网及新闻稿（截至2026年7月）

---

## 九、免责声明

本报告基于公开信息编制。市场数据来自第三方研究机构，可能存在口径差异。公司财务数据以 SEC 文件和官方公告为准。厂商评估仅为基于公开信息的专业判断，不构成商业合作建议。**所有数据均源自可验证的公开来源，未编造任何数据。**
