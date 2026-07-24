---
tags: [rss, monitoring, strategy, cross-region]
created: 2026-07-23
updated: 2026-07-23
aliases: [HaH RSS Monitor, Policy RSS, 全球政策RSS]
---

# HaH 全球政策 RSS 监控

> 17 个 RSS 源覆盖 10+ 地区，每 6 小时自动扫描，10:00 每日简报聚合。

## 当前配置

| 源 | 地区 | 类型 | 状态 |
|----|------|------|------|
| Google News RSS — HaH Global | 全球 | Google News | ✅ |
| Google News RSS — US | 美国 | Google News | ✅ |
| Google News RSS — UK | 英国 | Google News | ✅ |
| Google News RSS — AU | 澳大利亚 | Google News | ✅ |
| Google News RSS — SG | 新加坡 | Google News | ✅ |
| Google News RSS — TW | 台湾 | Google News | ✅ |
| Google News RSS — HK | 香港 | Google News (gl=US workaround) | ✅ |
| Google News RSS — CA | 加拿大 | Google News | ✅ |
| Google News RSS — JP | 日本 | Google News | ✅ |
| MHLW RSS | 日本 | 厚生劳动省官方 | ✅ |
| Google News RSS — DE | 德国 | Google News | ✅ |
| Google News RSS — FR | 法国 | Google News | ✅ |
| Google News RSS — KR | 韩国 | Google News | ✅ |
| Google News RSS — CN | 中国 | Google News | ✅ |
| Google News RSS — IL | 以色列 | Google News | ✅ |
| Google News RSS — BR | 巴西 | Google News | ✅ |
| Google News RSS — NL | 荷兰 | Google News | ✅ |

## 关键词告警级别

- 🔴 **高优先级**：政策变革、新立法、大额融资、并购
- 🟡 **中优先级**：试点项目、临床证据、市场准入更新
- ⚪ **低优先级**：行业动态、会议简报、人事变动

## 相关工作流

- 每日简报：`topics/每日资讯.md`（自动追加）
- 完整报告：`reports/*hah-policy-rss-briefing.md`（cron 输出）
- 配置来源：`rss-policy-monitor` skill
