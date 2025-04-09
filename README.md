# BigDataProject

![Big Data Project Architecture](https://github.com/user-attachments/assets/e9df7e9b-ae3c-40d9-84dc-f97b0cd612de)

# **Amazon Customer Sales Pipeline**

## **1. Problem Statement**  
### **Title**: Analyzing Customer Sentiments and Trends in Amazon Reviews to Enhance Product Strategies  

### **Objective**  
The project aims to **leverage big data analytics** to gain actionable insights into **customer sentiments, product performance, and market trends** from the **Amazon Customer Reviews dataset**. By analyzing large-scale review data, we can better understand customer feedback, identify trends, and support **data-driven decision-making** for product improvement and strategic planning.  

### **Key Questions**  
1. **Sentiment Analysis**: What are the overall sentiments expressed in customer reviews for different products, and how do they vary by product category or brand?  
2. **Trend Analysis**: How do review trends (e.g., ratings, review volume) evolve over time? Are there any noticeable patterns?  
3. **Rating Distribution**: What is the distribution of ratings across different products? Are there specific products or categories that receive consistently high or low ratings?  
4. **Product Comparison**: How do different products or brands compare in terms of customer satisfaction and review metrics?  
5. **Demographic Insights**: If demographic data is available, how do different customer segments rate products and express sentiments?  

---

## **2. Project Overview**  
### **Key Features**  
✔ **Data Storage**: Uses **Amazon S3** as a scalable data lake.  
✔ **Data Processing**: Cleans and transforms data using **AWS Glue & Apache Spark on EMR**.  
✔ **Querying**: Enables analysis with **Amazon Athena & AWS Glue Data Catalog**.  
✔ **Visualization**: Uses **Power BI** for trend analysis & insights.  
✔ **Automation**: GitHub Actions triggers **AWS CLI commands** to manage the ETL pipeline.  

---

## **3. Architecture Overview**  

### **Workflow**  
The project follows a structured **ETL pipeline** built on **AWS services** for **scalability, automation, and efficiency**.  

### **1️⃣ Data Ingestion (Amazon S3 - Data Lake)**  
- Raw customer review data is stored in **Amazon S3**.  
- This allows cost-effective, scalable storage for structured and unstructured data.  

### **2️⃣ Data Cleaning (AWS Glue - ETL Processing)**  
- **AWS Glue Jobs** remove **duplicates, missing values, and inconsistencies**.  
- The cleaned dataset is stored back in **Amazon S3** for further processing.  

### **3️⃣ Data Transformation (Amazon EMR + Apache Spark)**  
- **Apache Spark on AWS EMR** processes and restructures the data into three categories:  
  - **Customers Data** → `s3://smalldataset1/customers/`  
  - **Products Data** → `s3://smalldataset1/products/`  
  - **Reviews Data** → `s3://smalldataset1/reviews/`  
- Data is saved in **Parquet format** for optimized querying.  

### **4️⃣ Metadata Management (AWS Glue Crawler + Data Catalog)**  
- **AWS Glue Crawler** scans the processed S3 datasets.  
- The **AWS Glue Data Catalog** stores metadata for seamless querying.  

### **5️⃣ Data Querying (Amazon Athena)**  
- **Athena** runs **serverless SQL queries** directly on structured S3 data.  
- This eliminates the need for a dedicated database.  

### **6️⃣ Data Visualization (Power BI)**  
- **Power BI** connects to **Amazon Athena** for interactive dashboards.  
- Business insights include **customer sentiment trends, product performance, and rating analysis**.  

---

## **4. Technologies Used**  

| **Service**   | **Purpose** |
|--------------|------------|
| **Amazon S3** | Stores raw and processed data |
| **AWS Glue** | Cleans data, removes duplicates, updates metadata |
| **Amazon EMR (Spark)** | Transforms and structures data |
| **Amazon Athena** | Runs SQL queries on cleaned data |
| **AWS Glue Data Catalog** | Manages metadata for easy querying |
| **Power BI** | Visualizes insights and trends |
| **GitHub Actions** | Automates ETL pipeline execution |

---

## **5. Expected Outcomes**  

### ✅ **Insights Gained**  
- **Sentiment Analysis**: Understanding customer sentiment trends across different products and categories.  
- **Trend Identification**: Recognizing **shifts in customer feedback** over time.  
- **Product Performance Comparison**: Identifying top-performing products & areas for improvement.  
- **Strategic Recommendations**: Providing **data-driven insights** for marketing, sales, and product teams.  

### **Business Impact**  
This project helps **Amazon vendors, product managers, and marketing teams** make **informed decisions** by analyzing customer reviews efficiently. The **cloud-based ETL pipeline** ensures **scalability, automation, and real-time insights** for continuous improvement.  

---

## **6. Setup & Execution**  

### **Prerequisites**  
- AWS CLI configured with **IAM permissions** for S3, EMR, and Glue.  
- GitHub repository with **GitHub Actions** configured.  

### **Steps to Run the ETL Pipeline**  
1. **Trigger GitHub Action manually** (or schedule it to run automatically).  
2. **Monitor AWS EMR** to ensure the Spark job completes successfully.  
3. **Run Glue Crawler** to update the Data Catalog.  
4. **Query the transformed data using Athena**.  
5. **Use Power BI for visualization**.  

---

## **7. Sample Queries for Amazon Athena**  

### **1️⃣ Get top 10 highest-rated products**
```sql
SELECT product_id, product_title, AVG(star_rating) AS avg_rating
FROM "smalldatabase"."reviews"
GROUP BY product_id, product_title
ORDER BY avg_rating DESC
LIMIT 10;
```

---

## 8. Power BI Dashboard Summary

| #  | Visualization Title          | Insight Summary                                                                 |
|----|------------------------------|----------------------------------------------------------------------------------|
| 1  | Hidden Gem Products          | Detects highly rated (≥ 4.5) but underexposed products (low votes), ideal for marketing boosts. |
| 2  | Mismatch Alert               | Flags products with high star ratings but neutral review sentiment.             |
| 3  | Verified Complaints          | Highlights poorly rated verified purchases (< 3 stars) to identify quality issues. |
| 4  | Top Performing Categories    | Ranks product categories by positive sentiment for promotional planning.        |
| 5  | Helpful Review Gap           | Compares total and helpful votes to assess review quality.                      |
| 6  | Sentiment Waves              | Reveals seasonal/monthly sentiment trends.                                      |
| 7  | Top Performers by Sentiment | Lists best-reviewed products with loyalty metrics.                              |
| 8  | Trust Filter                 | Evaluates influence of non-verified reviews to detect manipulation.             |
| 9  | Voice of the Unhappy         | Word cloud highlights key complaints in negative reviews.                       |
| 10 | High-Traffic SKUs            | Shows most engaged products based on votes and reviews.                         |


### **🧠 Business Value and Impact**
**This report empowers Amazon’s product and marketing teams to:**

**Detect and fix product issues early**

**Promote underrated but high-potential items**

**Build customer trust through verified insights**

**Strategically allocate resources to trending and high-engagement products**

**Tailor campaigns based on real-time customer sentiment**

![Visualization Demo](https://github.com/Shubham9975/BigDataProject/blob/main/Insights.gif?raw=true)


