<div width="100%" height="100%" align="center">
  
<h1 align="center">
  <p align="center">Computer Organization and Design RISC-V Edition</p>
  <a href="https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-812275-4">
    <img width="50%" src="https://raw.githubusercontent.com/erectbranch/Computer_Organization_and_Design/master/cover.jpg" />
  </a>
</h1>
  
<b>David Patterson, John Hennessy 저</b></br>
Elsevier · 2017년 4월 13일 출시</b> 

</div>

## :bulb: 목표 <!-- {docsify-ignore-all} -->

- **컴퓨터 구조를 공부한다.**

  > RISC-V 컴퓨터 하드웨어, 소프트웨어 인터페이스를 자세히 공부한다.

<br/>

## 🚩 정리한 문서 목록

### 📙 Computer Abstractions

 - [Computer Abstractions and Technology](notes/cod/ch01.md)

   > response time(execution time): wall clock time(elapsed time), CPU time, clock rate, clock period, CPI(Clock cycles Per Instruction), Effective CPI, MIPS

   > Power Wall, multicore processor, parallel programming, Amdahl's Law

### ⚙️ RISC-V

 - [RISC-V Instructions(RV64I)](notes/cod/ch02-summary01.md)

   > CISC vs RISC, general purpose register(register file), register operands, data alignment(MIPS vs RISC-V), byte addressing, little/big Endian, register spilling, bit extension

   > R-format instructions(arithmetic), I-format instructions(load, immediate arithmetic), S-format instructions(stores)

   > addressing mode(immediate, register, base, PC-relative), logical operations(shift, and, or, xor)

 - [Conditional Operation, Branch](notes/cod/ch02-summary02.md)

   > branch instructions(if-else, while example), procedure calling, procedure call instructions, memory layout, stack, leaf procedure, non-leaf procedure(factorial example), string copy example

 - [wide, branch instructions, data race](notes/cod/ch02-summary03.md)

   > wide immediate operands, branch addressing, SB-format, branching far away

   > data race, synchronization, atomic swap, mutex lock

### 🎛 RISC-V Processor

 - [RISC-V Processor datapath](notes/cod/ch04-summary01.md)

   > instruction execution: IF(Instruction Fetch), ID(Instruction Decode/register file read), EX(Execute/address calculation), MEM(Memory access), WB(Write Back)

   > combinational element, state element, sequential elements, multiplexer, control unit(function unit, control line)

 - [RISC-V Pipelining](notes/cod/ch04-summary02.md)

   > single-cycle vs pipelined performance, pipeline bubble, steady state

   > pipeline hazard: structural hazard, data hazard(forwarding, code scheduling), control hazard(static/dynamic branch prediction)

 - [RISC-V Pipelined datapath, ILP](notes/cod/ch04-summary03.md)

   > pipeline register, forwarding, double data hazard
   
   > Instruction Level Parallelism, Multiple Issue, Speculation, VLIW(Very Long Instruction Word), Loop Unrolling

### 🪜 Cache

- [memory hierarchy, direct mapped cache](notes/cod/ch05-summary01.md)

   > SRAM, DRAM, temporary locality, spatial locality

   > hit ratio, miss ratio, direct mapped cache(tag, valid bit, address subdivision), block size considerations

- [cache miss, cache write, set-associative cache](notes/cod/ch05-summary02.md)

   > cache miss(compulsory/capacity/conflict misses), cache write(write-through, write buffer, write-back, write allocation)

   > N-way set-associative cache(miss rate and associativity), fully-associative cache, replacement policy(LRU, random)

   > split cache(instruction cache, data cache), cache performance(memory-stall clock cycles, AMAT), multilevel caches(primary cache, secondary cache)

### ⛓ Parallel Processors

- [interconnect, heterogeneity, thread](notes/cod/ch06-summary01.md)

   > interconnection, I/O register mapping(memory mapped I/O, I/O mapped I/O), polling, interrupt

   > heterogeneous computing, parallel programming, process vs thread, Thread-Level Parallelism(TLP): Temporal Multi-Threading(Coarse-grained, Fine-grained), Simultaneous Multi-Threading(SMT)

   > Shared Memory Multiprocessor(SMP), Uniform Memory Access, Non-Uniform Memory Access, PThread Programming

   > Message Passing Interface(MPI), MPI programming 

<br/>

## :mag: 목차

### 1. Computer Abstractions and Technology

### 2. Instructions: Language of the Computer

### 3. Arithmetic for Computers

### 4. The RISC-V Processor

### 5. Large and Fast: Exploiting Memory Hierarchy

### 6. Parallel Processors from Client to Cloud

### A. The Basics of Logic Design

### B. Graphics and Computing GPUs

### C. Mapping Control to Hardware

### D. A Survey of RISC Architectures