# Ontario Health atHome 深度分析报告

**Kate 调研团队 | 省级居家医疗模型对标分析**
**执笔：Kenneth Ye | 2026-07-03**

> 对标 iHomeCare：加拿大最大省级公共居家医疗系统的架构、支付、运营与 HaH 探索路径

---

## 一、整合背景与组织架构

### 1.1 从 LHIN 到 Ontario Health atHome 的三阶段演进

Ontario 的居家医疗治理经历了三个关键阶段：

| 阶段 | 时间 | 架构 | 特点 |
|:-----|:-----|:-----|:-----|
| **Phase 1：LHIN 时代** | 2006–2019 | 14 个 LHIN（Local Health Integration Networks） | 区域分散管理，负责规划、整合和资助本地医疗服务，含居家护理 |
| **Phase 2：HCCSS 过渡期** | 2019–2024 | 14 个 Home and Community Care Support Services | LHIN 被改组为纯居家与社区护理机构，剥离医疗系统规划职能给 Ontario Health |
| **Phase 3：OHaH 统一平台** | 2024–至今 | Ontario Health atHome（单一省级机构） | 14 个 HCCSS 合并为单一 Crown Agency |

### 1.2 Bill 135: Convenient Care at Home Act, 2023

2023 年 10 月，安大略省卫生部长 Sylvia Jones 提出第 135 号法案《便捷居家护理法案》，2023 年底获 Royal Assent 并正式立法，授权：

- 将 14 个 HCCSS 组织合并为单一的 **Ontario Health atHome** 服务机构
- 赋予 Ontario Health 要求 OHaH 披露服务合同信息（含保密定价和数量）的权力
- 允许 OHaH 将职能分包给服务提供商组织（SPO）或 Ontario Health Teams（OHTs）
- 从法律层面为居家护理的集中化、标准化奠定基础

**官方论述**：政府表示此举将"使人们更容易找到和导航居家护理服务，为居家护理服务提供强大且集中的基础"。

**争议与批评**：Ontario Health Coalition 等组织认为 Bill 135 实质上进一步推动了居家护理的**私有化**——通过将评估和采购职能集中于单一机构后，更易于将服务外包给营利性 SPO。

### 1.3 当前组织架构

```
Ontario Health（省级卫生署）
    │
    ├── Ontario Health atHome（Crown Agency，单一省级居家护理机构）
    │       │
    │       ├── 6 个区域团队（Central, East, North East, North West, Toronto, West）
    │       │       │
    │       │       └── Care Coordinators（评估 + 制定护理计划）
    │       │
    │       └── Service Provider Organizations (SPOs)
    │               │
    │               ├── 营利性/非营利性居家护理机构（Bayshore, SE Health, Paramed, VON 等）
    │               ├── 社区护理诊所（Community Nursing Clinics）
    │               └── 个人支持工作者（PSW）、注册护士（RN/RPN）、治疗师
    │
    └── Ontario Health Teams (OHTs)
            │
            └── 整合型区域医疗团队（医院 + 初级保健 + 居家护理 + 长期护理 + 精神健康 + 姑息护理）
```

**核心运营逻辑**：OHaH 作为**评估-授权-采购方**，不直接提供服务。实际护理由签约 SPO 交付。这一"评估者-提供者分离"模式是理解 Ontarian 系统的关键。

### 1.4 关键数字速览

| 指标 | 数据 | 来源/时间 |
|:-----|:-----|:-----|
| 员工总数 | 9,200+ | 2024-25 商业计划 |
| 年服务患者数 | ~651,850 人 | 2024-25 商业计划 |
| 年 LTC 入住安置 | ~28,750 人 | 同上 |
| 高需求患者数 | ~150,000 人 | 2024 年（较 2014-15 增长 34%） |
| 居家护理等候名单 | >15,000 人 | VON 报告 2024 |
| 新转诊 SPO 接受率 | <50% | VON 报告（历史低位） |
| 省级年度预算（居家和社区护理） | ~$60 亿（2026-27 预测） | Ontario 2026 预算 |

---

## 二、服务范围：全生命周期、全场景覆盖

