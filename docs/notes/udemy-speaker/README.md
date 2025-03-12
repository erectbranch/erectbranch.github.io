<div width="100%" height="100%" align="center">
  
<h1 align="center">
  <p align="center">Speaker Recognition</p>
  <a href="https://www.udemy.com/course/speaker-recognition/">
  </a>
</h1>
  
  
<b>강의 주제: Audio processing, Feature extraction, Speaker recognition</b></br>
Instructor : Quan Wang(Software Engineer, Google)</br>
[[course](https://www.udemy.com/course/speaker-recognition/)]</b>

</div>

## :bulb: 목표

- **화자 인식 기초 개념 공부**

  > 화자 인식 기초 개념을 공부한다.

- **음성 처리 기법을 파악**

  > 음향학과 음성 데이터 처리 기법을 파악한다.

</br>

## 🚩 정리한 문서 목록

### 📖 Basics of Audio Processing

- [History of Voice Identity Techniques](notes/udemy-speaker/Section02.md)

  > pattern matching, per-segment matching, Gaussian Mixture Models, factor analysis, deep learning

- [Acoustics, Frequency, Sound](notes/udemy-speaker/Section03-summary01.md)

  > utterance, generation of speech(vocal folds, glottis, vocal tract), human hearing(ear canal, ossicles, cochlea)

  > sine wave, Fourier analysis, spectrum, frequency, fundamental frequency, pitch, formant

  > intensity, loudness

  > nonlinearity of frequency(Bark scale, Mel scale, Equivalent Rectangular Bandwidth, Cochlear frequency-position function scale), nonlinearity of intensity

- [Analog-to-digital](notes/udemy-speaker/Section03-summary02.md)

  > Analog-to-Digital Converter(ADC): sampling(sampling rate, Nyquist frequency), quantization

  > audio coding: linear PCM, non-linear PCM(μ-law, A-law), Adaptive PCM, Differential PCM, Linear Predictive Coding(LPC), frequency domain coding(Sub-Band Coding, Adaptive Transform Coding)

  > audio formats: WAV, SPHERE, FLAC, MP3, AAC, OPUS, Speex, WMA

  > sound processing programs: SoX, FFmpeg

- [Short-time analysis, Post-processing](notes/udemy-speaker/Section04-summary01.md)

  > short-time analysis: framing(frame size, frame step), window function(Gaussian, Hanning, Hamming)

  > Frame post-processing: frame stacking, frame subsampling, frame normalization

- [Time domain feature, Frequency domain feature](notes/udemy-speaker/Section04-summary02.md)

  > Time domain features: short-time enearge, short-time average magnitude, short-time zero cross rate, short-time auto-correlation, short-time average magnitude difference fuction, short-time linear predictive coding

  > Frequency domain features: Discrete Fourier Transform(DFT), Fast Fourier Transform(FFT), Short-Time Fourier Transform(STFT), Spectrogram, Cepstrum

  > Commonly used features: Perceptual Linear Prediction(PLP), Mel-Frequency Cepstral Coefficients(MFCC), Power-Normalized Cepstral Coefficient(PNCC), Log-mel Filterbank Energies(LFBE)

### ⚙️ Fundamentals of Speaker Recognition

- [Speaker Verification, Speaker Identification](notes/udemy-speaker/Section05-summary01.md)

  > speech vs speaker recognition, speaker verification, speaker identification

  > Textual content(Text-Dependent, Text-Independent, Text-Prompted)

  > system workflow: training(speaker encoder, embedding), enrollment(aggregation), recognition

- [Similarity Score, Evaluation](notes/udemy-speaker/Section05-summary02.md)

  > Thresholding, Similarity Score(Cosine Similarity, Euclidean Distance, Model-based similarity score), Score Triaging

  > Evaluation: Pair-based Evaluation, Set-based Evaluation

  > False Accept Rate(FAR), False Reject Rate(FRR), ROC curve(Area Under Curve(AUC)), DET curve, Equal Error Rate(EER), Minimum Detection Cost Function(minDCF) 

### 📻 Early Speaker Recognition Approaches

- [Gaussian Mixture Models](notes/udemy-speaker/Section06-summary01.md)

  > Gaussian Distribution, Multivariate Gaussian Distribution
  
  > Gaussian Mixture Model(GMM): sharing covariance matrix/simpler covariance matrix(diagonal covariance matrix), parameter estimation(Expectation-Maximization algorithm)

  > Universal Background Model(UBM), Bayesian Adaptation, GMM-UBM, supervector

  > Support Vector Machine(SVM): linear SVM, linear SVM with soft margin, non-linear SVM(kernel trick)

- [Joint Factor Analysis, i-vector](notes/udemy-speaker/Section06-summary02.md)

  > Factor Analysis: observed/unobserved, correlated/uncorrelated variables, common factor, unique factor, loading matrix

  > Joint Factor Analysis, JFA-SVM, i-vector(channel compensation)

### 🧠 Speaker Recognition with Deep Learning

- [Indirect/direct use of Neural Network, Inference](notes/udemy-speaker/Section08-summary01.md)

  > Indirect use(Tandem deep features, DNN i-vector, j-vector), Direct use(neural network encoder, embeddings, loss function, optimizer)

  > Inference: Frame-independent, Fixed window, Full sequence(RNN, attention), Sliding window(RNN, attention)

</br>

## :mag: Schedule

### Lecture 1: Introduction

### Lecture 2: The History of Voice Identity Techniques

### Lecture 3: Fundamental of Audio Processing

### Lecture 4: Acoustic Feature Extraction

### Lecture 5: Fundamentals of Speaker Recognition

### Lecture 6: Early Spearker Recognition Approaches

### Lecture 7: Deep Learning Basics

### Lecture 8: Speaker Recognition with Deep Learning

### Lecture 9: Data Processing in Speaker Recognition

### Lecture 10: Data Processing in Speaker Recognition

### Lecture 11: Final Project [[github](https://docsify-this.net?basePath=https://raw.githubusercontent.com/wq2012/SpeakerRecognitionFromScratch&homepage=README.md)] 