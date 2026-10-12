---
layout: default
title: "AIHOT 每日情报：2026-10-12"
date: 2026-10-12
lang: zh
---

> 从 16 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [浏览器工具可视化小型 LLM 选择下一个单词的过程](#item-tech-news-1) ⭐️ 8.0/10
2. [使用 Sliced Wasserstein 嵌入和 HNSW 进行 48k 画作色彩搜索的新方法](#item-tech-news-2) ⭐️ 8.0/10
3. [本条资讯的中文解读暂未生成](#item-tech-news-3) ⭐️ 7.0/10
4. [朝鲜地图绘制项目引发社区关注](#item-tech-news-4) ⭐️ 7.0/10
5. [LLM 能力理解差距扩大](#item-tech-news-5) ⭐️ 7.0/10
6. [Passkeys are a trap](#item-tech-news-6) ⭐️ 7.0/10
7. [机器人领域的突破：世界动作模型与可变长度动作的比较](#item-tech-news-7) ⭐️ 7.0/10
8. [Jebadiah v2.1 模型更新：每项允许标签的评分模型](#item-tech-news-8) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### 浏览器工具可视化小型 LLM 选择下一个单词的过程 ⭐️ 8.0/10

一位用户开发了一个浏览器工具，用于可视化小型语言模型（LLM）的注意力机制，展示了它是如何选择下一个单词的。这个工具可以在浏览器中运行，无需服务器支持，用户可以通过它来观察模型在生成文本时的注意力分布情况。

reddit · r/MachineLearning · /u/Minute-Mountain2665 · 10月11日 22:30

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x3lgnz/i_built_a_browser_tool_to_visualize_how_a_small/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x3lgnz/i_built_a_browser_tool_to_visualize_how_a_small/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** 语言模型中的注意力机制是一种允许模型根据输入数据中的相关部分动态聚焦的技术。这种机制在自然语言处理（NLP）中取得了突破性进展，使得模型能够更好地理解单词的意义及其与周围上下文的关系。SmolLM 2 是一系列紧凑的语言模型，具有 135M、360M 和 1.7B 个参数三种大小，能够在保持轻量级的同时解决各种任务。这些模型在包含 FineWeb-Edu、DCLM 和 The Stack 的 2 万亿个标记的广泛和多样化的数据集上进行了训练。

**「影响」** 该浏览器工具的创建为理解小型语言模型的注意力机制提供了直观的视角，有助于用户更深入地了解语言模型如何选择下一个单词。这种可视化方法对于研究人员和开发者来说是一个重要的工具，因为它可以帮助他们分析和优化语言模型的行为。

**「社区讨论」** 目前没有可用的社区评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://inferix.co/models/HuggingFaceTB/SmolLM2-135M" target="_blank" rel="noopener noreferrer">SmolLM 2 - 135 M · Model · Inferix</a></li>
<li><a href="https://www.promptlayer.com/models/smollm2-135m/" target="_blank" rel="noopener noreferrer">SmolLM 2 - 135 M | PromptLayer Models</a></li>
<li><a href="https://ai.azure.com/catalog/models/unsloth-smollm2-135m-instruct" target="_blank" rel="noopener noreferrer">unsloth- smollm 2 - 135 m -instruct | Model Catalog | Microsoft Foundry</a></li>
<li><a href="https://www.ai21.com/knowledge/attention-mechanisms-language-models/" target="_blank" rel="noopener noreferrer">What are Attention Mechanisms in Language Models ? | AI21</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2019/11/comprehensive-guide-attention-mechanism-deep-learning/" target="_blank" rel="noopener noreferrer">Attention Mechanism in Deep Learning</a></li>
<li><a href="https://nat.io/blog/llm-attention-mechanisms" target="_blank" rel="noopener noreferrer">Attention Mechanisms in LLMs: How They Work | nat.io</a></li>
<li><a href="https://www.datacamp.com/blog/attention-mechanism-in-llms-intuition" target="_blank" rel="noopener noreferrer">What is Attention and Why Do LLMs and Transformers... | DataCamp</a></li>
<li><a href="https://arxiv.org/pdf/2305.03210" target="_blank" rel="noopener noreferrer">AttentionViz: A Global View of Transformer Attention</a></li>
<li><a href="https://www.comet.com/site/blog/explainable-ai-for-transformers/" target="_blank" rel="noopener noreferrer">Explainable AI: Visualizing Attention in Transformers</a></li>

</ul>
</details>

**标签**: `#Machine Learning`, `#Language Models`, `#Attention Mechanism`, `#Visualization`, `#Browser Tool`

---

<a id="item-tech-news-2"></a>
### 使用 Sliced Wasserstein 嵌入和 HNSW 进行 48k 画作色彩搜索的新方法 ⭐️ 8.0/10

介绍了一种使用 Sliced Wasserstein 嵌入和 HNSW 索引在 48k 画作数据集中进行色彩搜索的新方法。该方法通过将颜色投影到 Fibonacci 半球的 8 个方向上，排序并平均到 16 个分位数，从而实现快速的色彩搜索。

reddit · r/MachineLearning · /u/Potential-Barber8658 · 10月11日 14:39

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x39uu6/sliced_wasserstein_embeddings_hnsw_for/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x39uu6/sliced_wasserstein_embeddings_hnsw_for/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** Palette Atlas 是一个通过颜色方案搜索公共领域绘画的工具。每个图像被简化为 128 种等权重的颜色，因此自然距离是地球迁移距离，对于在 48,695 个项目上进行最近邻搜索来说太慢了（每对约 6 毫秒）。该嵌入方法：将颜色（OKLab）投影到斐波那契半球的 8 个方向上，排序并平均到 16 个分位数。两个向量之间的 L1 是方向上 W1 的平均值，是真实 W1 的下界。与 240 个查询（与精确的前 10 个重叠以及前 10 个有多远）的精确 EMD 相比：- 切片 8x16，L1：78%，1.8% - 切片 8x16，L2：69%，3.4% - 软颜色直方图，Hellinger：45%，13.5% - 平均颜色：3%，161%。索引是从头开始编写的 HNSW（M=16，efConstruction=200）：在 ef=32 时的召回率@10 为 1.000，0.25 毫秒，而暴力搜索为 14 毫秒。向量的内在维度约为 11，因此层次结构仍然有帮助（参见 Munyampirwa 等人 2025 年的研究，关于何时它不起作用）。与论文中的一个变化：顶层持有 8 个 k-means 地标，而不是随机抽取的节点。搜索成本相同（平均 2,558 与 2,556 距离计算），顶层成为每个颜色家族的一幅典型画作。文档：https://github.com/itzik123/PaletteAtlas/blob/main/docs/searching-by-color.md 代码：https://github.com/itzik123/PaletteAtlas

**「影响」** 这项新技术为计算机视觉和机器学习领域提供了对 48k 幅画作进行颜色方案搜索的新方法，通过使用 Sliced Wasserstein 嵌入和 HNSW 索引，可以显著提高搜索效率和准确性。

**「社区讨论」** 目前没有可用的社区评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.palette-atlas.com/search" target="_blank" rel="noopener noreferrer">Color search · Palette Atlas</a></li>
<li><a href="https://www.palette-atlas.com/" target="_blank" rel="noopener noreferrer">Palette Atlas — Color palettes rooted in culture</a></li>
<li><a href="https://coolors.co/palettes/search" target="_blank" rel="noopener noreferrer">Search Color Palettes - Coolors</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2023/10/introduction-to-hnsw-hierarchical-navigable-small-world/" target="_blank" rel="noopener noreferrer">Introduction to HNSW : Hierarchical Navigable Small World</a></li>
<li><a href="https://milvus.io/docs/hnsw.md" target="_blank" rel="noopener noreferrer">HNSW | Milvus Documentation</a></li>
<li><a href="https://medium.com/pinterest-engineering/manas-hnsw-realtime-powering-realtime-embedding-based-retrieval-dc71dfd6afdd" target="_blank" rel="noopener noreferrer">Manas HNSW Realtime: Powering Realtime Embedding -Based...</a></li>
<li><a href="https://jkatz05.com/post/postgres/pgvector-hnsw-performance/" target="_blank" rel="noopener noreferrer">An early look at HNSW performance with pgvector | Jonathan Katz</a></li>
<li><a href="https://www.pinecone.io/learn/series/faiss/hnsw/" target="_blank" rel="noopener noreferrer">Hierarchical Navigable Small Worlds ( HNSW ) | Pinecone</a></li>
<li><a href="https://milvus.io/docs/hnsw.md" target="_blank" rel="noopener noreferrer">HNSW | Milvus Documentation</a></li>

</ul>
</details>

**标签**: `#Computer Vision`, `#Machine Learning`, `#Data Indexing`, `#Color Scheme Search`, `#Artificial Intelligence`

---

<a id="item-tech-news-3"></a>
### 本条资讯的中文解读暂未生成 ⭐️ 7.0/10

中文解读生成失败，请稍后重新生成本期资讯。

hackernews · jttnr · 10月11日 18:04 · [社区讨论](https://news.ycombinator.com/item?id=50045984)

<div class="story-actions"><a class="story-action story-action--primary" href="https://nanolathe.gg/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://nanolathe.gg/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**标签**: `#RTS Gaming`, `#Total Annihilation`, `#Game Modernization`, `#Community Engagement`, `#Software Engineering`

---

<a id="item-tech-news-4"></a>
### 朝鲜地图绘制项目引发社区关注 ⭐️ 7.0/10

一个详细且独特的朝鲜地图绘制项目吸引了社区的广泛关注。该项目展示了朝鲜的地理信息，对软件工程和地理信息系统领域具有启示意义，尽管它并非一项突破性的技术进步。

hackernews · edent · 10月11日 19:46 · [社区讨论](https://news.ycombinator.com/item?id=50047091)

<div class="story-actions"><a class="story-action story-action--primary" href="https://cartographers-nk.wonyoung.so/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://cartographers-nk.wonyoung.so/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** 北朝鲜的地图绘制项目是一个独特且详尽的地理信息系统项目。在 1945 年第二次世界大战结束后，朝鲜半岛被分为南北两部分，北部由苏联占领，南部由美国占领。北朝鲜政府适应了开源文化，并保持了与互联网的紧密控制连接。这些历史背景对于理解北朝鲜的地图绘制项目具有重要意义。

**「影响」** 该项目对地理信息系统（GIS）和软件工程领域产生了积极的影响，因为它提供了一个独特的视角来理解朝鲜的地理和基础设施。这种深入的研究有助于提高对朝鲜地区地理信息的理解，对于需要精确地图和地理数据的开发者和组织来说，这是一个宝贵的资源。

**「社区讨论」** 社区成员对这一项目表现出浓厚的兴趣。有人指出朝鲜似乎允许游客自由拍摄视频，这些视频在 YouTube 上出现，为人们提供了以前未曾见过的朝鲜生活片段。还有人对项目的数据布局和可读性表示赞赏，并分享了项目背后的故事，即一位名为“P791”的人通过绘制地图来帮助朝鲜人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/North_Korea_Uncovered" target="_blank" rel="noopener noreferrer">North Korea Uncovered - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/North_Korea" target="_blank" rel="noopener noreferrer">North Korea - Wikipedia</a></li>
<li><a href="https://senseable.mit.edu/papers/pdf/20200217_SoDuarte_CartographersNK_Geoforum.pdf" target="_blank" rel="noopener noreferrer">Cartographers of North Korea_ Who are they and what are the ...</a></li>
<li><a href="https://www.esri.com/" target="_blank" rel="noopener noreferrer">GIS Software for Mapping and Spatial Analytics | Esri</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/15230406.2021.1910075" target="_blank" rel="noopener noreferrer">tandfonline.com/doi/full/10.1080/15230406.2021.1910075</a></li>
<li><a href="https://map.seabreezegeo.az/" target="_blank" rel="noopener noreferrer">Sea Breeze GIS | Interactive 3D Map &amp; Infrastructure</a></li>

</ul>
</details>

**标签**: `#Mapping`, `#Geographic Information Systems`, `#North Korea`, `#Software Engineering`, `#Community Interest`

---

<a id="item-tech-news-5"></a>
### LLM 能力理解差距扩大 ⭐️ 7.0/10

讨论了 LLM 能力理解差距扩大的问题及其对技术行业的影响。

hackernews · albertzeyer · 10月11日 20:20 · [社区讨论](https://news.ycombinator.com/item?id=50047422)

<div class="story-actions"><a class="story-action story-action--primary" href="https://twitter.com/karpathy/status/2109361546505966046" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://twitter.com/karpathy/status/2109361546505966046">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** 大型语言模型（LLM）的发展经历了从基础语言建模研究到 Transformer 架构（Vaswani 等人，2017 年）的突破，再到 2025-2026 年发布的当代前沿模型，如 GPT、Claude、Gemini、Llama、Qwen 和 DeepSeek 系列。这些模型的多模态能力已成为标准，但一致性仍是一个挑战，模型在常见图像-文本组合上表现良好，但在罕见视觉情境、低分辨率输入和需要连接视觉和文本证据的跨模态推理上表现下降。此外，全球大型语言模型（LLM）市场正在进入一个决定性的阶段，从过去几年的规模竞赛和实验部署中脱颖而出，生成式 AI 现在正转变为企业和平台的数字基础设施的核心。

**「社区讨论」** 社区中有人认为 AI 并没有真正改善人们的生活，甚至使生活变得更糟。另一些人则认为，对于大型、复杂项目，LLM 的能力可能使得项目完成速度加快，但同时也存在对 LLM 可能产生的错误和假设的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6887539" target="_blank" rel="noopener noreferrer">The Evolution, Capabilities, Limitations, and Future of Large ...</a></li>
<li><a href="https://aimultiple.com/future-of-large-language-models" target="_blank" rel="noopener noreferrer">The Future of Large Language Models</a></li>
<li><a href="https://www.makebot.ai/blog-en/llm-market-enterprise-trends" target="_blank" rel="noopener noreferrer">10 Key LLM Market Trends for 2026 - makebot.ai</a></li>

</ul>
</details>

**标签**: `#Artificial Intelligence`, `#Machine Learning`, `#LLM Capabilities`, `#Technology Industry`, `#Community Interest`

---

<a id="item-tech-news-6"></a>
### Passkeys are a trap ⭐️ 7.0/10

本文讨论了技术安全中 passkeys 的潜在风险和局限性。

hackernews · laurex · 10月11日 21:59 · [社区讨论](https://news.ycombinator.com/item?id=50048312)

<div class="story-actions"><a class="story-action story-action--primary" href="https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** Passkeys（FIDO2 身份验证方法）是一种用于用户身份验证的技术，它通过验证提供者或设备在注册过程中的真实性来增强安全性。在注册过程中强制执行声明可以提供通过 FIDO 元数据服务（MDS）进行加密可验证的设备身份。此外，如果在注册时未获得声明，则强制执行声明后用户不会阻止登录。Passkeys 的声明验证有助于确定生成凭据的验证器的制造商和型号，并讨论如何将声明元数据与凭据一起存储。

**「影响」** 对于用户来说，使用 passkeys 可能带来便携性和安全性的权衡。一些用户担心，passkeys 的便携性可能会牺牲安全性，因为他们不想将自己的身份验证绑定到单个设备上。此外，passkeys 的域绑定特性虽然提高了安全性，但也可能限制了其在某些场景下的使用。

**「社区讨论」** 社区讨论主要集中在 passkeys 的便携性、安全性以及在不同服务中的使用控制上。一些用户表示他们尚未自愿启用 passkeys，主要是因为他们希望保持便携性，并避免被绑定到任何可能丢失的单个设备。还有用户提到，他们不认为使用手机指纹解锁的安全性等同于在密码管理器中使用长密码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2" target="_blank" rel="noopener noreferrer">Passkeys (FIDO2) authentication method in Microsoft Entra ID ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2" target="_blank" rel="noopener noreferrer">How to enable passkeys (FIDO2) in Microsoft Entra ID</a></li>
<li><a href="https://developers.yubico.com/Passkeys/Passkey_relying_party_implementation_guidance/Attestation/Utilizing_passkey_attestation_during_registration.html" target="_blank" rel="noopener noreferrer">Utilizing passkey attestation during registration - Yubico</a></li>
<li><a href="https://www.dashlane.com/blog/what-is-a-passkey-and-how-does-it-work" target="_blank" rel="noopener noreferrer">What Is a Passkey and How Do Passkeys Work?</a></li>
<li><a href="https://developers.google.com/identity/passkeys" target="_blank" rel="noopener noreferrer">Passkeys | Google for Developers</a></li>
<li><a href="https://www.goodrequest.com/blog/passkeys-why-the-future-of-login-doesn-t-involve-passwords" target="_blank" rel="noopener noreferrer">Passkeys : Why the future of login doesn&#x27;t involve... | GoodRequest</a></li>

</ul>
</details>

**标签**: `#Security`, `#Passkeys`, `#Technology`, `#Software Engineering`, `#User Authentication`

---

<a id="item-tech-news-7"></a>
### 机器人领域的突破：世界动作模型与可变长度动作的比较 ⭐️ 7.0/10

Reddit 上的一篇讨论突出了世界动作模型（World Action Models）与可变长度动作（VLAs）在机器人领域的比较，这可能是机器人技术领域的一个重大进步。

reddit · r/MachineLearning · /u/moschles · 10月11日 13:51

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x38qpy/world_action_models_vs_vlas_robotics_just_had_its/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x38qpy/world_action_models_vs_vlas_robotics_just_had_its/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** 在机器人领域，世界动作模型（World Action Models）和可变长度动作（Variable Length Actions，简称 VLAs）的比较引起了广泛关注。世界动作模型结合了未来世界预测与可执行动作生成，而可变长度动作则是一种多模态 AI 系统，它接受相机图像和自然语言指令作为输入，并输出机器人动作。这一讨论反映了机器人领域在 AI 和软件工程方面的最新进展。

**「影响」** 这项研究可能会对机器人领域产生重大影响，因为它比较了世界动作模型（WAMs）和可变长度动作（VLAs），这可能会改变机器人策略的架构。WAMs 通过将动作模块附加到视频世界模型主干上，取代了将动作头嫁接到预训练视觉语言模型（VLMs）上的 VLA 模型。这种新的方法有望提高机器人策略的泛化能力，使它们能够在更广泛的场景中执行任务。

**「社区讨论」** 目前没有可用的社区评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://clearlab-sustech.github.io/WorldModelSurvey/" target="_blank" rel="noopener noreferrer">From World Models to World Action Models: A Concise Tutorial ...</a></li>
<li><a href="https://www.researchgate.net/publication/408341676_From_World_Models_to_World_Action_Models_A_Concise_Tutorial_for_Robotics" target="_blank" rel="noopener noreferrer">(PDF) From World Models to World Action Models: A Concise ...</a></li>
<li><a href="https://rcl-robotics.github.io/Awesome-World-Action-Models/" target="_blank" rel="noopener noreferrer">World-Action Models for Robot Learning and Control: A Survey</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision%E2%80%93language%E2%80%93action_model" target="_blank" rel="noopener noreferrer">Vision–language–action model - Wikipedia</a></li>
<li><a href="https://www.smashingrobotics.com/what-are-vision-language-action-models-in-robotics/" target="_blank" rel="noopener noreferrer">Vision Language Action Models in Robotics (October 2026 Guide)</a></li>
<li><a href="https://mlanthology.org/iclr/2025/zhao2025iclr-vlas/" target="_blank" rel="noopener noreferrer">VLAS: Vision-Language-Action Model with Speech Instructions ...</a></li>
<li><a href="https://arxiv.org/abs/2603.22078v1" target="_blank" rel="noopener noreferrer">Do World Action Models Generalize Better than VLAs? A ... Beyond VLAs: How World Action Models Reshape Robot ... NVIDIA World Action Models vs VLA for Robot Manipulation Beyond VLAs: How World Action Models Reshape Robot ... [2609.16074] World-Action Models for Robot Learning and ... Beyond VLAs: How World Action Models Reshape Robot ... World Action Models: What They Are and How They Work</a></li>
<li><a href="https://developer.nvidia.com/blog/beyond-vlas-how-world-action-models-reshape-robot-manipulation/" target="_blank" rel="noopener noreferrer">Beyond VLAs: How World Action Models Reshape Robot ...</a></li>
<li><a href="https://paperscode.org/articles/moving-beyond-vlas-why-world/" target="_blank" rel="noopener noreferrer">NVIDIA World Action Models vs VLA for Robot Manipulation</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#AI`, `#MachineLearning`, `#SoftwareEngineering`, `#RoboticsResearch`

---

<a id="item-tech-news-8"></a>
### Jebadiah v2.1 模型更新：每项允许标签的评分模型 ⭐️ 7.0/10

Jebadiah v2.1 模型更新，包括 27B 和 9B 版本，对决策作为封闭集评分问题进行处理。在 Decision Index 0.3 公共套件中，27B 模型在知识、语言和检索方面有所提升，而 9B 模型在所有领域都有所改进。同时，也讨论了模型的一些退化问题。

reddit · r/MachineLearning · /u/WebDevToday · 10月11日 09:33

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x33wgz/p_pecision_models_that_score_every_allowed_label/" target="_blank" rel="noopener noreferrer">社区讨论</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x33wgz/p_pecision_models_that_score_every_allowed_label/">复制链接</button><span class="story-access-note">部分社区网站可能因网络环境无法访问。</span></div>

**「背景」** Jebadiah 是一个开源的决策模型，它通过回答带有固定答案的问题来提供每个选项的概率，而不是生成文本。Jebadiah v2.1 更新了 27B 和 9B 两个版本，这些模型将决策视为一个封闭集评分问题，而不是文本生成问题。输入是结构化上下文加上一个带选项的固定类型问题，输出是每个选项的概率，这些概率来自候选标签的 logits。该模型在 Decision Index 0.3 公共套件上进行了基准测试，结果显示在知识、语言、检索、艺术等领域有所提升，但在某些特定任务上出现了下降。此外，该模型还提供了量化结果和代码评估。

**「影响」** Jebadiah v2.1 模型的更新带来了性能的提升，特别是在知识、语言和检索方面。然而，也出现了一些性能下降的情况，例如 When2Call 的评分下降。这些变化可能会影响使用这些模型进行决策的用户和开发者，需要密切关注并评估这些变化对实际应用的影响。

**「社区讨论」** 目前没有可用的社区评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/frontier-infra/jebadiah-4b-v2-MLX" target="_blank" rel="noopener noreferrer">frontier-infra/jebadiah-4b-v2-MLX · Hugging Face</a></li>
<li><a href="https://huggingface.co/frontier-infra/jebadiah-9b-v2" target="_blank" rel="noopener noreferrer">frontier-infra/jebadiah-9b-v2 · Hugging Face</a></li>
<li><a href="https://jebadiah.ai/" target="_blank" rel="noopener noreferrer">Jebadiah</a></li>
<li><a href="https://huggingface.co/frontier-infra/jebadiah-9b-v2" target="_blank" rel="noopener noreferrer">frontier-infra/jebadiah-9b-v2 · Hugging Face</a></li>
<li><a href="https://tools4all.ai/trends/jebadiah-9b-v2-llm-benchmarks-faster-on-rtx-5070" target="_blank" rel="noopener noreferrer">Jebadiah 9B V2 LLM Benchmarks Faster on RTX 5070 - tools4all.ai</a></li>
<li><a href="https://benchlm.ai/compare/decider-4b-v2-vs-decision-index-0-3-jebadiah-27b" target="_blank" rel="noopener noreferrer">decider-4b v2 vs Jebadiah 27B: Benchmarks &amp; Cost | BenchLM.ai</a></li>
<li><a href="https://www.youtube.com/watch?v=MZ5OqjYF0c8" target="_blank" rel="noopener noreferrer">Genshin Impact 2 . 1 - The 4 Electro Arrow Compass Puzzle... - YouTube</a></li>
<li><a href="https://huggingface.co/mradermacher/jebadiah-9b-v2-GGUF" target="_blank" rel="noopener noreferrer">mradermacher/ jebadiah -9b- v 2 -GGUF · Hugging Face</a></li>
<li><a href="https://modelium.tech/zhurnal/jebadiah-4b-v2-gguf-mlx-local-decisions/" target="_blank" rel="noopener noreferrer">Jebadiah 4B v 2 : GGUF и MLX для локальных решений — Modelium</a></li>

</ul>
</details>

**标签**: `#MachineLearning`, `#AI`, `#ModelUpdates`, `#Benchmarking`, `#SoftwareEngineering`

---