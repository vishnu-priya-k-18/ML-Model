import numpy as np
import pandas as pd

dataset = pd.read_csv("Guide_Data.csv")

X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values


