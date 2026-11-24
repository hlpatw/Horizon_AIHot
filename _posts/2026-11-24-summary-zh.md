---
layout: default
title: "AIHOT 每日情报：2026-11-24"
date: 2026-11-24
lang: zh
---

> 从 14 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [NariQ：BF16 级 Qwen3.8-27B 在 10GB 文件中](#item-tech-news-1) ⭐️ 8.0/10
2. [本条资讯的中文解读暂未生成](#item-tech-news-2) ⭐️ 8.0/10
3. [GLM-5.4：首个循环 Transformer 架构的通用编码](#item-tech-news-3) ⭐️ 7.0/10

**科技博客**
1. [ERNIE 5.5 Flash Preview：插件部署与端到端推理加速](#item-tech-blog-1) ⭐️ 9.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### NariQ：BF16 级 Qwen3.8-27B 在 10GB 文件中 ⭐️ 8.0/10

NariQ，Qwen3.8-27B 的 3 位以下量化版本，在各种任务中展现出接近 BF16 的质量。社区反馈表明，人们对这项工作既有怀疑也有赞赏。

hackernews · toebee · 11月23日 13:42 · [社区讨论](https://news.ycombinator.com/item?id=50611402)

<div class="story-actions"><a class="story-action story-action--primary" href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** NariQ 是一种新的 3 位以下量化技术，它对 Qwen3.8-27B 进行了量化处理，能够在各种任务中保持接近 BF16 的质量。这种量化技术首次在长周期代理任务上实现了 BF16 级别的性能。NariQ 的引入标志着 AI 和机器学习领域的一项重要进展，它通过减少模型的大小，同时保持高性能，为模型部署提供了新的可能性。

**「影响」** NariQ 的推出为 AI 和机器学习领域带来了显著的进步，它通过 3 位以下的量化技术，在保持接近 BF16 质量的同时，显著减小了模型文件的大小。这对于在消费级 GPU 上运行复杂模型具有重要意义，因为它使得更多的用户能够访问和使用高性能的 AI 模型，从而推动了 AI 技术的普及和应用。

**「社区讨论」** 社区成员对 NariQ 的性能表示怀疑，认为它可能过度优化于基准数据集，而在实际应用中无法达到“几乎一样好”的保证。同时，也有人对这种量化方法表示赞赏，认为它在多个类型的长期任务上展示了良好的结果，并进行了基本的检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50611402" target="_blank" rel="noopener noreferrer">NariQ : BF 16 -level Qwen 3 .8-27B in a 10 GB file | Hacker News</a></li>
<li><a href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF" target="_blank" rel="noopener noreferrer">nari -labs/Qwen 3 .8-27B- NariQ -GGUF · Hugging Face</a></li>
<li><a href="https://github.com/nari-labs/nari-llama.cpp" target="_blank" rel="noopener noreferrer">GitHub - nari -labs/ nari -llama.cpp: llama.cpp fork that runs NariQ ...</a></li>
<li><a href="https://arxiv.org/abs/2611.26157" target="_blank" rel="noopener noreferrer">[2611.26157] NariQ: Sub-3-Bit Quantization for Long-Horizon ...</a></li>
<li><a href="https://arxiv.org/pdf/2611.26157" target="_blank" rel="noopener noreferrer">NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks</a></li>
<li><a href="https://grafy.ai/news/nariq-method-improves-sub-3-bit-quantization-for-ai-agents" target="_blank" rel="noopener noreferrer">NariQ method improves sub-3-bit quantization — Grafy News</a></li>

</ul>
</details>

**标签**: `#AI`, `#Machine Learning`, `#Quantization`, `#NLP`, `#Benchmarking`

---

<a id="item-tech-news-2"></a>
### 本条资讯的中文解读暂未生成 ⭐️ 8.0/10

中文解读生成失败，请稍后重新生成本期资讯。

rss · Simon Willison · 11月23日 21:46

<div class="story-actions"><a class="story-action story-action--primary" href="https://simonwillison.net/2026/Nov/23/ladybird/" target="_blank" rel="noopener noreferrer">查看原文</a><button class="copy-story-link" type="button" data-copy-url="https://simonwillison.net/2026/Nov/23/ladybird/">复制链接</button></div>

**标签**: `#Browser Technology`, `#Web Development`, `#Open Source`, `#Alpha Release`, `#Software Engineering`

---

<a id="item-tech-news-3"></a>
### GLM-5.4：首个循环 Transformer 架构的通用编码 ⭐️ 7.0/10

Z.ai 的 GLM 5.4 模型引入了循环 Transformer 架构，这是 AI 模型设计的一项重大进步。该架构通过多次迭代共享权重的层来深化网络，而不增加参数数量。GLM 5.4 目前无法通过常规 API 访问，需要通过 Z.ai 的 Coding Plan 订阅来使用。

rss · Simon Willison · 11月23日 23:40

<div class="story-actions"><a class="story-action story-action--primary" href="https://simonwillison.net/2026/Nov/23/glm-54/" target="_blank" rel="noopener noreferrer">查看原文</a><button class="copy-story-link" type="button" data-copy-url="https://simonwillison.net/2026/Nov/23/glm-54/">复制链接</button></div>

**「背景」** Transformer 模型是人工智能领域广泛使用的一种模型，它通过自注意力机制处理序列数据。在传统的 Transformer 模型中，每个层在一次前向传播中只运行一次。而循环 Transformer（Loop Transformer）则是一种新的架构，其中一组权重共享的层会运行多次迭代，从而细化前一次传播中的隐藏状态。这种架构可以在不增加参数数量的情况下，实现更深层次的网络。Z.ai 的 GLM-5.4 是首个采用循环 Transformer 架构的模型，这标志着 AI 模型设计的一个重要进展。

**「影响」** GLM 5.4 的循环 Transformer 架构可能为 AI 编码任务带来更高效的推理能力，尤其是在需要高质量推理的编码任务中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techstackups.com/articles/loop-architecture-explained/" target="_blank" rel="noopener noreferrer">Loop Architecture Explained: Why Looped Transformers Are ...</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/" target="_blank" rel="noopener noreferrer">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.emergentmind.com/topics/looped-transformer-architecture" target="_blank" rel="noopener noreferrer">Looped Transformer Architecture - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#AI Research`, `#Machine Learning`, `#Transformer Models`, `#AI News`, `#Software Engineering`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### ERNIE 5.5 Flash Preview：插件部署与端到端推理加速 ⭐️ 9.0/10

rss · vLLM Blog · 11月24日 00:00

<div class="story-actions"><a class="story-action story-action--primary" href="https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview" target="_blank" rel="noopener noreferrer">查看原文</a><button class="copy-story-link" type="button" data-copy-url="https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview">复制链接</button></div>

**「背景」** 随着机器学习模型规模的不断扩大，推理加速成为了一个重要的研究方向。ERNIE 5.5 Flash Preview 模型由百度 ERNIE 团队和 vLLM 团队共同开发，旨在通过优化模型架构和推理过程，实现高效的推理加速。

**「方案」** ERNIE 5.5 Flash Preview 模型采用了多种优化技术，包括稀疏索引器加速、量化、推测解码和推理加速等。通过 vLLM 插件，用户可以轻松地将该模型集成到 vLLM 环境中，实现高效的端到端推理加速。模型架构方面，ERNIE 5.5 Flash Preview 采用了 280B 的总参数和 14B 的激活参数，支持 1M-token 的上下文，并使用了多种注意力机制和量化技术。

**「启示」** ERNIE 5.5 Flash Preview 模型通过优化模型架构和推理过程，实现了高效的推理加速，为机器学习模型的部署提供了新的思路。

**标签**: `#Machine Learning`, `#Model Optimization`, `#ERNIE 5.5 Flash`, `#vLLM`, `#Inference Acceleration`, `#Plugin Integration`

---