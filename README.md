# Awesome Multimodal Research [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

![build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![prs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

> Organize based on [Paul Liang's repo: Reading List for Topics in Multimodal Machine Learning](https://github.com/pliang279/awesome-multimodal-ml), any suggestions are welcome! 


## Research Papers

* [Survey Papers](#survey-papers)
* [Core Areas](#core-areas)
  * [Representation Learning](#representation-learning)
  * [Multimodal Fusion](#multimodal-fusion)
  * [Multimodal Alignment](#multimodal-alignment)
  * [Multimodal Translation](#multimodal-translation)
  * [Missing or Imperfect Modalities](#missing-or-imperfect-modalities)
  * [Knowledge Graphs and Knowledge Bases](#knowledge-graphs-and-knowledge-bases)
  * [Intepretable Learning](#intepretable-learning)
  * [Generative Learning](#generative-learning)
  * [Semi-supervised Learning](#semi-supervised-learning)
  * [Self-supervised Learning](#self-supervised-learning)
  * [Language Models](#language-models)
  * [Adversarial Attacks](#adversarial-attacks)
  * [Few-Shot Learning](#few-shot-learning)
* [Applications](#applications)
  * [Language and Visual QA](#language-and-visual-qa)
  * [Language Grounding in Vision](#language-grounding-in-vision)
  * [Language Grouding in Navigation](#language-grouding-in-navigation)
  * [Multimodal Machine Translation](#multimodal-machine-translation)
  * [Multi-agent Communication](#multi-agent-communication)
  * [Commonsense Reasoning](#commonsense-reasoning)
  * [Multimodal Reinforcement Learning](#multimodal-reinforcement-learning)
  * [Multimodal Dialog](#multimodal-dialog)
  * [Language and Audio](#language-and-audio)
  * [Audio and Visual](#audio-and-visual)
  * [Media Description](#media-description)
  * [Video Generation from Text](#video-generation-from-text)
  * [Affect Recognition and Multimodal Language](#affect-recognition-and-multimodal-language)
  * [Healthcare](#healthcare)
  * [Robotics](#robotics)
* [Workshops](#workshops)
* [Tutorials](#tutorials)
* [Courses](#courses)


## Applications

### Language and Visual QA

[Interactive Language Learning by Question Answering](https://arxiv.org/abs/1908.10909), EMNLP 2019 [[code]](https://github.com/xingdi-eric-yuan/qait_public)

[Fusion of Detected Objects in Text for Visual Question Answering](https://arxiv.org/abs/1908.05054), arXiv 2019 

[RUBi: Reducing Unimodal Biases in Visual Question Answering](https://arxiv.org/abs/1906.10169), NeurIPS 2019 [[code]](https://github.com/cdancette/rubi.bootstrap.pytorch)

[GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering](https://arxiv.org/abs/1902.09506), CVPR 2019 [[code]](https://cs.stanford.edu/people/dorarad/gqa/)

[OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge](https://arxiv.org/abs/1906.00067), CVPR 2019 [[code]](http://okvqa.allenai.org/)

[MUREL: Multimodal Relational Reasoning for Visual Question Answering](https://arxiv.org/abs/1902.09487), CVPR 2019 [[code]](https://github.com/Cadene/murel.bootstrap.pytorch)

[Social-IQ: A Question Answering Benchmark for Artificial Social Intelligence](http://openaccess.thecvf.com/content_CVPR_2019/html/Zadeh_Social-IQ_A_Question_Answering_Benchmark_for_Artificial_Social_Intelligence_CVPR_2019_paper.html), CVPR 2019 [[code]](https://github.com/A2Zadeh/Social-IQ)

[Probabilistic Neural-symbolic Models for Interpretable Visual Question Answering](https://arxiv.org/abs/1902.07864), ICML 2019 [[code]](https://github.com/kdexd/probnmn-clevr)

[Learning to Count Objects in Natural Images for Visual Question Answering](https://arxiv.org/abs/1802.05766), ICLR 2018, [[code]](https://github.com/Cyanogenoid/vqa-counting)

[Overcoming Language Priors in Visual Question Answering with Adversarial Regularization](https://arxiv.org/abs/1810.03649), NeurIPS 2018

[Neural-Symbolic VQA: Disentangling Reasoning from Vision and Language Understanding](https://arxiv.org/abs/1810.02338), NeurIPS 2018 [[code]](https://github.com/kexinyi/ns-vqa)

[RecipeQA: A Challenge Dataset for Multimodal Comprehension of Cooking Recipes](https://arxiv.org/abs/1809.00812), EMNLP 2018 [[code]](https://hucvl.github.io/recipeqa/)

[TVQA: Localized, Compositional Video Question Answering](https://www.aclweb.org/anthology/D18-1167), EMNLP 2018 [[code]](https://github.com/jayleicn/TVQA)

[Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering](https://arxiv.org/abs/1707.07998), CVPR 2018 [[code]](https://github.com/facebookresearch/pythia)

[Don't Just Assume; Look and Answer: Overcoming Priors for Visual Question Answering](https://arxiv.org/abs/1712.00377), CVPR 2018 [[code]](https://github.com/AishwaryaAgrawal/GVQA)

[Stacked Latent Attention for Multimodal Reasoning](http://openaccess.thecvf.com/content_cvpr_2018/papers/Fan_Stacked_Latent_Attention_CVPR_2018_paper.pdf), CVPR 2018

[Learning to Reason: End-to-End Module Networks for Visual Question Answering](https://arxiv.org/abs/1704.05526), ICCV 2017 [[code]](https://github.com/ronghanghu/n2nmn)

[CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning](https://arxiv.org/abs/1612.06890), CVPR 2017 [[code]](https://github.com/facebookresearch/clevr-iep) [[dataset generation]](https://github.com/facebookresearch/clevr-dataset-gen)

[Are You Smarter Than A Sixth Grader? Textbook Question Answering for Multimodal Machine Comprehension](https://ieeexplore.ieee.org/document/8100054/), CVPR 2017 [[code]](http://vuchallenge.org/tqa.html)

[Multimodal Compact Bilinear Pooling for Visual Question Answering and Visual Grounding](https://arxiv.org/abs/1606.01847), EMNLP 2016 [[code]](https://github.com/akirafukui/vqa-mcb)

[MovieQA: Understanding Stories in Movies through Question-Answering](https://arxiv.org/abs/1512.02902), CVPR 2016 [[code]](http://movieqa.cs.toronto.edu/home/)

[VQA: Visual Question Answering](https://arxiv.org/abs/1505.00468), ICCV 2015 [[code]](https://visualqa.org/)

### Language Grounding in Vision

[Grounded Video Description](https://arxiv.org/abs/1812.06587), CVPR 2019

[Show, Control and Tell: A Framework for Generating Controllable and Grounded Captions](https://arxiv.org/abs/1811.10652), CVPR 2019

[Multilevel Language and Vision Integration for Text-to-Clip Retrieval](https://arxiv.org/abs/1804.05113), AAAI 2019 [[code]](https://github.com/VisionLearningGroup/Text-to-Clip_Retrieval)

[Binary Image Selection (BISON): Interpretable Evaluation of Visual Grounding](https://arxiv.org/abs/1901.06595), arXiv 2019 [[code]](https://github.com/facebookresearch/binary-image-selection)

[Finding “It”: Weakly-Supervised Reference-Aware Visual Grounding in Instructional Videos](http://openaccess.thecvf.com/content_cvpr_2018/papers/Huang_Finding_It_Weakly-Supervised_CVPR_2018_paper.pdf), CVPR 2018

[SCAN: Learning Hierarchical Compositional Visual Concepts](https://arxiv.org/abs/1707.03389), ICLR 2018

[Visual Coreference Resolution in Visual Dialog using Neural Module Networks](https://arxiv.org/abs/1809.01816), ECCV 2018 [[code]](https://github.com/facebookresearch/corefnmn)

[Gated-Attention Architectures for Task-Oriented Language Grounding](https://arxiv.org/abs/1706.07230), AAAI 2018

[Using Syntax to Ground Referring Expressions in Natural Images](https://arxiv.org/abs/1805.10547), AAAI 2018 [[code]](https://github.com/volkancirik/groundnet)

[Grounding language acquisition by training semantic parsers using captioned videos](https://cbmm.mit.edu/sites/default/files/publications/Ross-et-al_ACL2018_Grounding%20language%20acquisition%20by%20training%20semantic%20parsing%20using%20caption%20videos.pdf), ACL 2018

[Interpretable and Globally Optimal Prediction for Textual Grounding using Image Concepts](https://arxiv.org/abs/1803.11209), NeurIPS 2017

[Localizing Moments in Video with Natural Language](https://arxiv.org/abs/1708.01641), ICCV 2017

[What are you talking about? Text-to-Image Coreference](https://ieeexplore.ieee.org/abstract/document/6909850/), CVPR 2014

[Grounded Language Learning from Video Described with Sentences](https://www.aclweb.org/anthology/P13-1006), ACL 2013

[Grounded Compositional Semantics for Finding and Describing Images with Sentences](https://nlp.stanford.edu/~socherr/SocherKarpathyLeManningNg_TACL2013.pdf), TACL 2013

### Language Grouding in Navigation

[Vision-and-Dialog Navigation](https://arxiv.org/abs/1907.04957), arXiv 2019 [[code]](https://github.com/mmurray/cvdn)

[Hierarchical Decision Making by Generating and Following Natural Language Instructions](https://arxiv.org/abs/1906.00744), arXiv 2019 [[code]](https://www.minirts.net/)

[Stay on the Path: Instruction Fidelity in Vision-and-Language Navigation](https://arxiv.org/abs/1905.12255), ACL 2019

[Are You Looking? Grounding to Multiple Modalities in Vision-and-Language Navigation](https://arxiv.org/abs/1906.00347), ACL 2019

[Touchdown: Natural Language Navigation and Spatial Reasoning in Visual Street Environments](https://arxiv.org/abs/1811.12354), CVPR 2019 [[code]](https://github.com/lil-lab/touchdown)

[Tactical Rewind: Self-Correction via Backtracking in Vision-And-Language Navigation](https://arxiv.org/abs/1903.02547), CVPR 2019

[Reinforced Cross-Modal Matching and Self-Supervised Imitation Learning for Vision-Language Navigation](https://arxiv.org/abs/1811.10092), CVPR 2019

[The Regretful Navigation Agent for Vision-and-Language Navigation](https://arxiv.org/abs/1903.01602), CVPR 2019 [[code]](https://github.com/chihyaoma/regretful-agent)

[Tactical Rewind: Self-Correction via Backtracking in Vision-and-Language Navigation](https://arxiv.org/abs/1903.02547), CVPR 2019 [[code]](https://github.com/Kelym/FAST)

[Multi-modal Discriminative Model for Vision-and-Language Navigation](https://www.aclweb.org/anthology/W19-1605), NAACL SpLU-RoboNLP Workshop 2019

[Self-Monitoring Navigation Agent via Auxiliary Progress Estimation](https://arxiv.org/abs/1901.03035), ICLR 2019 [[code]](https://github.com/chihyaoma/selfmonitoring-agent)

[From Language to Goals: Inverse Reinforcement Learning for Vision-Based Instruction Following](https://arxiv.org/abs/1902.07742), ICLR 2019

[Read, Watch, and Move: Reinforcement Learning for Temporally Grounding Natural Language Descriptions in Videos](https://arxiv.org/abs/1901.06829), AAAI 2019

[Learning to Navigate Unseen Environments: Back Translation with Environmental Dropout](https://www.aclweb.org/anthology/N19-1268), NAACL 2019 [[code]](https://github.com/airsplay/R2R-EnvDrop)

[Attention Based Natural Language Grounding by Navigating Virtual Environment](https://arxiv.org/abs/1804.08454), IEEE WACV 2019

[Mapping Instructions to Actions in 3D Environments with Visual Goal Prediction](https://arxiv.org/abs/1809.00786), EMNLP 2018 [[code]](https://github.com/lil-lab/ciff)

[Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://arxiv.org/abs/1711.07280), CVPR 2018 [[code]](https://bringmeaspoon.org/)

[Embodied Question Answering](https://arxiv.org/abs/1711.11543), CVPR 2018 [[code]](https://embodiedqa.org/)

[Look Before You Leap: Bridging Model-Free and Model-Based Reinforcement Learning for Planned-Ahead Vision-and-Language Navigation](https://arxiv.org/abs/1803.07729), ECCV 2018


### Multimodal Machine Translation

[Visual Agreement Regularized Training for Multi-Modal Machine Translation](https://arxiv.org/abs/1912.12014), AAAI 2020

[VATEX: A Large-Scale, High-Quality Multilingual Dataset for Video-and-Language Research](https://arxiv.org/abs/1904.03493), ICCV 2019 [[code]](http://vatex.org/main/index.html)

[Latent Variable Model for Multi-modal Translation](https://arxiv.org/pdf/1811.00357), ACL 2019

[Distilling Translations with Visual Awareness](https://arxiv.org/pdf/1906.07701), ACL 2019

[Probing the Need for Visual Context in Multimodal Machine Translation](https://www.aclweb.org/anthology/N19-1422), NAACL 2019

[Emergent Translation in Multi-Agent Communication](https://openreview.net/pdf?id=H1vEXaxA-), ICLR 2018

[Zero-Resource Neural Machine Translation with Multi-Agent Communication Game](https://arxiv.org/pdf/1802.03116), AAAI 2018

[Learning Translations via Images with a Massively Multilingual Image Dataset](http://aclweb.org/anthology/P18-1239), ACL 2018

[A Visual Attention Grounding Neural Model for Multimodal Machine Translation](http://aclweb.org/anthology/D18-1400), EMNLP 2018

[Adversarial Evaluation of Multimodal Machine Translation](http://aclweb.org/anthology/D18-1329), EMNLP 2018

[Doubly-Attentive Decoder for Multi-modal Neural Machine Translation](http://aclweb.org/anthology/P17-1175), ACL 2017

[An empirical study on the effectiveness of images in Multimodal Neural Machine Translation](http://aclweb.org/anthology/D17-1095), EMNLP 2017

[Incorporating Global Visual Features into Attention-based Neural Machine Translation](http://aclweb.org/anthology/D17-1105), EMNLP 2017

[Multimodal Pivots for Image Caption Translation](http://aclweb.org/anthology/P16-1227), ACL 2016

[Multi30K: Multilingual English-German Image Descriptions](https://aclweb.org/anthology/W16-3210.pdf), ACL Workshop on Language and Vision 2016

[Does Multimodality Help Human and Machine for Translation and Image Captioning?](http://www.statmt.org/wmt16/pdf/W16-2358.pdf), ACL WMT 2016

### Multi-agent Communication

[Emergence of Compositional Language with Deep Generational Transmission](https://arxiv.org/abs/1904.09067), ICML 2019

[On the Pitfalls of Measuring Emergent Communication](https://arxiv.org/abs/1903.05168), AAMAS 2019 [[code]](https://github.com/facebookresearch/measuring-emergent-comm)

[Emergent Translation in Multi-Agent Communication](https://arxiv.org/abs/1710.06922), ICLR 2018 [[code]](https://github.com/facebookresearch/translagent)

[Emergent Communication in a Multi-Modal, Multi-Step Referential Game](https://openreview.net/pdf?id=rJGZq6g0-), ICLR 2018 [[code]](https://github.com/nyu-dl/MultimodalGame)

[Emergence of Linguistic Communication From Referential Games with Symbolic and Pixel Input](https://openreview.net/pdf?id=HJGv1Z-AW), ICLR 2018

[Emergent Communication through Negotiation](https://openreview.net/pdf?id=Hk6WhagRW), ICLR 2018 [[code]](https://github.com/ASAPPinc/emergent_comms_negotiation)

[Emergence of Grounded Compositional Language in Multi-Agent Populations](https://arxiv.org/abs/1703.04908), AAAI 2018

[Emergence of Language with Multi-agent Games: Learning to Communicate with Sequences of Symbols](https://arxiv.org/abs/1705.11192), NeurIPS 2017

[Natural Language Does Not Emerge 'Naturally' in Multi-Agent Dialog](https://arxiv.org/abs/1706.08502), EMNLP 2017 [[code1]](https://github.com/batra-mlp-lab/lang-emerge) [[code2]](https://github.com/kdexd/lang-emerge-parlai)

[Learning Cooperative Visual Dialog Agents with Deep Reinforcement Learning](https://arxiv.org/abs/1703.06585), ICCV 2017 [code](https://github.com/batra-mlp-lab/visdial-rl)

[Multi-agent Cooperation and the Emergence of (natural) Language](https://arxiv.org/abs/1612.07182), ICLR 2017

[Learning to Communicate with Deep Multi-agent Reinforcement Learning](https://arxiv.org/abs/1605.06676), NIPS 2016.

[Learning multiagent communication with backpropagation](http://papers.nips.cc/paper/6398-learning-multiagent-communication-with-backpropagation.pdf), NIPS 2016.

[The Emergence of Compositional Structures in Perceptually Grounded Language Games](https://www.cs.utexas.edu/~kuipers/readings/Vogt-aij-05.pdf), AI 2005

### Commonsense Reasoning

[Heterogeneous Graph Learning for Visual Commonsense Reasoning](https://arxiv.org/abs/1910.11475), NeurIPS 2019

[SocialIQA: Commonsense Reasoning about Social Interactions](https://arxiv.org/abs/1904.09728), arXiv 2019

[From Recognition to Cognition: Visual Commonsense Reasoning](https://arxiv.org/abs/1811.10830), CVPR 2019 [[code]](https://visualcommonsense.com/)

[CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge](https://arxiv.org/abs/1811.00937), NAACL 2019

### Multimodal Reinforcement Learning

[Language as an Abstraction for Hierarchical Deep Reinforcement Learning](https://arxiv.org/abs/1906.07343), NeurIPS 2019

[Hierarchical Decision Making by Generating and Following Natural Language Instructions](https://arxiv.org/abs/1906.00744), NeurIPS 2019 [[code]](https://github.com/facebookresearch/minirts)

[Habitat: A Platform for Embodied AI Research](https://arxiv.org/abs/1904.01201), ICCV 2019 [[code]](https://aihabitat.org/)

[Embodied Multimodal Multitask Learning](https://arxiv.org/abs/1902.01385), arXiv 2019

[Multimodal Hierarchical Reinforcement Learning Policy for Task-Oriented Visual Dialog](https://arxiv.org/abs/1805.03257), SIGDIAL 2018

[Mapping Instructions and Visual Observations to Actions with Reinforcement Learning](https://www.cs.cornell.edu/~dkm/papers/mla-emnlp.2017.pdf), EMNLP 2017

[Reinforcement Learning for Mapping Instructions to Actions](https://people.csail.mit.edu/regina/my_papers/RL.pdf), ACL 2009

### Multimodal Dialog

[MELD: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversations](https://arxiv.org/abs/1810.02508), ACL 2019 [[code]](http://affective-meld.github.io/)

[CLEVR-Dialog: A Diagnostic Dataset for Multi-Round Reasoning in Visual Dialog](https://www.aclweb.org/anthology/N19-1058), NAACL 2019 [[code]](https://github.com/satwikkottur/clevr-dialog)

[Talk the Walk: Navigating New York City through Grounded Dialogue](https://arxiv.org/abs/1807.03367), arXiv 2018

[Dialog-based Interactive Image Retrieval](https://arxiv.org/abs/1805.00145), NeurIPS 2018 [[code]](https://github.com/XiaoxiaoGuo/fashion-retrieval)

[Towards Building Large Scale Multimodal Domain-Aware Conversation Systems](https://arxiv.org/abs/1704.00200), arXiv 2017 [[code]](https://amritasaha1812.github.io/MMD/)

[Visual Dialog](https://arxiv.org/abs/1611.08669), CVPR 2017 [[code]](https://github.com/batra-mlp-lab/visdial)

### Language and Audio

[Lattice Transformer for Speech Translation](https://arxiv.org/abs/1906.05551), ACL 2019

[Exploring Phoneme-Level Speech Representations for End-to-End Speech Translation](https://arxiv.org/abs/1906.01199), ACL 2019

[Audio Caption: Listen and Tell](https://arxiv.org/abs/1902.09254), ICASSP 2019

[Audio-Linguistic Embeddings for Spoken Sentences](https://arxiv.org/abs/1902.07817), ICASSP 2019

[From Semi-supervised to Almost-unsupervised Speech Recognition with Very-low Resource by Jointly Learning Phonetic Structures from Audio and Text Embeddings](https://arxiv.org/abs/1904.05078), arXiv 2019

[From Audio to Semantics: Approaches To End-to-end Spoken Language Understanding](https://arxiv.org/abs/1809.09190), arXiv 2018

[Natural TTS Synthesis by Conditioning Wavenet on Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884), ICASSP 2018 [[code]](https://github.com/NVIDIA/tacotron2)

[Deep Voice 3: Scaling Text-to-Speech with Convolutional Sequence Learning](https://arxiv.org/abs/1710.07654), ICLR 2018

[Deep Voice 2: Multi-Speaker Neural Text-to-Speech](https://arxiv.org/abs/1705.08947), NeurIPS 2017

[Deep Voice: Real-time Neural Text-to-Speech](https://arxiv.org/abs/1702.07825), ICML 2017

[Text-to-Speech Synthesis](https://dl.acm.org/citation.cfm?id=1592988), 2009

### Audio and Visual

[Learning Individual Styles of Conversational Gesture](https://arxiv.org/abs/1906.04160), CVPR 2019 [[code]](http://people.eecs.berkeley.edu/~shiry/speech2gesture)

[Capture, Learning, and Synthesis of 3D Speaking Styles](https://ps.is.tuebingen.mpg.de/uploads_file/attachment/attachment/510/paper_final.pdf), CVPR 2019 [[code]](https://github.com/TimoBolkart/voca)

[Disjoint Mapping Network for Cross-modal Matching of Voices and Faces](https://arxiv.org/abs/1807.04836), ICLR 2019

[Wav2Pix: Speech-conditioned Face Generation using Generative Adversarial Networks](https://arxiv.org/abs/1903.10195), ICASSP 2019 [[code]](https://imatge-upc.github.io/wav2pix/)

[Jointly Discovering Visual Objects and Spoken Words from Raw Sensory Input](https://arxiv.org/abs/1804.01452), ECCV 2018 [[code]](https://github.com/LiqunChen0606/Jointly-Discovering-Visual-Objects-and-Spoken-Words)

[Seeing Voices and Hearing Faces: Cross-modal Biometric Matching](https://arxiv.org/abs/1804.00326), CVPR 2018 [[code]](https://github.com/a-nagrani/SVHF-Net)

[Learning to Separate Object Sounds by Watching Unlabeled Video](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w49/Gao_Learning_to_Separate_CVPR_2018_paper.pdf), CVPR 2018

[Deep Audio-Visual Speech Recognition](https://arxiv.org/abs/1809.02108), IEEE TPAMI 2018

[Look, Listen and Learn](http://openaccess.thecvf.com/content_ICCV_2017/papers/Arandjelovic_Look_Listen_and_ICCV_2017_paper.pdf), ICCV 2017

[Unsupervised Learning of Spoken Language with Visual Context](https://papers.nips.cc/paper/6186-unsupervised-learning-of-spoken-language-with-visual-context.pdf), NeurIPS 2016

[SoundNet: Learning Sound Representations from Unlabeled Video](https://arxiv.org/abs/1610.09001), NeurIPS 2016 [[code]](http://projects.csail.mit.edu/soundnet/)

### Media Description

[Towards Unsupervised Image Captioning with Shared Multimodal Embeddings](https://arxiv.org/abs/1908.09317), ICCV 2019

[Video Relationship Reasoning using Gated Spatio-Temporal Energy Graph](https://arxiv.org/abs/1903.10547), CVPR 2019 [[code]](https://github.com/yaohungt/GSTEG_CVPR_2019)

[Joint Event Detection and Description in Continuous Video Streams](https://arxiv.org/abs/1802.10250), WACVW 2019

[Learning to Compose and Reason with Language Tree Structures for Visual Grounding](https://arxiv.org/abs/1906.01784), TPAMI 2019

[Neural Baby Talk](https://arxiv.org/abs/1803.09845), CVPR 2018 [[code]](https://github.com/jiasenlu/NeuralBabyTalk)

[Grounding Referring Expressions in Images by Variational Context](https://arxiv.org/abs/1712.01892), CVPR 2018

[Video Captioning via Hierarchical Reinforcement Learning](https://arxiv.org/abs/1711.11135), CVPR 2018

[Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos](https://arxiv.org/abs/1804.09626), CVPR 2018 [[code]](https://allenai.org/plato/charades/) 

[Neural Motifs: Scene Graph Parsing with Global Context](https://arxiv.org/abs/1711.06640), CVPR 2018 [[code]](http://github.com/rowanz/neural-motifs)

[No Metrics Are Perfect: Adversarial Reward Learning for Visual Storytelling](https://arxiv.org/abs/1804.09160), ACL 2018

[Generating Descriptions with Grounded and Co-Referenced People](https://arxiv.org/abs/1704.01518), CVPR 2017

[DenseCap: Fully Convolutional Localization Networks for Dense Captioning](https://cs.stanford.edu/people/karpathy/densecap/), CVPR 2016

[Review Networks for Caption Generation](https://arxiv.org/abs/1605.07912), NeurIPS 2016 [[code]](https://github.com/kimiyoung/review_net)

[Hollywood in Homes: Crowdsourcing Data Collection for Activity Understanding](https://arxiv.org/abs/1604.01753), ECCV 2016 [[code]](https://allenai.org/plato/charades/)

[Show and Tell: Lessons learned from the 2015 MSCOCO Image Captioning Challenge](https://arxiv.org/abs/1609.06647), TPAMI 2016 [[code]](https://github.com/tensorflow/models/tree/master/research/im2txt)

[Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/abs/1502.03044), ICML 2015 [[code]](https://github.com/kelvinxu/arctic-captions)

[Deep Visual-Semantic Alignments for Generating Image Descriptions](https://arxiv.org/abs/1412.2306v2), CVPR 2015 [[code]](https://github.com/karpathy/neuraltalk2)

[Show and Tell: A Neural Image Caption Generator](https://arxiv.org/abs/1411.4555), CVPR 2015 [[code]](https://github.com/karpathy/neuraltalk2)

[A Dataset for Movie Description](https://arxiv.org/abs/1501.02530), CVPR 2015 [[code]](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/vision-and-language/mpii-movie-description-dataset/)

[What’s Cookin’? Interpreting Cooking Videos using Text, Speech and Vision](https://arxiv.org/abs/1503.01558), NAACL 2015 [[code]](https://github.com/malmaud/whats_cookin)

[Microsoft COCO: Common Objects in Context](https://arxiv.org/abs/1405.0312), ECCV 2014 [[code]](http://cocodataset.org/#home)

### Video Generation from Text

[Image Generation from Scene Graphs](https://arxiv.org/abs/1804.01622), CVPR 2018

[Learning to Color from Language](https://arxiv.org/abs/1804.06026), NAACL 2018

[Generative Adversarial Text to Image Synthesis](https://arxiv.org/abs/1605.05396), ICML 2016

### Affect Recognition and Multimodal Language

[Towards Multimodal Sarcasm Detection (An Obviously_Perfect Paper)](https://arxiv.org/abs/1906.01815), ACL 2019 [[code]](https://github.com/soujanyaporia/MUStARD)

[Multimodal Language Analysis with Recurrent Multistage Fusion](https://arxiv.org/abs/1808.03920), EMNLP 2018

[Multimodal Language Analysis in the Wild: CMU-MOSEI Dataset and Interpretable Dynamic Fusion Graph](http://aclweb.org/anthology/P18-1208), ACL 2018 [[code]](https://github.com/A2Zadeh/CMU-MultimodalSDK)

[Multi-attention Recurrent Network for Human Communication Comprehension](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewFile/17390/16123), AAAI 2018 [[code]](https://github.com/A2Zadeh/CMU-MultimodalSDK)

[AMHUSE - A Multimodal dataset for HUmor SEnsing](https://dl.acm.org/citation.cfm?id=3136806), ICMI 2017 [[code]](http://amhuse.phuselab.di.unimi.it/)

[Decoding Children’s Social Behavior](http://www.cbi.gatech.edu/mmdb/docs/mmdb_paper.pdf), CVPR 2013 [[code]](http://www.cbi.gatech.edu/mmdb/)

[Collecting Large, Richly Annotated Facial-Expression Databases from Movies](http://users.cecs.anu.edu.au/%7Eadhall/Dhall_Goecke_Lucey_Gedeon_M_2012.pdf), IEEE Multimedia 2012 [[code]](https://cs.anu.edu.au/few/AFEW.html)

[The Interactive Emotional Dyadic Motion Capture (IEMOCAP) Database](https://sail.usc.edu/iemocap/Busso_2008_iemocap.pdf), 2008 [[code]](https://sail.usc.edu/iemocap/)

### Healthcare

[Leveraging Medical Visual Question Answering with Supporting Facts](https://arxiv.org/abs/1905.12008), arXiv 2019

[Unsupervised Multimodal Representation Learning across Medical Images and Reports](https://arxiv.org/abs/1811.08615), ML4H 2018

[Multimodal Medical Image Retrieval based on Latent Topic Modeling](https://aiforsocialgood.github.io/2018/pdfs/track1/75_aisg_neurips2018.pdf), ML4H 2018

[Improving Hospital Mortality Prediction with Medical Named Entities and Multimodal Learning](https://arxiv.org/abs/1811.12276), ML4H 2018

[Knowledge-driven Generative Subspaces for Modeling Multi-view Dependencies in Medical Data](https://arxiv.org/abs/1812.00509), ML4H 2018

[Multimodal Depression Detection: Fusion Analysis of Paralinguistic, Head Pose and Eye Gaze Behaviors](https://ieeexplore.ieee.org/document/7763752), TAC 2018

[Learning the Joint Representation of Heterogeneous Temporal Events for Clinical Endpoint Prediction](https://arxiv.org/abs/1803.04837), AAAI 2018

[Understanding Coagulopathy using Multi-view Data in the Presence of Sub-Cohorts: A Hierarchical Subspace Approach](http://mucmd.org/CameraReadySubmissions/67%5CCameraReadySubmission%5Cunderstanding-coagulopathy-multi%20(6).pdf), MLHC 2017

[Machine Learning in Multimodal Medical Imaging](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5357511/), 2017

[Cross-modal Recurrent Models for Weight Objective Prediction from Multimodal Time-series Data](https://arxiv.org/abs/1709.08073), ML4H 2017

[SimSensei Kiosk: A Virtual Human Interviewer for Healthcare Decision Support](https://dl.acm.org/citation.cfm?id=2617388.2617415), AAMAS 2014

[Dyadic Behavior Analysis in Depression Severity Assessment Interviews](https://dl.acm.org/citation.cfm?doid=2663204.2663238), ICMI 2014

[Audiovisual Behavior Descriptors for Depression Assessment](https://dl.acm.org/citation.cfm?doid=2522848.2522886), ICMI 2013

### Robotics

[See, Feel, Act: Hierarchical Learning for Complex Manipulation Skills with Multi-sensory Fusion](https://robotics.sciencemag.org/content/4/26/eaav3123), Science Robotics 2019 

[Early Fusion for Goal Directed Robotic Vision](https://arxiv.org/abs/1811.08824), IROS 2019

[Simultaneously Learning Vision and Feature-based Control Policies for Real-world Ball-in-a-Cup](https://arxiv.org/abs/1902.04706), RSS 2019

[Probabilistic Multimodal Modeling for Human-Robot Interaction Tasks](http://www.roboticsproceedings.org/rss15/p47.pdf), RSS 2019

[Making Sense of Vision and Touch: Self-Supervised Learning of Multimodal Representations for Contact-Rich Tasks](https://arxiv.org/abs/1810.10191), ICRA 2019

[Evolving Multimodal Robot Behavior via Many Stepping Stones with the Combinatorial Multi-Objective Evolutionary Algorithm
](https://arxiv.org/abs/1807.03392), arXiv 2018

[Multimodal Probabilistic Model-Based Planning for Human-Robot Interaction](https://arxiv.org/abs/1710.09483), arXiv 2017 

[Perching and Vertical Climbing: Design of a Multimodal Robot](https://ieeexplore.ieee.org/document/6907472), ICRA 2014

[Multi-Modal Scene Understanding for Robotic Grasping](http://kth.diva-portal.org/smash/get/diva2:459199/FULLTEXT01), 2011

[Strategies for Multi-Modal Scene Exploration](https://am.is.tuebingen.mpg.de/uploads_file/attachment/attachment/307/2010_IROS_bjbk_camred.pdf), IROS 2010




## Papers With Code

  - [Multimodal Related --- from Papers With Code](https://paperswithcode.com/search?q=multimodal)


## Research Team
  - [CMU --- MultiComp Lab](http://multicomp.cs.cmu.edu/)
  - [MIT --- SYNTHETIC INTELLIGENCE LABORATORY](http://synthintel.org/)
  - [NTU --- SenticNet Team](http://sentic.net/)
  - [SenticNet GitHub](https://github.com/SenticNet)
  - [MultiMT](https://multimt.github.io/)
  

## Related Datasets

  - [CMU MultimodalSDK --- Affect Recognition and Multimodal Language](https://github.com/A2Zadeh/CMU-MultimodalSDK)
  - [AMHUSE --- Affect Recognition and Multimodal Language](http://amhuse.phuselab.di.unimi.it/)
  - [Multi30k Dataset --- Multimodal Machine Translation](https://github.com/multi30k/dataset)
  - [VATEX --- Multimodal Machine Translation](http://vatex.org/main/index.html)
  - [MELD --- Multimodal Dialog](https://affective-meld.github.io/)
  - [CLEVR-Dialog --- Multimodal Dialog](https://github.com/satwikkottur/clevr-dialog)
  - [Charades-Ego --- Media Description](https://allenai.org/plato/charades/)
  - [MPII --- Media Description](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/vision-and-language/mpii-movie-description-dataset/)
  - [RecipeQA --- Language and Visual QA](https://hucvl.github.io/recipeqa/)
  - [GQA --- Language and Visual QA](https://cs.stanford.edu/people/dorarad/gqa/)
  - [CLEVR --- Language and Visual QA](https://github.com/facebookresearch/clevr-dataset-gen)
