# Kate 知识库 v4.0

> 一句话：全球政府都在把医疗从医院搬到家里，但每个国家卡在不同的地方——香港卡在第一步（支付方未定），日本卡在最后一步（劳动力不够）。这个知识库帮你找到你的国家卡在哪一步。

## 这是什么

一个专注于**居家医疗（Hospital-at-Home / Home Health / 长期护理保险）**的全球研究知识库。

- 📊 **178 份深度报告**：覆盖 17 个国家、54 家公司
- 🏠 **香港优先**：iHomeCare 总部所在地，所有分析以香港决策为锚点
- 🤖 **自动更新**：RSS 监控 + 每日简报 + 数据新鲜度检测
- 📱 **一键分享**：每份报告自动生成精美 HTML，微信直接发投资人

## 快速开始

- **我是 Kenneth**：打开 `pages/hong-kong/overview.md` ——你今天该知道的 3 件事
- **我是投资人**：打开 `html/index.html` —— 178 份报告目录，搜索/筛选/查看
- **我是 AI Agent**：读取 `data/facts.json` —— 结构化数据，可直接 fine-tune

## 架构

```
data/    → 结构化事实（JSON，机器可读）
pages/   → 人类视图（.md，Obsidian 可编辑）  
reports/ → 深度报告（.md 源文件 + .html 发布版）
html/    → 精美 HTML（单文件，可分享）
scripts/ → 自动化管线（搜索/摄入/刷新/出版）
```

## 许可证

MIT · Kenneth Ye · iHomeCare
