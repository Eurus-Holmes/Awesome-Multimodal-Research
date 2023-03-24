# Awesome Multimodal Research [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

![build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![prs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

> This repo is reorganized from [Paul Liang's repo: Reading List for Topics in Multimodal Machine Learning](https://github.com/pliang279/awesome-multimodal-ml), feel free to raise pull requests! 


## News

**[03/2023] OpenAI:** *[ChatGPT plugins](https://platform.openai.com/docs/plugins/introduction) are tools designed specifically for language models with safety as a core principle, and help ChatGPT access up-to-date information, run computations, or use third-party services. https://openai.com/blog/chatgpt-plugins*
> *"We’re also hosting two plugins ourselves, a [web browser](https://openai.com/blog/chatgpt-plugins#browsing) and [code interpreter](https://openai.com/blog/chatgpt-plugins#code-interpreter). We’ve also open-sourced the code for a knowledge base [retrieval plugin](https://github.com/openai/chatgpt-retrieval-plugin), to be self-hosted by any developer with information with which they’d like to augment ChatGPT."*

**[03/2023] Google Research:** *[Bard](https://blog.google/technology/ai/try-bard/) is an early experiment that lets you collaborate with generative AI, powered by a research large language model (LLM), specifically a lightweight and optimized version of LaMDA. https://bard.google.com/*

**[03/2023] OpenAI:** *[GPT-4](https://cdn.openai.com/papers/gpt-4.pdf) is a large multimodal model (accepting image and text inputs, emitting text outputs) that, while less capable than humans in many real-world scenarios, exhibits human-level performance on various professional and academic benchmarks. https://openai.com/research/gpt-4*

**[03/2023] Google Research:** *[PaLM-E](https://palm-e.github.io/assets/palm-e.pdf) is a new generalist robotics model that overcomes these issues by transferring knowledge from varied visual and language domains to a robotics system. https://ai.googleblog.com/2023/03/palm-e-embodied-multimodal-language.html*

**[03/2023] OpenAI:** *[ChatGPT and Whisper APIs](https://openai.com/blog/introducing-chatgpt-and-whisper-apis), developers can now integrate ChatGPT and Whisper models into their apps and products through API. https://openai.com/blog/introducing-chatgpt-and-whisper-apis*

**[02/2023] MSR:** *[Kosmos-1](https://arxiv.org/pdf/2302.14045.pdf) is a multimodal large language model (MLLM) that is capable of perceiving multimodal input, following instructions, and performing in-context learning for not only language tasks but also multimodal tasks. https://github.com/microsoft/unilm#llm--mllm-multimodal-llm*

**[01/2023] Google Research:** *[2022 & beyond: Language, vision and generative models](https://ai.googleblog.com/2023/01/google-research-2022-beyond-language.html), a post of a series in which researchers across Google will highlight some exciting progress in 2022 and present the vision for 2023 and beyond. https://ai.googleblog.com/2023/01/google-research-2022-beyond-language.html*

**[11/2022] OpenAI:** *[ChatGPT](https://chat.openai.com/chat) is a sibling model to [InstructGPT](https://openai.com/research/instruction-following), which is trained to follow an instruction in a prompt and provide a detailed response. https://openai.com/blog/chatgpt*

**[08/2022] MSR:** *[Multimodal Pretraining](https://github.com/microsoft/unilm#multimodal-x--language): [BEiT-3](https://arxiv.org/abs/2208.10442) is a general-purpose multimodal foundation model, which achieves state-of-the-art transfer performance on both vision and vision-language tasks. https://github.com/microsoft/unilm/tree/master/beit*

**[04/2022] OpenAI:** *[DALL·E 2](https://arxiv.org/pdf/2204.06125.pdf) is a new AI system that can create realistic images and art from a description in natural language. https://openai.com/dall-e-2/*

**[05/2021] Google:** *[MuM](https://blog.google/products/search/introducing-mum/), a new AI milestone for understanding information. https://blog.google/products/search/introducing-mum/*

**[03/2021] OpenAI:** *[Multimodal Neurons](https://distill.pub/2021/multimodal-neurons/) in Artificial Neural Networks, which may explain CLIP’s accuracy in classifying surprising visual renditions of concepts, and is also an important step toward understanding the associations and biases that CLIP and similar models learn. https://openai.com/blog/multimodal-neurons/*

**[01/2021] OpenAI:** *[CLIP](https://openai.com/blog/clip/) maps images into categories described in text, and [DALL-E](https://openai.com/blog/dall-e/) creates new images from text. A step toward systems with deeper understanding of the world. https://openai.com/multimodal/*


## Research Papers

* [Survey Papers](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Survey-Papers)
* [Core Areas](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas)
  * [Representation Learning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Representation-Learning)
  * [Multimodal Fusion](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Multimodal-Fusion)
  * [Multimodal Alignment](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Multimodal-Alignment)
  * [Multimodal Translation](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Multimodal-Translation)
  * [Missing or Imperfect Modalities](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Missing-or-Imperfect-Modalities)
  * [Knowledge Graphs and Knowledge Bases](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Knowledge-Graphs-and-Knowledge-Bases)
  * [Intepretable Learning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Intepretable-Learning)
  * [Generative Learning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Generative-Learning)
  * [Semi-supervised Learning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Semi-supervised-Learning)
  * [Self-supervised Learning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Self-supervised-Learning)
  * [Language Models](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Language-Models)
  * [Adversarial Attacks](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Adversarial-Attacks)
  * [Few-Shot Learning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Few-Shot-Learning)
  * [Bias and Fairness](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Core-Areas/Bias-and-Fairness)
* [Applications](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications)
  * [Language and Visual QA](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Language-and-Visual-QA)
  * [Language Grounding in Vision](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Language-Grounding-in-Vision)
  * [Language Grouding in Navigation](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Language-Grouding-in-Navigation)
  * [Multimodal Machine Translation](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Multimodal-Machine-Translation)
  * [Multi-agent Communication](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Multi-agent-Communication)
  * [Commonsense Reasoning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Commonsense-Reasoning)
  * [Multimodal Reinforcement Learning](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Multimodal-Reinforcement-Learning)
  * [Multimodal Dialog](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Multimodal-Dialog)
  * [Language and Audio](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Language-and-Audio)
  * [Audio and Visual](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Audio-and-Visual)
  * [Media Description](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Media-Description)
  * [Video Generation from Text](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Video-Generation-from-Text)
  * [Affect Recognition and Multimodal Language](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Affect-Recognition-and-Multimodal-Language)
  * [Healthcare](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Healthcare)
  * [Robotics](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Robotics)
  * [Autonomous Driving](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/papers/Applications/Autonomous-Driving)
* [Workshops](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/workshops)
* [Tutorials](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/tutorials)
* [Courses](https://github.com/Eurus-Holmes/Awesome-Multimodal-Research/tree/master/courses)


## Recent Workshop

[Social Intelligence in Humans and Robots](https://social-intelligence-human-ai.github.io/), ICRA 2021

[LANTERN 2021](https://www.lantern.uni-saarland.de/2021/): The Third Workshop Beyond Vision and LANguage: inTEgrating Real-world kNowledge, EACL 2021

Multimodal workshops: [Multimodal Learning and Applications](https://mula-workshop.github.io/), [Sight and Sound](http://sightsound.org/), [Visual Question Answering](https://visualqa.org/workshop), [Embodied AI](https://embodied-ai.org/), [Language for 3D Scenes](http://language3dscenes.github.io/), CVPR 2021

[Advances in Language and Vision Research (ALVR)](https://alvr-workshop.github.io/), NAACL 2021

[Visually Grounded Interaction and Language (ViGIL)](https://vigilworkshop.github.io/), NAACL 2021

[Wordplay: When Language Meets Games](https://wordplay-workshop.github.io/), NeurIPS 2020

[NLP Beyond Text](https://sites.google.com/view/nlpbt-2020), EMNLP 2020

[International Challenge on Compositional and Multimodal Perception](https://camp-workshop.stanford.edu/), ECCV 2020

[Multimodal Video Analysis Workshop and Moments in Time Challenge](https://sites.google.com/view/multimodalvideo-v2), ECCV 2020

[Video Turing Test: Toward Human-Level Video Story Understanding](https://dramaqa.snu.ac.kr/Workshop/2020), ECCV 2020

[Grand Challenge and Workshop on Human Multimodal Language](http://multicomp.cs.cmu.edu/acl2020multimodalworkshop/), ACL 2020

[Workshop on Multimodal Learning](https://mul-workshop.github.io/), CVPR 2020

[Language & Vision with applications to Video Understanding](https://languageandvision.github.io/), CVPR 2020

[International Challenge on Activity Recognition (ActivityNet)](http://activity-net.org/challenges/2020/), CVPR 2020

[The End-of-End-to-End A Video Understanding Pentathlon](https://www.robots.ox.ac.uk/~vgg/challenges/video-pentathlon/), CVPR 2020

[Towards Human-Centric Image/Video Synthesis, and the 4th Look Into Person (LIP) Challenge](https://vuhcs.github.io/), CVPR 2020

[Visual Question Answering and Dialog](https://visualqa.org/workshop), CVPR 2020


## Recent Tutorial

[Tutorials on Multimodal Machine Learning](https://cmu-multicomp-lab.github.io/mmml-tutorial/cvpr2022/), CVPR 2022 && NAACL 2022

[Multi-modal Information Extraction from Text, Semi-structured, and Tabular Data on the Web (Cutting-edge)](https://sites.google.com/view/acl-2020-multi-modal-ie), ACL 2020

[Achieving Common Ground in Multi-modal Dialogue (Cutting-edge)](https://github.com/malihealikhani/Grounding_in_Dialogue), ACL 2020

[Recent Advances in Vision-and-Language Research](https://rohit497.github.io/Recent-Advances-in-Vision-and-Language-Research/), CVPR 2020

[Neuro-Symbolic Visual Reasoning and Program Synthesis](http://nscv.csail.mit.edu/), CVPR 2020

[Large Scale Holistic Video Understanding](https://holistic-video-understanding.github.io/tutorials/cvpr2020.html), CVPR 2020

[A Comprehensive Tutorial on Video Modeling](https://cvpr20-video.mxnet.io/), CVPR 2020



