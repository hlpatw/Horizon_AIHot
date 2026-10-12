---
layout: default
title: "AIHOT Daily: 2026-10-12"
date: 2026-10-12
lang: en
---

> From 16 items, 8 important content pieces were selected

---

**Technology News**
1. [Browser Tool Visualizes Attention Mechanism of Small Language Model](#item-tech-news-1) ⭐️ 8.0/10
2. [New Method for Color-Scheme Search in Paintings Dataset](#item-tech-news-2) ⭐️ 8.0/10
3. [Total Annihilation, rebuilt for modern computers](#item-tech-news-3) ⭐️ 7.0/10
4. [Cartographers of North Korea \(2019\)](#item-tech-news-4) ⭐️ 7.0/10
5. [The Widening Gap in LLM Capability Understanding](#item-tech-news-5) ⭐️ 7.0/10
6. [Passkeys Security Concerns](#item-tech-news-6) ⭐️ 7.0/10
7. [World Action Models vs VLAs: Robotics Breakthrough](#item-tech-news-7) ⭐️ 7.0/10
8. [Precision Models Jebadiah v2.1 Updates](#item-tech-news-8) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### Browser Tool Visualizes Attention Mechanism of Small Language Model ⭐️ 8.0/10

A browser-based tool has been developed to visualize the attention mechanism of a small language model, SmolLM2-135M. This tool allows users to see how the model selects the next word by displaying probabilities and attention weights between tokens. The tool is accessible through a browser and can be used on mobile devices, providing insights into the internal workings of language models.

reddit · r/MachineLearning · /u/Minute-Mountain2665 · Oct 11, 22:30

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x3lgnz/i_built_a_browser_tool_to_visualize_how_a_small/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x3lgnz/i_built_a_browser_tool_to_visualize_how_a_small/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on Language Models and Attention Mechanisms」** Language models, such as the SmolLM 2 series, are designed to understand and generate human language. They are trained on vast datasets and can perform a range of tasks. One key component of these models is the attention mechanism, which allows the model to focus on different parts of the input text when generating output. This mechanism is crucial for understanding the context and relationships between words in a sentence. The attention mechanism has been a significant advancement in natural language processing, enabling models to dynamically focus on relevant parts of the input data, which enhances their performance and accuracy.

**「Impact on Users and Developers」** The browser tool provides users and developers with a practical and accessible way to understand the attention mechanism in language models. By visualizing how a small language model selects the next word and where its attention is directed, the tool enhances the learning experience and aids in the development of more informed models.

**「Community Discussion」** No community comments available.

<details><summary>References</summary>
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

**Tags**: `#Machine Learning`, `#Language Models`, `#Attention Mechanism`, `#Visualization`, `#Browser Tool`

---

<a id="item-tech-news-2"></a>
### New Method for Color-Scheme Search in Paintings Dataset ⭐️ 8.0/10

A novel method for color-scheme search in a dataset of 48k paintings has been introduced, utilizing Sliced Wasserstein embeddings and HNSW indexing. This approach aims to improve the efficiency of color-scheme searches by reducing the computational time for nearest-neighbor searches.

reddit · r/MachineLearning · /u/Potential-Barber8658 · Oct 11, 14:39

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x39uu6/sliced_wasserstein_embeddings_hnsw_for/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x39uu6/sliced_wasserstein_embeddings_hnsw_for/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Color Scheme Search in Art Databases」** Color scheme search in art databases involves techniques to analyze and compare the color palettes used in various images. One common approach is to reduce each image to a set number of representative colors, such as 128, and then use distance metrics like Earth Mover&\#x27;s Distance \(EMD\) to measure the similarity between color schemes. However, EMD can be computationally expensive for large datasets. This background is relevant to the new method presented, which uses Sliced Wasserstein embeddings and HNSW indexing to improve the efficiency of color-scheme search over a dataset of 48k paintings.

**「Impact on Color Scheme Search」** The introduction of Sliced Wasserstein embeddings and HNSW indexing for color-scheme search in a dataset of 48k paintings significantly improves search efficiency. This method reduces the search time from approximately 6 ms per pair to just 0.25 ms using HNSW indexing, making it feasible to perform nearest-neighbor searches over a large dataset. This advancement in color-scheme search can lead to more efficient and accurate searches in various applications, such as art analysis and color scheme recommendation systems.

**「Community Discussion」** No community comments available.

<details><summary>References</summary>
<ul>
<li><a href="https://www.palette-atlas.com/search" target="_blank" rel="noopener noreferrer">Color search · Palette Atlas</a></li>
<li><a href="https://www.palette-atlas.com/" target="_blank" rel="noopener noreferrer">Palette Atlas — Color palettes rooted in culture</a></li>
<li><a href="https://coolors.co/palettes/search" target="_blank" rel="noopener noreferrer">Search Color Palettes - Coolors</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2023/10/introduction-to-hnsw-hierarchical-navigable-small-world/" target="_blank" rel="noopener noreferrer">Introduction to HNSW : Hierarchical Navigable Small World</a></li>
<li><a href="https://milvus.io/docs/hnsw.md" target="_blank" rel="noopener noreferrer">HNSW | Milvus Documentation</a></li>
<li><a href="https://medium.com/pinterest-engineering/manas-hnsw-realtime-powering-realtime-embedding-based-retrieval-dc71dfd6afdd" target="_blank" rel="noopener noreferrer">Manas HNSW Realtime: Powering Realtime Embedding -Based...</a></li>

</ul>
</details>

**Tags**: `#Computer Vision`, `#Machine Learning`, `#Data Indexing`, `#Color Scheme Search`, `#Artificial Intelligence`

---

<a id="item-tech-news-3"></a>
### Total Annihilation, rebuilt for modern computers ⭐️ 7.0/10

Community discusses the modernization of the classic RTS game Total Annihilation, highlighting improvements and community engagement.

hackernews · jttnr · Oct 11, 18:04 · [Discussion](https://news.ycombinator.com/item?id=50045984)

<div class="story-actions"><a class="story-action story-action--primary" href="https://nanolathe.gg/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://nanolathe.gg/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**Tags**: `#RTS Gaming`, `#Total Annihilation`, `#Game Modernization`, `#Community Engagement`, `#Software Engineering`

---

<a id="item-tech-news-4"></a>
### Cartographers of North Korea \(2019\) ⭐️ 7.0/10

The Cartographers of North Korea project, initiated in 2019, has captured the interest of the community with its detailed and unique mapping of North Korea. This project offers a unique perspective on mapping the region, which has implications for software engineering and geographic information systems.

hackernews · edent · Oct 11, 19:46 · [Discussion](https://news.ycombinator.com/item?id=50047091)

<div class="story-actions"><a class="story-action story-action--primary" href="https://cartographers-nk.wonyoung.so/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://cartographers-nk.wonyoung.so/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Historical Mapping of North Korea」** The mapping of North Korea has a rich history, with projects like &\#x27;North Korea Uncovered&\#x27; providing comprehensive mappings of the region. The division of Korea in 1945, following the Japanese surrender at the end of World War II, led to the north being occupied by the Soviet Union and the south by the United States. This historical context has influenced the mapping efforts, particularly in terms of connectivity and control over information. The North Korean government has adapted open-source culture while maintaining strict control over internet access, which has implications for the mapping projects and the information they provide.

**「Impact on Users and Developers」** The detailed and unique mapping project of North Korea has implications for software engineering and geographic information systems. It provides developers with a rich dataset for understanding the region, which could lead to improved GIS software and applications. Users gain a deeper insight into the geography and infrastructure of North Korea, fostering a better understanding of the region and potentially aiding in humanitarian efforts.

**「Community Discussion」** Community members have expressed a strong interest in the project. Some have noted the increasing openness of North Korea to tourists, which is reflected in the availability of videos on platforms like YouTube. Others have praised the detailed and easy-to-read layout of the mapping data, highlighting its importance for navigation and geographic understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/North_Korea_Uncovered" target="_blank" rel="noopener noreferrer">North Korea Uncovered - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/North_Korea" target="_blank" rel="noopener noreferrer">North Korea - Wikipedia</a></li>
<li><a href="https://senseable.mit.edu/papers/pdf/20200217_SoDuarte_CartographersNK_Geoforum.pdf" target="_blank" rel="noopener noreferrer">Cartographers of North Korea_ Who are they and what are the ...</a></li>
<li><a href="https://www.esri.com/" target="_blank" rel="noopener noreferrer">GIS Software for Mapping and Spatial Analytics | Esri</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/15230406.2021.1910075" target="_blank" rel="noopener noreferrer">tandfonline.com/doi/full/10.1080/15230406.2021.1910075</a></li>
<li><a href="https://map.seabreezegeo.az/" target="_blank" rel="noopener noreferrer">Sea Breeze GIS | Interactive 3D Map &amp; Infrastructure</a></li>

</ul>
</details>

**Tags**: `#Mapping`, `#Geographic Information Systems`, `#North Korea`, `#Software Engineering`, `#Community Interest`

---

<a id="item-tech-news-5"></a>
### The Widening Gap in LLM Capability Understanding ⭐️ 7.0/10

The discussion highlights the increasing disparity in the shared understanding of Large Language Model \(LLM\) capabilities within the technology industry. This gap is a significant topic of interest and engagement among the community, indicating its relevance and potential impact on the industry.

hackernews · albertzeyer · Oct 11, 20:20 · [Discussion](https://news.ycombinator.com/item?id=50047422)

<div class="story-actions"><a class="story-action story-action--primary" href="https://twitter.com/karpathy/status/2109361546505966046" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://twitter.com/karpathy/status/2109361546505966046">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on Large Language Models \(LLMs\)」** Large Language Models \(LLMs\) have evolved significantly since their foundational language-modelling research. The Transformer architecture, introduced in 2017 by Vaswani et al., marked a significant milestone in this evolution. Contemporary models, including GPT, Claude, Gemini, Llama, Qwen, and DeepSeek, have been released in 2025-2026. These models have multimodal capabilities, though challenges remain in consistency, particularly in rare visual contexts, low-resolution inputs, and cross-modal reasoning. The LLM market is entering a decisive phase, transitioning into core digital infrastructure for enterprises, governments, and platforms, after several years of scale races and experimental deployments.

**「Community Discussion」** Community members express varied opinions on the impact of AI and LLMs. Some argue that AI has not significantly improved life for the average person, while others discuss the divide between those who are cautious about LLMs due to potential issues and those who are more confident in their capabilities. There is also a discussion on the general public&\#x27;s understanding and use of these models.

<details><summary>References</summary>
<ul>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6887539" target="_blank" rel="noopener noreferrer">The Evolution, Capabilities, Limitations, and Future of Large ...</a></li>
<li><a href="https://aimultiple.com/future-of-large-language-models" target="_blank" rel="noopener noreferrer">The Future of Large Language Models</a></li>
<li><a href="https://www.makebot.ai/blog-en/llm-market-enterprise-trends" target="_blank" rel="noopener noreferrer">10 Key LLM Market Trends for 2026 - makebot.ai</a></li>

</ul>
</details>

**Tags**: `#Artificial Intelligence`, `#Machine Learning`, `#LLM Capabilities`, `#Technology Industry`, `#Community Interest`

---

<a id="item-tech-news-6"></a>
### Passkeys Security Concerns ⭐️ 7.0/10

The article discusses the potential risks and limitations of passkeys in technology security, sparking community engagement on the topic. It raises concerns about the use of passkeys, particularly regarding their portability and the control over credential strength.

hackernews · laurex · Oct 11, 21:59 · [Discussion](https://news.ycombinator.com/item?id=50048312)

<div class="story-actions"><a class="story-action story-action--primary" href="https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on Passkeys and Attestation」** Passkeys, a part of the FIDO2 authentication method, are designed to provide a more secure and convenient way to authenticate users. They involve the use of cryptographic keys stored on a user&\#x27;s device, which can be used to authenticate to various services. One key aspect of passkeys is attestation, which verifies the authenticity of the passkey provider or device during registration. This process ensures that the device used to register the passkey is legitimate and can provide cryptographically verifiable device identity through the FIDO Metadata Service \(MDS\). Attestation enforcement can be configured to allow passkeys only during registration, and users who register a passkey without attestation are not blocked from sign-in if attestation enforcement is set to Yes later. This method of utilizing passkey attestation during registration is also discussed by vendors like Yubico, emphasizing the importance of authenticator make and model verification and storing attestation metadata with the credential.

**「Impact on User Authentication」** The discussion on passkeys highlights the importance of understanding their limitations and risks. Users who are concerned about portability and control over their credentials may prefer traditional password managers over passkeys. This could lead to a shift in user preferences for authentication methods, potentially affecting the adoption of passkeys.

**「Community Discussion」** Community members are debating the effectiveness and security of passkeys. Some express concerns about the lack of attestation during login and the potential for being tied to a single device. Others highlight the security benefits, such as resistance to Man-In-The-Middle attacks and the ability to use attested passkeys for added safety.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2" target="_blank" rel="noopener noreferrer">Passkeys (FIDO2) authentication method in Microsoft Entra ID ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2" target="_blank" rel="noopener noreferrer">How to enable passkeys (FIDO2) in Microsoft Entra ID</a></li>
<li><a href="https://developers.yubico.com/Passkeys/Passkey_relying_party_implementation_guidance/Attestation/Utilizing_passkey_attestation_during_registration.html" target="_blank" rel="noopener noreferrer">Utilizing passkey attestation during registration - Yubico</a></li>
<li><a href="https://www.dashlane.com/blog/what-is-a-passkey-and-how-does-it-work" target="_blank" rel="noopener noreferrer">What Is a Passkey and How Do Passkeys Work?</a></li>
<li><a href="https://developers.google.com/identity/passkeys" target="_blank" rel="noopener noreferrer">Passkeys | Google for Developers</a></li>
<li><a href="https://www.goodrequest.com/blog/passkeys-why-the-future-of-login-doesn-t-involve-passwords" target="_blank" rel="noopener noreferrer">Passkeys : Why the future of login doesn&#x27;t involve... | GoodRequest</a></li>

</ul>
</details>

**Tags**: `#Security`, `#Passkeys`, `#Technology`, `#Software Engineering`, `#User Authentication`

---

<a id="item-tech-news-7"></a>
### World Action Models vs VLAs: Robotics Breakthrough ⭐️ 7.0/10

A Reddit discussion highlights a comparison between World Action Models and Variable Length Actions \(VLAs\) in robotics, potentially marking a significant advancement in the field. This development could have a notable impact on software engineering and AI systems, representing a novel approach in robotics.

reddit · r/MachineLearning · /u/moschles · Oct 11, 13:51

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x38qpy/world_action_models_vs_vlas_robotics_just_had_its/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x38qpy/world_action_models_vs_vlas_robotics_just_had_its/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on World Action Models and VLAs」** The discussion on Reddit revolves around the comparison between World Action Models and Variable Length Actions \(VLAs\) in the field of robotics. World Action Models \(WAMs\) are a recent development that couple future world prediction with executable action generation, as highlighted in the survey by RCL Robotics. These models are part of the advancements in world models, video generation, and Vision-Language-Action \(VLA\) policies. On the other hand, VLAs are multimodal AI systems that take camera images and natural language instructions to output robot actions. The integration of speech modality in VLAs, as proposed in the VLAS model, represents a significant step in robot manipulation. This comparison and the potential advancements in the field are based on recent research and tutorials available online, such as the concise tutorial on world models and world action models for physical AI and robotics.

**「Impact on Robotics Field」** The comparison between World Action Models and Variable Length Actions in robotics could lead to significant advancements in the field. This development, which involves replacing Vision-Language-Action \(VLA\) models with World Action Models \(WAMs\), aims to improve the generalization of robot policies beyond training demonstrations, potentially enhancing the capabilities of AI-driven robot control systems.

**「Community Discussion」** No community comments available.

<details><summary>References</summary>
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

**Tags**: `#Robotics`, `#AI`, `#MachineLearning`, `#SoftwareEngineering`, `#RoboticsResearch`

---

<a id="item-tech-news-8"></a>
### Precision Models Jebadiah v2.1 Updates ⭐️ 7.0/10

Jebadiah v2.1, precision models with 27B and 9B parameters, have been updated with open weights and self-run benchmark results. The 27B model improved on the Decision Index 0.3 public suite, while the 9B model also saw enhancements. However, there were regressions in specific tasks, particularly When2Call, with no identified cause yet.

reddit · r/MachineLearning · /u/WebDevToday · Oct 11, 09:33

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1x33wgz/p_pecision_models_that_score_every_allowed_label/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1x33wgz/p_pecision_models_that_score_every_allowed_label/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on Jebadiah Models」** Jebadiah is a family of open decision models developed by Frontier Infra. These models are designed to answer typed questions by providing probabilities for each possible option, rather than generating text. The models operate on a forward pass per question, making them efficient for decision-making tasks. Previous versions of Jebadiah, such as the 4B and 9B variants, have been benchmarked and showcased their performance on various platforms and hardware, including Apple silicon and RTX 5070 GPUs. The models are known for their precision and efficiency in handling decision-making scenarios.

**「Impact on Users and Developers」** The release of Jebadiah v2.1, with its 27B and 9B precision models, offers improved performance across various domains such as Knowledge, Language, Retrieval, Arts, and Tools. This update is significant for users and developers as it provides more accurate and efficient models for decision-making tasks, potentially enhancing the capabilities of applications in these areas. However, the identified regressions in specific benchmarks like When2Call raise concerns that need to be addressed to ensure the reliability of the models.

**「Community Discussion」** No community comments available.

<details><summary>References</summary>
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

**Tags**: `#MachineLearning`, `#AI`, `#ModelUpdates`, `#Benchmarking`, `#SoftwareEngineering`

---