### 2.1 服务体系总览

Ontario Health atHome 的服务覆盖四大领域，贯穿从学校到临终的全生命周期：

| 服务领域 | 对象 | 核心服务 | 交付场景 |
|:---------|:-----|:---------|:---------|
| **居家护理（Home Care）** | 所有年龄段 | 护理访问、个人支持（PSW）、物理/职业/言语治疗、医疗设备与耗材、营养咨询、社会工作 | 患者家中 |
| **社区支持（Community Support）** | 成人/老年人 | 社区护理诊所、邻里护理模式、过渡护理床位、成人日间项目、送餐、交通 | 社区设施 |
| **姑息护理（Palliative Care）** | 生命限制性疾病患者 | 临终关怀护士执业者、疼痛与症状管理、居所临终关怀、哀伤支持 | 家中/临终关怀机构 |
| **学校健康支持（School Health）** | 学龄儿童/青少年 | 在校护理、PSW、OT/PT/SLP、营养师、医疗器械 | 公立/私立学校/家庭学校 |
| **长期护理安置** | 老年人/残疾人 | LTC 之家入住评估、等候名单管理、过渡期临时安置 | LTC 之家 |

### 2.2 居家护理（Home Care）——核心产品

**服务类型**：

| 服务 | 描述 | 典型频率 |
|:-----|:-----|:-----|
| **Visit Nursing（访问护理）** | 注册护士上门提供伤口护理、静脉治疗、糖尿病管理、导管护理、药物管理等 | 每次 30-60 分钟，按需 |
| **Shift Nursing（班次护理）** | 复杂病患需连续数小时护理（如呼吸机依赖儿童） | 4-12 小时/班次 |
| **Personal Support（个人支持）** | PSW 协助洗澡、穿衣、如厕、转移、喂食等 ADL | 每次 30-120 分钟 |
| **Therapies（康复治疗）** | 物理治疗、职业治疗、言语语言病理学 | 按评估计划 |
| **Medical Equipment & Supplies** | 病床、轮椅、步行器、失禁用品、伤口敷料等 | 按需供应 |

**社区护理诊所（Community Nursing Clinics）**：OHaH 的创新服务模式。符合条件的移动患者前往指定诊所接受护理（注射、静脉治疗、伤口护理等），无需护士上门——提高效率、降低人力成本。

**邻里护理模式（Neighbourhood Models of Care）**：将服务协调下沉至更小地理单元，提升区域内的护理协同效率。

### 2.3 姑息护理（Palliative Care）

Ontario Palliative Care Network（OPCN）与 Ontario Health 合作建立的三层框架：

1. **社区成人模式（2019）**：居家姑息护理 + 社区临终关怀
2. **医院成人模式（2025.09）**：医院场景下的姑息护理标准化
3. **儿科模式**：覆盖所有场景的儿童姑息护理

OHaH 的姑息护理团队包括：护理协调员、临终关怀护士执业者、疼痛与症状管理顾问、高级执业护士、临终关怀机构员工、社区医疗服务提供者和精神照护人员。

### 2.4 儿科与学校健康支持

OHaH 是 Ontario 学校健康支持服务的主要协调者：

- **公立学校**：护理、个人支持、营养师、医疗器械
- **私立学校/家庭学校**：护理、PSW、OT、SLP、营养师、医疗器械

儿童在学服务资格条件：持有有效 Ontario 健康卡 + 经 Care Coordinator 评估认定需要专业或个人支持服务才能上学。

---

## 三、支付体系：公共支付 + 私人补充的双轨制

### 3.1 核心原则

> **OHIP 不直接支付居家护理**。省级医疗保险法（OHIP）覆盖的是医生和医院服务。居家护理由 Ontario Health atHome 通过独立预算拨款管理。

### 3.2 公共支付路径

```
公民/居民
    │
    ├── 联系 Ontario Health atHome（310-2222，免区号）
    │
    ├── Care Coordinator 评估需求
    │       │
    │       ├── 符合资格 → 制定护理计划 → 分配 SPO 提供服务 → 公共资金支付
    │       │
    │       └── 不符合资格 → 转介其他社区资源 或 自费寻找私人护理
    │
    └── 服务范围与额度由评估结果决定，非按需无限提供
```

