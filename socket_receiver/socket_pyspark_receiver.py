import pyspark.sql.functions as F

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WB72698").getOrCreate()

df = (
    spark
    .readStream
    .format("socket")
    .option("host", "host.docker.internal")
    .option("port", "9999")
    .load()
)

df = df.select(
        F.col("value").cast('string').alias("otrzymany tekst"),
    )
df = df.select(
    F.col("otrzymany tekst"),
    F.length("otrzymany tekst").alias("ilosc znakow"),
    F.size(F.split("otrzymany tekst", " ")).alias("ilosc slow"),
)

query = (
    df.writeStream
    .outputMode("append")
    .option("truncate", "false")
    .format("console")
    .start()
    .awaitTermination()
)
