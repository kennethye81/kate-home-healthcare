# HaH 全球支付模型跨国对比矩阵

**作者**: Kenneth Ye  
**日期**: 2026-07-03  
**报告类型**: 跨国支付体系对比研究  
**覆盖市场**: 8 个（US/UK/JP/DE/AU/SG/TW/HK）  
**数据来源**: 85 份已有报告提取 + 多语言补充搜索 + 一手政策文件

---

## 执行摘要

本报告构建 Hospital-at-Home（HaH）全球支付模型的统一口径跨国对比矩阵，覆盖 8 个市场的支付方结构、支付单元、金额范围、患者自付比例、准入标准、质量挂钩机制及支付创新试点。核心发现：

1. **支付成熟度阶梯**: TW（NHI 试办）> SG（沙盒主流化）> US（Medicare Waiver）≫ UK（Virtual Ward 框架）> AU（州级 HITH）> DE（Pflegeversicherung 居家替代有限）> JP（无急性 HaH 支付编码）≫ HK（几乎空白）
2. **支付单元分化**: 美国以 per-discharge DRG 为主，英国/新加坡/台湾/澳洲以 per-diem 为主，德国/日本以 per-visit FFS 为主，香港无支付单元
3. **患者自付梯度**: 英国（£0）< 台湾（NHI 免部分负担）< 澳洲（$0 公立）< 新加坡（PCHI 分层）< 德国（~25% 自付）< 日本（10-30%）< 美国（$0-$45 copay + 20% coinsurance）< 香港（几乎 100% 自费或商保）
4. **最大空白**: 日本虽有全球最成熟的介護保険体系（¥11.2兆），却无急性期 HaH 支付编码——这是全球 HaH 支付体系最大的制度性空白

---

## 一、支付方结构与资金来源

| 市场 | 支付方类型 | 政府支付占比 | 商保占比 | 自费占比 | 资金来源机制 |
|:----|:---------|:---------:|:------:|:------:|:----------|
| 🇺🇸 **US** | Medicare FFS + MA + Medicaid + 商保 | ~44% (Medicare) | ~35% (MA+商保) | ~10-15% | CMS AHCAH Waiver 下按 IPPS DRG 支付；MA 按人头/ bundled；Medicaid 12 州覆盖 |
| 🇬🇧 **UK** | NHS 单一采购 (single-payer) | ~95%+ | ~3% | ~2% | NHS England 通过 ICS 分配 Virtual Ward 预算；Better Care Fund + 地方拨款 |
| 🇯🇵 **JP** | 介護保険 + 医療保険双轨 | ~70% (公費50%+保険料50%) | ~5% | ~10-30% | 介護保険（40岁以上强制）；医療保険（訪問診療/訪問看護）；无急性 HaH 编码 |
| 🇩🇪 **DE** | Pflegeversicherung + GKV/PKV双轨 | ~60% (SPV) | ~10% (PKV) | ~25% | Pflegeversicherung 按 Pflegegrad 1-5 定额给付；§37 SGB V 居家护理 |
| 🇦🇺 **AU** | MBS + 州级公立 + 私立保险 | ~68% (联邦+州) | ~15% | ~17% | HITH 纳入州级 ABF 框架，与住院同价；MBS 覆盖 GP/专科但非 HITH 核心 |
| 🇸🇬 **SG** | 补贴 (MOH) + MediSave + MediShield Life + IP | ~40-50% (补贴) | ~20% (IP) | ~10-20% | S+3Ms 框架：补贴(PCHI分层) + MediSave(强制储蓄) + MediShield Life(基本险) + IP(综合健保) |
| 🇹🇼 **TW** | NHI 单一保险人 | ~95%+ | ~3% | ~2% | NHI 總額預算內編列「在宅急症照護試辦計畫」經費；患者免部分負擔（重大傷病/山地離島） |
| 🇭🇰 **HK** | HA 公营 + 私人自费/商保 | ~50% (HA补贴) | ~20% (商保) | ~30% | HA 按床日成本内部结算（HK$120/日 公众病房）；VHIS 不覆盖居家急性护理 |

---

## 二、HaH 支付单元与金额范围

