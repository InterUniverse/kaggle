import pandas as pd
import numpy as np

path = "~/Documents/Projects/kaggle/titanic/data/raw/"

df_raw = pd.read_csv(f'{path}train.csv')

df_raw.info(memory_usage='deep')