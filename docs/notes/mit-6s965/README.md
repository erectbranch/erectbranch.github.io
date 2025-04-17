<div width="100%" height="100%" align="center">
  
<h1 align="center">
  <p align="center">TinyML and Efficient Deep Learning Computing</p>
</h1>
  
  
<b>강의 주제: TinyML and Efficient Deep Learning Computing</b>
<br>
Instructor : Song Han(Associate Professor, MIT EECS)

</div>

## 🚩 정리한 문서 목록

### 📖 Basics of Deep Learning

- [Basic Terminologies, Shape of Tensors](notes/mit-6s965/lec02-summary01.md)

  > Synapse(weight), Neuron(activation), Cell body

  > Fully-Connected layer, Convolution layer(padding, stride, receptive field, grouped convolution), Pooling layer

- [Efficiency Metrics](notes/mit-6s965/lec02-summary02.md)

  > Metrics(latency, storage, energy)

  > Memory-Related(\#parameters, model size, \#activations), Computation(MACs, FLOP)

### 📔 Efficient Inference

- [Pruning Granularity, Pruning Critertion](notes/mit-6s965/lec03.md)

  > Unstructured/Structured pruning(Fine-grained/Pattern-based/Vector-level/Kernel-level/Channel-level)
  
  > Pruning Criterion: Magnitude(L1-norm, L2-norm), Sensitivity and Saliency(SNIP), Loss Change(First-Order, Second-Order Taylor Expansion)
  
  > Data-Aware Pruning Criterion: Average Percentage of Zero(APoZ), Reconstruction Error, Entropy

- [Automatic Pruning, Lottery Ticket Hypothesis](notes/mit-6s965/lec04-summary01.md)

  > Finding Pruning Ratio: Reinforcement Learning based, Rule based, Regularization based, Meta-Learning based 

  > Lottery Ticket Hypothesis(Winning Ticket, Iterative Magnitude Pruning, Scaling Limitation)

  > Pruning at Initialization(Connection Sensitivity, Gradient Flow)

- [System & Hardware Support for Fine-grained Sparsity](notes/mit-6s965/lec04-summary02.md)

  > Efficient Inference Engine(EIE format: relative index, column pointer)

  > Sparse Matrix-Matrix Multiplication(SpMM), Sparse Coding(CSR format)

  ---

- [Basic Concepts of Quantization](notes/mit-6s965/lec05-summary01.md)

  > Numeric Data Types: Integer, Fixed-Point, Floating-Point(IEEE FP32/FP16, BF16, NVIDIA FP8), INT4 and FP4

  > Uniform vs Non-uniform quantization, Symmetric vs Asymmetric quantization

  > Linear Quantization: Integer-Arithmetic-Only Quantization, Sources of Quantization Error(clipping, rounding, scaling factor, zero point)

- [Vector Quantization](notes/mit-6s965/lec05-summary02.md)

  > Vector Quantization(Deep compression: iterative pruning, K-means based quantization, Huffman encoding), Product Quantization

- [Post Training Quantization](notes/mit-6s965/lec06-summary01.md)

  > Weight Quantiztion: Per-Tensor Activation Per-Channel Activation, Group Quantization(Per-Vector, MX), Weight Equalization, Adative Rounding

  > Activation Quantization: During training(EMA), Calibration(Min-Max, KL-divergence, Mean Squared Error)

  > Bias Correction, Zero-Shot Quantization(ZeroQ)

- [Quantization-Aware Training, Low bit-width quantization](notes/mit-6s965/lec06-summary02.md)

  > Fake quantization, Straight-Through Estimator

  > Binary Quantization(Deterministic, Stochastic, XNOR-Net), Ternary Quantization

  ---

- [Neural Architecture Search: basic concepts & manually-designed neural networks](notes/mit-6s965/lec07-summary01.md)

  > input stem, stage, head
  
  > AlexNet, VGGNet, SqueezeNet(fire module), ResNet(bottleneck block, residual connection), ResNeXt(grouped convolution)
  
  > MobileNet(depthwise-separable convolution, width/resolution multiplier), MobileNetV2(inverted bottleneck block), ShuffleNet(channel shuffle), SENet(squeeze-and-excitation block), MobileNetV3(redesigning expensive layers, h-swish)

- [Neural Architecture Search: Search Space](notes/mit-6s965/lec07-summary02.md)

  > Search Space: Macro, Chain-Structured, Cell-based(NASNet), Hierarchical(Auto-DeepLab, NAS-FPN)

  > design search space: Cumulative Error Distribution, FLOPs distribution, zero-cost proxy

- [Neural Architecture Search: Performance Estimation & Hardware-Aware NAS](notes/mit-6s965/lec08.md)

  > Weight Inheritance, HyperNetwork, Weight Sharing(super-network, sub-network)

  > Performance Estimation Heuristics: Zen-NAS, GradSign

  ---

- [Knowledge Distillation](notes/mit-6s965/lec10-summary01.md)

  > Knowledge Distillation(distillation loss, softmax temperature)
  
  > What to Match?: intermediate weights, features(attention maps), sparsity pattern, relational information

  > Distillation Scheme: Offline Distillation, Online Distillation, Self-Distillation

- [Distillation for Applications](notes/mit-6s965/lec10-summary02.md)

  > Applications: Object Detection, Semantic Segmentation, GAN, NLP

  > Tiny Neural Network: NetAug

  ---

- [MCUNet](notes/mit-6s965/lec11.md)

  > MCUNetV1: TinyNAS, TinyEngine

  > MCUNetV2: MCUNetV2 architecture(MobileNetV2-RD), patch-based inference, joint automated search

### ⚙️ Efficient Training and System Support

- [TinyEngine](notes/mit-6s965/lec17.md)

  > Memory Hierarchy of Microcontroller, Primary Memory Format(NCHW, NHWC, CHWN)

  > Parallel Computing Techniques: Loop Unrolling, Loop Reordering, Loop Tiling, SIMD programming
  
  > Inference Optimization: Im2col, In-place depthwise convolution, appropriate data layout(pointwise, depthwise convolution), Winograd convolution

  ---

### 🔧 Application-Specific Optimizations

- [Efficient Video(live) Understanding](notes/mit-6s965/lec19-summary01.md)

  > 2D CNNs for Video(live) Understanding, 3D CNNs for Video(live) Understanding(I3D), Temporal Shift Module(TSM)

  > Other Efficient Methods: Kernel Decomposition, Multi-Scale Modeling, Neural Architecture Search(X3D), Skipping Redundant Frames/Clips, Utilizing Spatial Redundancy

- [Generative Adversarial Networks (GANs)](notes/mit-6s965/lec19-summary02.md)

  > GANs(Generator, Discriminator), Conditional/Unconditional GANs, Difficulties in GANs

  > Compress Generator(GAN Compression), Dynamic Cost GANs(Anycost GANs), Data-Efficient GANs(Differentiable Augmenatation)

  ---

- [Transformer](notes/mit-6s965/2023-lec12-summary01.md)

  > NLP Task(Discriminative, Generative), Pre-Transformer Era(RNN, LSTM, CNN)

  > Transformer: Tokenizer, Embedding, Multi-Head Attention, Feed-Forward Network, Layer Normalization(Pre-Norm, Post-Norm), Positional Encoding

- [Transformer Design Variants](notes/mit-6s965/2023-lec12-summary02.md)

  > Encoder-Decoder(T5), Encoder-only(BERT), Decoder-only(GPT), Relative Positional Encoding, KV cache optimization, Gated Linear Unit

- [Efficient Vision Transformer](notes/mit-6s965/2023-lec14-summary01.md)

  > Vision Transformer, Window Attention(Swin Transformer), Sparse Window Attention(FlatFormer), ReLU Linear Attention(EfficientViT), Sparsity-Aware Adaptation(SparseViT)