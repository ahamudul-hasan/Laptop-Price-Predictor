# 💻 Laptop Price Predictor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red?style=for-the-badge&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8.0-orange?style=for-the-badge&logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-3.0.2-blue?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-2.4.4-cyan?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.8-yellow?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-purple?style=for-the-badge)

A machine learning-based web application that predicts laptop prices in Bangladesh Taka (৳) based on hardware specifications and features.

</div>

---
## 🎯 Overview

<div align="center">

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║        🎯 LAPTOP PRICE PREDICTOR 🎯                       ║
║                                                            ║
║      Intelligent Machine Learning Price Estimation         ║
║         For Bangladeshi Laptop Market (৳)                  ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

</div>

**Laptop Price Predictor** is an intelligent machine learning application that accurately predicts laptop prices based on comprehensive hardware specifications. Built with Python, Scikit-learn, and Streamlit, this application provides an intuitive interface for users to input laptop configurations and receive real-time price predictions.

Whether you're a buyer looking for market prices or a seller trying to set competitive rates, this tool helps you make informed decisions with data-driven predictions.

---

## 📊 Key Metrics at a Glance

<div align="center">

| Metric | Value |
|--------|-------|
| 🔬 **Model Type** | Linear Regression with Polynomial Features |
| 📊 **Dataset Size** | 1000+ Laptop Records |
| 🎯 **Input Features** | 12 Specifications |
| 🔢 **Output Format** | Bangladeshi Taka (৳) |
| 💹 **Currency Rate** | 1 INR = 1.32 BDT |
| ⚙️ **Framework** | Python + Scikit-learn |
| 🎨 **UI Framework** | Streamlit |
| ✅ **Status** | Production Ready |

</div>

---

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h3>🔮 Intelligent Predictions</h3>
      <p>Advanced machine learning model trained on extensive laptop dataset</p>
    </td>
    <td width="50%">
      <h3>🎨 Beautiful UI</h3>
      <p>User-friendly Streamlit interface with interactive components</p>
    </td>
  </tr>
  <tr>
    <td>
      <h3>💱 Multi-Currency</h3>
      <p>Results displayed in Bangladeshi Taka (৳) with proper formatting</p>
    </td>
    <td>
      <h3>📊 Comprehensive Features</h3>
      <p>Considers 12+ laptop specifications for accurate predictions</p>
    </td>
  </tr>
  <tr>
    <td>
      <h3>⚡ Real-time Results</h3>
      <p>Instant price predictions with formatted currency display</p>
    </td>
    <td>
      <h3>🛠️ Easy to Use</h3>
      <p>Simple dropdowns and input fields for quick configuration</p>
    </td>
  </tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone or download the repository:**

```bash
cd "Laptop Price Predictor"
```

2. **Create a virtual environment:**

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

### Running the Application

Navigate to the src folder and run the Streamlit app:

```bash
cd src
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

---

## 📋 How to Use

<div align="center">

```
STEP-BY-STEP PREDICTION WORKFLOW
════════════════════════════════════════════════════════

START
  │
  ▼
┌─────────────────────────────────────┐
│  SELECT LAPTOP SPECIFICATIONS       │
├─────────────────────────────────────┤
│ • Brand & Type                      │
│ • RAM & Storage (HDD/SSD)           │
│ • Display (IPS, Touchscreen)        │
│ • CPU & GPU                         │
│ • Screen Size & Resolution          │
│ • Weight & OS                       │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ CLICK PREDICT│
        └──────┬───────┘
               │
               ▼
        [PROCESSING...]
               │
               ▼
        ┌──────────────────┐
        │  ML MODEL RUNS   │
        │  Transforms Data │
        │ Calculates Price │
        └──────┬───────────┘
               │
               ▼
      ┌────────────────────┐
      │  PRICE PREDICTION  │
      │   Displays in      │
      │  Taka (৳ 45,600)  │
      └────────────────────┘
               │
               ▼
             END