| 市场 | 支付单元 | 本地货币金额 | USD 等价（近似） | 对标住院成本比 | 支付编码/制度 |
|:----|:-------|:-----------|:-------------:|:----------:|:----------|
| 🇺🇸 **US** | Per-discharge (DRG) | ~$6,500-8,500/episode (IPPS base rate + adjustments) | $6,500-8,500 | ~62-70% | CMS AHCAH Waiver → IPPS DRG（与住院同码） |
| 🇬🇧 **UK** | Per-diem / Block contract | ~£22-25/bed-day (virtual ward operating cost) | ~$28-32 | ~4-5% (vs £536 inpatient) | NHS Payment Scheme 无专属 Virtual Ward 价格；ICS 通过 block contracts 采购 |
| 🇯🇵 **JP** | Per-visit FFS (无急性 HaH 编码) | ¥8,880/日（在宅患者訪問診療料）+ ¥9,382/回（訪問看護） | ~$59 + $63/visit | N/A（这是慢性在宅医疗，非 HaH） | 診療報酬 C001（在宅患者訪問診療料）+ 訪問看護療養費；无急性住院替代编码 |
| 🇩🇪 **DE** | Per-visit / Per-month FFS | €796-2,299/月 (Pflegesachleistung PG 2-5) | ~$870-2,520 | 部分覆盖 | Pflegeversicherung SGB XI 给付；§37 SGB V（häusliche Krankenpflege） |
| 🇦🇺 **AU** | Per-diem (ABF) | ~A$500-800/day (HITH, 州级差异大) | ~$330-530 | ~50-70% | 州级 ABF (Activity Based Funding)；无统一国家 HITH MBS item |
| 🇸🇬 **SG** | Per-diem (等同住院病房) | S$263-497/day (补贴后自付部分), 全额 ~S$800-1,200/day | ~$195-370 (自付) | 等同住院（患者不因选择 HaH 多付钱） | MIC@Home Sandbox → 永久化(2024.4)；MOH 补贴 + MediSave + MSHL + IP |
| 🇹🇼 **TW** | Per-diem (每日醫療費 + 每日護理費) | 每日醫療費 + 每日護理費 + 醫事人員訪視費（NHI 點值約 NT$3,000-5,000/日估算） | ~$95-160/day | ~30-55% (vs 住院) | NHI「全民健康保險在宅急症照護試辦計畫」(2024.7启动)；独立支付编码 |
| 🇭🇰 **HK** | **无专属 HaH 支付单元** | HA 公众病房 HK$120/日；私家医院 HK$500-3,000+/日 | $15-385+ | N/A | 无 HaH 支付编码；VHIS（自愿医保）仅覆盖住院和日间手术 |

> **注**: USD 换算使用 2026年7月近似汇率: £1=$1.28, ¥150=$1, €1=$1.09, A$1=$0.66, S$1=$0.74, NT$31=$1, HK$7.8=$1

---

## 三、患者自付比例与支付保护

| 市场 | 患者自付比例 | 自付上限/保护机制 | 自付对 HaH 选择的影响 |
|:----|:---------:|:---------------|:------------------|
| 🇺🇸 **US** | 0-20%（Medicare Part A 住院免 copay；MA plan $0-45 copay/visit） | Medicare Part A deductible $1,676 (2026)；MA plan OOP max ~$8,850 | 低——AHCAH 下患者费用等于或低于住院 |
| 🇬🇧 **UK** | ~0% | NHS 免费 at point of care | 零——无经济障碍 |
| 🇯🇵 **JP** | 10-30%（医療保険自付）+ 介護保険 10-30% 自付 | 高額療養費制度（月额上限 ~¥80,100+ 所得分层）；介護保険无上限 | 中高——但这不是 HaH 而是慢性在宅照护 |
| 🇩🇪 **DE** | ~25%（Pflegeversicherung 是"部分给付保险"） | 无硬性年度上限；Pflegegrad 定额给付 vs 实际费用差额大 | 高——机构自费 €2,000-3,000/月，HaH 较便宜但仍需自付差额 |
| 🇦🇺 **AU** | 0%（公立 HITH）| Medicare 公立医院免费；私立保险覆盖；MBS safety net | 低（公立）— 中（私立） |
| 🇸🇬 **SG** | 50-70% (补贴后)；可使用 MediSave | MediShield Life 年度 claim limit；IP 额外覆盖 | 低——患者不因选择 MIC@Home 多付钱 |
| 🇹🇼 **TW** | ~0-5%（重大伤病/山地离岛免部分负担；普通患者约 5%） | NHI 年度部分负担上限 NT$48,000 (2026) | 极低——NHI 在宅急症照護等同住院给付 |
| 🇭🇰 **HK** | 几乎 100%（非 HA 覆盖部分） | 无；VHIS 不覆盖居家急性护理；HA 公众病房 HK$120/日但非 HaH | 极高——这是香港 HaH 最大障碍 |

