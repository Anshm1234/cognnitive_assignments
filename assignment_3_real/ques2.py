import pandas as pd
data = {    
    "Refund": ["yes","no","no","yes","no","no","yes","no","no","no"],
    "Marital_status": ["single","married","single","married","divorced","merried","divorced","single","married","single"],
    "Taxable_income": [125000,100000,70000,120000,95000,60000,220000,85000,75000,90000],
    "cheat": ["no","no","no","no","yes","no","no","yes","no","yes"]}
df=pd.DataFrame(data)
print(df.iloc[[0,4,7,8]])