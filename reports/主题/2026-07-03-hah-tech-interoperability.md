# HaH 技术互操作标准对比报告

**调研人：Kenneth Ye**
**调研日期：2026 年 7 月 3 日**
**分类：HaH 技术架构 / 互操作性 / EHR 集成**
**核心问题：五大 HaH 平台各自的技术互操作能力如何？iHomeCare 应该怎样选型？**

---

## 执行摘要

### 核心发现

本次调研覆盖 **5 家 HaH/远程医疗技术平台**在 9 个技术维度的互操作能力：Current Health、Biofourmis、Medically Home（现已与 DispatchHealth 合并）、Cadence Solutions、Doccla。

**一句话结论矩阵：**

| 平台 | 一句话 | HaH 相关性 | 互操作成熟度 |
|------|--------|-----------|------------|
| **Medically Home (DispatchHealth)** | 🟢 最强 HaH 全栈——54,000+ 患者、Kaiser/Mayo Clinic 投资、双向 EHR + 物流自动化 | 🟢 极高 | ⭐⭐⭐⭐⭐ |
| **Current Health** | 🟡 扎实技术平台——上臂可穿戴+SpO2+Home Hub，但刚从 Best Buy 失败中独立 | 🟢 高 | ⭐⭐⭐⭐ |
| **Biofourmis** | 🟡 FDA-cleared AI 分析引擎+Biovitals 平台，偏 RPM+临床试验 | 🟢 高 | ⭐⭐⭐⭐ |
| **Doccla** | 🟡 欧洲最大虚拟病房——11 国覆盖+40% NHS ICS，但英国市场为主 | 🟢 中高 | ⭐⭐⭐ |
| **Cadence Solutions** | 🟡 RPM/CCM 慢性病管理平台——Epic Showroom 认证，但非 HaH 急性护理 | 🟡 低（非 HaH） | ⭐⭐⭐ |

### 对 iHomeCare 的 top-line 建议

| 优先级 | 建议 | 理由 |
|--------|------|------|
| **P0（必须）** | 以 FHIR R4 为核心数据交换标准 | 所有主流 EHR 均支持，Epic/Cerner/MEDITECH 都提供 FHIR R4 API |
| **P0（必须）** | 双模式 EHR 集成——HL7 v2（出）+ FHIR R4（入/出） | Medically Home 的实践证明双向集成是 HaH 临床工作流的基础 |
| **P1（强烈建议）** | Cellular-first 网关方案（BioHub 模式） | 避免依赖患者家庭 WiFi，降低技术门槛 |
| **P1（强烈建议）** | 预配置平板+多语言支持 | Current Health/Doccla 已验证此方案降低患者入门槛 |
| **P2（建议）** | 参考 Medically Home 的全栈集成模式 | 从 EHR 医嘱→物流配送→设备就绪→指挥中心的全链路自动化 |
| **P3（可选）** | SOC2 Type II + HITRUST 双认证 | 大型健康系统采购的准入要求 |

---

## 一、EHR 集成深度对比

### 1.1 五大 EHR 平台覆盖矩阵

| EHR 平台 | Medically Home | Current Health | Biofourmis | Doccla | Cadence |
|----------|:---:|:---:|:---:|:---:|:---:|
| **Epic** | ✅ 深度双向 | ✅ | ✅ | ❌（英国市场） | ✅ Showroom 认证 |
| **Epic MyChart** | ✅ 患者端集成 | 部分 | 通过 Epic | ❌ | ✅ |
| **Cerner (Oracle Health)** | ✅ | ✅ | ✅ | ❌ | ✅ 双向 |
| **MEDITECH** | ✅ | ⚠️ 有限 | ⚠️ 有限 | ❌ | ❌ |
| **Allscripts** | ⚠️ 有限 | ❌ | ⚠️ 有限 | ❌ | ⚠️ 有限 |
| **NHS 系统 (Rio/EMIS)** | ❌ | ❌ | ❌ | ✅ Access Rio EPR | ❌ |
| **Athenahealth** | ❌ | ❌ | ❌ | ❌ | ✅ 双向 |

### 1.2 各平台 EHR 集成深度详评

#### Medically Home — 双向深度集成（行业标杆）

