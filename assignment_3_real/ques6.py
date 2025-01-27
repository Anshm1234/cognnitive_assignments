import pandas as pd
data = {    
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]}
df=pd.DataFrame(data)
#1
# print(df.shape)

#2
# print(df.info())

#3
# print(df.describe())

#4
# print(df.iloc[0:6])
# print(df.iloc[-3:])

#5(1)
# descriptive=df.describe()
# print(descriptive.loc['mean'])

#5(2)
# print(df['Bonus'].sum())

#5(3)
# print(df['Age'].min())

#5(4)
# print(df['Rating'].max())

#6
# print(df.sort_values(by="Salary",ascending = False))

#7
# df["Performance"]=pd.cut(df["Rating"],bins=[0,4.0,4.5,5],labels=["Average","Good","Excelent"])
# print(df[["Name","Performance"]])

#8
# print(df.isnull().sum())

#9
# df.rename(columns={"Employee_ID" : "ID"},inplace=True)
# print(df)

#10(1)
# print( df[(df["Years_of_Experience"] > 8) ])

#10(2)
# print(df[(df["Department"] == "IT")])

#11
# df["Tax"]=df["Salary"]*0.1
# print(df["Tax"])

#12
df_csv = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df.to_csv("modified_employees.csv", index=False)
print("DataFrame saved to 'modified_employees.csv'")