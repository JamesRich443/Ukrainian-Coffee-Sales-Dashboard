# ☕ Ukrainian Coffee Sales Dashboard

A complete end-to-end data analytics project that visualizes coffee sales data across Ukraine. The project leverages Python for data extraction, Azure for cloud storage, and Power BI for dynamic reporting.

---

## 📊 Project Overview
- **Goal**: Analyze trends in coffee sales across Ukraine over time.
- **Data Source**: Kaggle (imported via API using Python) 
- **Storage**: Azure Blob Storage
- **Visualization**: Power BI

---

## 🛠️ Tools Used
- Python
- Kaggle API
- Azure Blob Storage
- Power BI
- DAX (Power BI formulas)

---

## 📈 Key Features
- Interactive dashboard with slicers (Product, Category, Country)
- Time series visualizations showing monthly sales and profit trends
- KPI cards displaying Total Sales, Profit, and Quantity
- Cloud-based data pipeline from raw CSV to dashboard insights

---

## 🖼️ Dashboard Preview

![Dashboard Screenshot](screenshots/dashboard.png)

---

## 🔁 Data Pipeline
graph TD
A[Kaggle API] --> B[Python Script]
B --> C[Azure Blob Storage]
C --> D[Power BI Dashboard]