---

## 四、准入标准 — 谁有资格获得 HaH 支付

| 市场 | 临床准入标准 | 支付准入条件 | 排除条件 |
|:----|:----------|:----------|:-------|
| 🇺🇸 **US** | 符合急性住院标准（需住院但病情稳定）；至少 daily 2 in-person + 1 physician visit | 医院持有 CMS AHCAH Waiver；患者为 Medicare FFS/MA/Medicaid 参保人；需 25+ 患者经验 | 临床不稳定；无合适居家环境/照护者；SNF 不适用 |
| 🇬🇧 **UK** | 病情稳定可居家管理；适合远程监测；GP/Consultant 转介 | NHS Trust 运行 Virtual Ward；ICS 审批；覆盖 NHS 患者 | 临床不稳定；无照护者；居家环境不合适 |
| 🇯🇵 **JP** | 通院困難（无法外出就诊）；需在宅医療 | ⚠️ 无急性 HaH 准入标准——只有慢性在宅医療/介護認定 | **无急性住院替代的支付准入** |
| 🇩🇪 **DE** | Pflegegrad 2-5（经 MDK 评定）；häusliche Krankenpflege 需要医生处方 | GKV/PKV 参保；Pflegegrad 认定；§37 SGB V 处方 | **无专门 HaH 住院替代准入标准** |
| 🇦🇺 **AU** | 急性住院级但适合居家管理；有照护者 | 公立医院 HITH 转介；州级临床治理审批 | 临床不稳定；偏远地区可及性问题 |
| 🇸🇬 **SG** | 普通内科病种（皮肤感染/UTI/CHF/COVID-19）；临床稳定 | MIC@Home 团队评估；适用 Admission Avoidance 或 Early Supported Discharge 路径 | 临床不稳定；无合适照护者；居家环境不适宜 |
| 🇹🇼 **TW** | 肺炎/尿路感染/软组织感染 3 类；应住院但适合在宅；居家醫療/照護機構/急診行動不便 3 类人群 | NHI 参保；照护团队评估；医师 3 天内完成实地访视 | 临床不稳定；不适合居家抗生素治疗 |
| 🇭🇰 **HK** | **无正式 HaH 准入标准** | N/A | 无制度 |

---

## 五、质量挂钩支付机制（VBP/P4P）

| 市场 | VBP/P4P 存在？ | 机制描述 | 质量指标 | 财务影响 |
|:----|:---:|:------|:------|:-------|
| 🇺🇸 **US** | ✅ 有 | Medicare HVBP (Hospital VBP) + HRRP (Readmissions Reduction) + HACRP；AHCAH 需月报 3 项质量指标 | 非预期死亡率；升级至实体住院率；总出院数；患者体验 | 最高 ±2% IPPS 支付调整；HRRP 最高 -3% |
| 🇬🇧 **UK** | ✅ 有限 | CQUIN (Commissioning for Quality and Innovation) 框架；Virtual Ward 部分 ICS 引入 QOF 式指标 | 床位占用率；患者满意度；再入院率 | CQUIN 最高 ~2.5% 合同价值；非惩罚性为主 |
| 🇯🇵 **JP** | ❌ 无（对 HaH） | 介護報酬有加算/減算机制（如看取り加算、緊急時訪問加算）但非系统性 VBP | N/A（无急性 HaH） | N/A |
| 🇩🇪 **DE** | ✅ 有限 | MDK 质量审查 (Qualitätsprüfung)；Pflege-TÜV 评级公开；但非支付挂钩 | Pflegegrad 评定质量；服务透明度 | 公开评级影响选择，非直接支付调整 |
| 🇦🇺 **AU** | ✅ 有 | NWAU (National Weighted Activity Unit) 质量调整；NSQHS 标准合规要求 | HITH 临床指标；感染率；再入院率 | 州级绩效拨款关联 |
| 🇸🇬 **SG** | ✅ 试点中 | MIC@Home 沙盒期间持续评估；MOH 要求临床+经济数据；未来可能引入 VBP | 死亡率；再入院率；患者满意度；成本节省 | 沙盒→主流化须验证安全+经济有效 |
| 🇹🇼 **TW** | ✅ 试点中 | ACAH 試辦計畫设有回饋獎勵金；床側檢驗加成 20→40% | 照護完成率 (~86%)；平均照護天数 (~7天)；减少住院床日 | 回饋獎勵金制度（绩效激励） |
| 🇭🇰 **HK** | ❌ 无 | HA 有内部 KPI 但不与支付挂钩 | N/A | N/A |

