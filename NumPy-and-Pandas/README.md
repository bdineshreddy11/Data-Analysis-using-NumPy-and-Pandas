# 📊 Python Data Analysis with NumPy and Pandas

<p align="center">

  **A Beginner-Friendly Data Analysis Project**

  <img src="https://img.shields.io/badge/Python-Data%20Analysis-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Data Analysis" />
  <img src="https://img.shields.io/badge/NumPy-Array%20Operations-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Manipulation-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />

</p>

---

## 📌 Project Overview

This project focuses on fundamental data analysis techniques using **NumPy and Pandas in Python**. It demonstrates how to create and inspect arrays, perform numerical calculations, work with labeled data, explore tabular datasets, and manipulate records.

The project uses daily temperature readings, student marks, and sales transaction records to practice essential data analysis operations.

## 🎯 Objectives

- Understand NumPy arrays and their properties.
- Perform numerical calculations and statistical operations.
- Apply array indexing, slicing, and filtering.
- Create and manipulate Pandas Series with custom indexes.
- Build and explore Pandas DataFrames.
- Filter, group, and summarize business transaction data.
- Update values, create new columns, and remove unwanted data.
- Develop a foundation for real-world data analysis tasks.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and data analysis |
| NumPy | Numerical computations and array operations |
| Pandas | Data manipulation and analysis |
| Jupyter Notebook / VS Code | Writing and executing Python code |
| Git and GitHub | Version control and project documentation |

## 📚 Concepts Covered

### 1. NumPy — Numerical Computing

NumPy provides efficient tools for working with numerical data and multidimensional arrays.

**Array creation and inspection**
- Creating one-dimensional arrays using `np.array()`.
- Creating two-dimensional arrays.
- Inspecting array shape with `.shape`.
- Checking data types with `.dtype`.
- Counting elements with `.size`.

**Numerical operations**
- Converting temperatures from Celsius to Fahrenheit.
- Calculating maximum and minimum values using `np.max()` and `np.min()`.
- Calculating averages using `np.mean()`.
- Performing arithmetic operations on entire arrays.

**Indexing and slicing**
- Extracting the first three temperature readings.
- Selecting the last two readings to represent weekend temperatures.
- Retrieving a middle section of an array.
- Accessing individual rows and selected columns in a two-dimensional array.
- Understanding zero-based indexing and slice boundaries.

### 2. Pandas Series — One-Dimensional Data

A Pandas Series stores data values alongside an index, which can contain labels or integers.

**Series creation and access**
- Creating a Series using `pd.Series()`.
- Assigning custom index labels such as `Rank1`, `Rank2`, and `Rank3`.
- Accessing elements using integer positions.
- Selecting labeled data with `.loc[]`.
- Selecting positional data with `.iloc[]`.

**Filtering and manipulation**
- Applying Boolean masks to select values greater than 90.
- Updating an existing value.
- Removing an entry using `.drop()`.
- Calculating CGPA-like values by dividing marks by 10.
- Understanding the difference between label-based and position-based selection.

### 3. Pandas DataFrame — Tabular Data Analysis

A DataFrame organizes data into rows and columns, similar to a spreadsheet or database table.

**Creating and inspecting data**
- Creating a DataFrame from a dictionary.
- Displaying records with `.head()` and `.tail()`.
- Inspecting dimensions using `.shape`.
- Retrieving column names with `.columns`.
- Checking data types with `.dtypes`.
- Reviewing dataset information using `.info()`.

**Selecting and filtering data**
- Selecting individual columns and multiple columns.
- Retrieving columns by integer position using `.iloc[]`.
- Filtering transactions by region and transaction amount.
- Finding category frequencies with `.value_counts()`.
- Identifying distinct regions using `.unique()`.

**Grouping and aggregation**
- Grouping transactions by region with `.groupby()`.
- Calculating average transaction amounts using `.mean()`.
- Summarizing transaction data to support business analysis.

**Data manipulation**
- Updating an amount for a specific transaction.
- Creating a discount column using a percentage calculation.
- Removing a record using a condition and `.drop()`.
- Deleting a column using `.drop(columns=...)`.
- Understanding how data cleaning changes a DataFrame.

## 🧩 Practical Scenarios

| Scenario | Data Used | Analysis Performed |
|---|---|---|
| Temperature Analysis | Daily temperatures across two weeks | Fahrenheit conversion, summary statistics, slicing, and weekly comparisons |
| Student Performance | Marks with custom rank labels | Indexing, filtering, updating marks, and calculating derived values |
| Sales Transactions | Transaction IDs, categories, regions, and amounts | Filtering, category counts, regional averages, discounts, and data modification |

## 💡 Key Learning Outcomes

After completing this project, I learned how to:

- Work with NumPy arrays and understand their dimensions and data types.
- Apply vectorized calculations to numerical datasets.
- Extract subsets of data using indexing and slicing.
- Understand the difference between Pandas `.loc[]` and `.iloc[]`.
- Filter records using Boolean conditions.
- Explore datasets using basic inspection methods.
- Use grouping and aggregation to summarize business data.
- Update records and create calculated columns.
- Remove unnecessary rows and columns during data preparation.
- Apply Python libraries to practical data analysis scenarios.

## 📂 Project Structure

```text
python-data-analysis-numpy-pandas/
│
├── README.md
├── numpy_array_operations.py
├── pandas_series_operations.py
└── pandas_dataframe_operations.py
```

*Note: The Python filenames above are suggested. Use the filenames that match your actual project files.*

## ⚙️ Installation and Execution

**Step 1: Install Python libraries**

```bash
pip install numpy pandas
```

**Step 2: Import the libraries**

```python
import numpy as np
import pandas as pd
```

**Step 3: Run the Python files**

```bash
python numpy_array_operations.py
python pandas_series_operations.py
python pandas_dataframe_operations.py
```

You can also execute the code in Jupyter Notebook or VS Code.

## 🔍 Why This Project Matters

NumPy and Pandas are widely used in data analytics for numerical calculations, data exploration, transformation, and preparation. These fundamentals help build the skills needed for more advanced work with Excel, SQL, Power BI, statistical analysis, and real-world business datasets.

This project establishes a practical foundation for progressing toward an entry-level **Data Analyst** role.

## 👨‍💻 Author

**Python Data Analysis Practice Project**

*Focus: NumPy fundamentals, Pandas Series, DataFrame operations, and exploratory data analysis.*

---

<p align="center">
  ⭐ Learning Python one practical concept at a time.
</p>