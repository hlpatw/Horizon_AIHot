---
layout: default
title: "AIHOT 每日情报：2026-10-31"
date: 2026-10-31
lang: zh
---

> 从 15 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [多令牌预测的正确做法](#item-tech-news-1) ⭐️ 9.0/10
2. [VS Code 扩展 Claude Code 存在后门](#item-tech-news-2) ⭐️ 7.0/10
3. [使用 Qwen 权重在 1GB 内运行工作的任天堂娱乐系统](#item-tech-news-3) ⭐️ 7.0/10
4. [本条资讯的中文解读暂未生成](#item-tech-news-4) ⭐️ 7.0/10
5. [Azure 的弱点：五个完整的跨租户妥协](#item-tech-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### 多令牌预测的正确做法 ⭐️ 9.0/10

介绍了一种在多令牌预测（MTP）领域的突破性改进，引入了软-MTP 和 KL 梯度恢复技巧，从而提高了 MTP 在各种任务中的性能。

reddit · r/MachineLearning · /u/jayden\_teoh\_ · 10月30日 18:53

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1xjnz40/multitoken_prediction_done_right_r/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1xjnz40/multitoken_prediction_done_right_r/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** 多令牌预测（MTP）是一种在机器学习和人工智能领域中常用的预训练方法。它通过让模型预测未来短块令牌来部分放松了传统的下一个令牌预测（NTP）。MTP 通常被宣传为一种通用的推理方法，但在实际应用中，它可能会受到噪声残差的影响，从而损害下一个令牌的预测。此外，MTP 的梯度隐藏了一个 KL 自蒸馏信号，这对于改进推测解码是有益的。

**「影响」** 这项研究为 Multi-Token Prediction \(MTP\)领域带来了显著的进步，通过引入 Soft-MTP 和 KL 梯度恢复技巧，显著提高了 MTP 在各种任务中的性能。这一改进对于机器学习和人工智能领域的研究者来说是一个重要的里程碑，因为它提供了一种新的方法来提升 MTP 的性能，从而可能推动相关应用的发展。

**「社区讨论」** 目前没有可用的社区评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2510.14751" target="_blank" rel="noopener noreferrer">Beyond Multi - Token Prediction : Pretraining LLMs with Future...</a></li>
<li><a href="https://www.linkedin.com/posts/kamen-stoykov-80413b54_multi-token-prediction-mtp-is-often-pitched-activity-7467572378034782226-u-Vc" target="_blank" rel="noopener noreferrer">Multi - Token Prediction ( MTP ) is often pitched as a universal inference...</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/12181" target="_blank" rel="noopener noreferrer">[Feature]: Multi - Token Prediction ( MTP ) · Issue #12181...</a></li>
<li><a href="https://www.tandfonline.com/doi/abs/10.2753/MTP1069-6679190202" target="_blank" rel="noopener noreferrer">tandfonline.com/doi/abs/10.2753/ MTP 1069-6679190202</a></li>
<li><a href="https://www.youtube.com/watch?v=qAVzRmgRvgU" target="_blank" rel="noopener noreferrer">Installing MTP Software - YouTube</a></li>
<li><a href="https://www.taylorfrancis.com/books/mono/10.1201/9781315371658/machine-learning-mohssen-mohammed-muhammad-badruddin-khan-eihab-bashier-mohammed-bashier" target="_blank" rel="noopener noreferrer">Machine Learning | Algorithms and Applications | Mohssen...</a></li>

</ul>
</details>

**标签**: `#MachineLearning`, `#AI`, `#MTP`, `#Pre-training`, `#Soft-MTP`

---

<a id="item-tech-news-2"></a>
### VS Code 扩展 Claude Code 存在后门 ⭐️ 7.0/10

Cursor Marketplace 上的 VS Code 扩展 Claude Code 被发现存在后门，可能影响用户的 SSH 密钥。恶意行为者利用 Cursor 市场发布篡改版的 Claude Code 扩展，该扩展并非由 Anthropic 构建或发布，官方渠道的版本不受影响。

hackernews · \_chall · 10月30日 07:09 · [社区讨论](https://news.ycombinator.com/item?id=50300683)

<div class="story-actions"><a class="story-action story-action--primary" href="https://phorion.io/blog/offical-claude-code-vsx-compromise/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://phorion.io/blog/offical-claude-code-vsx-compromise/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** Claude Code 是一款用于 VS Code 的扩展程序，它允许用户在编辑代码时进行智能补全和代码分析。该扩展程序托管在 Cursor Marketplace 上。最近，Cursor Marketplace 上的一款 Claude Code 扩展程序被发现存在安全漏洞，这可能对用户的 SSH 密钥造成影响。这个安全漏洞是由一个恶意行为者利用 Cursor 市场访问权限发布的篡改版 Claude Code 扩展程序引起的，这个版本并非由 Anthropic 开发或发布。

**「影响」** 受影响的用户需要检查其 SSH 授权密钥，以确定是否被恶意扩展修改。如果发现名为&\#x27;svc-telemetry&\#x27;的密钥，则表明机器受到了影响，需要采取相应的修复措施。

**「社区讨论」** Felix from Anthropic 表示，他们正在与 Cursor 合作处理此事件，但事件并非 Anthropic 系统或员工笔记本电脑的妥协。恶意行为者利用 Cursor 市场的访问权限发布了篡改版的 Claude Code 扩展。jonas21 提供了检查是否受影响的命令，而 AdrianCX 询问了事件的起源和发生方式。yubblegum 提到了 Phorion 报告的详细信息，而 xx\_ns 对受影响的扩展市场表示了不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html" target="_blank" rel="noopener noreferrer">Official Claude Code VS Code Extension Compromised to Install...</a></li>
<li><a href="https://cursor.com/blog/claude-code-extension-security-notice" target="_blank" rel="noopener noreferrer">Security notice — malicious version of Anthropic. claude - code ...</a></li>
<li><a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/" target="_blank" rel="noopener noreferrer">Official Claude Code Extension Compromise: Security ... | Phorion</a></li>
<li><a href="https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html" target="_blank" rel="noopener noreferrer">Official Claude Code Extension on Cursor Marketplace ...</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/" target="_blank" rel="noopener noreferrer">Inside a malicious Claude Code-branded extension and its ...</a></li>
<li><a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/" target="_blank" rel="noopener noreferrer">Official Claude Code Extension Compromise: Security Advisory</a></li>

</ul>
</details>

**标签**: `#Security Breach`, `#VS Code Extension`, `#SSH Keys`, `#Cursor Marketplace`, `#Software Security`

---

<a id="item-tech-news-3"></a>
### 使用 Qwen 权重在 1GB 内运行工作的任天堂娱乐系统 ⭐️ 7.0/10

一个使用 Qwen 权重来模拟任天堂娱乐系统的项目，引发了关于 AI 和机器学习应用的讨论。

hackernews · dbreunig · 10月30日 16:40 · [社区讨论](https://news.ycombinator.com/item?id=50306442)

<div class="story-actions"><a class="story-action story-action--primary" href="https://github.com/dbreunig/nesformer" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://github.com/dbreunig/nesformer">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** Nintendo Entertainment System（NES）是一款经典的家用游戏机，而 NES 模拟器则是允许玩家在计算机上运行 NES 游戏的重要工具。Qwen 是一个强大的 AI 模型，能够处理多种任务，包括文本理解、图像和视频理解等。在这个项目中，开发者使用 Qwen 权重来模拟 NES，这标志着 AI 和机器学习在游戏模拟领域的新应用。这种技术不仅展示了 AI 在处理复杂任务方面的潜力，而且可能对软件工程和 AI 系统的发展产生深远影响。

**「影响」** 该项目通过使用 Qwen 权重来模拟任天堂娱乐系统，引发了关于人工智能和机器学习应用的讨论。这表明，该技术可能对软件工程和 AI 系统领域产生实际影响，尤其是在计算效率和资源利用方面。

**「社区讨论」** 社区成员对这一过程进行了讨论，有人认为这为在 LLM 权重内编译小型虚拟机提供了有趣的机遇，而另一些人则对这种方法的效率表示担忧，认为与传统的确定性程序相比，这种方法效率低下。还有人对 nesformer 的性能表示关注，指出其运行速度比真实控制台慢 150-290 倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://joeheyming.github.io/emulator/nes/" target="_blank" rel="noopener noreferrer">NES Emulator — Nintendo Entertainment System</a></li>
<li><a href="https://qwen.ai/" target="_blank" rel="noopener noreferrer">Qwen</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B" target="_blank" rel="noopener noreferrer">Qwen / Qwen 3.8-27B · Hugging Face</a></li>
<li><a href="https://pragma-core.com/blog/qwen-38-27b-and-the-year-the-open-weights-caught-up-how-a-17gb-download-started-beating-the-frontier" target="_blank" rel="noopener noreferrer">Qwen 3.8 27B and the year the open weights caught up: how a 17GB ...</a></li>
<li><a href="https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463" target="_blank" rel="noopener noreferrer">Alibaba Unveils Qwen3.8-27B and Releases Weights of Qwen3.8 Flagship ...</a></li>
<li><a href="https://www.analyticsinsight.net/artificial-intelligence/alibabas-qwen38-ai-model-what-developers-should-know-about-the-open-weight-release" target="_blank" rel="noopener noreferrer">Alibaba Qwen3.8 AI Model: What Developers Should Know</a></li>

</ul>
</details>

**标签**: `#AI`, `#Machine Learning`, `#Emulation`, `#Nintendo`, `#Software Engineering`

---

<a id="item-tech-news-4"></a>
### 本条资讯的中文解读暂未生成 ⭐️ 7.0/10

中文解读生成失败，请稍后重新生成本期资讯。

hackernews · zlliang · 10月30日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=50305573)

<div class="story-actions"><a class="story-action story-action--primary" href="https://tangled.org/blog/forge/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://tangled.org/blog/forge/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**标签**: `#Code Collaboration`, `#Federated Code Forge`, `#Tangled`, `#Software Engineering`, `#Open Source`

---

<a id="item-tech-news-5"></a>
### Azure 的弱点：五个完整的跨租户妥协 ⭐️ 7.0/10

对 Azure 跨租户功能中的安全漏洞进行了分析，突出了对用户和企业可能产生的影响。

hackernews · swq115 · 10月30日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50301854)

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.binarysecurity.no/posts/2026/10/one-root-case" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.binarysecurity.no/posts/2026/10/one-root-case">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** Azure 作为云计算行业的主要参与者，其跨租户功能的安全性一直备受关注。历史上，Azure 平台曾出现过多次跨租户和跨订阅的安全问题。这些问题通常在服务器端得到修复，并且历史上大多数问题没有分配 CVE 编号。例如，OMIGOD、FabriXss/Super FabriXss 和 SynLapse 等少数问题分配了 CVE 编号。这些历史问题的存在表明，Azure 的跨租户功能在安全性方面存在潜在的风险。

**「社区讨论」** 社区成员讨论了 Azure 在跨租户泄露方面的表现，有人质疑为什么企业仍然选择 Azure，同时也有人赞扬了发现这些漏洞的工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.hacktricks.wiki/en/pentesting-cloud/azure-security/az-cross-tenant-and-cross-subscription-attacks/historical-cross-tenant-vulnerabilities.html" target="_blank" rel="noopener noreferrer">Az - Historical Cross-Tenant Vulnerabilities - HackTricks Cloud</a></li>
<li><a href="https://www.theprotec.com/blog/azure-cross-tenant-vulnerabilities-api-connections/" target="_blank" rel="noopener noreferrer">How Azure cross-tenant vulnerabilities exposed API ...</a></li>
<li><a href="https://www.binarysecurity.no/posts/2026/10/one-root-case" target="_blank" rel="noopener noreferrer">Azure&#x27;s Weakest Link - Five Full Cross-Tenant Compromises</a></li>

</ul>
</details>

**标签**: `#Azure`, `#Security Vulnerabilities`, `#Cloud Computing`, `#Cybersecurity`, `#Enterprise IT`

---