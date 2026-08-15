# Wiki Log

> 全库操作日志。追加写入，500 条轮转。
> 格式：`## [YYYY-MM-DD] action | subject`
> Actions: create, update, ingest, query, lint, archive, delete

## [2026-08-15] archive | 知识库结构修复（专题/对比/报告归位 + 残留清理）
- 🔧 pages/专题/（13 专题）→ topics/；pages/对比分析/（4 对比）→ pages/compare/
- 🧹 删除 Topics/ 空壳、System/Lint/、pages/国家/、Projects/、空文件启动路径
- 📦 6 robotics 27dim 报告归位 reports/国家/{国}/（澳/新/中/日/美/英）
- 🔗 29 处 wikilink 旧路径引用修复，0 断裂
- 🛡️ macOS 大小写不敏感误删事故，git 100% 恢复，数据零丢失
- 保留: copilot/ scripts/ daily-brief/ 主题/（跨国家专题）专题/（项目文档）

## [2026-08-01] ingest | 🇨🇳 中国 每日情报监控（4维度）
- 🇨🇳 4 维度（政策/行业/技术/M&A）× 8引擎并行中搜索，~80条结果
- P0: 长护险省级大规模落地加速——青海/辽宁/湖南/贵州4省密集发布实施方案
- P0: 贵州黔府办发〔2026〕11号全文入库（费率0.3%，2028年底全覆盖）
- P0: 湖南征求意见稿全文入库（3年三步走）
- P1: 泰州孝馨智慧家庭养老获长护险资质（智慧养老×长护险耦合案例）
- P1: 中研网报告：智慧养老行业并购重组窗口期
- 新增 raw: 3篇
- 更新: pages/global/中国/01-政策与法律法规.md（+5项省级落地里程碑）
- 新增: pages/daily/2026-08-01-china-briefing.md

## [2026-07-29] ingest | 🇬🇧 英国 每日情报监控（4维度）
- 🇬🇧 4 维度（政策/行业/技术/M&A）× 8引擎并行搜索，72+条结果
- P0: NHS Virtual Wards Operational Framework正式发布（PRN01289）
- P1: SMART虚拟病房80→120张+24/7运营，年底200床目标
- P1: Nelson Advisors虚拟病房五年战略预测（2026-2031）
- P2: Doccla AI虚拟病房数据（住院-61%, GP预约-89%, 非选择性入院-39%）
- P2: Grant Thornton Q1 UK医疗M&A 114笔（+37% YoY）
- P3: UK Parliament POST发布虚拟病房研究简报PN-0744
- 新增 raw: 7篇
- 更新: pages/global/英国/00-概览.md + 01-政策与法律法规.md
- 新增: pages/daily/2026-07-29-uk-briefing.md
- 更新: Updates.md

## [2026-07-28] ingest | 🇯🇵 日本 + 🇹🇼 台湾 每日情报监控（4维度）
|- 🇯🇵 4 维度（政策/行业/技术/M&A）× 8引擎并行搜索，约67条结果
|- P0: 2026年度介護報酬臨時改定6月施行——訪問介護28.7%、訪問看護1.8%加算新設
|- P1: 訪問看護ステーション最新データ13選（社保審第259回）——19,314事業所、収支差率10.3%
|- P1: 診療報酬改定2026在宅医療——重症患者要件・D to P with N新設
|- P2: 予防型介護DX——未病管理+非拘束センシング+空間センシングのハイブリッド
|- P3: 2026年介護M&A動向——業界再編加速
|- 新增 raw: 3篇日本（GemMed+ビジケア+Liquid Design）
|- 新增 raw: 3篇台湾（行政院長照3.0+津台洽谈会+US商務部遠距医療報告）
|- 更新: pages/global/日本/00-概览.md（+5条目）
|- 更新: pages/global/日本/01-政策与法律法规.md（+2026報酬詳細+診療報酬改定）
|- 更新: pages/global/台湾/00-概览.md（+4条目）
|- 更新: pages/global/台湾/01-政策与法律法规.md（+長照3.0章節）
|- 新增: pages/daily/2026-07-28-japan-briefing.md
|- 新增: pages/daily/2026-07-28-taiwan-briefing.md
|- 更新: Updates.md（+9条目）
|- 🇹🇼 中文--zh模式将「台湾」误解析为「台州」→改用英语搜索改善

## [2026-07-31] ingest | 🇺🇸 US Daily Intelligence Monitoring
- 4-dimension search: policy, industry, technology, M&A
- 6 raw articles saved (CMS AHCAH data release, RPM/RTM/AI codes, HHCN trends, Hendon Q2 M&A, Capstone sector update, Galen Growth funding)
- Updated: pages/global/美国/00-概览.md (+5 entries), pages/global/美国/01-政策与法律法规.md (+3 entries)
- Created: pages/daily/2026-07-31-us-briefing.md
- Updated: Updates.md

