import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns 

# Load Dataset
df=pd.read_csv("train.csv")
print(df.head())

print("\n Dataset Shape:")
print(df.shape)

print("\n Dataset Info:")
print(df.info())

print("\n Summary Statistics:")
print(df.describe())

#Missing Values
print("\n Missing Values:")
print(df.isnull().sum())

#Survival Count
print("\n Survival Count:")
print(df["Survived"].value_counts())

#Gender Count
print("\n Gender Count:")
print(df["Sex"].value_counts())

#Passenger Class
print("\n Passenger Class:")
print(df["Pclass"].value_counts())

#Average Age & Fare
print("\n Average Age:", df["Age"].mean())
print("Average Fare:", df["Fare"].mean())

#Survival Bar Chart
plt.figure(figsize=(6,4))
sns.countplot(x="Survived", data=df)

plt.title("Survival Count")
plt.xlabel("Survived (0=No, 1=Yes)")
plt.ylabel("Number of Passengers")

plt.savefig("survival_count.png")
plt.show()

#Gender Count Bar Chart
plt.figure(figsize=(6,4))
sns.countplot(x="Sex", data=df)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.savefig("gender_distribution.png")
plt.show()

#Passenger Class Chart
plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", data=df)

plt.title("Passenger Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")

plt.savefig("passenger_class_distribution.png")
plt.show()

#Age Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Age"].dropna(), bins=20)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.savefig("age_distribution.png")
plt.show()

#Fare Box Plot (Outliers)
plt.figure(figsize=(6,4))
sns.boxplot(y=df["Fare"])

plt.title("Fare Outliers")

plt.savefig("fare_outliers.png")
plt.show()

#Correlation Heatmap
plt.figure(figsize=(8,6))

sns.heatmap(df.select_dtypes(include=['number']).corr(),
            annot=True,
            cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")
plt.show()

#Insights
print("\n----- Insights -----")
print("1. Most passengers were in 3rd class.")
print("2. Male passengers were more than female passengers.")
print("3. Majority of passengers did not survive.")
print("4. Fare has some outliers.")
print("5. Average age of passengers is around 30 years.")