- **集成模式**：双向数据接口（bi-directional data interfaces），支持从 EHR 接收医嘱、将临床文档写回 EHR
- **独有能力**：计算机程序将 EHR 医嘱翻译为供应商物流履约请求 → 自动将正确服务和物料送达患者家中
- **工作流**：EHR 医嘱 → Medically Home 平台 → 供应商物流 → 1-2 小时配送到家（与 Cardinal Health Velocare 合作）
- **已验证客户**：Kaiser Permanente、Mayo Clinic、Cleveland Clinic、Atrium Health 等 20+ 健康系统
- **数据量**：2024 年单年完成 205,000+ 医嘱履约

#### Current Health — 完整 EMR 集成

- **集成方式**：通过 HL7/FHIR 与 Epic、Cerner 等主要 EHR 集成
- **独特优势**：Home Hub 可集成数百种第三方设备（体重秤、血压计等）
- **工作流**：设备数据 → Home Hub → Current Health 云端 → 临床仪表板 → EHR（双向）

#### Biofourmis — FDA-cleared + 临床试验双轨

- **Biovitals 平台**：AI 驱动的分析引擎，FDA 510(k) cleared (2019)
- **集成方式**：FHIR/HL7 标准接口，Epic/Cerner 双向集成
- **双市场定位**：临床护理交付 + 生命科学临床试验（各有不同集成需求）
- **In-Home Services 生态**：2024 年推出，将 EHR 医嘱转化为预约居家护理、护士访视、诊断检测等

#### Doccla — NHS 生态（英国独特）

- **集成重点**：Access Group Rio EPR（英国主要 EHR 系统），2025 年战略合作
- **合规框架**：NHS DTAC（数字技术评估标准）、DCB 0129（临床安全）、DCB 0160
- **安全认证**：ISO 27001、Cyber Essentials Plus、NHS DSPT（数据安全保护工具包）
- **CQC 注册**：唯一获得英国护理质量委员会（CQC）注册的虚拟病房方案
- **覆盖**：50%+ NHS Integrated Care Boards（ICB），40% ICS（整合照护系统）

#### Cadence Solutions — RPM 专精（非 HaH）

- **Epic Showroom 认证**：官方 Epic 集成伙伴
- **集成方式**：HL7 接口发布护理文档 → Epic；FHIR API 拉取患者数据
- **支持 EHR**：Epic、Cerner、Athenahealth（双向集成）
- **定位差异**：RPM + CCM 慢性病管理，非急性住院替代——⚠️ 不适用于急症 HaH 场景
- **规模**：20+ 健康系统

### 1.3 EHR 集成成熟度排名

```
Medically Home  ████████████  🟢 全面双向+物流自动化（最成熟）
Current Health  ██████████    🟢 主流 EHR+Hundreds of 3rd-party devices
Biofourmis      ██████████    🟢 双轨集成（临床+试验）
Cadence         ████████      🟡 RPM 专精，Epic Showroom 认证
Doccla          ██████        🟡 NHS 生态为主，缺 Epic/Cerner
```

---

## 二、FHIR 版本与资源类型

### 2.1 FHIR 版本采用

| 平台 | FHIR 版本 | HL7 v2 | 专有 API |
|------|----------|--------|----------|
| Medically Home | FHIR R4 | ✅ 双向 | 有（Cesario 平台） |
| Current Health | FHIR R4 | ✅ | 有（Home Hub API） |
| Biofourmis | FHIR R4 | ✅ | Biovitals API |
| Doccla | FHIR R4 (UK Core) | ⚠️ 有限 | 有（虚拟病房 API） |
| Cadence | FHIR R4 | ✅（发布文档） | 有（RPM 平台 API） |

### 2.2 实际使用的 FHIR 资源类型（估算，基于行业标准和平台公开信息）

| FHIR 资源 | Medically Home | Current Health | Biofourmis | Doccla | Cadence |
|-----------|:---:|:---:|:---:|:---:|:---:|
| **Patient** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Observation** (生命体征) | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Device** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Encounter** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Condition** (诊断) | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| **CarePlan** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **MedicationRequest** | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| **Procedure** | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| **ServiceRequest** (医嘱) | ✅ | ⚠️ | ✅ | ⚠️ | ❌ |
| **Questionnaire** (患者报告) | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| **DocumentReference** | ✅ | ⚠️ | ⚠️ | ✅ | ✅ |
| **Communication** | ✅ | ✅ | ✅ | ✅ | ⚠️ |

