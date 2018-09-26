#!/usr/bin/python

import pandas as pd

data = pd.read_csv("../GovData/NCHS_Leading_Causes_of_Death_United_States.csv")

df = pd.DataFrame(data)
print(df.dtypes)
