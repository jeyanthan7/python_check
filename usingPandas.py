import pandas as pd
import re

df = pd.read_csv("/Users/jeyanthanc/Downloads/git_clone/python_check/files/input.csv",dtype = str)
#df.to_parquet('/Users/jeyanthanc/Downloads/git_clone/python_check/files/input.csv')
#dy = pd.read_parquet(path="/Users/jeyanthanc/Downloads/git_clone/python_check/files/input.parquet")

for _, row in df.iterrows():
    print (row['name'])