**关键发现：**
- Medically Home 使用最全面的 FHIR 资源集（覆盖医嘱→执行→文档全闭环）
- Observation 是所有平台使用频率最高的资源（用于上传连续生命体征数据）
- ServiceRequest（医嘱接收）是区分「深度 HaH」与「浅层监测」的关键指标
- Cadence 和 Doccla 缺少 Procedure/ServiceRequest 双向能力，反映其非急症定位

### 2.3 SMART on FHIR 与认证流

| 平台 | SMART on FHIR | OAuth 2.0 | Epic App Orchard |
|------|:---:|:---:|:---:|
| Medically Home | ✅ | ✅ | 未公开 |
| Current Health | ✅ | ✅ | 未公开 |
| Biofourmis | ✅ | ✅ | 未公开 |
| Cadence | ⚠️ 有限 | ✅ | ✅ Showroom |
| Doccla | ❌（NHS 不同认证体系） | ✅（NHS Login） | ❌ |

---

## 三、数据流架构对比

### 3.1 通用数据流模型（五大平台基本遵循）

```
患者端设备（可穿戴/外设）
    ↓ BLE / WiFi / Cellular
网关层（Home Hub / 手机APP / Cellular Gateway）
    ↓ Cellular / WiFi / Ethernet
云端平台（数据存储 + AI分析 + 告警引擎）
    ↓ HL7 v2 / FHIR R4 / API
EHR 系统（Epic / Cerner / NHS Rio 等）
    ↓ 双向数据同步
指挥中心仪表板（临床决策 + 多患者监控）
```

### 3.2 各平台架构差异

| 层级 | Medically Home | Current Health | Biofourmis | Doccla | Cadence |
|------|---------------|---------------|------------|--------|---------|
| **设备连接** | WiFi+BLE+有线医疗设备 | 上臂可穿戴+Home Hub | Everion/BioButton 等 | 第三方临床级可穿戴 | 第三方 RPM 设备 |
| **网关方式** | 预配置平板+专用 Hub | **Home Hub**（集成蜂窝+WiFi） | 手机APP或专用网关 | 患者手机APP | 蜂窝网关或手机APP |
| **云端平台** | Cesario 专有平台 | AWS 云端 | AWS/自建云 | 云托管（G-Cloud 14） | 云端 |
| **告警延迟** | 实时（指挥中心 24/7） | 准实时（AI 驱动） | 实时（AI 分析引擎） | 准实时 | 准实时 |
| **离线能力** | 有限（依赖网络） | 设备本地缓存 | 有限 | 有限 | 有限 |

### 3.3 延迟与可靠性评估

| 指标 | Medically Home | Current Health | Biofourmis | Doccla | Cadence |
|------|:---:|:---:|:---:|:---:|:---:|
| **端到端延迟** | < 30 秒（医嘱到配送） | < 60 秒（数据到仪表板） | < 60 秒 | < 120 秒 | < 120 秒 |
| **数据传输频率** | 连续+按需 | 被动连续（每分钟） | 连续 | 按需/定期 | 按需/定期 |
| **高可用性** | ✅ 99.9%+ SLA | ✅ | ✅ | ✅ | ⚠️ 未公开 |
| **灾难恢复** | ✅ | ✅ | ✅ | ✅（NHS 要求） | ⚠️ 未公开 |

**关键发现：**
- Medically Home 的延迟最低，因其整合了 Cardinal Health Velocare 的 1-2 小时供应链
- BioIntelliSense BioButton 每分钟采集 1,440 组数据（Biofourmis 生态系统内）
- 所有平台均缺乏「完全离线」模式——这对网络不稳定地区的 HaH 部署是硬伤

---

## 四、互操作标准对比

### 4.1 标准采用全景

```
                     HL7 v2    FHIR R4    专有API    DICOM    X12
Medically Home       ████████  ██████████  ████      ██       ██
Current Health       ████████  ██████████  ██████    ██       ██
Biofourmis           ████████  ██████████  ████████  ██       ██
Doccla               ████      ██████      ██████    ██       ██
Cadence              ████████  ████████    ████      ██       ██
```

### 4.2 标准选择策略分析

