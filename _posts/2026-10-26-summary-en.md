---
layout: default
title: "AIHOT Daily: 2026-10-26"
date: 2026-10-26
lang: en
---

> From 11 items, 3 important content pieces were selected

---

**Technology News**
1. [memt-1.0 Architecture Breakdown](#item-tech-news-1) ⭐️ 8.0/10
2. [10-Year-Old CNN Outperforms Frontier LLMs in Skin Cancer Diagnosis](#item-tech-news-2) ⭐️ 7.0/10
3. [Nanbeige Releases Nanbeige4.3-33B Teacher Model](#item-tech-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### memt-1.0 Architecture Breakdown ⭐️ 8.0/10

The memt-1.0 architecture introduces a memory-native design with gated deltanet-2 and mixture-of-storage, offering efficiency improvements and a 66x smaller storage footprint for agent memory compared to a full-context kv cache setup.

reddit · r/MachineLearning · /u/Mrs-Grumpy23 · Oct 25, 05:31

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1xeu0ht/memt10_architecture_breakdown_gated_deltanet2/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1xeu0ht/memt10_architecture_breakdown_gated_deltanet2/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on memt-1.0 Architecture」** The memt-1.0 architecture represents a significant advancement in machine learning, particularly in the area of memory management and efficiency improvements. It incorporates innovative techniques such as Gated DeltaNet-2 and Mixture-of-Storage \(MoS\) to enhance memory-native design. Gated DeltaNet-2 is a linear attention layer that decouples erase and write operations, allowing for fine-grained control over the recurrent state. Mixture-of-Storage is a layer designed to scale capacity while maintaining efficiency. These advancements aim to reduce the storage footprint for agent memory and improve the overall performance of machine learning models.

**「Impact」** The introduction of memt-1.0&\#x27;s architecture could lead to more efficient and compact memory usage for agents, potentially enabling the development of long-horizon agents that are not limited by kv cache memory bottlenecks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.22791" target="_blank" rel="noopener noreferrer">Gated DeltaNet - 2 : Decoupling Erase and Write in Linear Attention</a></li>
<li><a href="https://www.alphaxiv.org/abs/2605.22791" target="_blank" rel="noopener noreferrer">Gated DeltaNet - 2 : Decoupling Erase and Write in Linear... | alphaXiv</a></li>
<li><a href="https://www.marktechpost.com/2026/05/24/nvidia-ai-releases-gated-deltanet-2-a-linear-attention-layer-that-decouples-erase-and-write-in-the-delta-rule/" target="_blank" rel="noopener noreferrer">NVIDIA AI Releases Gated DeltaNet - 2 : A Linear... - MarkTechPost</a></li>

</ul>
</details>

**Tags**: `#MachineLearning`, `#AI`, `#MemoryManagement`, `#Efficiency`, `#SoftwareEngineering`

---

<a id="item-tech-news-2"></a>
### 10-Year-Old CNN Outperforms Frontier LLMs in Skin Cancer Diagnosis ⭐️ 7.0/10

A 10-year-old Convolutional Neural Network \(CNN\) has outperformed cutting-edge Large Language Models \(LLMs\) in skin cancer diagnosis, sparking a debate on the effectiveness of different models in the technology industry.

hackernews · sungam · Oct 25, 17:15 · [Discussion](https://news.ycombinator.com/item?id=50233779)

<div class="story-actions"><a class="story-action story-action--primary" href="https://lynchlab.net/llm-skin-cancer" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://lynchlab.net/llm-skin-cancer">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Skin Cancer Diagnosis and AI Models」** Convolutional Neural Networks \(CNNs\) have been used in medical imaging for several years, particularly in dermatology for skin cancer diagnosis. A CNN, specifically an Inception v3 model, was fine-tuned on a dataset of dermoscopic and clinical images to diagnose skin cancer. This model, which is over 10 years old, has been compared against frontier Large Language Models \(LLMs\) such as GPT-6 Astra and Claude Fable 5.1, which are state-of-the-art in natural language processing. The comparison revealed that the older CNN outperformed the LLMs in skin cancer diagnosis tasks.

**「Impact on Skin Cancer Diagnosis」** The use of a 10-year-old CNN for skin cancer diagnosis has demonstrated superior accuracy compared to state-of-the-art LLMs, such as GPT-6 Astra and Claude Fable 5.1. This finding challenges the notion that more complex models are always superior and suggests that specialized, older models can still be highly effective in specific tasks, potentially leading to more accurate and reliable diagnoses in the field of dermatology.

**「Community Discussion」** The community discussion highlights the debate on the effectiveness of different models. Some argue that dedicated classifiers with the right architecture are more accurate for large-scale applications, while others point out that LLMs can reduce the cost of making such models. There is also a discussion on the limitations of using LLMs for specific tasks like skin cancer diagnosis.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/cnn-beats-gpt-6-astra-claude-fable-5-1-skin-cancer-diagnosis-lynch-2026" target="_blank" rel="noopener noreferrer">CNN vs GPT-6 Astra vs Fable 5.1: Skin Cancer, 62% vs 42% ...</a></li>
<li><a href="https://lynchlab.net/llm-skin-cancer" target="_blank" rel="noopener noreferrer">A 10-year-old CNN outperforms frontier LLMs for skin cancer ...</a></li>
<li><a href="https://youlidao.ai/en/intelligence/10-year-old-cnn-beats-llms-skin-cancer-diagnosis" target="_blank" rel="noopener noreferrer">10-Year-Old CNN Beats LLMs at Skin Cancer Diagnosis</a></li>
<li><a href="https://lynchlab.net/llm-skin-cancer" target="_blank" rel="noopener noreferrer">A 10-year-old CNN outperforms frontier LLMs for skin cancer ...</a></li>
<li><a href="https://explainx.ai/blog/cnn-beats-gpt-6-astra-claude-fable-5-1-skin-cancer-diagnosis-lynch-2026" target="_blank" rel="noopener noreferrer">CNN vs GPT-6 Astra vs Fable 5.1: Skin Cancer, 62% vs 42% ...</a></li>
<li><a href="https://vexdynamics.com/news/older-cnn-outperforms-stateoftheart-llms-in-skin-cancer" target="_blank" rel="noopener noreferrer">Older CNN Outperforms State-of-the-Art LLMs in Skin Cancer ...</a></li>

</ul>
</details>

**Tags**: `#AI in Medicine`, `#Machine Learning`, `#CNN vs LLM`, `#Skin Cancer Diagnosis`, `#Technology News`

---

<a id="item-tech-news-3"></a>
### Nanbeige Releases Nanbeige4.3-33B Teacher Model ⭐️ 7.0/10

Nanbeige has released Nanbeige4.3-33B, a teacher model designed for smaller agents, showcasing promising performance on benchmark tests such as Terminal-Bench 2.1 and SWE-Bench Pro. The model is licensed under Apache 2.0, enhancing its accessibility to the community.

reddit · r/MachineLearning · /u/jatingargiitk · Oct 25, 16:32

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1xf6x35/nanbeige_releases_nanbeige4333b_an_apache_20/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1xf6x35/nanbeige_releases_nanbeige4333b_an_apache_20/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Nanbeige4.3-33B Model Overview」** Nanbeige4.3-33B is a teacher model released by Nanbeige, designed for smaller agents. It operates under the Apache 2.0 license, which allows for broader community access and usage. The model features a 512K context window and has demonstrated promising performance on benchmark tests such as Terminal-Bench 2.1 and SWE-Bench Pro. While not the top performer in all categories, it shows incremental improvement over previous models and is particularly suited for agentic coding and office-style &\#x27;cowork&\#x27; tasks.

**「Impact on Users and Developers」** The release of Nanbeige4.3-33B by Nanbeige represents a significant advancement in the field of machine learning, particularly for developers and researchers interested in smaller agent models. The model&\#x27;s performance on benchmark tests, while not the highest, demonstrates incremental improvement and provides a valuable tool for further research and development in the area of agentic coding and office-style tasks. The use of the Apache 2.0 license also ensures that the model is accessible to the wider community, fostering collaboration and innovation.

**「Community Discussion」** No community comments available.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datastudios.org/post/nanbeige-4-3-33b-open-weight-dense-agentic-model-512k-context" target="_blank" rel="noopener noreferrer">Nanbeige4.3-33B: Apache 2.0 dense agentic coding model with ...</a></li>
<li><a href="https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/" target="_blank" rel="noopener noreferrer">Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding ...</a></li>
<li><a href="https://www.ai-digest-1.com/news/nanbeige-llm-lab-releases-nanbeige4-3-33b-open-agentic-coding-model-19432" target="_blank" rel="noopener noreferrer">Nanbeige LLM Lab Releases Nanbeige4.3-33B Open Agentic Coding ...</a></li>
<li><a href="https://arxiv.org/pdf/2512.06266v1" target="_blank" rel="noopener noreferrer">Nanbeige4-3B Technical Report: Exploring the Frontier of ...</a></li>
<li><a href="https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/" target="_blank" rel="noopener noreferrer">Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding ...</a></li>
<li><a href="https://www.datastudios.org/post/nanbeige-4-3-33b-open-weight-dense-agentic-model-512k-context" target="_blank" rel="noopener noreferrer">Nanbeige4.3-33B: Apache 2.0 dense agentic coding model with ...</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#AI`, `#Model Release`, `#Benchmark Performance`

---