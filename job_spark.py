from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("DesafioSpark")
    .getOrCreate()
)

censo = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load("s3://datalake-elvis-desafio-igti-estudo-920036772581/raw-data/censo2020/matricula_*.CSV")
)

(
    censo
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("CO_UF")
    .save("s3://datalake-elvis-desafio-igti-estudo-920036772581/staging/censo2020")
)