from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("test").getOrCreate()

sc=spark.sparkContext

rdd = sc.parallelize([1,2,3])

print(rdd.collect())







