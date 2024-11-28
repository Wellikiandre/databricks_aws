# Databricks notebook source
from delta.tables import *

# Cria DataFrames de exemplo
data1 = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
data2 = [("David", 23), ("Eva", 31), ("Frank", 40)]
data3 = [("George", 50), ("Hannah", 28), ("Ian", 35)]
columns = ["Name", "Age"]
df1 = spark.createDataFrame(data1, columns)
df2 = spark.createDataFrame(data2, columns)
df3 = spark.createDataFrame(data3, columns)

# Especifica os nomes das tabelas Delta
delta_table_name1 = "bronze.dados_abertos.xxx1"
delta_table_name2 = "bronze.dados_abertos.xxx2"
delta_table_name3 = "bronze.dados_abertos.xxx3"
silver_table_name = "silver.dados_abertos.unificada"

# Cria os catálogos e schemas se não existirem
spark.sql("CREATE CATALOG IF NOT EXISTS bronze")
spark.sql("CREATE CATALOG IF NOT EXISTS silver")
spark.sql("CREATE SCHEMA IF NOT EXISTS bronze.dados_abertos")
spark.sql("CREATE SCHEMA IF NOT EXISTS silver.dados_abertos")

# Salva os DataFrames como tabelas Delta
df1.write.format("delta").mode("overwrite").saveAsTable(delta_table_name1)
df2.write.format("delta").mode("overwrite").saveAsTable(delta_table_name2)
df3.write.format("delta").mode("overwrite").saveAsTable(delta_table_name3)

# Carrega as tabelas Delta
delta_table1 = DeltaTable.forName(spark, delta_table_name1)
delta_table2 = DeltaTable.forName(spark, delta_table_name2)
delta_table3 = DeltaTable.forName(spark, delta_table_name3)

# Unifica as tabelas bronze em uma tabela prata
df_silver = delta_table1.toDF().union(delta_table2.toDF()).union(delta_table3.toDF())

# Adiciona uma coluna com a soma das idades
from pyspark.sql.functions import sum
total_age = df_silver.agg(sum("Age").alias("Total_Age")).collect()[0]["Total_Age"]
df_silver = df_silver.withColumn("Total_Age", df_silver["Age"] + total_age)

# Salva o DataFrame como tabela Delta com mergeSchema habilitado
df_silver.write.format("delta").mode("overwrite").option("mergeSchema", "true").saveAsTable(silver_table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Img Exemplo
# MAGIC
# MAGIC [Exemplo 1](https://ibb.co/pZh314P)
# MAGIC
# MAGIC [Exemplo 2](https://ibb.co/jbqPwH2)
