import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("amazon_products.csv")

print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

#Top 10 Product
print("\nTop 10 Best Rated Products")

top_rated = df.sort_values(by="stars", ascending=False)

print(top_rated[["title", "stars", "price"]].head(10))

#Price Distribution Chart
plt.figure(figsize=(8,5))

sns.histplot(df["price"], bins=30)

plt.title("Product Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")

plt.savefig("price_distribution.png")
plt.show()

#Rating Distribution
plt.figure(figsize=(8,5))

sns.histplot(df["stars"], bins=10)

plt.title("Product Rating Distribution")
plt.xlabel("Stars")
plt.ylabel("Count")

plt.savefig("rating_distribution.png")
plt.show()

#Best Seller Chart
plt.figure(figsize=(6,4))

sns.countplot(x="isBestSeller", data=df)

plt.title("Best Seller Products")

plt.savefig("bestseller_chart.png")
plt.show()

#Price vs Rating
plt.figure(figsize=(8,5))

plt.scatter(df["price"], df["stars"], alpha=0.5)

plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Stars")

plt.savefig("price_vs_rating.png")
plt.show() 

#Missing Values
print("\nMissing Values")
print(df.isnull().sum())

#Insights
print("\n----- Insights -----")

print("1. Product prices analyzed.")
print("2. Rating distribution analyzed.")
print("3. Best seller products identified.")
print("4. Relationship between price and rating observed.")
print("5. Dataset contains very few missing values.")
