import pandas as pd

# Series Programs
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

s2 = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s2)
print(s2["b"])
print(s2[s2 > 20])
print(s2 + 5)
print(s2.describe())

d = {"math": 90, "science": 85, "english": 78}
s3 = pd.Series(d)
print(s3)

# CSV File Reading Programs
sample_data = """id,name,age,salary,department
1,Alice,25,50000,HR
2,Bob,30,65000,IT
3,Charlie,35,70000,IT
4,David,28,48000,Finance
5,Eva,40,90000,HR"""

with open("employees.csv", "w") as f:
    f.write(sample_data)

df = pd.read_csv("employees.csv")

print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df["name"])
print(df[["name", "salary"]])
print(df[df["salary"] > 60000])
print(df[df["department"] == "IT"])