### 3.3 私人支付生态

| 支付方式 | 场景 | 市场规模 |
|:---------|:-----|:-----|
| **自费（Private Pay）** | 不符合公共资格 或 需要超出公共配额的额外护理 | 主要支付方式 |
| **私人健康保险** | 雇主提供的扩展健康福利（extended health benefits） | 补充公共缺口 |
| **OSCAH 税收抵免** | Ontario Seniors Care at Home Tax Credit：为自费居家护理提供 ~25% 可退还税收抵免 | 政策激励 |
| **长期护理保险** | 加拿大私人 LTC 保险市场较小，渗透率低 | 小众 |

**私人居家护理大致价格**（安大略省）：

| 服务 | 时薪范围（CAD） |
|:-----|:-----|
| 个人支持/家政 | $28–$40 |
| 注册护士 | $60–$100 |
| 注册实习护士（RPN） | $50–$75 |
| 物理/职业治疗 | $100–$150 |
| 24/7 住家护理 | $250–$350/天 |

### 3.4 关键痛点

1. **公共供给不足**：15,000+ 等候名单、SPO 接受率 <50%
2. **服务额度限制**：即使通过公共资格评估，分配的小时数常低于实际需求
3. **公私鸿沟**：能自费的群体可获得充足服务；不能自费的只能等待有限的公共配额
4. **护士工资差距**：居家护理护士平均收入仅为医院护士的 70%，导致招聘困难

---

## 四、覆盖数据与预算全景

### 4.1 关键绩效指标（2024/25 年度报告）

OHaH 通过 Service Accountability Agreements（SAAs）向 Ontario Health 报告业绩：

| 指标 | 目标 | 省级实际 | 达成情况 |
|:-----|:----:|:----:|:-----|
| PSW 访问等待 ≤5天（复杂需求患者）| ≥90% | 87% | ⚠️ 未达标 |
| 护理访问等待 ≤5天 | ≥95% | 92% | ⚠️ 未达标 |
| 社区转诊中位等待时间 | ≤7天 | 7天 | ✅ |
| 社区转诊 90分位等待时间 | ≤21天 | 42天 | 🔴 严重超标 |
| 出院到居家服务中位等待 | ≤1天 | 2天 | ⚠️ |
| 出院到居家服务 90分位等待 | ≤7天 | 14天 | 🔴 超标 |
| SPO 访问护理接受率 | 90-94% | 81% | 🔴 严重不达标 |
| SPO 班次护理接受率 | 90-94% | 39% | 🔴 极度不达标 |
| SPO 个人支持接受率 | 90-94% | 80% | 🔴 不达标 |
| 护理漏服务率 | 0.05-0.1% | 0.03% | ✅ 优于目标 |

**核心解读**：
- 服务**及时性**勉强及格——中位等待时间尚可，但长尾问题严重（90分位超标 2-3 倍）
- **SPO 接受率**是最大瓶颈——班次护理仅 39%，意味着大部分复杂护理需求无法被满足
- 漏服务率优于目标——说明一旦锁定服务，交付质量较高

### 4.2 预算与投资趋势

| 财政年度 | 安省卫生总支出 | 居家社区护理预算 | 关键投资 |
|:---------|:-----|:-----|:-----|
| 2024-25 | $91.6B | ~$55 亿（估） | $1.1B 三年承诺启动（$982M 核心 + H2H） |
| 2025-26 | ~$93B | 持续增长 | High-Intensity Bundled Home Care 启动 |
| 2026-27 | $101.2B（预算） | ~$60 亿 | 追加 $1.1B 居家社区护理 + $325M 初级保健 |
| 2027-28 | ~$93.6B（FAO 预测） | — | 预测恢复平衡 |