---

## 六、支付创新试点

| 市场 | 创新类型 | 试点名称 | 状态 | 关键特征 |
|:----|:-------|:-------|:---:|:------|
| 🇺🇸 **US** | Bundled Payment / Shared Savings | BPCI Advanced; ACO REACH; CMS Innovation Center models | ✅ 运行中 | MA 按人头支付；ACO 共享节省；H.R.4313 拟延长 AHCAH 至 2030 |
| 🇬🇧 **UK** | Block → Activity-based transition | NHS Payment Scheme 2027/28 改革 | 🔄 规划中 | 从 block contract 向 activity-based + outcome-based 转型 |
| 🇯🇵 **JP** | **无 HaH 支付创新** | N/A | ❌ 空白 | 最大制度空白——有 ¥11.2兆介護保険却无急性 HaH 编码 |
| 🇩🇪 **DE** | 居家优先 (ambulant vor stationär) | §37 SGB V 扩大；Zukunftspakt Pflege | 🔄 讨论中 | PNOG 法案 (2027.1 实施) 改革 Pflegeversicherung 财源 |
| 🇦🇺 **AU** | 公私合作 HaH 交付 | Amplar Health (Medibank) 为 SA Health 交付 My Home Hospital | ✅ 运行中 | 私立保险子公司承办公立 HaH；已服务 20,000+ 患者 |
| 🇸🇬 **SG** | 监管沙盒→主流化 | MIC@Home Sandbox→Mainstream (2024.4) | ✅ 已完成 | **全球首个完成沙盒→主流化的亚洲 HaH 项目**；100→400 床位路线图 |
| 🇹🇼 **TW** | 行政试办 | 全民健康保險在宅急症照護試辦計畫 (2024.7) | ✅ 运行中 | 256机构/169团队参与；4,305 人次至 2025.8；115年5月新增提早出院模式 |
| 🇭🇰 **HK** | **无** | iHomeCare（提案阶段） | ❌ 未启动 | 最大制度空白——无沙盒、无试点、无支付编码 |

---

## 七、跨国支付成熟度矩阵（综合对比）

| 维度 | 🇺🇸 US | 🇬🇧 UK | 🇯🇵 JP | 🇩🇪 DE | 🇦🇺 AU | 🇸🇬 SG | 🇹🇼 TW | 🇭🇰 HK |
|:----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **支付方明确性** | 🟢 明确 | 🟢 明确 | 🟡 双轨模糊 | 🟡 双轨局限 | 🟢 明确 | 🟢 明确 | 🟢 明确 | 🔴 无 |
| **HaH 专属支付编码** | 🟢 DRG | 🟡 无专属 | 🔴 无 | 🔴 无 | 🟡 州级差异 | 🟢 等同住院 | 🟢 试点编码 | 🔴 无 |
| **支付金额透明度** | 🟢 高 | 🟡 中 | 🔴 无(对HaH) | 🟡 定额给付 | 🟡 中 | 🟢 高 | 🟡 试点中 | 🔴 无 |
| **患者经济保护** | 🟡 中 | 🟢 高 | 🟢 高(高額療養費) | 🟡 部分给付 | 🟢 公立免费 | 🟢 高 | 🟢 高 | 🔴 低 |
| **VBP/P4P 整合** | 🟢 成熟 | 🟡 有限 | 🔴 无 | 🟡 有限 | 🟡 有限 | 🟡 试点 | 🟡 试点 | 🔴 无 |
| **支付创新活跃度** | 🟢 高 | 🟡 转型中 | 🔴 停滞 | 🟡 讨论中 | 🟢 创新(Amplar) | 🟢 标杆 | 🟢 快速推进 | 🔴 零 |
| **规模化潜力** | 🟡 中(waiver不确定) | 🟢 高(ICS统一) | 🔴 无 | 🔴 低 | 🟡 中 | 🟢 高 | 🟢 高 | 🔴 无 |
| **综合评分** | ⭐⭐⭐⭐ | ⭐⭐⭐½ | ⭐ | ⭐⭐ | ⭐⭐⭐½ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ☆ |

