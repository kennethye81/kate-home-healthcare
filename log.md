# Wiki Log

> 全库操作日志。追加写入，500 条轮转。
> 格式：`## [YYYY-MM-DD] action | subject`
> Actions: create, update, ingest, query, lint, archive, delete

## [2026-07-24] ingest | 🇺🇸 美国每日情报监控 — 第二轮补充入库
- 新发现4篇高价值素材，追加入库
- P1: Homecare Homebase报告：63.3%拒绝转诊，RN离职率25.46%，护工34%，个人护理>70%
- P1: H1 2026 M&A全景（Levin）：55笔交易，41% PE，CMS注册暂停推高并购难度
- P2: 并购估值指南（CT Acquisitions）：Medicare HH 8-12x，非医疗7-11x，临终关怀9-15x+
- P0: CMS第三方RPM禁令草案（J&R Report版本，含Cadence临床证据：Mayo研究27%住院减少+JACC研究70%血压控制）
- 新增 raw: 4篇（文档负担报告+Levin H1 M&A+CT Acquisitions估值指南+CMS RPM禁令替代源）
- 更新: pages/global/美国/00-概览.md（追加文档负担报告，合并CMS RPM+M&A条目）
- 更新: pages/daily/2026-07-24-US-briefing.md（追加H1 M&A全景、估值指南、文档负担报告）

## [2026-07-24] ingest | 🇺🇸 美国每日情报监控（4维度）
- 4 维度（政策/行业/技术/M&A）× 7引擎并行搜索，约95条结果，筛选入库22条核心信息
- P0: CMS提议禁止第三方RPM供应商计费（2027医师费用表草案，2026-07-21）
- P1: Q2 2026居家医疗并购：量降价升（General Atlantic $30亿 + Kinderhook $11亿）
- P0: AHCAH豁免延长5年至2030年（回顾性入库AMA数据）
- P2: HHCN六大趋势、KFF Medicaid劳动力调查报告
- 新增 raw: 4篇原始文章
- 更新: pages/global/美国/00-概览.md 最新动态（+3条）
- 更新: pages/global/美国/01-政策与法律法规.md（+RPM政策章节+其他政策动态）
- 新增: pages/daily/2026-07-24-US-briefing.md

## [2026-07-23] create | Wiki 初始化（llm-wiki skill）
- 创建 SCHEMA.md — 领域定义、标签体系、frontmatter 规范
- 创建 index.md — 全库内容目录（国家/机构/专题/对比/模板）
- 创建 log.md — 操作日志
- 创建 raw/ — 不可变原始来源目录
- 清理运维类文档（双工具协同运维手册、Hermes向量诊断、质控报告、架构设计）
- 重组 topics/ 为 5 子分类（clinical/economics/tech/workforce/strategy）
- 更新 Home.md — 聚焦 HaH/Healthcare Tech 导航
- 精简 config.yaml — 移除 Quartz/publish 残留
- 知识库状态：16 国 × 79 机构 × 136 报告 × 9 专题 × 20 期简报 = 347 文件

## [2026-07-23] create | 新增 Adaptive Innovations（AI 原生居家医疗）
- 按 llm-wiki 流程完成完整 ingest：
  - ① 抓取原始来源 → raw/sources/2026-06-adaptive-innovations-series-a.md（4 个来源聚合）
  - ② 创建实体页 → pages/global/美国/03-头部机构/Adaptive-Innovations.md（frontmatter + 关键数据 + 商业模式）
  - ③ 更新 US 概览页 → 追加最新动态 + 头部机构索引
  - ④ 更新 index.md → 新增 Adaptive-Innovations 到 US 机构列表
  - ⑤ 更新 log.md → 本条目
- 公司信息：$50M Series A（Felicis 领投），再住院率 <5%，文档时间减 80%
- 当前状态：8 国 × 68 机构 × 136 报告 × 9 专题 = 294 文件
- **注意：** 用户要求新闻级内容不建 03-头部机构 实体页。Adaptive-Innovations.md 已删除，仅保留 raw/sources/ + US 概览页最新动态

## [2026-07-23] ingest | HaH 学术综述论文（PMC10229033）
- 来源：PMC 学术论文 "Hospital at Home: An Evolving Model for Comprehensive Healthcare" (2021)
- 保存到 raw/sources/2021-hah-evolving-model-comprehensive-healthcare.md
- 更新 US 概览页：追加到 相关报告 节
- 关键数据：成本降 32%、LOS 3.2 vs 4.9 天、再住院率 8.6% vs 15.6% (Mount Sinai)