**FAO（财政问责办公室）关键发现**：
- 2022-23 至 2027-28 之间，省级卫生拨款与需求之间的**缺口达 $213 亿**
- 人均医院床位将从 220 张/10万人下降至 203 张
- 人均 LTC 床位从 60 张/千名 75+ 老人下降至 56 张
- **结论**：居家护理必须承担更大的医疗系统缓冲功能，但拨款增幅（年均 0.7%）落后于需求增长（居家护理需求年增 12.1%）

### 4.3 服务量参考

| 年度 | 服务机构 | 数据 |
|:-----|:-----|:-----|
| 2022-23 | PSW 在自然退休社区（NORCs）| 350 万小时，价值 $1.2 亿+ |
| 2024-25 | H2H 项目 | ~8,100 名患者，47 个站点 |
| 2024-25 | OHaH 总患者 | ~651,850 人 |
| 2019 | 居家护理利用 (Ontario) | 护理 13.1/百人/周、个人护理 179.7/百人/周、治疗 4.1/百人/周 |

---

## 五、Ontario 的 HaH（Hospital at Home）探索

### 5.1 当前状态：无正式 CMS 式 AcHAH 项目，但有多条并行路径

**Ontario 没有美国 CMS 急性期医院居家（Acute Hospital Care at Home）那样的正式项目**，但正通过以下路径逼近 HaH 模型：

| 项目 | 定位 | HaH 等级 | 规模 |
|:-----|:-----|:-----|:-----|
| **High-Intensity Bundled Home Care** | 医院级护理套餐，$700/天 | ⭐⭐⭐ 最接近 | 2025.11 启动 |
| **Hospital to Home (H2H)** | 出院后过渡护理，最长 16 周 | ⭐⭐ 过渡期 HaH | 47 站点/~8,100 患者/年 |
| **Community Nursing Clinics** | 非住院护理集中交付 | ⭐ 替代门诊 | 全省扩展中 |
| **Home First 操作指令** | 政策导向：从"LTC 优先"转向"居家优先" | — | 2024.08 发布 |

### 5.2 High-Intensity Bundled Home Care — 最接近 HaH 的探索

**2025 年 11 月启动**（BNN Bloomberg/CTV News 报道）：

- **支付**：居家护理机构 $700 CAD/天（约 $500 USD），管理高需求患者的医院级护理
- **模式**：由注册护士主导，PSW 和治疗师团队支持
- **目标人群**：需要 24/7 监护或高级别个人/医疗护理、出院后在医院等待 LTC 的 ALC（Alternate Level of Care）患者
- **政策背景**：Ontario 医院中高达 20% 的住院患者提前符合出院条件却因 LTC 容量不足而滞留

**与 CMS AcHAH 的关键差异**：
- Ontario 项目是 **ALC 出院通路**，非急性入院替代
- 美国 AcHAH 是 **从急诊/社区直接收入居家医院**，完全替代住院
- Ontario 模式更像是"出院后密集过渡 + LTC 等候期桥接"

### 5.3 国家层面：加拿大 HaH 全局

**CADTH（加拿大药品与卫生技术署）2024 年 5 月 Horizon Scan** 指出：
- 加拿大急性护理床位占用率 2021 年达 86.7%
- 虚拟病房（Virtual Wards）/ HaH 在加拿大多省处于试点阶段
- **British Columbia** 的"Home is Best"方法
- **Quebec** 的自主任居家护理（Self-Directed Care）
- **New Brunswick** 的护理协调领先实践

**总体判断**：加拿大各省的 HaH 发展不均衡。Ontario 作为人口和经济最大省，在资金投入上处于领先，但在"急性入院替代"这一 HaH 核心理念上的实践仍落后于英国 NHS @home 和澳大利亚 HITH 模式。

---

## 六、国际对比：美/英/澳 vs Ontario