---

## 八、可视化：支付成熟度阶梯

```
支付成熟度

  ★★★★★ ─ 🇸🇬 SG (MIC@Home 主流化) ─ 🇹🇼 TW (NHI 快速扩展)
  │
  ★★★★  ─ 🇺🇸 US (Medicare Waiver 成熟但不确定)
  │
  ★★★½  ─ 🇬🇧 UK (Virtual Ward 规模化但缺专属支付) ─ 🇦🇺 AU (州级 HITH 成熟)
  │
  ★★    ─ 🇩🇪 DE (Pflegeversicherung 覆盖居家但非 HaH)
  │
  ★     ─ 🇯🇵 JP (最大制度空白 — 有 ¥11.2兆介護保険 却无急性 HaH 编码)
  │
  ☆     ─ 🇭🇰 HK (几乎空白 — 无沙盒、无编码、无 VHIS 覆盖)
```

---

## 九、关键洞察与对 iHomeCare（香港）的启示

### 9.1 支付是 HaH 规模化的必要条件

全球证据一致表明：**没有独立支付编码 = 没有规模化**。日本的经验最为典型——虽有全球最成熟的介護保険（¥11.2兆/年，706万认定者），但因缺乏急性期 HaH 支付编码，在宅医療始终停留在慢性管理层面，无法替代急性住院。

### 9.2 三大成功模式

| 模式 | 代表市场 | 核心特征 | 适合香港？ |
|:----|:------|:------|:---:|
| **行政试办驱动** | 🇹🇼台湾 | NHI 以行政命令启动「在宅急症照護試辦計畫」，无需修法；支付编码在试办中同步建立 | ✅ 极高 |
| **监管沙盒→主流化** | 🇸🇬新加坡 | MOHT 沙盒同时解决监管+支付；2年后正式纳入 MOH 补贴+MediSave+保险全覆盖 | ✅ 极高 |
| **公私混合交付** | 🇦🇺澳洲 | Amplar Health (Medibank 子公司) 与州政府签约交付 HITH；公私分工清晰 | ✅ 可行 |

### 9.3 对香港的 7 条可操作建议

1. **启动 HA HaH 行政试办计划** — 参照台湾 NHI 模式，以 HA 行政命令启动 2-3 联网试点，无需等待立法
2. **建立 HaH 内部结算价** — 从第一天起设立独立的 HaH 按日结算价（如 HK$1,500-2,500/日），避免日本碎片化困局
3. **推动 VHIS 扩展** — 与保险业监管局（IA）协商，将 HaH 纳入 VHIS 标准计划的住院替代选项
4. **设立创新沙盒** — 参照新加坡 MOHT，在 HA 内部或卫生局下设立 HaH 创新沙盒机制
5. **引入公私合作** — 允许 AIA/Bupa/Prudential 等投资 HaH 交付公司，与 HA 签约服务
6. **建立质量支付框架** — 试点期间即设计 P4P 指标（再入院率、患者满意度、成本节省分成）
7. **政府高层背书** — 新加坡的经验证明：部长级别的公开承诺（"患者不会多付一分钱"）对规模化至关重要

---

## 十、数据来源与交叉验证

### Tier 1 — 官方政务源

- [T1-政府] CMS "Report on the Study of the Acute Hospital Care at Home Initiative", 2024.9
- [T1-政府] CMS FY2025 IPPS Final Rule (CMS-1808-F)
- [T1-政府] CMS AHCAH Data Release Fact Sheet, 2024.1
- [T1-政府] MedPAC "Medicare's Acute Hospital Care at Home Program", June 2024
- [T1-政府] NHS England — Virtual Wards Operational Framework
- [T1-政府] NHS England — NHS Payment Scheme 2025/26
- [T1-政府] MHLW 厚生労働省「令和6年度診療報酬改定の概要【在宅】」, 2024
- [T1-政府] BMG "Pflegeversicherung" & Pflegeneuordnungsgesetz (PNOG) 草案, 2026.6
- [T1-政府] MOH Singapore — MIC@Home 主流化宣布, Straits Times, 2024.3
- [T1-政府] MOHT Singapore — MIC@Home Programme page
- [T1-政府] NHIA 台湾 —「全民健康保險在宅急症照護試辦計畫」, 2024.7
- [T1-政府] NHIA 台湾 — 2024-2025 Annual Report
- [T1-政府] Queensland Health — Hospital in the Home Guideline
- [T1-政府] HA 香港 — Fees and Charges; VHIS 官网

