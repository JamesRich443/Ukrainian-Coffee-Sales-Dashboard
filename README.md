☕ Ukrainian Coffee Sales Dashboard

A complete end-to-end data analytics project that visualizes coffee sales data. This project leverages Python for data extraction and automation, Azure Blob Storage for cloud hosting, and Power BI for dynamic reporting.The dataset originates from [View Dataset here](https://www.kaggle.com/datasets/ihelon/coffee-sales/data?select=index_2.csv) and tracks weekly sales from a coffee vending machine in Vinnytsia, Ukraine. The data pipeline is fully automated—Python retrieves the latest data via the Kaggle API, processes it, and uploads it to Azure Blob Storage. Power BI then pulls directly from this source to keep the dashboard always up-to-date.

📊 Project Overview

Goal: Simulate a stakeholder request by presenting clear insights into coffee sales trends and performance.
Data Source: Kaggle (retrieved via Python and the Kaggle API)
Cloud Storage: Azure Blob Storage
Visualization Tool: Power BI
🛠️ Tools & Technologies

Python (for data extraction and transformation)
Azure Blob Storage (for hosting processed data)
Power BI (for interactive visualizations)
📈 Key Features

Interactive dashboard with dynamic filters
Time-series visuals showing monthly trends in sales and profit
KPI cards highlighting Total Sales
Automated cloud-based pipeline from raw CSVs to actionable insights

---

## 🖼️ Dashboard Preview

<img width="1196" alt="Ukranian Coffee Sales Power BI" src="https://github.com/user-attachments/assets/07693c68-f546-4d95-89b2-98b400224286" />


---

## 🔁 Data Pipeline
 [Kaggle API] --> B[Python Script] --> [Azure Blob Storage] --> [Power BI Dashboard]
