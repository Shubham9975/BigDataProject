from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder.appName("AmazonDataTransformation").getOrCreate()

# Read the input CSV file with tab separator
input_path = "s3a://newsmalldatabucket/smalldata/all.csv"
df = spark.read.csv(input_path, sep="\t", header=True, inferSchema=True)


# Define a function to handle transformations (except reviews)
def process_and_write(df, columns, unique_column, output_path):
    selected_df = df.select(columns).dropDuplicates([unique_column])
    selected_df.write.mode("overwrite").parquet(output_path)
    print(f"Data written successfully to: {output_path}")


# Process and write customers data
process_and_write(
    df,
    columns=["marketplace", "customer_id", "vine"],
    unique_column="customer_id",
    output_path="s3a://smalldataset1/customers/"
)

# Process and write products data
process_and_write(
    df,
    columns=["product_id", "product_parent", "product_title", "product_category"],
    unique_column="product_id",
    output_path="s3a://smalldataset1/products/"
)

# Process reviews data with review_date casted to date type
df_reviews = (
    df.select(
        "marketplace",
        "review_id",
        "customer_id",
        "product_id",
        "star_rating",
        "helpful_votes",
        "total_votes",
        "vine",
        "verified_purchase",
        "review_headline",
        "review_body",
        col("review_date").cast("date").alias("review_date")  # Explicitly cast review_date to date
    )
)

df_reviews.write.mode("overwrite").parquet("s3a://smalldataset1/reviews/")

# Stop SparkSession
spark.stop()
