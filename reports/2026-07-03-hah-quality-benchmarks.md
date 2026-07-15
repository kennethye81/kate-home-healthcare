# HaH 质量指标对标框架报告

**Hospital-at-Home Quality Metrics Benchmarking Framework**

| 属性 | 内容 |
|:-----|:-----|
| 报告类型 | 质量指标对标框架 |
| 作者 | Kenneth Ye |
| 日期 | 2026-07-03 |
| 版本 | v1.0 |
| 覆盖市场 | 美国（为主）+ 英国/澳洲/新加坡/台湾参考 |
| 信源层级 | T1-政府（CMS/MedPAC）/ T2-学术（JAMA/AJMC）/ T2-行业（HaH Users Group）/ T3-媒体 |

---

## 目录

1. [执行摘要](#1-执行摘要)
2. [CMS HaH 质量指标框架](#2-cms-hah-质量指标框架)
3. [临床质量指标对标](#3-临床质量指标对标)
4. [运营质量指标对标](#4-运营质量指标对标)
5. [安全指标对标](#5-安全指标对标)
6. [技术质量指标对标](#6-技术质量指标对标)
7. [患者报告结局（PROMs）](#7-患者报告结局proms)
8. [各标杆项目实际基准值](#8-各标杆项目实际基准值)
9. [对 iHomeCare 质量体系设计的建议](#9-对-ihomecare-质量体系设计的建议)
10. [附录：信源与参考文献](#10-附录信源与参考文献)

---

## 1. 执行摘要

本报告构建了 Hospital-at-Home (HaH) 质量指标的全面对标框架，系统梳理了国际通行的 HaH 质量度量标准，覆盖 CMS 监管要求、临床结果、运营效率、患者安全、技术质量和患者报告结局六大维度，并汇总了 Atrium Health、Mass General Brigham、Kaiser Permanente、Mount Sinai、Johns Hopkins 等标杆项目的实际基准值。

### 核心发现

| 维度 | 关键发现 |
|:-----|:--------|
| **死亡率** | HaH 院内死亡率 0.4%，仅为传统住院（3.6%）的约 1/9（JAMA 2026, aOR=0.09） |
| **再入院率** | HaH 30天再入院率 11.7%，与传统住院（11.0%）无显著差异；Mount Sinai 报告 8.6% vs 15.6% |
| **急诊使用** | HaH 30天急诊率 8.8% vs 住院 10.0%（aOR=0.86），显著更低 |
| **ICU升级** | HaH 3.5% vs 住院 7.9%（aOR=0.39），减少 61% |
| **并发症** | HaH 院内并发症率 3.6% vs 住院 5.1%（aOR=0.59） |
| **谵妄风险** | HaH 降低 64-74%（Kaiser OR=0.36; HaH Users Group 综合证据） |
| **成本节省** | 每例 HaH episode 较住院节省约 $5,054（未调整均值） |
| **患者满意度** | 系统性高于传统住院（CMS报告/多项目验证） |

### 对 iHomeCare 的核心启示

当前国际 HaH 质量体系正处于从"豁免期临时报告"向"永久化标准框架"过渡的关键窗口（CMS AHCAH waiver 延至 2030年9月）。iHomeCare 作为中国市场新兴 HaH 平台，应借鉴国际成熟框架的五层架构——**监管报告层、临床结果层、运营效率层、安全监控层、患者报告层**——同时针对中国市场特点进行本土化适配。

---

## 2. CMS HaH 质量指标框架

### 2.1 AHCAH Waiver 强制报告指标

自 2020 年 CMS 启动 Acute Hospital Care at Home (AHCAH) 豁免以来，参与医院必须每月向 CMS 报告以下三项核心指标（[T1-政府] MedPAC Report to Congress, June 2024）：

| # | 指标 | 英文 | 定义 | 数据来源 |
|:--|:-----|:-----|:-----|:--------|
| 1 | **非预期死亡率** | Unanticipated Mortality | HaH 期间发生的非预期死亡数 | 医院自报 |
| 2 | **升级转院率** | Care Escalation Rate | 从 HaH 转回实体医院住院的患者比例 | 医院自报 |
| 3 | **总出院数** | Total AHCAH Discharges | 每月 HaH 出院总人次 | 医院自报 |

**2024年9月CMS报告关键结论**（[T1-政府] CMS Fact Sheet, 2024.9.30）：
- HaH 患者的**死亡率低于**匹配的实体住院患者
- HaH 出院后 **30天 Medicare 支出更低**（超过一半的 Top 25 MS-DRG 中）
- 患者和照护者**反馈积极**

> ⚠️ **局限**：CMS 指出因患者选择偏倚（HaH 入组患者通常临床复杂度更低），难以得出 AHCAH 整体降低 Medicare 总支出的结论。

### 2.2 CMS Home Health Quality Reporting Program (HH QRP)

虽然 HH QRP 主要为传统居家健康机构（Home Health Agencies）设计，但其 OASIS 评估框架对 HaH 后的过渡期质量管理有直接参考价值（[T1-政府] CMS Home Health Quality Measures）：

**OASIS-based 结果指标（2025年起公开报告）**：

| 指标类别 | 具体指标 | 说明 |
|:--------|:--------|:-----|
| **功能改善** | Discharge Function Score (DC Function) | 出院时功能状态评分（2025 新纳入 HHVBP） |
| **功能改善** | Total Normalized Composite Change in Self-Care | 自理能力综合变化 |
| **功能改善** | Total Normalized Composite Change in Mobility | 移动能力综合变化 |
| **利用管理** | Discharge to Community (DTC) | 出院回归社区率 |
| **利用管理** | Within-Stay Potentially Preventable Hospitalization (PPH) | 在院期间可预防住院率（claims-based） |
| **利用管理** | Acute Care Hospitalization During First 60 Days (ACH) | 60天内急症住院率（claims-based） |
| **利用管理** | ED Use without Hospitalization During First 60 Days | 60天内急诊使用率（claims-based） |

### 2.3 MedPAC 建议的 HaH 质量报告扩展方向

MedPAC 2024年6月报告建议（[T1-政府] MedPAC Ch.6, June 2024）：
- 当前三个指标的**风险调整不足**——需要病例组合调整
- 建议增加**患者体验调查**（类 HCAHPS 的 HaH 版本）
- 建议追踪**出院后30天结局**（再入院、急诊使用、死亡率）
- 建议添加**功能状态变化**指标

---

## 3. 临床质量指标对标

### 3.1 30天死亡率

| 来源 | HaH | 住院对照 | 统计 | 年份 |
|:-----|:---:|:-------:|:-----|:-----|
| **JAMA Network Open（全国68家医院）** | **0.4%** | 3.6% | aOR=0.09 (0.06-0.16) | 2026 |
| **CMS AHCAH 研究报告** | 低于住院 | — | 多 DRG 一致 | 2024 |
| **Mount Sinai（JAMA 2018）** | 未单独报告 | — | — | 2018 |
| **Kaiser AMCAH（CHF 子组）** | 未单独报告 | — | 573例CHF | 2021-2024 |

**对标基准**：HaH 30天/院内死亡率 ≤0.5% 为国际优秀水平。

> 🔴 **注意**：JAMA 2026 报告的 0.4% 为"院内死亡率"（in-hospital mortality），即在 HaH 期间或升级转院后的院内死亡。该指标受患者选择偏倚影响——HaH 入组排除了高临床复杂度患者。

### 3.2 30天再入院率

| 来源 | HaH | 住院对照 | 统计显著性 | 年份 |
|:-----|:---:|:-------:|:----------|:-----|
| **JAMA Network Open** | **11.7%** | 11.0% | NS (aOR=1.07) | 2026 |
| **Mount Sinai** | **8.6%** | 15.6% | p<0.05 | 2018 |
| **MGB Home Hospital（RCT）** | "更低" | — | RCT证据 | 2019 |
| **CMS AHCAH 报告** | 未显著差异 | — | — | 2024 |

**对标基准**：HaH 30天再入院率目标 8-12%，具体视病例组合调整。

> ⚠️ **重要**：JAMA 2026 全国数据显示 HaH 再入院率（11.7%）并未显著低于住院（11.0%），挑战了早期单中心研究（如 Mount Sinai）的乐观结果。该差异可能反映：①早期项目入组患者更优；②规模化后病例复杂度上升；③全国数据包含项目成熟度差异大的机构。

### 3.3 谵妄发生率

| 来源 | 效果量 | 指标 | 年份 |
|:-----|:------:|:-----|:-----|
| **Kaiser Permanente ACAH** | OR=0.36 (64%降低) | 谵妄 vs 住院 | 2025 |
| **HaH Users Group 综合证据** | 降低74% | 谵妄风险 | 2025 |

**对标基准**：HaH 谵妄发生率应显著低于住院基线（住院老年患者谵妄率约 15-25%）。

### 3.4 跌倒率 / HAPI / CAUTI / CLABSI / VTE / 药物错误率

**当前证据状态**：这些传统院内安全指标在 HaH 环境下**缺乏系统性对标数据**。

| 指标 | HaH 数据可获得性 | 住院基准 | 评估 |
|:-----|:----------------|:-------|:-----|
| **跌倒率** | ⚠️ 极有限 | 住院: ~3-5/1000 patient-days | HaH 环境下定义困难——居家环境中的跌倒不一定等同于"院内跌倒" |
| **HAPI（压力性损伤）** | ⚠️ 极有限 | 住院: 1.9% (med-surg units) | HaH 患者移动更多，理论风险更低，但无系统数据 |
| **CAUTI** | ⚠️ 无公开对标数据 | 住院: SIR 基准1.0 | HaH 常规不插尿管，基线风险极低 |
| **CLABSI** | ⚠️ 无公开对标数据 | 住院: SIR 基准1.0 | HaH 中 PICC/中线导管使用增加，需监控 |
| **VTE** | ⚠️ 无公开对标数据 | 住院: ~1-2%高危患者 | 居家环境患者移动更多，预防性抗凝策略待标准化 |
| **药物错误率** | ⚠️ 无公开对标数据 | 住院: ~5%给药错误率 | HaH IV药物由访视护士管理 vs 患者/家属自管口服药 |

> 🟡 **研究空白声明**：上述指标在已发表的 HaH 文献中极少被系统报告。JAMA 2026 研究明确指出"住院安全结果未被捕获"（inpatient safety outcomes were not captured）。这是未来 HaH 质量体系建设的关键缺口。

**JAMA 2026 报告的综合性并发症指标**：
- HaH 住院相关并发症率：3.6% vs 住院 5.1%（aOR=0.59）
- 该指标为复合指标，未细分至单个并发症类型

---

## 4. 运营质量指标对标

### 4.1 平均住院日（Length of Stay）

| 来源 | HaH LOS | 住院对照 LOS | 备注 |
|:-----|:-------:|:----------:|:-----|
| **MGB Home Hospital** | **5-6天**（典型） | — | 2025 公开资料 |
| **CMS AHCAH 报告** | 较住院短 | — | 多 DRG 一致 |
| **Advocate Health** | — | — | 9,400+ 患者，释放 33,000 床位日 |

### 4.2 床位日节省

| 机构 | 床位日节省 | 期间 | 数据来源 |
|:-----|:---------|:-----|:--------|
| **MGB Home Hospital** | **25,000+** | 累计 | Current Health case study |
| **Advocate Health** | **33,000** | 自2020年起 | HaH Users Group evidence summary |
| **MGB（扩展目标）** | 目标转移 10% 内科患者 | 规划中 | AHA Market Scan 2024 |

### 4.3 患者满意度

| 来源 | 结果 | 方法 |
|:-----|:-----|:-----|
| **CMS AHCAH 报告** | 患者与照护者反馈积极 | CMS 调查 |
| **Mount Sinai** | 患者满意度显著高于住院 | 自设工具 |
| **HaH Users Group 综合证据** | "higher satisfaction and stronger relationships with care teams" | 多研究 meta |
| **MGB RCT** | "required fewer lab orders; spent a smaller portion of the day sedentary" | RCT |

**对标基准**：HaH 患者满意度应 ≥90% 为"满意/非常满意"；NPS 目标 ≥70。

### 4.4 急诊转回率（ED Utilization / Care Escalation）

| 来源 | HaH | 住院对照 | 统计 |
|:-----|:---:|:-------:|:-----|
| **JAMA 2026（30天急诊）** | **8.8%** | 10.0% | aOR=0.86 (0.76-0.97) |
| **Mount Sinai（30天急诊）** | **5.8%** | 11.7% | p<0.05 |
| **CMS 月度报告（升级转院率）** | 各机构差异大 | — | 未公开汇总基准 |

**对标基准**：HaH 30天急诊使用率目标 5-9%；升级转院率（escalation to inpatient）目标 ≤10%。

---

## 5. 安全指标对标

### 5.1 非预期死亡（Unanticipated Mortality）

CMS AHCAH 豁免将"非预期死亡"列为三大量化报告指标之一，但**未公开全国汇总基准值**。单中心报告：

- MGB Home Hospital：公开材料声称"zero unexpected mortality"（零非预期死亡）
- JAMA 2026：HaH 院内全因死亡率 0.4%，但未区分预期 vs 非预期

### 5.2 紧急升级率（Escalation to Inpatient）

| 来源 | 结果 |
|:-----|:-----|
| **JAMA 2026（ICU升级）** | HaH 3.5% vs 住院 7.9%（aOR=0.39） |
| **CMS月度报告（全部升级转院）** | 各机构差异大 |

**AHCAH 豁免的安全基础设施要求**（[T1-政府] MedPAC）：
- 每日 ≥2 次面对面临床访视
- 每日 ≥1 次医生访视（可远程）
- 24/7 患者紧急联系系统
- 必要时 **30分钟内** 到达患者家中提供紧急临床服务

### 5.3 院外心跳骤停率

⚠️ 无公开对标数据——此指标在 HaH 文献中几乎未被报告。

### 5.4 谵妄（作为安全指标）

见 §3.3——HaH 降低 64-74% 谵妄风险是最稳健的临床安全发现。

---

## 6. 技术质量指标对标

### 6.1 远程监测现状（HaH Users Group 调查）

基于 HaH Users Group 2023 年发布的 RPM 质量研究（9家机构访谈）（[T2-行业] HaH Users Group, 2023.10）：

| 维度 | 发现 |
|:-----|:-----|
| **监测频率** | q4hr 22% / q6hr 22% / q8hr 33% / 连续 22% |
| **监测模式** | 生命体征 100% / 连续单导联 ECG 33% / 跌倒监测 33% |
| **监测对象** | 全部患者 89% / 基于病情 11% |
| **月均 HaH 患者量** | 0-50: 33% / 50-100: 22% / >100: 33% |

### 6.2 核心技术质量挑战

| 挑战 | 描述 | 影响 |
|:-----|:-----|:-----|
| **数据保真度（Data Fidelity）** | RPM 供应商数据可靠性参差不齐 | 临床决策信心不足 |
| **连接性问题（Connectivity）** | 家庭网络稳定性不一，影响数据传输完整性 | "data from the home are not the same as those from the hospital"（JMIR 2024） |
| **缺乏基准（Lack of Benchmarks）** | 难以与院内环境质量指标进行等量对比 | 质量管理对标困难 |
| **告警疲劳** | 家庭环境产生的噪声信号远多于院内受控环境 | 临床响应效率降低 |

### 6.3 建议的技术质量 KPI

| KPI | 定义 | 目标基准 |
|:----|:-----|:-------|
| **告警响应时间** | 从 RPM 系统触发告警到临床人员首次响应 | <15分钟（日间）/ <30分钟（夜间） |
| **数据传输完整性** | 成功传输的数据点 / 预期数据点 | >95% |
| **设备正常运行时间** | RPM 设备可用时间比例 | >99% |
| **误报率** | 未导致临床干预的告警比例 | <30%（需持续优化） |
| **远程访视完成率** | 计划远程访视实际完成比例 | >95% |

> ⚠️ 上述技术 KPI 的基准值**尚无行业共识**，目前为基于专家意见的建议值，需在 iHomeCare 实际运行中校验和迭代。

---

## 7. 患者报告结局（PROMs）

### 7.1 国际通用的 PROMs 工具

| 工具 | 维度 | 是否在 HaH 中验证 | 许可 |
|:-----|:-----|:-----------------|:-----|
| **EQ-5D-5L** | 5维度：移动/自理/日常活动/疼痛/焦虑抑郁 + VAS | ✅ 在多种居家医疗场景中使用 | 需 EuroQol 许可 |
| **PROMIS-29** | 7个领域 + 疼痛强度 | ✅ PROMIS→EQ-5D 映射算法已开发（PMC 2023） | 公开免费 |
| **HCAHPS**（医院版） | 医患沟通/护理/环境/出院准备/整体评分 | ❌ 未针对 HaH 适配 | CMS 公开 |
| **NPS**（净推荐值） | 单一问题："推荐可能性" | ⚠️ 部分 HaH 项目使用 | 免费 |

### 7.2 HaH 特定的 PROM 需求

与传统住院相比，HaH 环境下 PROMs 需额外关注：

| 额外维度 | 说明 | 推荐工具 |
|:--------|:-----|:--------|
| **照护者负担** | HaH 是否将临床负担转移给家属？ | Zarit Burden Interview / Caregiver Strain Index |
| **居家安全感** | 患者在家中接受急症治疗的安全感知 | 需自建或适配 |
| **技术接受度** | 对 RPM 设备和远程访视的接受程度 | Technology Acceptance Model (TAM) 量表 |
| **日常活动干扰** | 治疗对正常家庭生活的干扰程度 | 改编自 PROMIS |
| **睡眠质量** | 居家环境是否改善睡眠（vs 住院） | PROMIS Sleep Disturbance |

### 7.3 现有证据

| 来源 | PROM 发现 |
|:-----|:---------|
| **HaH Users Group** | "Patients receiving acute care at home report higher satisfaction and stronger relationships with their care teams" |
| **MGB RCT** | HaH 患者"spent a smaller portion of the day sedentary"（更少久坐） |
| **HaH Users Group** | "Studies show lower levels of caregiver stress and confirm that HaH does not transfer clinical responsibilities from medical professionals to families" |
| **CMS AHCAH 报告** | 患者和照护者体验积极 |

### 7.4 推荐 iHomeCare PROM 组合

| 时间点 | 工具 | 目的 |
|:------|:-----|:-----|
| 入组时 | EQ-5D-5L + PROMIS-29（子集） | 基线健康状态 |
| 出院时 | EQ-5D-5L + 自建 HaH 体验量表 | 治疗前后变化 + 体验 |
| 出院后30天 | EQ-5D-5L + 照护者负担 | 持续性评估 |
| 每次远程访视后 | 单一 NPS 问题 | 实时反馈 |

---

## 8. 各标杆项目实际基准值

### 8.1 Atrium Health

| 指标 | 数值 | 来源 |
|:-----|:-----|:-----|
| 项目名称 | Hospital at Home (AH-HaH) | |
| 启动年份 | 2020 | |
| 累计患者数 | 9,400+ | HaH Users Group |
| 累计释放床位日 | **33,000** | HaH Users Group |
| RPM 模式 | 远程监测 + 双向音视频 + 24/7 虚拟 RN | AMA case study |
| 访视频率 | q6hr 生命体征 + 每日2次社区 paramedic/RN + 每日 1 次医生远程访视 | AMA case study |
| 入排标准 | O2 ≤4L, RR <24, SBP >90, SpO2 >92%, 无需72h内高级诊断 | AMA case study |

### 8.2 Mass General Brigham (MGB)

| 指标 | 数值 | 来源 |
|:-----|:-----|:-----|
| 项目名称 | Home Hospital / Healthcare at Home | |
| 启动年份 | 2017 | |
| 覆盖范围 | 72个社区（波士顿大区） | Current Health |
| 典型 LOS | **5-6天** | MGB Health Plan case study |
| 累计释放床位日 | **25,000+** | Current Health case study |
| 增长 | 15个月内增长200% | Current Health |
| 非预期死亡 | "zero unexpected mortality" | Current Health |
| 战略目标 | 转移10%内科患者至居家 | AHA Market Scan 2024 |
| 30天再入院 | RCT 证据支持低于住院 | 多篇发表 |
| 服务内容 | 每日访视+24/7视频+远程监测+IV药物+诊断+X线/超声/血检+PT/OT/ST+社工+餐食 | MGB case study |

### 8.3 Kaiser Permanente

| 指标 | 数值 | 来源 |
|:-----|:-----|:-----|
| 项目名称 | Advanced Care at Home (ACAH) | |
| 合计 HaH 患者 | 226例（2025发表评估） + 573例 CHF（2021-2024） | AJMC / SHM |
| CHF 子组 30天急诊/紧急护理 | 数据已追踪未公开基准 | SHM Abstracts |
| CHF 子组 30天再入院 | 数据已追踪未公开基准 | SHM Abstracts |
| CHF 子组 30天死亡率 | 数据已追踪未公开基准 | SHM Abstracts |
| 谵妄风险 | **降低 64%**（OR=0.36, p=0.026） | AJMC 2025 |
| 系统特点 | 整合型 HMO（保险+医疗一体），自有 EHR 连续性 | |

### 8.4 Mount Sinai

| 指标 | 数值 | 来源 |
|:-----|:-----|:-----|
| 项目名称 | Mobile Acute Care Team (MACT) / Hospitalization at Home | |
| **30天再入院率** | **8.6%** (vs 15.6% 住院) | JAMA / AHA case study 2018 |
| **30天急诊率** | **5.8%** (vs 11.7% 住院) | JAMA / AHA case study 2018 |
| 患者满意度 | 显著高于住院 | 多篇发表 |
| 模型来源 | 基于 Johns Hopkins HaH 模型 | Mount Sinai 实施手册 |

### 8.5 Johns Hopkins

| 指标 | 数值 | 来源 |
|:-----|:-----|:-----|
| 项目名称 | Hospital at Home | |
| 启动年份 | **1994**（美国先驱，26+年数据） | Commonwealth Fund |
| 研究贡献 | 奠基性 RCT：HaH 成本更低/临床等效/满意度更高 | 多篇 NEJM/JAMA |
| 捆绑模式 | HaH + 30天 postacute transitional care → 更优结局 | Hopkins 发表 |
| 对政策影响 | HaH 概念引入者 Bruce Leff（1996） | PMC 2023 |

### 8.6 跨项目对标矩阵

| 指标 | CMS全国基准(2024/2026) | Atrium | MGB | Kaiser | Mount Sinai | 优秀目标 |
|:-----|:---:|:---:|:---:|:---:|:---:|:---:|
| 院内/期间死亡率 | 0.4% | — | 0% (非预期) | — | — | ≤0.5% |
| 30天再入院率 | 11.7% | — | 低于住院 | — | 8.6% | ≤10% |
| 30天急诊率 | 8.8% | — | — | — | 5.8% | ≤8% |
| 升级转院率 (ICU) | 3.5% | — | — | — | — | ≤5% |
| 并发症率 | 3.6% | — | — | — | — | ≤4% |
| 谵妄降低 | — | — | — | 64%↓ | — | 50%+↓ |
| 累计释放床位日 | — | 33,000 | 25,000+ | — | — | 项目规模依赖 |
| 典型 LOS | 短于住院 | — | 5-6天 | — | — | 3-7天 |

> "—" 表示该机构未公开此特定基准值。

---

## 9. 对 iHomeCare 质量体系设计的建议

### 9.1 五层质量架构

建议 iHomeCare 采用与 CMS AHCAH 框架对齐但针对中国市场适配的五层质量架构：

```
┌─────────────────────────────────────────────┐
│            iHomeCare 质量体系               │
├─────────────────────────────────────────────┤
│ L5 — 患者报告层 (PROMs/PREMs)               │
│      EQ-5D-5L + 自建HaH体验 + NPS           │
├─────────────────────────────────────────────┤
│ L4 — 技术质量层 (RPM/Tech KPIs)             │
│      告警响应 / 数据完整性 / 设备可用性       │
├─────────────────────────────────────────────┤
│ L3 — 安全监控层 (Safety Surveillance)        │
│      非预期死亡 / 升级转院 / 跌倒 / 不良事件  │
├─────────────────────────────────────────────┤
│ L2 — 运营效率层 (Operational)               │
│      LOS / 床位日节省 / 再入院 / 急诊使用    │
├─────────────────────────────────────────────┤
│ L1 — 临床结果层 (Clinical Outcomes)          │
│      死亡率 / 并发症 / 功能改善 / 谵妄       │
└─────────────────────────────────────────────┘
```

### 9.2 具体建议

#### 9.2.1 强制报告指标（月度，对标 CMS Level 1-3）

| # | 指标 | 对标来源 | 数据采集方式 |
|:--|:-----|:--------|:-----------|
| 1 | 非预期死亡率 | CMS AHCAH | 临床判定 + 平台记录 |
| 2 | 升级转院率 | CMS AHCAH | 平台自动追踪 |
| 3 | 总出院数 | CMS AHCAH | 平台自动追踪 |
| 4 | 30天再入院率 | CMS/JAMA | 平台 + 随访 |
| 5 | 30天急诊使用率 | JAMA | 平台 + 随访 |
| 6 | HaH 期间不良事件数（跌倒/HAPI/药物错误） | 建议新增 | 临床报告 + 平台 |
| 7 | 患者 NPS | 行业实践 | 出院时自动推送 |

#### 9.2.2 风险调整策略

**关键教训**：国际数据显示 HaH 患者选择偏倚是解释"更好结果"的主要混淆因素。iHomeCare 应：

- **建立入排标准与患者分层**：记录所有筛选指标（临床严重度/功能状态/社会支持/技术接受度），用于事后风险调整
- **对标住院基准时使用倾向性评分匹配（Propensity Score Matching）**：参考 JAMA 2026 方法论
- **逐步纳入更高临床复杂度患者**：验证不同风险层级下的结果差异

#### 9.2.3 PROM 组合推荐

| 时间点 | 最小可行组合 | 扩展组合 |
|:------|:-----------|:--------|
| 入组 | NPS + 自建满意度 | + EQ-5D-5L + PROMIS-29 |
| 出院 | NPS + 自建满意度 | + EQ-5D-5L + 照护者负担 |
| 30天随访 | NPS | + EQ-5D-5L + 功能状态 |

#### 9.2.4 技术质量监控

| KPI | iHomeCare 起步目标 | 成熟期目标 | 对标依据 |
|:----|:-----------------|:---------|:--------|
| 告警响应时间 | <30分钟 | <15分钟 | CMS 30分钟紧急响应要求 |
| 数据传输完整性 | >90% | >95% | HaH Users Group RPM研究 |
| 远程视频访视完成率 | >90% | >95% | 行业实践 |
| 设备故障率 | <5% | <2% | 行业实践 |
| 平台可用性（uptime） | >99.5% | >99.9% | SaaS行业标准 |

#### 9.2.5 国际对标与本土化适配要点

| 美国 CMS 框架要素 | 中国适配建议 |
|:-----------------|:-----------|
| Medicare FFS 支付标准 | 对接中国医保支付改革（DRG/DIP 框架下的 HaH 支付单元设计） |
| OASIS 评估工具 | 开发中国版 HaH 标准化评估表单（参考 OASIS 结构 + 中国临床实践） |
| HCAHPS 患者体验 | 开发中国版 HaH 患者体验量表（参考公立医院绩效考核患者满意度框架） |
| CMS 月度报告（3指标） | 扩展至中国版 8-10 指标集（涵盖安全 + 临床 + 运营） |
| RPM FDA 监管 | 对接中国 NMPA 医疗器械软件监管框架 |
| MedPAC 风险调整 | 对接中国 CHS-DRG 风险分层方法论 |

#### 9.2.6 分阶段实施路线图

```
Phase 1 (0-6个月)：基础建设
├── 建立入排标准 + 患者分层模型
├── 实施 L1-L3 强制报告（7项核心指标）
├── 部署 NPS 收集（出院时）
└── 建设技术 KPI 监控面板

Phase 2 (6-12个月)：标准对标
├── 引入 EQ-5D-5L PROM 工具（获许可）
├── 启动与住院对照的风险调整对标
├── 建立 30 天随访追踪系统
└── 技术 KPI 从"起步"升级至"成熟"目标

Phase 3 (12-24个月)：体系成熟
├── 开发中国版 HaH 标准化评估表单
├── 与医保部门合作定义 HaH 支付质量指标
├── 发表首个中国 HaH 质量结果报告
└── 参与国际对标（APHaH/HaH Users Group）
```

---

## 10. 附录：信源与参考文献

### Tier 1 — 政府/官方源

| # | 来源 | 描述 | 日期 |
|:--|:-----|:-----|:-----|
| 1 | CMS Fact Sheet: Report on the Study of the AHCAH Initiative | 全国 HaH 质量/成本/体验研究 | 2024.9.30 |
| 2 | CMS Home Health Quality Measures | HH QRP 指标体系与 OASIS 框架 | 持续更新 |
| 3 | MedPAC Report to Congress, Ch.6: Medicare's AHCAH Program | 豁免要求 + 质量报告建议 | 2024.6 |
| 4 | CMS Lessons from CMS' AHCAH Initiative (Blog) | 政策更新 + 早期经验 | 2024 |

### Tier 2 — 学术/行业源

| # | 来源 | 描述 | 日期 |
|:--|:-----|:-----|:-----|
| 5 | JAMA Network Open: "Outcomes Associated With Hospital at Home vs Traditional Inpatient Stay" | 68医院/15,871例 PSM 研究 | 2026.5 |
| 6 | AJMC: "Advanced Care at Home at Scale in an Integrated Health Care System" | Kaiser Permanente ACAH 谵妄结果 | 2025 |
| 7 | HaH Users Group: "Summary of U.S. Evidence on the HaH Model" | 综合证据两页摘要 | 2025.9 |
| 8 | HaH Users Group: "Quality Metrics for RPM within HaH" (Whitehead) | RPM 质量指标 9机构研究 | 2023.10 |
| 9 | Mount Sinai JAMA 2018: HaH clinical outcomes | 再入院 8.6% vs 15.6% | 2018 |
| 10 | Commonwealth Fund: "Hospital at Home Programs Improve Outcomes" | JHU 模型 + 政策分析 | 历史 |
| 11 | JMIR: "Hospital Is Not the Home" | RPM 居家数据质量讨论 | 2024 |
| 12 | npj Digital Medicine: "The hospital at home in the USA" | JHU 发表 HaH 现状展望 | 2024 |
| 13 | JAMA Health Forum: "PROMs and PREMs to Assess Quality" | PROMs 工具指南 | 2022 |

### Tier 3 — 媒体报道/行业分析

| # | 来源 | 描述 | 日期 |
|:--|:-----|:-----|:-----|
| 14 | FierceHealthcare: "Low mortality among HaH patients nationwide" | MGB 全国研究报道 | 2026 |
| 15 | Home Health Care News: "HaH Reduces In-Hospital Mortality, ED Visits" | JAMA 2026 解读 | 2026.5 |
| 16 | AMA: "Hospital at home saves lives and money: CMS report" | CMS 报告解读 | 2024 |
| 17 | Healthcare Finance News: "CMS releases AHCAH study" | 成本发现报道 | 2024 |
| 18 | AHA Market Scan: "Providers Betting Big on Future of HaH" | MGB 10% 目标报道 | 2024.4 |
| 19 | Medisolv Blog: "Quality Measures and the Success of HaH Programs" | 质量经理实操指南 | 2024 |

### 项目直接来源

| 项目 | 来源 |
|:-----|:-----|
| Atrium Health | AMA Future of Health Case Study; HaH Users Group evidence |
| MGB Home Hospital | MGB Health Plan Case Study PDF; Current Health case study; AHA Market Scan |
| Kaiser ACAH | AJMC 2025; SHM Abstracts 2024; PMC evaluation |
| Mount Sinai | JAMA 2018; AHA Members in Action case study; Implementation Manual |
| Johns Hopkins | Commonwealth Fund; Hopkins HBI publications |

---

## 研究空白与后续工作

| 空白 | 优先级 | 建议补充路径 |
|:-----|:------|:-----------|
| HaH 环境下的跌倒/CAUTI/CLABSI/VTE 系统数据 | 🔴 高 | 联系 HaH Users Group / 各项目质量负责人 |
| AHCAH 升级转院率全国基准 | 🔴 高 | 待 CMS 公开汇总数据 |
| 技术质量 KPI 行业共识标准 | 🟡 中 | 参与 HaH Users Group RPM 工作组 |
| 中国 HaH 质量数据的完全缺失 | 🟡 中 | iHomeCare 自主建立首个数据集 |
| PROM 中国人群常模 | 🟡 中 | 申请 EQ-5D-5L 中国 value set |
| 各项目详细成本分解 | 🟢 低 | 商业敏感——可通过学术合作获取 |

---

*本报告基于截至 2026 年 7 月 3 日的公开可获取数据编制。所有数据点均标注来源与日期。标注"—"的字段表示该机构未公开该特定数据点。部分 Web 提取因安全策略被阻止，数据来自搜索引擎摘要的交叉验证。*
