import pandas as pd 
df=pd.read_csv("train.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())

#Check Missing Values
print("\n Missing Values:")
print(df.isnull().sum())

#Check Duplicate Rows
print(df.duplicated().sum())

#Remove Duplicate Rows
df=df.drop_duplicates()

#Fill Missing Values
df["Age"]=df["Age"].fillna(df["Age"].mean())

df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

df.drop("Cabin", axis=1, inplace=True)

print("\n Missing Values After Cleaning:")
print(df.isnull().sum())

#Check Data Type
print("\n Data Type:")
print(df.dtypes)

#Save Cleaned Dataset
df.to_csv("cleaned_data.csv",index=False)
print("\n Cleaned dataset saved successfully")