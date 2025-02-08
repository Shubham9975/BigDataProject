# BigDataProject
![NewProjFlow](https://github.com/user-attachments/assets/f3412cf0-61ca-4f0b-9fb9-c9ef5eb61501)

# Amazon Customer Sales Pipeline

## Overview
This project processes the **Amazon Customer Reviews Dataset** using **AWS services** for **ETL (Extract, Transform, Load)**. The pipeline performs **data cleaning, transformation, and visualization** to analyze product performance and customer sentiments.

## **Architecture**
### **Workflow:**
1. **Triggering the ETL Pipeline**
   - GitHub Actions triggers AWS CLI commands to start the pipeline.

2. **Data Storage**
   - Raw data is stored in **Amazon S3 (Data Lake)**.

3. **Data Cleaning (AWS Glue)**
   - Missing values and duplicates are removed using **AWS Glue**.

4. **Data Processing (EMR + Spark)**
   - Spark processes the raw dataset and **splits it into three structured datasets**:
     - **Customers Data** → `s3://smalldataset1/customers/`
     - **Products Data** → `s3://smalldataset1/products/`
     - **Reviews Data** → `s3://smalldataset1/reviews/`
   - Data is saved in **Parquet format** for optimized querying.

5. **Metadata Management (AWS Glue Crawler)**
   - AWS Glue Crawler scans the processed S3 data and updates the **AWS Glue Data Catalog**.

6. **Querying Data (Amazon Athena)**
   - Athena runs SQL queries on the **cleaned and transformed data**.

7. **Visualization (Power BI)**
   - Power BI connects to Athena for **interactive data visualization**.

---

## **Technologies Used**
| **Service**   | **Purpose** |
|--------------|------------|
| **Amazon S3** | Stores raw and processed data |
| **AWS Glue** | Cleans and catalogs data |
| **Apache Spark on EMR** | Processes and transforms data |
| **Amazon Athena** | Queries structured data |
| **Power BI** | Data visualization |
| **GitHub Actions** | Automates pipeline execution |

---

## **PySpark Script (Processing Steps)**
1. **Read Data**
   - Loads the raw dataset from **S3** using Spark.

2. **Process & Save Data**
   - Extracts **customer**, **product**, and **review** information.
   - Removes duplicates and missing values.
   - Saves the cleaned data in **Parquet format** to S3.

3. **Run AWS Glue Crawler**
   - Updates metadata in the AWS Glue Data Catalog.

---

## **How to Run**
### **Prerequisites**
- AWS CLI configured with **IAM permissions** for S3, EMR, and Glue.
- GitHub repository with **GitHub Actions** configured.

### **Steps**
1. **Trigger the GitHub Action manually** or set up a schedule.
2. **Monitor AWS EMR** to ensure the Spark job completes successfully.
3. **Run Glue Crawler** to update the Data Catalog.
4. **Query the transformed data using Athena**.
5. **Use Power BI for visualization**.

---

## **Example Queries in Amazon Athena**
```sql
-- Get top 10 best-rated products
SELECT product_id, product_title, AVG(star_rating) AS avg_rating
FROM "smalldatabase"."reviews"
GROUP BY product_id, product_title
ORDER BY avg_rating DESC
LIMIT 10;
