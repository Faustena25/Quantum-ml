# Quantum Machine Learning — Lab Exercises
### MDS572B | MSc Data Science | CHRIST (Deemed to be University)

---

## Overview

This repository contains hands-on implementations of Quantum Machine Learning algorithms developed as part of the **MDS572B: Quantum Machine Learning** course. The experiments explore the intersection of quantum computing and machine learning using **Qiskit** — covering quantum circuit design, quantum-enhanced clustering, and quantum neural networks applied to real-world datasets.

---

## Topics Covered

- Quantum circuit fundamentals — single qubit gates, Bloch sphere visualization
- Quantum feature encoding and state preparation
- Quantum kernel methods and similarity computation
- Quantum clustering using Swap Test and Spectral Clustering
- Variational Quantum Circuits (VQC) for classification
- Hybrid quantum-classical machine learning pipelines
- Performance benchmarking — quantum vs classical models

---

## Implementations

### Quantum Gate Operations
Exploration of fundamental single-qubit gates including Pauli-X, Pauli-Y, Pauli-Z, Hadamard, S, and T gates. Each gate is analyzed mathematically via statevectors and geometrically via Bloch sphere visualizations.

### Quantum Clustering
A hybrid quantum-classical clustering pipeline applied to genomic cancer data. Quantum similarity between data points is computed using the **Swap Test** circuit, and clustering is performed using K-Means on the resulting quantum similarity matrix.

**Dataset:** Breast Cancer Wisconsin (genomic cellular features)
**Method:** Swap Test → Quantum Similarity Matrix → K-Means Clustering

### Quantum Neural Network (VQC Classifier)
A Variational Quantum Circuit trained to classify breast cancer patients as malignant or benign. The QNN combines a **ZZFeatureMap** for data encoding and an **EfficientSU2 ansatz** for trainable quantum weights, optimized using the COBYLA optimizer.

**Dataset:** Breast Cancer Wisconsin
**Method:** ZZFeatureMap + EfficientSU2 → COBYLA Optimizer → Binary Classification

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| Qiskit | Quantum circuit construction and simulation |
| Qiskit Aer | Local quantum simulator |
| Scikit-learn | Classical ML baselines and preprocessing |
| NumPy | Numerical computation |
| Matplotlib | Visualization |
| SciPy | Classical optimization (COBYLA) |
| Jupyter Notebook | Interactive development environment |

---

## Setup and Installation

**1. Clone the repository**
```bash
git clone https://github.com/Faustena25/quantum-ml-labs.git
cd quantum-ml-labs
```

**2. Create and activate a conda environment**
```bash
conda create -n qml_env python=3.10
conda activate qml_env
```

**3. Install dependencies**
```bash
pip install qiskit qiskit-aer scikit-learn matplotlib numpy pandas scipy
```

**4. Launch Jupyter Notebook**
```bash
jupyter notebook
```

---

## Results

| Experiment | Method | Outcome |
|-----------|--------|---------|
| Gate Operations | Statevector Simulation | Bloch sphere SVGs generated for all gates |
| Quantum Clustering | Swap Test + K-Means | Cluster structure visualized and compared against classical K-Means |
| QNN Classification | VQC + COBYLA | Loss reduced from ~1.13 → ~0.27 over training |

---

## Key Concepts Demonstrated

- **Superposition and Entanglement** — encoded into real datasets via ZZFeatureMap
- **Quantum Advantage** — kernel-based similarity computed in Hilbert space
- **Hybrid Architecture** — quantum feature extraction + classical optimization
- **Benchmarking** — systematic comparison of quantum vs classical approaches

---

## Course Details

| | |
|-|-|
| **Course** | MDS572B: Quantum Machine Learning |
| **Institution** | CHRIST (Deemed to be University), Bengaluru |
| **Program** | MSc Data Science (Batch 2025–27) |

---

## Author

**Faustena S**
MSc Data Science — CHRIST (Deemed to be University)
GitHub: [github.com/Faustena25](https://github.com/Faustena25)

