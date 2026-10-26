---
layout: default
title: "AIHOT 每日情报：2026-10-26"
date: 2026-10-26
lang: zh
---

> 从 11 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [memt-1.0 架构解析：内存原生设计及效率提升](#item-tech-news-1) ⭐️ 8.0/10
2. [10 年旧 CNN 在皮肤癌诊断中优于前沿 LLM 引发技术行业模型有效性讨论](#item-tech-news-2) ⭐️ 7.0/10
3. [南贝吉发布南贝吉 4.3-33B，Apache 2.0 授权的小型代理教师模型](#item-tech-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### memt-1.0 架构解析：内存原生设计及效率提升 ⭐️ 8.0/10

memt-1.0 架构引入了内存原生设计，采用 gated deltanet-2 和 mixture-of-storage 技术，实现了对代理内存的效率提升和存储占用减少。

reddit · r/MachineLearning · /u/Mrs-Grumpy23 · 10月25日 05:31

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1xeu0ht/memt10_architecture_breakdown_gated_deltanet2/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1xeu0ht/memt10_architecture_breakdown_gated_deltanet2/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** 机器学习（ML）是人工智能的一个分支，它使计算机能够从数据中学习并做出预测或决策，而无需为每个任务明确编程。在机器学习中，我们称这样的性能衡量函数为损失函数。对于回归问题，存在几种流行的损失函数。例如，均方误差（MSE）是最常用的损失函数之一。scikit-learn 是一个用于 Python 的机器学习库，它提供了许多常用的机器学习算法和工具，使得在 Python 中进行高级分析变得容易。

**「影响」** memt-1.0 在 128k 历史长度的上下文中，相比全上下文 kv 缓存设置，实现了约 1.86 倍的端到端推理速度提升和 66 倍的持久化存储减少，这对于构建长期代理具有重要意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/machine-learning/machine-learning-tutorial/" target="_blank" rel="noopener noreferrer">Machine Learning Tutorial - GeeksforGeeks</a></li>
<li><a href="https://mlu-explain.github.io/linear-regression/" target="_blank" rel="noopener noreferrer">A visual, interactive explanation of linear regression for machine ...</a></li>
<li><a href="https://scikit-learn.org/stable/index.html" target="_blank" rel="noopener noreferrer">scikit- learn : machine learning in Python — scikit- learn ...</a></li>

</ul>
</details>

**标签**: `#MachineLearning`, `#AI`, `#MemoryManagement`, `#Efficiency`, `#SoftwareEngineering`

---

<a id="item-tech-news-2"></a>
### 10 年旧 CNN 在皮肤癌诊断中优于前沿 LLM 引发技术行业模型有效性讨论 ⭐️ 7.0/10

一项研究表明，一个 10 年前的卷积神经网络（CNN）在皮肤癌诊断方面优于前沿的大型语言模型（LLM），引发了关于模型有效性的行业讨论。

hackernews · sungam · 10月25日 17:15 · [社区讨论](https://news.ycombinator.com/item?id=50233779)

<div class="story-actions"><a class="story-action story-action--primary" href="https://lynchlab.net/llm-skin-cancer" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://lynchlab.net/llm-skin-cancer">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** 卷积神经网络（CNN）在皮肤癌诊断方面的应用已有 10 年历史，最近的一项研究显示，一个 10 年前的 CNN 在皮肤癌诊断方面优于前沿的大型语言模型（LLM）。这一发现引发了关于模型有效性的技术行业内的讨论。研究表明，与 GPT-6 Astra 和 Claude Fable 5.1 等前沿 LLM 相比，这个老式的 CNN 在诊断皮肤癌方面表现更佳。这一结果对于软件工程和 AI 系统领域的研究人员具有重要意义。

**「影响」** 这项研究表明，一个 10 年前的卷积神经网络（CNN）在皮肤癌诊断方面的表现优于前沿的大型语言模型（LLM），这可能会促使医疗行业重新评估和优化 AI 模型的选择和应用。对于皮肤癌患者来说，这意味着更准确和及时的诊断，从而可能提高治疗效果。

**「社区讨论」** 社区讨论中，有人认为对于大规模应用，使用专门的设计架构（如神经网络、贝叶斯等）的分类器会更加准确。同时，也有人指出，尽管 LLM 在参数数量上远超旧 CNN，但在某些特定任务上（如围棋）表现不佳，这表明 LLM 在其他方面可能更有优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/cnn-beats-gpt-6-astra-claude-fable-5-1-skin-cancer-diagnosis-lynch-2026" target="_blank" rel="noopener noreferrer">CNN vs GPT-6 Astra vs Fable 5.1: Skin Cancer, 62% vs 42% ...</a></li>
<li><a href="https://lynchlab.net/llm-skin-cancer" target="_blank" rel="noopener noreferrer">A 10-year-old CNN outperforms frontier LLMs for skin cancer ...</a></li>
<li><a href="https://youlidao.ai/en/intelligence/10-year-old-cnn-beats-llms-skin-cancer-diagnosis" target="_blank" rel="noopener noreferrer">10-Year-Old CNN Beats LLMs at Skin Cancer Diagnosis</a></li>
<li><a href="https://lynchlab.net/llm-skin-cancer" target="_blank" rel="noopener noreferrer">A 10-year-old CNN outperforms frontier LLMs for skin cancer ...</a></li>
<li><a href="https://explainx.ai/blog/cnn-beats-gpt-6-astra-claude-fable-5-1-skin-cancer-diagnosis-lynch-2026" target="_blank" rel="noopener noreferrer">CNN vs GPT-6 Astra vs Fable 5.1: Skin Cancer, 62% vs 42% ...</a></li>
<li><a href="https://vexdynamics.com/news/older-cnn-outperforms-stateoftheart-llms-in-skin-cancer" target="_blank" rel="noopener noreferrer">Older CNN Outperforms State-of-the-Art LLMs in Skin Cancer ...</a></li>

</ul>
</details>

**标签**: `#AI in Medicine`, `#Machine Learning`, `#CNN vs LLM`, `#Skin Cancer Diagnosis`, `#Technology News`

---

<a id="item-tech-news-3"></a>
### 南贝吉发布南贝吉 4.3-33B，Apache 2.0 授权的小型代理教师模型 ⭐️ 7.0/10

南贝吉发布了南贝吉 4.3-33B，这是一个为小型代理设计的教师模型，在基准测试中展现出有前景的性能。该模型采用 Apache 2.0 许可证，使得模型对社区更加开放。

reddit · r/MachineLearning · /u/jatingargiitk · 10月25日 16:32

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1xf6x35/nanbeige_releases_nanbeige4333b_an_apache_20/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1xf6x35/nanbeige_releases_nanbeige4333b_an_apache_20/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** Nanbeige4.3-33B 是一个基于 Apache 2.0 许可的开源密集型代理编码模型，拥有 512K 的上下文窗口。该模型由 Nanbeige LLM Lab 开发，旨在用于代理编码和办公风格的协同工作任务。Nanbeige4.3-33B 在 Terminal-Bench 2.1 和 SWE-Bench Pro 上的表现显示出渐进的改进，尽管并非在所有方面都取得了最高分数。该模型的发布为机器学习领域带来了重要的发展，特别是对于那些对 AI 和计算机系统感兴趣的人来说。

**「影响」** Nanbeige4.3-33B 的发布为机器学习领域带来了重要的发展，特别是对于对 AI 和计算机系统感兴趣的人来说。该模型在 Terminal-Bench 2.1 和 SWE-Bench Pro 上的表现，虽然不是最高的，但展示了渐进的改进，值得关注。此外，Apache 2.0 许可证的使用使得该模型对社区更加开放。

**「社区讨论」** 目前没有可用的社区评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datastudios.org/post/nanbeige-4-3-33b-open-weight-dense-agentic-model-512k-context" target="_blank" rel="noopener noreferrer">Nanbeige4.3-33B: Apache 2.0 dense agentic coding model with ...</a></li>
<li><a href="https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/" target="_blank" rel="noopener noreferrer">Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding ...</a></li>
<li><a href="https://www.ai-digest-1.com/news/nanbeige-llm-lab-releases-nanbeige4-3-33b-open-agentic-coding-model-19432" target="_blank" rel="noopener noreferrer">Nanbeige LLM Lab Releases Nanbeige4.3-33B Open Agentic Coding ...</a></li>
<li><a href="https://arxiv.org/pdf/2512.06266v1" target="_blank" rel="noopener noreferrer">Nanbeige4-3B Technical Report: Exploring the Frontier of ...</a></li>
<li><a href="https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/" target="_blank" rel="noopener noreferrer">Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding ...</a></li>
<li><a href="https://www.datastudios.org/post/nanbeige-4-3-33b-open-weight-dense-agentic-model-512k-context" target="_blank" rel="noopener noreferrer">Nanbeige4.3-33B: Apache 2.0 dense agentic coding model with ...</a></li>

</ul>
</details>

**标签**: `#Machine Learning`, `#AI`, `#Model Release`, `#Benchmark Performance`

---