## [2026-07-30] ingest | 🇦🇺 澳大利亚 + 🇨🇦 加拿大 每日情报监控（4维度）
|- 🇦🇺 4 维度（政策/行业/技术/M&A）× --fast 多引擎搜索，59条结果
|- 🇨🇦 4 维度（政策/行业/技术/M&A）× --fast 多引擎搜索，53条结果
|- P0: 🇦🇺 Support at Home Program全面取代Home Care Packages（新Aged Care Act生效）
|- P1: 🇦🇺 CHA敦促加速HITH资金改革
|- P1: 🇦🇺 居家医疗市场规模 USD 12.9B→USD 28.0B(2034), CAGR 8.71%
|- P1: 🇦🇺 Telehealth并购AUD 16亿（2026-02）；ANZ早期5笔交易合计$1.8亿
|- P2: 🇦🇺 患者监测市场 USD 1.4B→USD 3.3B(2034), CAGR 9.22%
|- P0: 🇨🇦 Connected Care for Canadians Act推出（联邦健康信息互通立法）
|- P1: 🇨🇦 居家护理行业 CAGR 6.3%（2021-2026, IBISWorld）
|- P1: 🇨🇦 Q1 2026居家护理并购6笔（环比翻倍）；2025全年+40.5% YoY
|- P1: 🇨🇦 WELL Health收购Equinoxe（魁北克居家护理）
|- P2: 🇨🇦 RPM市场2026年$39.6亿，AI居家监测加速
|- web_extract不可用（432错误），全文基于搜索snippets重构
|- 新增 raw: 17篇（AU 8篇 + CA 9篇）
|- 更新: pages/global/澳大利亚/00-概览.md（+5条目）
|- 更新: pages/global/加拿大/00-概览.md（+5条目）+ 01-政策.md（+Connected Care Act）
|- 新增: pages/daily/2026-07-30-australia-briefing.md + 2026-07-30-canada-briefing.md

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

## [2026-07-25] ingest | 🇨🇳 中国每日情报监控（4维度）
- 4 维度（政策/行业/技术/投资）× Bocha (--zh) 搜索，128 条目 → 筛选入库 14 条核心信息
- **P0：** 8省2026年Q2密集发布长护险实施方案——青海（青政办〔2026〕12号）、山西（费率0.3%,居民首年0.15%）、贵州（黔府办发〔2026〕11号）、江西、辽宁、河南（三年递进模式）、湖南、甘肃
- **P1：** 全国银发经济企业近20万家，2025年同比增长23.95%（经济日报/全国组织机构统一社会信用代码数据服务中心）
- **P1：** 国家长护险数字化平台「云护计划」正式启动（2026-07-16），物联网+AI 监控服务全过程
- **P2：** 中研普华预计智慧养老行业进入整合期，头部企业通过并购扩大市场份额
- 新增 raw: 6篇（山西方案+河南时间表+多省汇总+云护计划+银发经济企业+并购报告）
- 更新: pages/global/中国/01-政策与法律法规.md（+各省实施方案详情表+时间表差异分析）
- 更新: pages/global/中国/00-概览.md（+2条最新动态+修复死链接3处）
- 新增: pages/daily/2026-07-25-China-briefing.md
- 修复: pages/global/中国/01-政策与法律法规.md 死链接3处（../../ → `reports`/`topics`/`pages`）

## [2026-07-26] query | Weekly Summary 2026-07-20 ~ 2026-07-26
- 本周监控覆盖：SG+HK（RSS）→ JP+TW（RSS）→ UK（HHCN+DHL）→ AU+CA（跳过，v5.0重构占用）→ US（4维×7引擎，95条→22条入库）→ China（4维×Bocha --zh，128条→14条入库）
- **P0 最高：** 中国8省LTCI方案密集发布 + CMS提议禁止第三方RPM供应商计费（2027医师费用表草案）
- **P1：** 美国Q2 M&A量降价升（GA $30亿 + Kinderhook $11亿）、AHCAH豁免延长至2030年
- **P1：** 中国云护计划启动、银发经济企业近20万家
- **报告产出：** Bamboos 2293.HK × Evercare × Sollis Health 三份27dim尽调（2026-07-24）
- **结构更新：** v5.0 重构——llm-wiki初始化、SCHEMA.md+index.md+log.md创建、topics/重组为5子分类、运维文档清理
- 新增 raw: 15篇（US 9篇 + China 6篇）
- 更新: 7个国家页面 + 3期简报 + Home.md死链修复

## [2026-07-27] ingest | 🇸🇬 新加坡 + 🇭🇰 香港 每日情报监控
- **🇸🇬 政策：** MIC@Home扩大至全岛所有政府重组医院（CNA）、MOH社区护理薪资修订（ST）、医疗人力20%增长目标（ST）
- **🇸🇬 技术：** NHG Health AI驱动居家护理生态（HMA）
- **🇸🇬 M&A：** iWOW科技S$11.2M收购The Gentle Group（ST）
- **🇭🇰 政策：** 院舍修订条例2026年10月生效（HCP新职级）、2026-27预算案安老服务券扩容、照顾者支援措施进展（LegCo）
- **🇭🇰 技术：** SCHSA智能跌倒侦测系统试点500户
- **🇭🇰 M&A：** 嘉涛（香港）控股2026年全年业绩利润增长56%
- 新增 raw: 10篇（SG 5篇 + HK 5篇）
- 更新: SG 00-概览 + 01-政策 + HK 00-概览 + 01-政策
- 新增: pages/daily/2026-07-27-sg-briefing.md + hk-briefing.md
