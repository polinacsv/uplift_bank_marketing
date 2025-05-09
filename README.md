# Uplift Bank Marketing Project

This project is designed to apply **uplift modeling** techniques to the **Bank Marketing dataset**. The primary goal is to estimate the **conditional average treatment effect (CATE)** for marketing strategies, helping identify which clients are most likely to respond positively to marketing efforts.

---

## 📌 Project Structure

```
UPLIFT_BANK_MARKETING/
├── build/                     <-- Build files (cleanly separated)
├── src/
│   └── uplift_bank_marketing/ <-- All project code
│       ├── data/              <-- Data loading and preprocessing
│       │   └── load_data.py   <-- Data loading script (auto-downloads from UCI)
│       ├── models/            <-- Model training and evaluation
│       ├── uplift/            <-- Uplift modeling methods
│       │   └── s_learner.py   <-- S-Learner uplift model
│       └── utils/             <-- Utility functions
│           └── __init__.py    <-- Utility initialization
├── tests/                     <-- Automated tests directory
│   └── test_data.py           <-- Tests for data loading and saving
│   └── test_models.py         <-- Tests for model training and evaluation (placeholder)
│   └── test_uplift.py         <-- Tests for uplift methods (S-Learner, T-Learner, etc.)
├── .gitignore                 <-- Ignored files (including data)
├── Makefile                   <-- Automation of build, install, clean, data loading
├── README.md                  <-- Project documentation (this file)
├── requirements.txt           <-- List of project dependencies
├── setup.py                   <-- Package configuration
```

---

## 🚀 Installation Instructions

### ✅ **1. Clone the Repository**
```bash
git clone https://github.com/polinacsv/uplift_bank_marketing.git
cd uplift_bank_marketing
```

### ✅ **2. Set Up a Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### ✅ **3. Install Dependencies**
- Use the Makefile for automation:
```bash
make setup
```

- Or manually:
```bash
pip install -r requirements.txt
pip install -e .
```

---

## 📊 Dataset Information

- **Source:** Bank Marketing Dataset, publicly available for research.
- **Citation:** [Moro et al., 2011] S. Moro, R. Laureano, and P. Cortez. 
  Using Data Mining for Bank Direct Marketing. ESM'2011.

- **Data Details:**

1. Relevant Information:

   The data is related with direct marketing campaigns of a Portuguese banking institution. 
   The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, 
   in order to access if the product (bank term deposit) would be (or not) subscribed. 

   There are two datasets: 
      1) bank-full.csv with all examples, ordered by date (from May 2008 to November 2010).
      2) bank.csv with 10% of the examples (4521), randomly selected from bank-full.csv.
   The smallest dataset is provided to test more computationally demanding machine learning algorithms (e.g. SVM).

   The classification goal is to predict if the client will subscribe a term deposit (variable y).

2. Number of Instances: 45211 for bank-full.csv (4521 for bank.csv)

3. Number of Attributes: 16 + output attribute.

4. Attribute information:

   For more information, read [Moro et al., 2011].

   Input variables:
   # bank client data:
   1 - age (numeric)

   2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student",
                                       "blue-collar","self-employed","retired","technician","services") 

   3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)

   4 - education (categorical: "unknown","secondary","primary","tertiary")

   5 - default: has credit in default? (binary: "yes","no")

   6 - balance: average yearly balance, in euros (numeric) 

   7 - housing: has housing loan? (binary: "yes","no")

   8 - loan: has personal loan? (binary: "yes","no")

   # related with the last contact of the current campaign:

   9 - contact: contact communication type (categorical: "unknown","telephone","cellular") 

   10 - day: last contact day of the month (numeric)

   11 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")

   12 - duration: last contact duration, in seconds (numeric)

   # other attributes:

   13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

   14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)

   15 - previous: number of contacts performed before this campaign and for this client (numeric)
   
   16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

   Output variable (desired target):
   17 - y - has the client subscribed a term deposit? (binary: "yes","no")
---

## ⚡️ Usage Instructions

### ✅ **Loading Data**
```python
from uplift_bank_marketing.data.load_data import load_data

# Load the dataset (adjust the file path as needed)
df = load_data("data/bank-full.csv")
```

### ✅ **Training an Uplift Model (S-Learner Example)**
```python
from uplift_bank_marketing.uplift.s_learner import s_learner

# Assuming 'treatment' is the treatment column and 'target' is the outcome
model = s_learner(df.drop("target", axis=1), df["treatment"], df["target"])
```

### ✅ **Running Tests**
- Use the Makefile:
```bash
make test
```

---

## 🛠 Makefile Commands

- `make setup` - Cleans, builds, and installs the project.
- `make setup-full` - Cleans, builds, installs the project, and downloads the Bank Marketing data.
- `make clean` - Deletes all build files, Python caches, and downloaded data.
- `make build` - Builds the project (packages it).
- `make install` - Installs the project in editable mode.
- `make test` - Runs all project tests in the `tests/` directory.
- `make data` - Downloads and saves the Bank Marketing dataset (or reloads if already saved).
- `make update-requirements` - Updates `requirements.txt` to match installed packages.


## ✅ Author
Created and maintained by Polina Polskaia.
