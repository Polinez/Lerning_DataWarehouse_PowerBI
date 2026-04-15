# E-commerce Lerning Project: Full Data Lifecycle (Data → BI → ML)

## Learning Objectives

The main goal of this project is to replicate the **complete data lifecycle** in a modern e-commerce enterprise.  
The project does not focus on a single domain but integrates:

- **Data Engineering**
- **Data Science**
- **Business Intelligence**

Through this project, I am developing competencies in the following areas:

---

### 1. Data Warehousing Architecture

- **Data Migration (ETL)** – moving raw CSV files to a **PostgreSQL** relational database using Python (`SQLAlchemy` / `Pandas`).
- **Data Modeling** – designing a professional **Star Schema**, the foundation of efficient data warehouses.
- **Data Layering** – implementing the **medallion architecture**:
  - `Bronze` – raw data
  - `Silver` – cleaned data
  - `Gold` – analytical views

---

### 2. Exploratory Analytics & BI (Exploratory Power BI)

- **EDA Visualization** – building the first **Power BI** dashboard to understand:
  - historical trends
  - logistics performance
  - geographical sales distribution in Brazil
- **Process Analysis** – identifying delivery process **bottlenecks** that affect customer satisfaction.

---

### 3. Advanced ML Modeling (Predictive Analytics)

- **Feature Engineering** – transforming temporal and logistics data into numerical features understandable by algorithms.
- **Classification (XGBoost)** – training a machine learning model to predict the **probability of customer dissatisfaction** (Churn / Satisfaction Prediction) based on order parameters.

---

### 4. Predictive Analytics in BI (Actionable Dashboard)

- **ML + BI Integration** – returning to Power BI to build a second, advanced dashboard.
- **Decision Support** – creating a report that not only shows **what happened** (history) but also indicates **what might happen** (prediction) and suggests actions.

---

## Future Directions

The project will evolve toward a **cloud-native, scalable data platform**:

- **Migration to Databricks** – moving the entire ETL process and `Bronze` / `Silver` / `Gold` layers to **Databricks** (leveraging Apache Spark for large-scale data processing).
- **Training Models in Databricks** – the environment will enable distributed ML libraries (e.g., `Spark MLlib`) and seamless integration with **Delta Lake**.
- **MLflow for Model Lifecycle Management** – experiment tracking, model registry, versioning, and production deployment – all within a single platform.

This will bring scalability, reproducibility, and professional MLOps to the project.

---

> The project currently combines **ETL**, **data modeling**, **visualization**, and **machine learning** – from raw CSV files to an interactive predictive dashboard. In the next stage, the entire pipeline will be migrated to **Databricks + MLflow**.