```

</div>

### Detailed Steps:

1. **Select Brand**: Choose your laptop manufacturer (Dell, HP, Lenovo, ASUS, etc.)
2. **Choose Type**: Select the laptop type (Notebook, Ultrabook, etc.)
3. **Set Hardware Specs**:

   - 🧠 **RAM**: Select memory from 2GB to 64GB
   - ⚖️ **Weight**: Enter weight in kilograms
   - 🖥️ **Screen Settings**:
     - Touchscreen (Yes/No)
     - IPS Display (Yes/No)
     - Screen Size (inches)
     - Resolution
4. **Storage Configuration**:

   - 💾 **HDD**: Select hard drive capacity
   - ⚡ **SSD**: Select SSD capacity
5. **Advanced Components**:

   - 🎮 **GPU**: Choose graphics card brand (Nvidia, AMD, Intel)
   - 📦 **CPU**: Select processor type
   - 🖲️ **OS**: Choose operating system
6. **Predict**: Click the **Predict Price** button to get instant price prediction in Bangladeshi Taka (৳)

---

## 📁 Project Structure

```
Laptop Price Predictor/
│
├── 📄 README.md                 # Project documentation
├── 📋 requirements.txt          # Python dependencies
│
├── 📁 Data/
│   └── laptop_data.csv         # Raw dataset
│
├── 📁 Models/
│   ├── pipe.pkl                # Trained ML pipeline
│   └── df.pkl                  # Processed dataframe
│
├── 📁 Notebooks/
│   └── Project.ipynb           # Data exploration & model training
│
└── 📁 src/
    └── app.py                  # Main Streamlit application
```

---

## 🗂️ Dataset Information

**Source**: Laptop hardware and pricing data
**Records**: 1000+ laptops
**Features**: 12+ specifications

### Key Attributes:

- **Brand/Company**: Manufacturer name
- **Type**: Laptop category (Notebook, Ultrabook, etc.)
- **CPU Brand**: Processor manufacturer (Intel Core i3/i5/i7, AMD)
- **RAM**: Memory size (2-64 GB)
- **Storage**: HDD and SSD configurations
- **GPU Brand**: Graphics processor (Nvidia, AMD, Intel)
- **Display**: Screen size, resolution, IPS, Touchscreen
- **Weight**: Laptop weight (kg)
- **OS**: Operating system
- **Price**: Target variable (in INR, converted to BDT)

---

## 🤖 Machine Learning Model

<div align="center">

![ML Pipeline](https://img.shields.io/badge/ML%20Pipeline-Scikit--Learn-blue?style=flat-square)
![Model Type](https://img.shields.io/badge/Model-Linear%20Regression-green?style=flat-square)

</div>

### Algorithm: Linear Regression Pipeline

<div align="center">

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│   Raw Data  │────▶│ Preprocessor │────▶│  Encoder    │────▶│  Regressor   │
│   (Features)│     │ (Scaling)    │     │(Categorical)│     │  (Linear)    │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                            ┌──────────────────┐
                                                            │ Price Prediction │
                                                            │   in Taka (৳)    │
                                                            └──────────────────┘
```

</div>

**Model Components:**

- ✅ Feature scaling and preprocessing
- ✅ Categorical encoding
- ✅ Polynomial feature generation
- ✅ Linear regression with log transformation

**Model Performance:**

- Trained on extensive laptop dataset
- Features: 12 comprehensive specifications
- Output: Price in Indian Rupees (converted to BDT)

**Conversion Rate:**

- 1 INR = 1.32 BDT ৳

### Data Flow Visualization

<div align="center">

```
📊 DATA PIPELINE
═══════════════════════════════════════════════════════

INPUT
  ├── Brand/Company
  ├── Laptop Type
  ├── CPU & GPU
  ├── RAM & Storage
  ├── Display (IPS, Touchscreen)
  ├── Resolution & PPI
  ├── Weight
  └── OS
        │
        ▼
   [PREPROCESSING]
        │
        ├── Numerical Scaling
        ├── Category Encoding
        └── Feature Engineering
              │
              ▼
        [ML MODEL]
              │
              ├── Load Trained Pipeline
              ├── Transform Features
              └── Make Prediction
                    │
                    ▼
              [OUTPUT]
                    │
                    ▼
            Price in BDT ৳
```

</div>

---

## 📊 Example Predictions

<div align="center">

### Price Prediction Examples

```
BUDGET TIER                    PREMIUM TIER
═════════════════════════════════════════════════════════════

Dell Notebook               ASUS Ultrabook
├── RAM: 8GB                ├── RAM: 16GB
├── CPU: i5                 ├── CPU: i7
├── SSD: 512GB              ├── SSD: 1024GB
├── GPU: Nvidia             ├── GPU: Nvidia
├── No Touchscreen          ├── Touchscreen: Yes
└── Price: ৳18-25K         └── Price: ৳28-43K

      ▲                            ▲
      │                            │
      └──────────────┬─────────────┘
                     │
            ACCURATE PREDICTIONS
            POWERED BY ML MODEL
```