## [2026-07-23] ingest | HaH 系统综述（PMC11587637）
- 来源：BMC Health Services Research 2024 系统综述 "Dimensions and Components of Hospital-at-Home Care"
- 保存到 raw/sources/2024-hah-dimensions-systematic-review.md
- 更新 US 概览页：追加到 相关报告 节
- 关键数据：179 篇文章纳入、88 个维度/组件、7 大类别
- 最常报告组件：成本节省(n=30)、患者满意度(n=23)、减少再入院(n=13)

## [2026-07-23] ingest | 新加坡 MIC@Home 扩大至全岛（CNA）
- 来源：Channel News Asia 2026-07-22
- 保存到 raw/sources/2026-07-singapore-mic@home-expansion.md
- 更新新加坡概览页：追加到 最新动态 节
- 关键数据：MIC@Home 扩展至所有政府重组医院；152人已受益 + 150人年底前；THKMC 60人护理团队；THRIVE 项目使入院/急诊降约1/3

## [2026-07-23] ingest | 中国家庭病床服务试点（CGTN）
- 来源：CGTN 2026-06-14 "Hospital at Home: How China's Push for In-Home Medical Care Actually Works"
- 保存到 raw/sources/2026-06-china-home-hospital-bed-guidelines.md
- 内容：中国卫健委"家庭病床服务"试点指南，社区医疗站为患者提供居家住院级照护
- 注意：中国不在当前知识库 8 国范围内，仅存档原始来源

## [2026-07-23] ingest | HaH 新技术综述（JMIR 2026）
- 来源：JMIR 2026-04-20 "Hospital-at-Home: New Technology Brings Acute Care to Patients' Homes"
- 保存到 raw/sources/2026-04-jmir-hah-new-technology.md
- 更新 US 概览页：追加到 相关报告 节
- 关键内容：Bruce Leff（Johns Hopkins）HaH 先驱访谈；远程监测/AI/可穿戴设备；"未来医院只剩 ER/OR/ICU"

## [2026-07-23] ingest | HHCN 2026 年居家健康趋势
- 来源：HHCN 2026-01 "Top Home Health Trends for 2026"
- 保存到 raw/sources/2026-01-hhcn-top-home-health-trends.md
- 更新 US 概览页：追加到 最新动态 节
- 六趋势：裁员、AI人性化、TEAM支付模型、纯居家模式终结、HaH萎缩、垂直整合放缓

## [2026-07-23] ingest | DispatchHealth + Saint Francis HaH 项目启动
- 来源：HHCN 2026-02
- 保存到 raw/sources/2026-02-dispatchhealth-saint-francis-hah.md
- 更新 US 概览页：追加到 最新动态 节
- 关键数据：俄克拉荷马州 Tulsa，初始 5-6 患者容量，目标 40 床，20 英里半径

## [2026-07-23] ingest | 3 篇 HaH 来源
- ① JAMA 研究 (HHCN 2026-05): HaH 降院内死亡率(0.4% vs 3.6%)和ED就诊，不降再入院
- ② HHCN 2023-07: HaH 市场赢家报告—Inbound Health/Biofourmis/Current Health
- ③ npj Digital Medicine 2024: Pandit/Leff/Topol US HaH 综述
- 均保存到 raw/sources/，更新 US 概览页 最新动态+相关报告

## [2026-07-23] ingest | Mordor Intelligence 全球居家医疗市场报告
- 来源：GlobeNewswire/Mordor Intelligence 2026-03
- 保存到 raw/sources/2026-03-mordor-home-healthcare-market.md
- 关键数据：全球市场 $335B(2025) → $545.69B(2031)，CAGR 8.46%

## [2026-07-23] ingest | 平安居家养老白皮书
- 来源：平安人寿/21世纪经济报道（PDF，中文）
- 保存到 raw/sources/pingan-china-home-elderly-care-white-paper.md
- 中国居家养老全景数据：2.64亿60+人口、9073格局、8-10万亿养老金缺口
- 注意：中国不在当前知识库范围，仅存档为参考

## [2026-07-23] ingest | Bain APAC Front Line of Healthcare 2026
- 来源：Bain & Company 2026 年亚太医疗报告（PDF，65K 字符）
- 保存到 raw/sources/2026-bain-apac-frontline-healthcare.md
- 更新新加坡概览页：telehealth 61% 渗透率、Healthier SG、38% 缺家庭医生
- 更新澳大利亚概览页：医生临床体验数据（90%/45%/35%）
- 深度分析见下文
