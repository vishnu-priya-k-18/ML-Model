# MACHINE LEARNING MODEL

## what is ML?
Machine Learning
* ML is a sort of data analysis where machine learn from data, identify patterns and predict or make decisions accordingly.

Example:

E-commerse - websites like flipkart and amazon use ML algorithm or ML model to provide relevant data to client.
## Steps to create ML model
import libraries
```
import numpy as np
import pandas as pd
```
import dataset using pandas
```
dataset = pd.read_csv("Data.csv")
```
separate independent [X] and dependent [Y] data
* Independent variables must present from 1st to last before column and dependent variable must in last column.
* This flow is followed in most ML model.
```
X = dataset.iloc[:,:-1] 
Y = dataset.iloc[:,-1]
```
