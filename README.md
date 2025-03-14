# Personal Finance Analysis

## 📌 Project Overview
This project aims to analyze personal finance data by extracting transaction records from bank statements in PDF format. The extracted data is processed and analyzed using Python libraries such as `pandas`, `numpy`, `matplotlib`, and `seaborn` to gain insights into income and expenses from 2021 to 2025.

The goal is to demonstrate proficiency in:
- API integration
- Data extraction from PDFs
- Data cleaning and transformation
- Exploratory Data Analysis (EDA)
- Data visualization
- Structuring a data analysis project

## 🏗️ Project Structure
```
📂 BANK-TRANSACTIONS
│── 📂 data                # Contains raw, processed, and preprocessed data
│   ├── 📂 raw            # Unprocessed bank statements in PDF format
│   ├── 📂 preprocessed   # Data after extraction and initial cleaning
│   ├── 📂 processed      # Final processed data ready for analysis
│
│── 📂 docs                # Documentation and project-related resources
│
│── 📂 notebooks           # Jupyter Notebooks for analysis and visualization
│
│── 📂 src                 # Source code for data extraction, processing, and analysis
│
│── .env                   # Environment variables (not included in Git)
│── .gitignore             # Files to be ignored by Git
│── environment.yml        # Conda environment dependencies
│── LICENSE                # Project license
│── README.md              # Project documentation
│── requirements.txt       # Python dependencies
```

## 🔧 Technologies Used
- **Python**: Main programming language
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib & seaborn**: Data visualization
- **PyPDF2 / pdfplumber**: Extracting data from PDFs
- **APIs**: Potential integration for external data sources

## 🎯 Project Objectives
- Extract transaction data from PDF bank statements
- Clean and structure the extracted data
- Identify income and expenses for the years 2021 to 2025
- Generate insights through data visualization
- Demonstrate best practices in data analysis and project structuring

## 🚀 Getting Started
### 1️⃣ Install Dependencies
You can install the required dependencies using:
```bash
pip install -r requirements.txt
```
Or, if using Conda:
```bash
conda env create -f environment.yml
conda activate personal-finance
```

### 2️⃣ Running the Project
- Place PDF bank statements in `data/raw/`
- Run the data extraction script from the `src/` folder:
```bash
python src/
```
- Process and analyze the data using the provided Jupyter notebooks:
```bash
jupyter notebook
```

### 3️⃣ Visualizing Data
Run the analysis notebooks in `notebooks/` to generate insights and visualizations.

## 📊 Sample Insights
- Monthly income and expense trends
- Categorization of expenses
- Savings patterns over time
- Yearly financial summaries

## 🤝 Contributing
If you’d like to contribute, feel free to fork the repository and submit a pull request.

## 📜 License
This project is licensed under the [Creative Commons](LICENSE).