| 维度 | 🇨🇦 Ontario (2024–) | 🇺🇸 US Medicare | 🇬🇧 NHS England | 🇦🇺 Australia |
|:-----|:-----|:-----|:-----|:-----|
| **治理模式** | 单一省级 Crown Agency + SPO 外包 | CMS 联邦统筹 + 商业保险并行 | NHS Trusts/ICBs + 公立服务为主 | 州政府 + Medicare Australia |
| **居家护理整合度** | 2024 年完成 14→1 整合 | 分散（Medicare HH + Medicaid HCBS + AcHAH） | NHS Community Trusts + Virtual Wards | 州级 HITH 项目 |
| **HaH 正式项目** | ❌ 无正式 AcHAH；High-Intensity Bundled 为最接近 | ✅ CMS AcHAH 豁免（300+ 医院，2020–） | ✅ NHS @home / Virtual Wards（2022–） | ✅ HITH 成熟（1990s–） |
| **公共支付对居家护理的覆盖** | 评估准入制，非普惠 | Medicare HH 按需（+ 20% copay）+ Medicaid HCBS | NHS 免费但 Access 受限于等待 | Medicare + 州辅助 |
| **年预算（居家社区护理）** | ~$60 亿 CAD（2026-27） | ~$180 亿 USD（Medicare HH 2023）+ Medicaid HCBS ~$1,500 亿 | NHS Community Health ~£130 亿 | ~AUD $40 亿（估） |
| **服务人口** | ~1,600 万（Ontario） | ~3.35 亿（全国） | ~6,800 万（英格兰） | ~2,700 万 |
| **人均居家护理支出** | ~$375 CAD/人 | ~$560 USD/人（含 Medicare + Medicaid HH） | ~£190/人 | ~AUD $150/人（估） |
| **核心挑战** | SPO 接受率极低（39-81%）| 2032 AcHAH 豁免到期不确定性 | 等待时间、人力短缺 | 城乡覆盖不均 |
| **人力模式** | PSW + RN/RPN + 治疗师（OHaH 采购） | HHA + RN + 治疗师（agency 为主） | District Nurse + Healthcare Assistant | RN + 社区护理 |

### 关键差异分析

1. **美国 vs Ontario**：美国 Medicare HH 和 AcHAH 有明确的联邦支付代码和费用表，提供可预测的收入流；Ontario 的居家护理资金来自省级总预算，无明确的服务费率表，受年度财政波动影响更大
2. **英国 vs Ontario**：NHS @home 的基础是 GP 注册制和 District Nurse 体系，与初级保健深度融合；Ontario 的 OHaH 与初级保健相对分离（正在通过 OHTs 改善）
3. **澳大利亚 vs Ontario**：澳洲 HITH 由州立医院系统直接管理，医生主导；Ontario 由独立于医院的 OHaH 管理，医生参与有限

---

## 七、对 iHomeCare 的借鉴

### 7.1 Ontario 模式的优缺点

**✅ 优势**：

| 维度 | 描述 | 对 iHomeCare 启示 |
|:-----|:-----|:-----|
| **统一评估入口** | OHaH 是全省唯一的居家护理入口（310-2222），降低用户导航成本 | 建立统一的评估标准和准入流程 |
| **评估-提供者分离** | OHaH（评估方）vs SPO（提供方），防止利益冲突 | 平台作为中立评估/匹配方，而非直接雇佣护理员 |
| **分级护理计划** | Care Coordinator 制定个性化计划 → 分配 SPO → 监控质量 | 建立 Care Plan 模板和服务级别协议（SLA） |
| **公私双轨制** | 公共支付基础覆盖 + 私人自费补充额度外需求 | 政府长护险 + 商业保险 + 自费的三层支付架构 |
| **从 LTC 到 Home First 的范式转变** | 政策明确优先居家，减少机构依赖 | 政策倡导：居家优先的经济与社会价值论证 |
| **社区护理诊所模式** | 非卧床护理集中交付，提升效率 | 考虑社区护理站点（service hub）的混合模式 |

**⚠️ 劣势/教训**：