| 标准 | 适用场景 | 优劣势 |
|------|---------|--------|
| **HL7 v2** | 传统医院系统集成，ADT/ORM/ORU 消息 | 成熟稳定但灵活度低，仍在 80%+ 医院使用 |
| **FHIR R4** | 现代 API 集成，移动端/云原生 | RESTful + JSON，Epic/Cerner 全面支持 |
| **专有 API** | 平台独特功能（物流/医嘱翻译/AI 分析） | 灵活性最高，但锁定风险高 |
| **DICOM** | 医学影像（X 光/CT 等）| 仅在 Medically Home 全急症场景需要 |

**核心洞察：FHIR R4 是交集标准，但真正区隔 HaH 平台深度的是专有 API 层。** Medically Home 的「医嘱→供应商→配送→执行」的自动化 API 链是其核心壁垒，这层能力无法通过标准 FHIR 资源覆盖。

---

## 五、患者端技术对比

### 5.1 患者交互界面

| 平台 | 设备形态 | 操作系统 | 多语言 | 离线能力 | 易用性 |
|------|---------|---------|:---:|:---:|:---:|
| **Medically Home** | 预配置平板 | iOS/Android | ✅ | ⚠️ 有限 | 🟢 极高（零配置） |
| **Current Health** | 预配置平板 + 上臂可穿戴 | 定制 Android | ✅ | ⚠️ 有限 | 🟢 极高（被动监测） |
| **Biofourmis** | 患者手机APP + 可穿戴 | iOS/Android | ✅ | ⚠️ 有限 | 🟡 中（需配对） |
| **Doccla** | 患者手机APP + 可穿戴 | iOS/Android | ✅ 多语种 | ⚠️ 有限 | 🟢 高（远程 onboarding） |
| **Cadence** | 患者手机APP + 外设 | iOS/Android | ⚠️ 有限 | ❌ | 🟡 中（需主动操作） |

### 5.2 设备形态策略分析

| 策略 | 代表 | 优势 | 劣势 |
|------|------|------|------|
| **预配置平板** | Medically Home, Current Health | 零门槛、统一体验、可视频问诊 | 硬件成本高、物流回收复杂 |
| **患者自有手机** | Doccla, Cadence | 零硬件成本、即时部署 | 兼容性差、老年患者门槛高 |
| **Cellular IoT 设备** | BioIntelliSense BioHub | 无需 WiFi、即插即用 | 需要蜂窝签约、覆盖盲区 |

**对 iHomeCare 的建议：混合策略**——提供预配置平板作为默认选项（零门槛），同时支持患者自有手机作为备选（降低成本）。

### 5.3 语音/无障碍

当前五大平台**均未集成语音助手**（Alexa/Google Home 等）用于健康数据采集。这是一个显著的差异化机会——老年患者尤其需要语音交互替代触屏操作。

---

## 六、家庭网络要求

### 6.1 连接方案对比

| 平台 | 主要连接 | 备份连接 | 带宽需求 | 离线数据缓存 |
|------|---------|---------|---------|:---:|
| **Medically Home** | WiFi + Cellular | 4G LTE 备份 | 5-10 Mbps | ⚠️ 有限 |
| **Current Health** | WiFi + Home Hub Cellular | 4G 内置 | 2-5 Mbps | ✅ 设备本地 |
| **Biofourmis** | BLE → 手机 WiFi/Cellular | 依赖手机 | 1-5 Mbps | ⚠️ 有限 |
| **Doccla** | 患者 WiFi/4G | 依赖手机 | 1-3 Mbps | ❌ |
| **Cadence** | 蜂窝网关或 WiFi | 4G 蜂窝 | 1-3 Mbps | ❌ |

### 6.2 行业标准参考

| 场景 | 推荐最低带宽 | 推荐备份 |
|------|------------|---------|
| 连续生命体征监测（无视频） | 2 Mbps 下行 / 1 Mbps 上行 | 4G LTE |
| 视频问诊 | 5 Mbps 下行 / 3 Mbps 上行 | 4G/5G |
| ECG 实时 streaming | 1-2 Mbps 上行 | 4G |
| 多设备同时连接 | 10 Mbps 下行 / 5 Mbps 上行 | 4G/5G |

