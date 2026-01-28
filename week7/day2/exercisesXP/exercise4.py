import pandas as pd


df = pd.read_csv('Iris.csv')

print(df.head())

# Id:	Qualitative (Nominal)	Although it consists of numbers, they are unique identifiers (labels) for each row. Performing math (like finding the average ID) provides no meaningful information.
# SepalLengthCm:	Quantitative (Continuous)	This is a numerical measurement of length in centimeters. It can be measured on a scale and averaged.
# SepalWidthCm:	Quantitative (Continuous)	Similar to sepal length, this is a physical measurement representing width.
# PetalLengthCm:	Quantitative (Continuous)	A measurable numerical value representing the length of the flower petal.
# PetalWidthCm:	Quantitative (Continuous)	A measurable numerical value representing the width of the flower petal.
# Species:	Qualitative (Nominal)	These are descriptive labels (e.g., Iris-setosa, Iris-versicolor) used to categorize the flowers into groups based on their type.