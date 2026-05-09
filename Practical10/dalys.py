import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('D:/IBI/')
print(os.getcwd())
print(os.listdir())
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
print(type(dalys_data))
print(dalys_data.head())
print(dalys_data.info())
print(dalys_data.describe())
print(dalys_data["Entity"])

print(dalys_data.iloc[0:10,3])