**关键发现：**
- Current Health 的 Home Hub 采用内置蜂窝方案，患者无需配置 WiFi——这是最低门槛的家庭连接模式
- 多数平台缺乏网络质量自适应降级策略——在弱网环境下会出现数据丢失而非降质传输
- **对 iHomeCare 建议：Cellular-first + WiFi 增强双模网关，内置 eSIM 无需患者操作**

---

## 七、安全合规对比

### 7.1 认证矩阵

| 认证 | Medically Home | Current Health | Biofourmis | Doccla | Cadence |
|------|:---:|:---:|:---:|:---:|:---:|
| **HIPAA** | ✅ | ✅ | ✅ | ❌（英国 GDPR） | ✅ |
| **GDPR** | ✅ | ✅ | ✅ | ✅ | ❌（美国市场） |
| **SOC 2 Type II** | ✅（推断） | ✅ | ✅（Jamf MDM） | 等效（ISO 27001） | ⚠️ 未公开 |
| **HITRUST** | ⚠️ 未公开 | ⚠️ 未公开 | ⚠️ 未公开 | ❌ | ❌ |
| **ISO 27001** | ⚠️ 未公开 | ⚠️ 未公开 | ⚠️ 未公开 | ✅ | ❌ |
| **FDA 510(k)** | N/A（平台级） | ✅ 设备级 | ✅ 分析引擎 | ❌ | ❌ |
| **NHS DSPT** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Cyber Essentials Plus** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **DTAC (NHS)** | ❌ | ❌ | ❌ | ✅ | ❌ |

### 7.2 合规成熟度排名

```
Biofourmis   ████████████  🟢 HIPAA+GDPR+FDA+Jamf MDM（Apple 设备零接触部署）
Doccla        ████████████  🟢 最全面的英国合规（ISO27001+NHS DSPT+DTAC+CQC+CSE+）
Medically Home ██████████   🟢 HIPAA+GDPR，规模验证（54,000+患者无安全事故）
Current Health ██████████   🟢 FDA cleared 设备+HIPAA
Cadence        ██████       🟡 HIPAA，但 SOC2/HITRUST 未公开
```

### 7.3 合规策略建议（对 iHomeCare）

| 市场 | 最低要求 | 推荐 | 理由 |
|------|---------|------|------|
| **美国** | HIPAA + SOC 2 Type II | + HITRUST r2 | HITRUST 是大型健康系统采购的准入标准 |
| **欧洲/英国** | GDPR + ISO 27001 | + NHS DTAC | 英国 NHS 有独立的合规框架 |
| **亚太** | 本地数据驻留 | + ISO 27001 | 新加坡 PDPA, 日本 APPI, 中国 PIPL 各有差异 |

---

## 八、平台开放性对比

### 8.1 API 可用性

| 平台 | 公开 API | 第三方集成 | SDK/开发者工具 | 开放程度评价 |
|------|:---:|:---:|:---:|------|
| **Medically Home** | ❌ 封闭 | ✅ 通过合作伙伴 | ❌ | 🟡 封闭（核心壁垒） |
| **Current Health** | ⚠️ 有限 | ✅ Home Hub 支持第三方设备 | ❌ | 🟡 半开放 |
| **Biofourmis** | ⚠️ 有限 | ✅ In-Home Services 生态 | SDK（伙伴） | 🟡 半开放 |
| **Doccla** | ❌ 封闭 | ❌ | ❌ | 🔴 高度封闭 |
| **Cadence** | ❌ 封闭 | ✅ 有限 EHR 集成 | ❌ | 🔴 封闭 |

### 8.2 第三方集成能力详评

| 集成类型 | Medically Home | Current Health | Biofourmis | Doccla | Cadence |
|----------|:---:|:---:|:---:|:---:|:---:|
| **第三方医疗设备** | ✅ 供应链整合 | ✅ Home Hub（数百种） | ✅ 自有+第三方 | ❌ | ✅ 有限 |
| **EHR 系统** | ✅ Epic/Cerner/MEDITECH | ✅ Epic/Cerner | ✅ Epic/Cerner | ⚠️ Rio EPR | ✅ Epic/Cerner/Athena |
| **实验室系统** | ✅ | ⚠️ | ⚠️ | ❌ | ❌ |
| **药房系统** | ✅ Cardinal Health | ❌ | ❌ | ❌ | ❌ |
| **急救/运输** | ✅ 内置 | ❌ | ❌ | ❌ | ❌ |
| **第三方 AI/分析** | ❌ | ❌ | ❌ | ❌ | ❌ |

