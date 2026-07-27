import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv("marketing_campaign.csv", sep="\t") 

print(df.head())

print(df.columns)

#Dataset Information
print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

#Education Distribution
plt.figure(figsize=(8,5))

sns.countplot(x="Education", data=df)

plt.title("Education Distribution")
plt.xticks(rotation=30)

plt.savefig("education_distribution.png")
plt.show()

#Marital Status
plt.figure(figsize=(8,5))

sns.countplot(x="Marital_Status", data=df)

plt.title("Marital Status Distribution")
plt.xticks(rotation=30)

plt.savefig("marital_status.png")
plt.show()

#Income Distribution
plt.figure(figsize=(8,5))

sns.histplot(df["Income"], bins=20)

plt.title("Income Distribution")

plt.savefig("income_distribution.png")
plt.show()

#Age Analysis
df["Age"] = 2026 - df["Year_Birth"]

plt.figure(figsize=(8,5))

plt.hist(df["Age"], bins=20)

plt.title("Customer Age Distribution")

plt.savefig("age_distribution.png")
plt.show()

#Income vs Wines
plt.figure(figsize=(8,5))

plt.scatter(df["Income"], df["MntWines"])

plt.title("Income vs Wine Spending")

plt.xlabel("Income")

plt.ylabel("Wine Spending")

plt.savefig("income_vs_wines.png")
plt.show()

#Web Purchases
plt.figure(figsize=(8,5))

sns.histplot(df["NumWebPurchases"], bins=15)

plt.title("Web Purchases")

plt.savefig("web_purchases.png")
plt.show()

#Insights
print("\n----- Customer Insights -----")

print("1. Education levels analyzed.")
print("2. Marital status analyzed.")
print("3. Income distribution analyzed.")
print("4. Customer age analyzed.")
print("5. Income vs Wine spending analyzed.")
print("6. Online purchasing behavior analyzed.")

#Correlational Heatmap
plt.figure(figsize=(12,8))

numeric_df = df.select_dtypes(include=['number'])

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")
plt.show()

#Top 10 Highest Income Customers
print("\nTop 10 Highest Income Customers")

top_customers = df.sort_values(by="Income", ascending=False)

print(top_customers[["ID", "Income", "Education", "Marital_Status"]].head(10))

#Response Count
plt.figure(figsize=(6,4))

sns.countplot(x="Response", data=df)

plt.title("Campaign Response")

plt.xlabel("0 = No Response, 1 = Response")

plt.savefig("campaign_response.png")
plt.show()

#Wine Spending by Education
plt.figure(figsize=(10,5))

sns.barplot(x="Education", y="MntWines", data=df)

plt.title("Average Wine Spending by Education")

plt.xticks(rotation=30)

plt.savefig("wine_by_education.png")
plt.show()
