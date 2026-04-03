# 💻 Laptop Price Predictor

<div align="center">

![Laptop](https://img.shields.io/badge/Project-Laptop%20Price%20Predictor-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=for-the-badge&logo=streamlit)
![Machine Learning](https://img.shields.io/badge/ML-Scikit%20Learn-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A machine learning-based web application that predicts laptop prices in Bangladesh Taka (৳) based on hardware specifications and features.

[Live Demo](#features) • [Installation](#installation) • [Usage](#usage) • [Dataset](#dataset)

</div>

---

## 🎯 Overview

**Laptop Price Predictor** is an intelligent machine learning application that accurately predicts laptop prices based on comprehensive hardware specifications. Built with Python, Scikit-learn, and Streamlit, this application provides an intuitive interface for users to input laptop configurations and receive real-time price predictions.

Whether you're a buyer looking for market prices or a seller trying to set competitive rates, this tool helps you make informed decisions with data-driven predictions.

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

### Algorithm: Linear Regression Pipeline

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

---

## 📊 Example Predictions

### Example 1: Budget Laptop
- **Brand**: Dell
- **Type**: Notebook
- **RAM**: 8 GB
- **CPU**: Intel Core i5
- **GPU**: Nvidia
- **SSD**: 512 GB
- **Prediction**: ~৳18,000 - ৳25,200

### Example 2: Premium Laptop
- **Brand**: ASUS
- **Type**: Ultrabook
- **RAM**: 16 GB
- **CPU**: Intel Core i7
- **SSD**: 1024 GB
- **Prediction**: ~৳28,800 - ৳43,200

---

## 💾 Dependencies

```
streamlit==1.0+
scikit-learn==1.0+
pandas==1.3+
numpy==1.20+
```

For complete list, see `requirements.txt`

---

## 🔧 Technologies Used

<div align="center">

| Technology | Purpose |
|-----------|---------|
| **Python** | Programming language |
| **Streamlit** | Web application framework |
| **Scikit-learn** | Machine learning library |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computing |
| **Pickle** | Model serialization |

</div>

---

**Last Updated**: April 2026  
**Version**: 1.0.0

</div>