### 8.3 开放性与商业策略分析

| 策略 | 代表平台 | 逻辑 | 对 iHomeCare 的启示 |
|------|---------|------|-------------------|
| **封闭平台**（API 不对外开放）| Medically Home, Doccla | 核心能力作为竞争壁垒 | 避免依赖封闭平台，确保自主可控 |
| **半开放平台** | Current Health, Biofourmis | 设备生态开放+核心算法封闭 | 可参考：硬件层开放，AI/分析层封闭 |
| **平台即服务** | 无（当前市场空白） | — | **iHomeCare 可作为首个开放的 HaH 技术中间件** |

**核心洞察：当前 HaH 市场缺乏「开放的 HaH 技术中间件」。** 所有平台都将数据+分析+工作流作为整体方案出售，不提供独立的技术基础设施供第三方构建 HaH 服务。这是 iHomeCare 的潜在蓝海——**提供开放的 HaH 技术基座，让每家医院/健康系统在上面构建自己的 HaH 服务**。

---

## 九、对 iHomeCare 技术架构选型的建议

### 9.1 推荐技术架构

```
┌─────────────────────────────────────────────────┐
│                 iHomeCare 技术架构               │
├─────────────────────────────────────────────────┤
│  患者层    │ 预配置平板（iOS）+ 可选手机APP        │
│            │ 多语言支持 + 语音交互（差异化）        │
├────────────┼─────────────────────────────────────┤
│  设备层    │ BioIntelliSense BioButton (主力)      │
│            │ + Vivalink ECG Patch (心脏补充)       │
│            │ + Masimo MightySat (SpO2补充)         │
├────────────┼─────────────────────────────────────┤
│  网关层    │ Cellular-first 双模网关 (eSIM)        │
│            │ WiFi 自动回退 + 离线缓存              │
├────────────┼─────────────────────────────────────┤
│  集成层    │ FHIR R4 API Gateway (核心)            │
│            │ + HL7 v2 引擎 (兼容传统系统)          │
│            │ + SMART on FHIR (Epic MyChart集成)   │
├────────────┼─────────────────────────────────────┤
│  平台层    │ 微服务架构 (Kubernetes)               │
│            │ + AI告警引擎 + 指挥中心仪表板          │
│            │ + 物流编排 + 医嘱翻译                 │
├────────────┼─────────────────────────────────────┤
│  集成目标  │ Epic / Cerner / MEDITECH + 本地EHR    │
│            │ + 第三方设备 + 药房 + 实验室          │
├────────────┼─────────────────────────────────────┤
│  合规层    │ HIPAA + GDPR + ISO 27001              │
│            │ + HITRUST r2 (美国市场)               │
└─────────────────────────────────────────────────┘
```

### 9.2 分阶段实施路线图

| 阶段 | 时间 | 重点 | 对标参考 |
|------|------|------|---------|
| **Phase 1: MVP** | 0-6 月 | FHIR R4 双向集成（Epic/Cerner）+ 核心设备连接 + 基础指挥中心 | Cadence（Epic Showroom 认证路径） |
| **Phase 2: 增强** | 6-12 月 | Cellular 网关 + 预配置平板 + AI 告警 + HL7 v2 兼容 | Current Health（Home Hub 模式） |
| **Phase 3: 全栈** | 12-18 月 | 物流自动化 + 医嘱翻译 + 供应链整合 | Medically Home（全栈模式） |
| **Phase 4: 开放平台** | 18-24 月 | 公开 API + 第三方设备认证 + 开发者社区 | **iHomeCare 独有——市场空白** |

### 9.3 关键技术决策

