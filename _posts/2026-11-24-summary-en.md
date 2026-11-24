---
layout: default
title: "AIHOT Daily: 2026-11-24"
date: 2026-11-24
lang: en
---

> From 14 items, 4 important content pieces were selected

---

**Technology News**
1. [NariQ: BF16-level Qwen3.8-27B in a 10 GB file](#item-tech-news-1) ⭐️ 8.0/10
2. [Ladybird&\#x27;s first alpha release](#item-tech-news-2) ⭐️ 8.0/10
3. [GLM-5.4: Loop Transformer Architecture Introduction](#item-tech-news-3) ⭐️ 7.0/10

**Technology Blog**
1. [ERNIE 5.5 Flash Preview：插件部署和端到端推理加速](#item-tech-blog-1) ⭐️ 9.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### NariQ: BF16-level Qwen3.8-27B in a 10 GB file ⭐️ 8.0/10

NariQ, a new 3-bit quantization of Qwen3.8-27B, has been developed, demonstrating near-BF16 quality across various tasks. This quantization is notable for its small file size of 10 GB and its performance on long-horizon agentic tasks, math, multilingual reasoning, and image understanding.

hackernews · toebee · Nov 23, 13:42 · [Discussion](https://news.ycombinator.com/item?id=50611402)

<div class="story-actions"><a class="story-action story-action--primary" href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on NariQ and Quantization」** Quantization in machine learning involves reducing the precision of numerical values used in calculations, which can lead to smaller model sizes and faster inference times. NariQ is a recent development in this field, representing a 3-bit-or-lower quantization of the Qwen3.8-27B model. This quantization aims to retain near-BF16 quality across various tasks such as agentic tasks, math, multilingual reasoning, and image understanding. The concept of quantization is crucial for optimizing AI models for deployment on devices with limited computational resources, as it can significantly reduce the memory footprint and inference latency.

**「Consequence for Users and Developers」** The introduction of NariQ allows for more efficient deployment of large language models on consumer GPUs, as it achieves near-BF16 quality with a significantly reduced file size. This could lead to broader adoption of AI applications that require large language models, as they become more accessible to a wider range of users and developers with less powerful hardware.

**「Community Discussion」** Community feedback on NariQ is mixed. Some users appreciate the comprehensive benchmarking and the ability to run the model on hardware with limited memory, like a 16GB MacBook. However, there is skepticism regarding the over-optimization on benchmark-like datasets and concerns about the loss of information due to the reduced file size.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50611402" target="_blank" rel="noopener noreferrer">NariQ : BF 16 -level Qwen 3 .8-27B in a 10 GB file | Hacker News</a></li>
<li><a href="https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF" target="_blank" rel="noopener noreferrer">nari -labs/Qwen 3 .8-27B- NariQ -GGUF · Hugging Face</a></li>
<li><a href="https://github.com/nari-labs/nari-llama.cpp" target="_blank" rel="noopener noreferrer">GitHub - nari -labs/ nari -llama.cpp: llama.cpp fork that runs NariQ ...</a></li>
<li><a href="https://arxiv.org/abs/2611.26157" target="_blank" rel="noopener noreferrer">[2611.26157] NariQ: Sub-3-Bit Quantization for Long-Horizon ...</a></li>
<li><a href="https://arxiv.org/pdf/2611.26157" target="_blank" rel="noopener noreferrer">NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks</a></li>
<li><a href="https://grafy.ai/news/nariq-method-improves-sub-3-bit-quantization-for-ai-agents" target="_blank" rel="noopener noreferrer">NariQ method improves sub-3-bit quantization — Grafy News</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#Quantization`, `#NLP`, `#Benchmarking`

---

<a id="item-tech-news-2"></a>
### Ladybird&\#x27;s first alpha release ⭐️ 8.0/10

The Ladybird project has released its first alpha version, showcasing an ambitious new browser with a unique implementation of key web technologies.

rss · Simon Willison · Nov 23, 21:46

<div class="story-actions"><a class="story-action story-action--primary" href="https://simonwillison.net/2026/Nov/23/ladybird/" target="_blank" rel="noopener noreferrer">Official source</a><button class="copy-story-link" type="button" data-copy-url="https://simonwillison.net/2026/Nov/23/ladybird/">Copy link</button></div>

**Tags**: `#Browser Technology`, `#Web Development`, `#Open Source`, `#Alpha Release`, `#Software Engineering`

---

<a id="item-tech-news-3"></a>
### GLM-5.4: Loop Transformer Architecture Introduction ⭐️ 7.0/10

Z.ai has released GLM 5.4, the first model to utilize a looped transformer architecture. This architecture allows for deeper networks without increasing the parameter count, enhancing the model&\#x27;s capabilities in tasks such as agentic coding.

rss · Simon Willison · Nov 23, 23:40

<div class="story-actions"><a class="story-action story-action--primary" href="https://simonwillison.net/2026/Nov/23/glm-54/" target="_blank" rel="noopener noreferrer">Official source</a><button class="copy-story-link" type="button" data-copy-url="https://simonwillison.net/2026/Nov/23/glm-54/">Copy link</button></div>

**「Looped Transformer Architecture」** Looped transformer architecture is a significant advancement in AI model design. It involves running a shared block of layers multiple times before producing the next token, as opposed to the standard Transformer model where each layer runs once per forward pass. This architecture allows for a deeper network without increasing the parameter count, enhancing the model&\#x27;s ability to apply more reasoning and reach the right answer with fewer tokens, particularly in tasks such as agentic coding that depend on reasoning quality. The introduction of this architecture in models like GLM-5.4 by Z.ai and Inkling 2 Mini from Thinking Machines Lab represents a trend in the field of AI.

**「Impact」** The introduction of the looped transformer architecture in GLM 5.4 could lead to more efficient and powerful AI models, particularly in coding tasks that require reasoning and fewer tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://techstackups.com/articles/loop-architecture-explained/" target="_blank" rel="noopener noreferrer">Loop Architecture Explained: Why Looped Transformers Are ...</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/" target="_blank" rel="noopener noreferrer">Looped Transformer | Sebastian Raschka, PhD</a></li>
<li><a href="https://www.emergentmind.com/topics/looped-transformer-architecture" target="_blank" rel="noopener noreferrer">Looped Transformer Architecture - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#AI Research`, `#Machine Learning`, `#Transformer Models`, `#AI News`, `#Software Engineering`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### ERNIE 5.5 Flash Preview：插件部署和端到端推理加速 ⭐️ 9.0/10

rss · vLLM Blog · Nov 24, 00:00

<div class="story-actions"><a class="story-action story-action--primary" href="https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview" target="_blank" rel="noopener noreferrer">Official source</a><button class="copy-story-link" type="button" data-copy-url="https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview">Copy link</button></div>

**「背景」** 随着机器学习模型变得越来越复杂，推理加速成为了一个关键问题。ERNIE 5.5 Flash Preview模型通过其独特的架构和优化技术，旨在提供高效的推理加速。本文将探讨该模型的架构、优化策略以及与vLLM的集成方式，为技术读者提供实用的技术细节和经验分享。

**「方案」** ERNIE 5.5 Flash Preview模型采用了280B的总参数和14B的激活参数，支持1M-token的上下文，并使用工具调用执行长期Agent任务。该模型通过vLLM-ERNIE插件与vLLM集成，插件是一个独立的包，可以安装到与官方vllm==0.32.0 wheel相同的环境中。模型架构包括37层使用Heavily Compressed Attention \(HCA\)和6层使用MLA with DSA sparse attention，以及多种优化技术如FlashIndexer、FP4 Quantization-Aware Training和Multi-Stage DSpark Speculative Decoding Training，旨在提高推理速度和效率。

**「启示」** ERNIE 5.5 Flash Preview模型通过其创新的架构和优化技术，为机器学习模型的推理加速提供了新的思路。该模型与vLLM的集成方式为技术读者提供了实用的解决方案，有助于提高机器学习模型的性能和效率。

**Tags**: `#Machine Learning`, `#Model Optimization`, `#ERNIE 5.5 Flash`, `#vLLM`, `#Inference Acceleration`, `#Plugin Integration`

---