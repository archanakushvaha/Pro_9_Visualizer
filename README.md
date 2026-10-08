# 📊 Data Analysis & Visualization Project

## 📌 Introduction

The **Data Analysis & Visualization Project** is a Python-based menu-driven application used to load, explore, clean, analyze, and visualize sales data.

This project uses **NumPy, Pandas, Matplotlib, and Seaborn** to perform different data analysis and visualization operations.

The project is designed in an easy-to-use menu format so that users can select different operations according to their requirements.

---

## 🎯 Objectives

* Load sales data from a CSV file.
* Explore the dataset.
* Check and clean missing values.
* Perform NumPy operations.
* Search, sort, and filter data.
* Split data based on categorical values.
* Perform statistical analysis.
* Create pivot tables.
* Create different types of visualizations.
* Save generated visualizations as image files.

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**

---

## 📚 Python Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 📂 Project Structure

```text
DataAnalysisVisualization/
│
├── main.py
├── SalesDataAnalyzer_100x11.csv
├── README.md
└── visualizations/
```

---

## 📊 Dataset

The project uses a CSV file containing sales-related data.

The dataset contains **100 rows and 11 columns**.

### Columns

| Column           | Description               |
| ---------------- | ------------------------- |
| Sale_ID          | Unique ID of each sale    |
| Customer_Name    | Name of the customer      |
| Gender           | Customer gender           |
| Region           | Sales region              |
| Product_Category | Category of product       |
| Units_Purchased  | Number of units purchased |
| Price_Per_Unit   | Price of one unit         |
| Sales            | Total sales amount        |
| Profit           | Profit earned             |
| Discount         | Discount given            |
| Order_Date       | Date of the order         |

The dataset also contains some missing values so that the **Data Cleaning** features can be tested.

---

# 🔹 Main Features

## 1. Load Dataset

The program asks the user to enter the CSV file path.

```text
Enter CSV file path:
```

After loading the dataset successfully, the first five rows are displayed.

---

## 2. Explore Dataset

This option provides different ways to understand the dataset.

### Options:

1. First 5 rows
2. Last 5 rows
3. Column names
4. Data types
5. Basic information
6. Back

---

## 3. Data Cleaning

This section is used to handle missing values.

### Options:

1. Show missing values
2. Fill numeric missing values with mean
3. Drop missing rows
4. Replace missing values
5. Back

For example, the program can calculate the mean of numeric columns and use it to fill missing numeric values.

---

## 4. NumPy Operations

The program automatically finds numeric columns and allows the user to select one numeric column.

The following operations are performed:

* Sum
* Mean
* Maximum
* Minimum
* Standard Deviation

Example:

```text
===== NumPy Operations =====

Sum: ...
Mean: ...
Maximum: ...
Minimum: ...
Standard Deviation: ...
```

---

## 5. Search / Sort / Filter

This option allows the user to work with a selected column.

### Options:

1. Sort ascending
2. Sort descending
3. Filter by value

This helps in finding and organizing required data from the dataset.

---

## 6. Split Data

The user can select a categorical column.

The program finds the unique values of that column and displays the first five records for each value.

For example, data can be split using:

```text
Gender
Region
Product_Category
```

---

## 7. Statistical Analysis

This section performs descriptive statistical analysis.

It displays:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum
* Quartiles
* Variance
* Median

The `describe()` function is used for descriptive statistics.

---

## 8. Pivot Table

The program allows the user to create a pivot table.

The user selects:

* Index column
* Values column
* Aggregation function

### Aggregation Options:

1. Sum
2. Mean
3. Count

Example:

```text
Enter index column: Region
Enter values column: Sales

1. Sum
2. Mean
3. Count
```

---

# 📈 9. Visualization

The project provides **8 different visualization options**.

### 1. Bar Plot

Used to compare values between categories.

### 2. Line Plot

Used to show changes or trends.

### 3. Scatter Plot

Used to show the relationship between two numeric columns.

### 4. Pie Chart

Used to show the distribution of categorical data.

### 5. Histogram

Used to show the frequency distribution of numeric data.

### 6. Stack Plot

Used to display multiple numeric data series together.

### 7. Heatmap

Used to show the correlation between numeric columns.

### 8. Box Plot

Used to display the distribution of numeric data for different categories.

---

## 💾 10. Save Visualization

After creating a visualization, the program allows the user to save it as an image file.

Example:

```text
Enter file name (example: sales_chart.png):
```

If no filename is entered, the default filename is:

```text
chart.png
```

The image is saved with **300 DPI**.

---

# 🖥️ Main Menu

The application provides the following menu:

```text
DATA ANALYSIS & VISUALIZATION PROJECT

1. Load Dataset
2. Explore Dataset
3. Data Cleaning
4. NumPy Operations
5. Search / Sort / Filter
6. Split Data
7. Statistical Analysis
8. Pivot Table
9. Visualization
10. Save Visualization
11. Exit
```

---

# ▶️ How to Run

### Step 1: Install required libraries

Open Command Prompt or Terminal and run:

```bash
pip install numpy pandas matplotlib seaborn
```

### Step 2: Keep the files in the same folder

```text
DataAnalysisVisualization/
│
├── main.py
├── SalesDataAnalyzer_100x11.csv
└── README.md
```

### Step 3: Run the Python program

```bash
python main.py
```

### Step 4: Load the dataset

When the program asks:

```text
Enter CSV file path:
```

Enter:

```text
SalesDataAnalyzer_100x11.csv
```

---

# 📌 Example Workflow

```text
1. Load Dataset
       ↓
2. Explore Dataset
       ↓
3. Data Cleaning
       ↓
4. NumPy Operations
       ↓
5. Search / Sort / Filter
       ↓
6. Split Data
       ↓
7. Statistical Analysis
       ↓
8. Pivot Table
       ↓
9. Visualization
       ↓
10. Save Visualization
```

---

# 🎓 Concepts Covered

This project demonstrates practical knowledge of:

* NumPy
* Pandas
* DataFrames
* CSV file handling
* Missing value handling
* Data filtering
* Data sorting
* Data splitting
* Descriptive statistics
* Pivot tables
* Matplotlib
* Seaborn
* Data visualization
* Object-Oriented Programming
* Classes and objects
* Exception handling
* Menu-driven programming
---

# ⭐ Conclusion

This project provides a simple and practical way to perform **sales data analysis and visualization using Python**.

It combines **Pandas for data handling, NumPy for numerical operations, Matplotlib and Seaborn for visualization**, and Object-Oriented Programming for organizing the application.

Video link: https://drive.google.com/file/d/19wHiwbZESkiXS58STN8ZFZNlOwIbNxj2/view?usp=sharing