### Example 1: Budget Laptop
- **Brand**: Dell
- **Type**: Notebook
- **RAM**: 8 GB
- **CPU**: Intel Core i5
- **GPU**: Nvidia
- **SSD**: 512 GB
- **Weight**: 1.9 kg
- **Touchscreen**: No
- **🎯 Predicted Price**: ~৳18,000 - ৳25,200

### Example 2: Premium Laptop
- **Brand**: ASUS
- **Type**: Ultrabook
- **RAM**: 16 GB
- **CPU**: Intel Core i7
- **GPU**: Nvidia
- **SSD**: 1024 GB
- **Weight**: 1.5 kg
- **Touchscreen**: Yes
- **🎯 Predicted Price**: ~৳28,800 - ৳43,200

</div>

---

## 💾 Dependencies

<div align="center">

### Core Libraries

| Package | Version | Purpose |
|---------|---------|---------|
| **streamlit** | 1.28.1+ | Web application framework |
| **scikit-learn** | 1.8.0+ | Machine learning & modeling |
| **pandas** | 3.0.2+ | Data manipulation & analysis |
| **numpy** | 2.4.4+ | Numerical computing |
| **matplotlib** | 3.10.8+ | Data visualization & plotting |
| **seaborn** | 0.13.2+ | Statistical data visualization |

</div>

### Installation Command

```bash
pip install streamlit scikit-learn pandas numpy matplotlib seaborn
```

Or install all dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

For complete list, see `requirements.txt`

---

## 🔧 Technologies Used

<div align="center">

| Technology             | Purpose                   |
| ---------------------- | ------------------------- |
| **Python**       | Programming language      |
| **Streamlit**    | Web application framework |
| **Scikit-learn** | Machine learning library  |
| **Pandas**       | Data manipulation         |
| **NumPy**        | Numerical computing       |
| **Pickle**       | Model serialization       |

</div>


---

## 🎨 Project Architecture Overview

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                  LAPTOP PRICE PREDICTOR                      ║
║                     SYSTEM OVERVIEW                          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ┌────────────────┐      ┌──────────────────┐              ║
║  │  DATA SOURCE   │      │  PREPROCESSING   │              ║
║  │  laptop_data   │─────▶│  Cleaning        │              ║
║  │    .csv        │      │  Feature Eng.    │              ║
║  └────────────────┘      └────────┬─────────┘              ║
║                                   │                         ║
║                                   ▼                         ║
║                        ┌──────────────────┐               ║
║                        │   ML PIPELINE    │               ║
║                        │ • Scaler         │               ║
║                        │ • Encoder        │               ║
║                        │ • Regressor      │               ║
║                        │ (Linear)         │               ║
║                        └────────┬─────────┘               ║
║                                 │                         ║
║              ┌──────────────────┴──────────────────┐      ║
║              │                                     │      ║
║              ▼                                     ▼      ║
║    ┌──────────────────┐            ┌──────────────────┐  ║
║    │  SERIALIZED      │            │  STREAMLIT APP   │  ║
║    │  MODELS          │            │  Interactive UI  │  ║
║    │ • pipe.pkl       │            │  User Input      │  ║
║    │ • df.pkl         │            │  Price Display   │  ║
║    └────────┬─────────┘            └────────┬─────────┘  ║
║             │                               │            ║
║             └───────────────┬───────────────┘            ║
║                             │                            ║
║                             ▼                            ║
║                  ┌──────────────────────┐              ║
║                  │  PRICE PREDICTION    │              ║
║                  │  INR → BDT (1.32×)   │              ║
║                  │  Display: ৳ 45,600   │              ║
║                  └──────────────────────┘              ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

</div>

### 📈 Model Training Pipeline

```
INPUT FEATURES (12)
    ├── Brand (Categorical)
    ├── Type (Categorical)
    ├── RAM (Numerical)
    ├── Weight (Numerical)
    ├── Touchscreen (Binary)
    ├── IPS (Binary)
    ├── PPI (Numerical)
    ├── CPU Brand (Categorical)
    ├── HDD (Numerical)
    ├── SSD (Numerical)
    ├── GPU Brand (Categorical)
    └── OS (Categorical)
         │
         ▼
    PREPROCESSING
         ├── StandardScaler (Numerical Features)
         ├── OneHotEncoder (Categorical Features)
         └── PolynomialFeatures (Interaction Terms)
         │
         ▼
    REGRESSION MODEL
         ├── Algorithm: Linear Regression
         ├── Target: log(Price)
         └── Transformation: exp(prediction)
         │
         ▼
    OUTPUT: Price in Bangladeshi Taka (৳)
```

---

**Last Updated**: April 2026
**Version**: 1.0.0

</div>
