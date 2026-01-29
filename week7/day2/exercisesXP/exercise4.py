# ==============================================================================
# EXERCISE 4: DATA TYPE EXPLORATION (IRIS DATASET)
# Objective: Classify columns into Qualitative and Quantitative variables.
# ==============================================================================

import pandas as pd

# 1. Load the dataset (Make sure Iris.csv is uploaded to your Colab environment)
iris_df = pd.read_csv('Iris.csv')

# ------------------------------------------------------------------------------
# DATA CLASSIFICATION AND REASONING:
# ------------------------------------------------------------------------------

# 1. ID (Qualitative / Nominal)
# Reasoning: Even though it contains numbers, the ID acts as a unique label
# for each row. Mathematical operations like finding the "average ID" have
# no statistical meaning. It is strictly for identification.

# 2. SEPAL_LENGTH_CM (Quantitative / Continuous)
# Reasoning: This represents a physical, numerical measurement of the flower's
# sepal. Since it is a measured value that can have decimals, it is continuous.

# 3. SEPAL_WIDTH_CM (Quantitative / Continuous)
# Reasoning: Like sepal length, this is a physical dimension. It is a
# quantitative value because we can perform calculations (mean, median) on it.

# 4. PETAL_LENGTH_CM (Quantitative / Continuous)
# Reasoning: This is a numerical measurement of the petal's size. It provides
# a specific quantity that can be compared mathematically across different samples.

# 5. PETAL_WIDTH_CM (Quantitative / Continuous)
# Reasoning: This is a measurable numerical value. It is classified as
# quantitative because it represents a "how much" or "how big" aspect of the petal.

# 6. SPECIES (Qualitative / Nominal)
# Reasoning: This column contains categories (Setosa, Versicolor, Virginica).
# You cannot perform math on "Setosa." It is used to group the data into
# distinct classes based on characteristics.

# ------------------------------------------------------------------------------
# SUMMARY FOR YOUR REPORT:
# - Quantitative Variables: SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm
# - Qualitative Variables: Id, Species
# ------------------------------------------------------------------------------

# Quick check of data types in the console:
print(iris_df.info())