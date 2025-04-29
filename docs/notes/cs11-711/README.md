<div width="100%" height="100%" align="center">
  
<h1 align="center">
  <p align="center">Advanced NLP</p>
  <a href="https://phontron.com/class/anlp2022/schedule.html">
  </a>
</h1>

<b>강의 주제: Natural Language Processing</b></br>
Instructor : Graham Neubig(Associate Professor, Carnegie Mellon University),<br/> Robert Frederking(Associate Dean for Ph.D. Programs, CMU Language Technologies Institute)</br>
[[schedule, codes](https://phontron.com/class/anlp2022/schedule.html)] | [[youtube](https://youtube.com/playlist?list=PL8PYTP1V4I8D0UkqW2fEhgLrnlDW9QK7z&si=3vCrtwi-s7LRntEl)]</b>

</div>

## :bulb: 목표 <!-- {docsify-ignore-all} -->

- **자연어 처리의 개념을 이해하고, 최신 기법을 파악한다.**

  > syntactic, semantic, discourse analysis 등 자연어 처리의 기초적인 개념을 이해하고, 관련된 최신 기법을 파악한다.


</br>

## 🚩 정리한 문서 목록

### 📖 Basics of Natural Language Processing

- [Generative, Discriminative Text Classfication](notes/cs11-711/lec02.md)

  > Generative Text Classification: Count-based Unigram Models, Bag-of-Words Generative Classifier(BoW) / Discriminative Text Classification: BOW Discriminative Classifier

  > Evaluation: accuracy, precision, recall, F1 score, statistical testing

### 📐 Modeling

- [Methods of Generation, Evaluation](notes/cs11-711/lec05.md)

  > Ancestral Sampling, Greedy Search, Beam Search

  > Evaluation(Human Evaluation, BLEU Score, Embedding-based Metrics, Perplexity), Meta-Evaluation, Difficulties(bad model + big beam), Alternative Methods(worse search for better outputs, minimize Bayes risk, Train Better Models)

- [Attention, Transformer](notes/cs11-711/lec06.md)

  > Attention, Attention Score Functions(MLP, Bilinear, Dot Product, Scaled Dot Product), Self Attention, Multi-Head Attention

  > Transformer: Transformer Architecture, Attention Tricks, Training Tricks, Masked Multi-Head Attention

  > Extensions to Attention: Incorporating Markov Properties, Hard Attention, Monotonic Attention, Coverage, Bidirectional Training, Alignment Attention

### 📙 Representation

- [Pre-training](notes/cs11-711/lec07-summary01.md)

  > Multi-task Learning: Standard, Pre-train and Fine-tune, Prompting

  > Pre-trained LMs: BERT, RoBERTa, ELECTRA, XLNet, DeBERTa

- [Pre-training Design Choices](notes/cs11-711/lec07-summary02.md)

  > Auto-regressive LMs for Generation/Prompting: GPT-2, GPT-3, PaLM, OPT, BLOOM

  > Pre-training Pros and Cons, Design Choices(Data, Transform, Representation, Output), Scaling Law

- [Multi-task, Multi-domain Learning](notes/cs11-711/lec08.md)

  > domain, domain shift(covariate shift, concept shift), domain adaptation

  > parameter sharing(domain tag, adapter, regularization-based), task weighting(uniform, proportional, temperature-based, uncertainty-based)

- [Prompt Engineering](notes/cs11-711/lec09-summary01.md)

  > Types of Prompts(filled, answered, prefix, cloze), Prompt Workflows, Pre-trained LM(MASS, BART, mBART, UNiLM, T5)

  > Prompt Engineering: Cloze, Prefix, Hand-crafted, Automated(Prompt Mining, Prompt Parapharasing, Gradient-based Search, Prefix/Prompt Tuning)

</br>

## :mag: Schedule

### Intro 1 - Overview of NLP (8/30/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-01-intro.pdf) | [video](https://youtu.be/watch?v=rVht4eK3EZw) ]

### Intro 2 - Text Classification (9/1/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-02-classification.pdf) | [video](https://youtu.be/boPpVexvDAI) ]

### Intro 3 - Language Modeling and NN Basics (9/6/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-03-lm.pdf) | [video](https://youtu.be/pifqfW2ApI4) ]

---

### Modeling 1 - Recurrent Networks (9/8/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-04-seqmod.pdf) | [video](https://youtu.be/N_Ip2zhIGSk) ]

### Modeling 2 - Conditioned Generation (9/13/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-05-condlm.pdf) | [video](https://youtu.be/FazNgBWvkkk) ]

### Modeling 3 - Attention (9/15/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-06-attention.pdf) | [video](https://youtu.be/0PPzD4mxpuM) ]

---

### Representation 1 - Pre-training Methods (9/20/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-07-pretraining.pdf) | [video](https://youtu.be/27LkyrxaUK4) ]

### Representation 2 - Multi-task, Multi-domain, and Multi-lingual Learning (9/22/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-08-multitask.pdf) | [video](https://youtu.be/BXPyIENMs4Y) ]

### Representation 3 - Prompting (9/27/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-09-prompting.pdf) | [video](https://youtu.be/5ef83Wljm-M) ]

### Guest Lecture - How to use pre-trained models?

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-10-raghunathan.pdf) | [video](https://youtu.be/t2J37IqSTww) ]

---

### Experimentation 1 - Experimental Design (10/04/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-11-experimentation.pdf) | [video](https://youtu.be/jb46q2ltFcs) ]

### Experimentation 2 - Interpreting and Debugging NLP Models (10/11/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-12-interpretation.pdf) | [video](https://youtu.be/4AgYVaAfHG4) ]

---

### Applications 1 - Text-based QA (10/13/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-13-textbasedqa.pdf) | [video](https://youtu.be/j_N4Xmv-mlA) ]

### Applications 2 - Bias and Fairness (10/25/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-14-bias.pdf) | [video](https://youtu.be/9n3GikALDPs) ]

### Applications 3 - Dialog (10/27/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-15-dialog.pdf) | [video](https://youtu.be/s9opjgRuj2Q) ]

### Applications 4 - Information Extraction and Knowledge-based QA (11/1/2022)

[ [slides](https://phontron.com/class/anlp2021/assets/slides/anlp-20-kb.pdf) | [video](https://youtu.be/18CTdWcJGL0) ]

---

### Analysis 1 - Word Segmentation and Morphology (11/3/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-17-wordseg-morphology.pdf) | [video](https://youtu.be/n7xa7gkmN2s) ]

### Analysis 2 - Syntax 1 (11/8/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-18-syntax1.pdf) | [video](https://youtu.be/DZxwGVDFmf0) ]

### Analysis 3 - Syntax 2 and Semantics 1 (11/10/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-19-syntax2semantics1.pdf) | [video](https://youtu.be/MkvVM8fidUQ) ]

### Analysis 4 - Semantics 2 and Discourse (11/15/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-20-semantics2discourse.pdf) | [video](https://youtu.be/lzS915PpHSw) ]

---

### Learning 1 - Modeling Long Sequences (11/17/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-21-document.pdf) | [video](https://youtu.be/lzS915PpHSw) ]

### Learning 2 - Structured Learning Algorithms (11/22/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-22-structure.pdf) | [video](https://youtu.be/HwgJN6WMk1g) ]

### Learning 3 - Latent Variable Models (11/29/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-23-latent.pdf) | [video](https://youtu.be/RnIu1YL7ffY) ]

### Learning 4 - Adversarial Methods for Text (12/1/2022)

[ [slides](https://phontron.com/class/anlp2022/assets/slides/anlp-24-adversarial.pdf) | [video](https://youtu.be/ySQ6hMosxdw) ]

---