| 痛点 | 根因 | 对 iHomeCare 启示 |
|:-----|:-----|:-----|
| SPO 接受率仅 39-81% | 支付费率低于市场，人力短缺 | 定价模型必须保证服务提供方可持续盈利 |
| 90 分位等待 42 天 | 需求增长（12.1%）远超预算（0.7%） | 建立动态容量预测 + 弹性供给池 |
| 护士工资差 ~30% | 居家护理未被纳入与医院/机构同等的薪酬体系 | 护理员薪酬需具备竞争力，避免人才流失 |
| 15,000+ 等候名单 | 公共预算约束下的配给制 | 避免单一依赖公共支付，设计多层次支付 |
| "评估-提供者分离"的执行困境 | OHaH 不控制 SPO 的供给端（招聘/留人） | 平台需深度参与供给侧管理，而非仅做匹配 |
| 居家 vs 医院医生分离 | 居家护理中极少有医生直接参与 | 建立远程医疗/医生巡诊的整合能力 |

### 7.2 可迁移的运营设计原则

```
┌─────────────────────────────────────────────────────────────────┐
│                 iHomeCare 平台架构参考 OHaH                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  支付方层                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ 公共保险  │  │ 商业保险  │  │ 自费客户  │  │ 公益基金  │       │
│  │(长护险)   │  │          │  │          │  │          │       │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
│       └──────────────┴────────────┴────────────┘               │
│                          │                                      │
│                    ┌─────▼──────┐                               │
│                    │  iHomeCare │ ← 统一评估 + 匹配引擎          │
│                    │  平台      │                                │
│                    └─────┬──────┘                               │
│                          │                                      │
│       ┌──────────────────┼──────────────────┐                   │
│       │                  │                  │                   │
│  ┌────▼─────┐      ┌─────▼──────┐     ┌─────▼──────┐          │
│  │ 护理机构  │      │ 个体护理员  │     │ 社区护理站  │          │
│  │ (SPO)    │      │ (PSW)     │     │ (Nurse     │          │
│  │          │      │           │     │  Clinic)   │          │
│  └──────────┘      └───────────┘     └────────────┘           │
│                                                                 │
│  核心借鉴点：                                                    │
│  ① 统一评估入口（像 OHaH 的 310-2222）                          │
│  ② Care Plan 驱动的服务分配                                    │
│  ③ 多层级供给池管理（机构 + 个体 + 诊所站点）                    │
│  ④ SLA 监控 + SPO 接受率/漏服务率仪表板                         │
│  ⑤ 公私支付双轨自动路由                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3 具体建议

1. **评估标准产品化**：借鉴 OHaH 的 Care Coordinator 角色，开发标准化的居家护理需求评估工具（类似 interRAI-HC），输出分级护理计划而非简单的人-服务匹配
2. **供给池健康度管理**：OHaH 最大教训是 SPO 接受率极低。iHomeCare 必须建立供给端的实时容量、报价弹性、服务质量三位一体监控
3. **分级 HaH 能力**：从轻度的"出院后过渡护理"（类似 H2H）开始，逐步建设到"急性替代级居家医院"（类似 High-Intensity Bundled），避免一步到位的高风险
4. **支付方管理**：Ontario 证明单一公共支付方导致供需长期失衡。设计时即预留多支付方接口（政府医保、商业保险、自费、公益补贴）
5. **社区服务站点网络**：Ontario 的 Community Nursing Clinic 降低了对 PSW 上门的高频依赖。对于密度较高的城市区域，考虑建立社区护理站

---

## 八、总结与展望

Ontario Health atHome 是**全球最大的省级公共居家医疗系统整合工程之一**。2024 年完成的 14→1 整合为 Ontario 居家护理奠定了统一的基础架构，但供需矛盾仍在加剧：

- **需求侧**：老龄化加速（75+ 人口即将翻倍），居家护理需求年增 12.1%
- **供给侧**：SPO 接受率低至 39%，人力工资差距显著，预算增长仅 0.7%
- **政策侧**：Home First 方向明确，2025-26 年 $1.1B+$1.1B 双重加码

对于 iHomeCare：Ontario 在**统一治理、公私双轨、全面服务链**上的实践值得深度借鉴，但其**人力供应链脆弱、SPO 激励不足、医生参与度低**的教训同样宝贵。最关键的启示是——**"评估-提供者分离"模式的核心不是技术平台，而是供需双方的激励机制设计**。

---

## 调研元数据

| 字段 | 内容 |
|:-----|:-----|
| 调研日期 | 2026-07-03 |
| 调研对象 | Ontario Health atHome |
| 对象类型 | 省级公共居家医疗系统（非商业公司） |
| 国家/地区 | 加拿大安大略省 |
| 数据来源 | Ontario 省政府新闻稿、OHaH 官方文档、Ontario Health 年度报告、FAO 财政分析、VON/Home Care Ontario 行业报告、CADTH Horizon Scan |
| 执笔 | Kenneth Ye |
| 对标目的 | iHomeCare 平台架构与运营模式设计参考 |

---

## 参考文献

| # | 来源 | 标题 | 日期 |
|:--|:-----|:-----|:-----|
| 1 | 安大略省政府 (T1) | *Ontario Making it Easier and More Convenient to Connect to Home Care*（Bill 135 公告） | 2023 |
| 2 | 安大略省立法 (T1) | *Bill 135: Convenient Care at Home Act, 2023*（S.O. 2023, c. 19） | 2023 |
| 3 | Ontario Health atHome (T1) | *Business Plan 2024-2025* | 2024.08 |
| 4 | Ontario Health atHome (T1) | *Consolidated HCCSS 2023-2024 / OHaH 2024-2025 Annual Report* | 2025.07 |
| 5 | Ontario Health (T1) | *Annual Report 2024-25*（含 OHaH SAA 业绩指标） | 2025 |
| 6 | Ontario Health (T1) | *Operational Direction: Home First* | 2024.08 |
| 7 | Ontario Health (T1) | *Transitions Between Hospital and Home Quality Standard (2026 Update)* | 2026.02 |
| 8 | Ontario Health (T1) | *Palliative Care Health Services Delivery Framework: Adult Hospital Model of Care* | 2025.09 |
| 9 | 安大略省政府 (T1) | *Ontario Investing $1.1 Billion to Protect and Expand Home Care* | 2024 |
| 10 | 安大略省政府 (T1) | *2026 Ontario Budget: A Plan to Protect Ontario*（Chapter 3 & 1B） | 2026.03 |
| 11 | Financial Accountability Office of Ontario (T1) | *Ontario Health Sector: 2025 Spending Plan Review* | 2025 |
| 12 | Financial Accountability Office of Ontario (T1) | *Ontario Health Sector: 2025 Spending Plan Review*（完整 PDF） | 2025 |
| 13 | CADTH (T2) | *Virtual Medicine Wards and Hospital-at-Home Programs: Horizon Scan* | 2024.05 |
| 14 | Home Care Ontario (T2) | *2025 Annual Report* | 2025.06 |
| 15 | Home Care Ontario (T2) | *Ontario Needs More Home Care: Pre-Budget Recommendations 2024-25* | 2024.01 |
| 16 | VON / OCSA (T2) | *How to Bring Health Home & Stabilize Ontario's Health System* | 2022 |
| 17 | VON / OCSA (T2) | *Pre-Budget 2025 Recommendations* | 2025.01 |
| 18 | BNN Bloomberg (T3) | *Ontario launching new home care program to relieve hospital overcrowding* | 2025.11 |
| 19 | CTV News (T3) | *Ontario quietly introduces $700-a-day home care* | 2025.11 |
| 20 | Hospital News (T3) | *Hospital to Home Program Aims to Reduce ER Visits and Readmissions* | 2024 |
| 21 | Ontario Health Coalition (T3) | *Briefing Note: Ford government's Bill 135 to further privatize home care* | 2023 |
| 22 | Medscape (T3) | *What Will Ontario's 2026 Budget Mean for Healthcare?* | 2026.03 |
| 23 | PMC/NIH (T2) | *Hospital at Home: An Evolving Model for Comprehensive Healthcare* | 2023 |
| 24 | Commonwealth Fund (T2) | *"Hospital at Home" Programs Improve Outcomes, Lower Costs But Face Resistance* | 2013 |
| 25 | RNAO (T2) | *Budget 2026 addresses investments in primary care and home care* | 2026.03 |

---
*报告完成于 2026-07-03 | Kate 调研团队 | Kenneth Ye*