### Tier 2 — 学术/机构源

- [T2-学术] JBI Evidence Implementation "Hospital-at-home care in Singapore: distilling policy and implementation strategies", 2025
- [T2-学术] PLOS One "A qualitative exploration of health system partners' state of readiness", 2025
- [T2-学术] PMC "Length of stay and economic sustainability of virtual ward care", 2024
- [T2-学术] Annals Academy of Medicine "NUHS@Home retrospective study", 2023
- [T2-学术] AHA "Fact Sheet: Extending the Hospital-at-Home Program", 2024
- [T2-学术] Commonwealth Fund — International Health System Profiles
- [T2-机构] Access Group "Virtual Wards Funding and Costs", 2025
- [T2-机构] Grattan Institute "Smarter Spending", 2025

### Tier 3 — 行业媒体（仅供佐证）

- [T3-媒体] AMA "Hospital at home saves lives and money", 2024
- [T3-媒体] Healthcare Finance News "CMS releases AHCAH study", 2024
- [T3-媒体] Straits Times "Subsidised hospital care in the comfort of home", 2024.3

### 内部知识库引用

- Kate 知识库: 美国-HaH.md, 英国-HaH.md, 日本-介護保険.md, 德国-Pflege.md, 澳大利亚-HaH.md, 新加坡-HaH.md, 台湾-HaH.md, 香港-HaH.md
- Kate 知识库: 各国HaH借鉴价值矩阵.md, 居家医疗支付体系对比.md
- 历史报告: 2026-07-03-singapore-moht-hah-analysis.md, 2026-06-28-hk-hah-strategic-planning-full.md

### ⚠️ 数据缺失声明

- **台湾NHI日支付精确金额**: 在宅急症照護試辦計畫的每日醫療費+護理費确切点数来自 NHIA 内部支付标准文件，PDF 提取受限。当前使用估算范围 NT$3,000-5,000/日。建议后续从台湾在宅医療学会或 NHIA 公开发布的支付标准 PDF 中精确提取。
- **澳洲HITH全国统一价**: 澳洲 HITH 为州级管理，无全国统一支付标准。当前金额范围为多州数据综合估算。
- **德国HaH住院替代支付**: 德国目前无专门的"krankenhausersetzende Behandlung zu Hause"支付编码。当前数据为最接近的 Pflegeversicherung + §37 SGB V 给付。

---

## 附录 A：关键制度时间线

```
1995 ─ 🇩🇪 DE: Pflegeversicherung 实施
2000 ─ 🇯🇵 JP: 介護保険 实施
2016 ─ 🇹🇼 TW: 居家醫療照護整合計畫 启动
2019 ─ 🇸🇬 SG: MOHT 提出 Home Hospital 概念
2020 ─ 🇺🇸 US: CMS AHCAH Waiver 启动 (COVID-19)
2022 ─ 🇸🇬 SG: MIC@Home 监管与融资沙盒启动
2024.04 ─ 🇸🇬 SG: ★ MIC@Home 沙盒→主流化
2024.07 ─ 🇹🇼 TW: ★ 在宅急症照護試辦計畫 启动
2025.03 ─ 🇬🇧 UK: NHS 达成 20 virtual ward beds/100K
2025.12 ─ 🇺🇸 US: House 通过 H.R.4313（延至2030）
2026.06 ─ 🇩🇪 DE: PNOG 法案公布（2027.1 实施）
2026.07 ─ 🇭🇰 HK: iHomeCare 仍在提案阶段
```

---

*报告完成。数据截止 2026-07-03。后续更新应追踪：台湾 ACAH 试办计划正式化时间表、美国 AHCAH Waiver 永久化立法进展、德国 PNOG 实施对 HaH 的影响、香港 HA 试点进展。*
