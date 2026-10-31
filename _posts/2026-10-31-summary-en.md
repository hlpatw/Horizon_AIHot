---
layout: default
title: "AIHOT Daily: 2026-10-31"
date: 2026-10-31
lang: en
---

> From 15 items, 5 important content pieces were selected

---

**Technology News**
1. [Multi-Token Prediction Improvement with Soft-MTP and KL Gradient-Recovery Trick](#item-tech-news-1) ⭐️ 9.0/10
2. [Backdoor in Claude Code for VS Code Extension on Cursor Marketplace](#item-tech-news-2) ⭐️ 7.0/10
3. [Nintendo Emulation with Qwen Weights](#item-tech-news-3) ⭐️ 7.0/10
4. [The federated code forge](#item-tech-news-4) ⭐️ 7.0/10
5. [Azure&\#x27;s Weakest Link - Five Full Cross-Tenant Compromises](#item-tech-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### Multi-Token Prediction Improvement with Soft-MTP and KL Gradient-Recovery Trick ⭐️ 9.0/10

A significant advancement in Multi-Token Prediction \(MTP\) has been achieved with the introduction of Soft-MTP and a KL gradient-recovery trick. This breakthrough enhances the performance of MTP across various tasks, offering a novel approach to improve MTP performance.

reddit · r/MachineLearning · /u/jayden\_teoh\_ · Oct 30, 18:53

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.reddit.com/r/MachineLearning/comments/1xjnz40/multitoken_prediction_done_right_r/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.reddit.com/r/MachineLearning/comments/1xjnz40/multitoken_prediction_done_right_r/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Understanding Multi-Token Prediction \(MTP\)」** Multi-Token Prediction \(MTP\) is a technique used in machine learning and artificial intelligence for pre-training large language models. It involves predicting short blocks of future tokens, which is a relaxation of the next-token prediction \(NTP\) that uses teacher forcing. MTP has been gaining attention as a universal inference method, but it has limitations in terms of its effectiveness and the challenges it poses in probabilistic token prediction.

**「Consequence for Users and Developers」** The introduction of Soft-MTP and the KL gradient-recovery trick in Multi-Token Prediction \(MTP\) significantly enhances the performance of MTP across various tasks. This advancement allows for improved speculative decoding and next-token prediction, benefiting users and developers by providing a more efficient and effective pre-training method for machine learning models.

**「Community Discussion」** No community comments available.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2510.14751" target="_blank" rel="noopener noreferrer">Beyond Multi - Token Prediction : Pretraining LLMs with Future...</a></li>
<li><a href="https://www.linkedin.com/posts/kamen-stoykov-80413b54_multi-token-prediction-mtp-is-often-pitched-activity-7467572378034782226-u-Vc" target="_blank" rel="noopener noreferrer">Multi - Token Prediction ( MTP ) is often pitched as a universal inference...</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/12181" target="_blank" rel="noopener noreferrer">[Feature]: Multi - Token Prediction ( MTP ) · Issue #12181...</a></li>
<li><a href="https://www.tandfonline.com/doi/abs/10.2753/MTP1069-6679190202" target="_blank" rel="noopener noreferrer">tandfonline.com/doi/abs/10.2753/ MTP 1069-6679190202</a></li>
<li><a href="https://www.youtube.com/watch?v=qAVzRmgRvgU" target="_blank" rel="noopener noreferrer">Installing MTP Software - YouTube</a></li>
<li><a href="https://www.taylorfrancis.com/books/mono/10.1201/9781315371658/machine-learning-mohssen-mohammed-muhammad-badruddin-khan-eihab-bashier-mohammed-bashier" target="_blank" rel="noopener noreferrer">Machine Learning | Algorithms and Applications | Mohssen...</a></li>

</ul>
</details>

**Tags**: `#MachineLearning`, `#AI`, `#MTP`, `#Pre-training`, `#Soft-MTP`

---

<a id="item-tech-news-2"></a>
### Backdoor in Claude Code for VS Code Extension on Cursor Marketplace ⭐️ 7.0/10

A security breach has been identified in the Claude Code extension for VS Code, hosted on the Cursor Marketplace. The breach potentially affects users&\#x27; SSH keys, as a malicious actor used access to Cursor&\#x27;s marketplace to publish a tampered copy of the extension.

hackernews · \_chall · Oct 30, 07:09 · [Discussion](https://news.ycombinator.com/item?id=50300683)

<div class="story-actions"><a class="story-action story-action--primary" href="https://phorion.io/blog/offical-claude-code-vsx-compromise/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://phorion.io/blog/offical-claude-code-vsx-compromise/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on Claude Code Extension Security Breach」** The Claude Code extension for VS Code, available on the Cursor Marketplace, has been compromised. This security breach involves a malicious version of the extension that was not developed by Anthropic, the company behind the original Claude Code. The malicious extension had the potential to append the attacker&\#x27;s public key to users&\#x27; SSH authorized keys, thereby compromising SSH keys. This incident highlights the importance of software security and the need for users to be vigilant about the extensions they install in their development environments.

**「Impact on Users」** Users of the Claude Code extension on the Cursor Marketplace may have had their SSH keys compromised due to a malicious extension that was live on the marketplace. This could lead to unauthorized access to their systems and data.

**「Community Discussion」** Felix from Anthropic confirmed that the incident did not compromise Anthropic&\#x27;s systems. The malicious extension appended the attacker&\#x27;s public key to users&\#x27; SSH authorized keys. Users are advised to check their SSH keys for the presence of the &\#x27;svc-telemetry&\#x27; key to determine if their machine is impacted.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html" target="_blank" rel="noopener noreferrer">Official Claude Code VS Code Extension Compromised to Install...</a></li>
<li><a href="https://cursor.com/blog/claude-code-extension-security-notice" target="_blank" rel="noopener noreferrer">Security notice — malicious version of Anthropic. claude - code ...</a></li>
<li><a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/" target="_blank" rel="noopener noreferrer">Official Claude Code Extension Compromise: Security ... | Phorion</a></li>
<li><a href="https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html" target="_blank" rel="noopener noreferrer">Official Claude Code Extension on Cursor Marketplace ...</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/" target="_blank" rel="noopener noreferrer">Inside a malicious Claude Code-branded extension and its ...</a></li>
<li><a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/" target="_blank" rel="noopener noreferrer">Official Claude Code Extension Compromise: Security Advisory</a></li>

</ul>
</details>

**Tags**: `#Security Breach`, `#VS Code Extension`, `#SSH Keys`, `#Cursor Marketplace`, `#Software Security`

---

<a id="item-tech-news-3"></a>
### Nintendo Emulation with Qwen Weights ⭐️ 7.0/10

A project has emerged that uses Qwen weights to emulate a Nintendo Entertainment System, sparking discussions on AI and machine learning applications. This innovative approach to emulation has generated significant community interest and could have implications for the field of software engineering and AI systems.

hackernews · dbreunig · Oct 30, 16:40 · [Discussion](https://news.ycombinator.com/item?id=50306442)

<div class="story-actions"><a class="story-action story-action--primary" href="https://github.com/dbreunig/nesformer" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://github.com/dbreunig/nesformer">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Background on NES Emulation and Qwen Weights」** NES emulation, or emulating the Nintendo Entertainment System, has been a popular area of interest in the software engineering and gaming communities. It involves replicating the functionality of the original console to run classic games. Qwen, on the other hand, is an AI model that offers various functionalities, including chatbot, image and video understanding, and document processing. The use of Qwen weights in NES emulation is a novel approach that has sparked discussions on the applications of AI and machine learning in this domain.

**「Impact on AI and Machine Learning Applications」** The project using Qwen weights to emulate a Nintendo Entertainment System has sparked discussions on AI and machine learning applications. It demonstrates the potential of using large language models for emulating complex systems, which could lead to new approaches in AI and machine learning development.

**「Community Discussion」** The community has expressed a range of opinions on the project. Some are fascinated by the potential of compiling a small VM inside LLM weights, while others appreciate the demonstration of the massive compute requirement between LLMs and ordinary programs. There&\#x27;s also a discussion on the efficiency of deterministic programs compared to AI and the simulation of both CPU and RAM in the model.

<details><summary>References</summary>
<ul>
<li><a href="https://joeheyming.github.io/emulator/nes/" target="_blank" rel="noopener noreferrer">NES Emulator — Nintendo Entertainment System</a></li>
<li><a href="https://qwen.ai/" target="_blank" rel="noopener noreferrer">Qwen</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B" target="_blank" rel="noopener noreferrer">Qwen / Qwen 3.8-27B · Hugging Face</a></li>
<li><a href="https://pragma-core.com/blog/qwen-38-27b-and-the-year-the-open-weights-caught-up-how-a-17gb-download-started-beating-the-frontier" target="_blank" rel="noopener noreferrer">Qwen 3.8 27B and the year the open weights caught up: how a 17GB ...</a></li>
<li><a href="https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463" target="_blank" rel="noopener noreferrer">Alibaba Unveils Qwen3.8-27B and Releases Weights of Qwen3.8 Flagship ...</a></li>
<li><a href="https://www.analyticsinsight.net/artificial-intelligence/alibabas-qwen38-ai-model-what-developers-should-know-about-the-open-weight-release" target="_blank" rel="noopener noreferrer">Alibaba Qwen3.8 AI Model: What Developers Should Know</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#Emulation`, `#Nintendo`, `#Software Engineering`

---

<a id="item-tech-news-4"></a>
### The federated code forge ⭐️ 7.0/10

A new code forge, Tangled, is discussed, highlighting its architecture, UI overhaul, and support for organizations, with community members showing interest and discussing its integration possibilities.

hackernews · zlliang · Oct 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=50305573)

<div class="story-actions"><a class="story-action story-action--primary" href="https://tangled.org/blog/forge/" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://tangled.org/blog/forge/">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**Tags**: `#Code Collaboration`, `#Federated Code Forge`, `#Tangled`, `#Software Engineering`, `#Open Source`

---

<a id="item-tech-news-5"></a>
### Azure&\#x27;s Weakest Link - Five Full Cross-Tenant Compromises ⭐️ 7.0/10

An analysis has been published highlighting five full cross-tenant compromises in Azure&\#x27;s cross-tenant capabilities, emphasizing the potential impact on users and enterprises.

hackernews · swq115 · Oct 30, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50301854)

<div class="story-actions"><a class="story-action story-action--primary" href="https://www.binarysecurity.no/posts/2026/10/one-root-case" target="_blank" rel="noopener noreferrer">Community discussion</a><button class="copy-story-link" type="button" data-copy-url="https://www.binarysecurity.no/posts/2026/10/one-root-case">Copy link</button><span class="story-access-note">Some community sites may be unavailable on certain networks.</span></div>

**「Azure Cross-Tenant Vulnerabilities Background」** Azure&\#x27;s cross-tenant capabilities have been a subject of concern due to several security vulnerabilities. Historically, Azure has faced cross-tenant and cross-subscription issues, which have often been fixed server-side without CVE assignments. Notable vulnerabilities include OMIGOD, FabriXss/Super FabriXss, and SynLapse. These vulnerabilities have impacted Key Vault, SQL, credentials, and applications within Azure. The current discussion revolves around five full cross-tenant compromises, highlighting the potential impact on users and enterprises.

**「Community Discussion」** Community members are discussing the severity of Azure&\#x27;s cross-tenant vulnerabilities, with some expressing concern about the lack of effective authentication and authorization measures, while others commend the efforts of researchers in uncovering these vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.hacktricks.wiki/en/pentesting-cloud/azure-security/az-cross-tenant-and-cross-subscription-attacks/historical-cross-tenant-vulnerabilities.html" target="_blank" rel="noopener noreferrer">Az - Historical Cross-Tenant Vulnerabilities - HackTricks Cloud</a></li>
<li><a href="https://www.theprotec.com/blog/azure-cross-tenant-vulnerabilities-api-connections/" target="_blank" rel="noopener noreferrer">How Azure cross-tenant vulnerabilities exposed API ...</a></li>
<li><a href="https://www.binarysecurity.no/posts/2026/10/one-root-case" target="_blank" rel="noopener noreferrer">Azure&#x27;s Weakest Link - Five Full Cross-Tenant Compromises</a></li>

</ul>
</details>

**Tags**: `#Azure`, `#Security Vulnerabilities`, `#Cloud Computing`, `#Cybersecurity`, `#Enterprise IT`

---