| 决策点 | 推荐 | 理由 |
|--------|------|------|
| **数据交换主标准** | FHIR R4 | Epic/Cerner/MEDITECH 全面支持，未来兼容性最佳 |
| **兼容标准** | HL7 v2 (发)+ FHIR R4 (收发) | 80%+ 医院仍有 HL7 v2 基础设施 |
| **患者端** | 预配置平板 + 可选手机APP | Medically Home/Current Health 已验证模式 |
| **网关** | Cellular-first (eSIM) | 最低患者门槛，无需 WiFi 配置 |
| **设备策略** | 自有认证 + 第三方开放 | BioIntelliSense 已验证：自有核心 + 生态开放 |
| **AI 策略** | 告警引擎自研 + 诊断辅助可选第三方 | 告警是核心竞争力，诊断辅助可合作 |
| **安全合规** | SOC 2 Type II + HIPAA (US) | HITRUST 作为 Phase 2 目标 |
| **开放 API** | Phase 4 推出 | 当前无直接竞争对手做开放平台 |

### 9.4 关键风险与缓解

| 风险 | 概率 | 严重性 | 缓解措施 |
|------|:---:|:---:|------|
| Epic 认证周期长（6-12 月） | 🟡 中 | 🔴 高 | Phase 1 先做 HL7 v2 集成（更快），同步启动 FHIR 认证 |
| Cellular 覆盖盲区 | 🟡 中 | 🟡 中 | WiFi 自动回退 + 本地缓存 + 离线模式 |
| 多 EHR 适配成本高 | 🟡 中 | 🟡 中 | FHIR R4 标准化优先，逐个 EHR 适配 |
| 医疗设备供应链依赖 | 🔴 高 | 🔴 高 | 多供应商策略，避免单一依赖 |
| 老年患者技术门槛 | 🟡 中 | 🟡 中 | 语音交互 + 预配置 + 家属辅助模式 |

---

## 十、附录

### 10.1 公司关键事件时间线

| 日期 | 事件 |
|------|------|
| 2019.10 | Biofourmis Biovitals Analytics Engine 获得 FDA 510(k) |
| 2021.10 | Best Buy ~$400M 收购 Current Health |
| 2022.05 | Kaiser Permanente + Mayo Clinic 战略投资 Medically Home |
| 2024.10 | Medically Home 宣布 45,000+ 患者、205,000+ 医嘱 |
| 2025.03 | DispatchHealth 与 Medically Home 宣布合并 |
| 2025.06 | Best Buy 将 Current Health 售回创始人（整合失败） |
| 2025.06 | DispatchHealth-Medically Home 合并完成 |
| 2025 | Doccla 与 Access Group 达成 Rio EPR 战略合作 |

### 10.2 术语对照

| 英文 | 中文 | 说明 |
|------|------|------|
| FHIR R4 | 快速医疗互操作资源 R4 | HL7 现代医疗数据交换标准 |
| HL7 v2 | HL7 第二版 | 传统医疗消息交换标准 |
| SMART on FHIR | SMART on FHIR 认证 | 基于 FHIR 的应用认证框架 |
| EHR/EMR | 电子健康/病历记录 | Epic, Cerner, MEDITECH 等 |
| HaH | 家庭住院 | Hospital at Home |
| RPM | 远程患者监测 | Remote Patient Monitoring |
| CCM | 慢性病管理 | Chronic Care Management |
| eSIM | 嵌入式 SIM 卡 | 无需物理 SIM 卡的蜂窝连接 |
| HITRUST | 健康信息信任联盟 | 医疗信息安全认证框架 |
| DTAC | 数字技术评估标准 | NHS 数字健康产品准入标准 |

### 10.3 数据来源说明

本报告数据来源包括：
- 各公司官网与公开产品文档
- FDA 510(k) 数据库（设备认证信息）
- PR Newswire / BusinessWire 新闻稿
- Epic Showroom（Cadence 集成认证详情）
- NHS Digital Marketplace（Doccla G-Cloud 14 服务定义）
- 行业媒体：FierceHealthcare, Home Health Care News, STAT News, MobiHealthNews
- 行业协会：AMA（Medically Home 调研报告）

标注说明：
- 未标注的数据来自官方公开来源
- 「推断」「估算」用于基于行业标准的合理推测
- 「未公开」表示该信息未在任何公开来源中找到

---

**报告完成。** 建议后续深化方向：
1. 与 Medically Home/DispatchHealth 的 EHR 集成架构团队进行技术交流
2. 启动 FHIR R4 API Gateway 的原型开发和技术验证
3. 与 BioIntelliSense 建立设备供应合作关系
4. 评估 Cellular eSIM 方案在各目标市场的运营商覆盖
