import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv("train.csv")

#Bar Chart
plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", data=df)

plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Count")

plt.savefig("bar_chart.png")
plt.show()

#Pie Chart
plt.figure(figsize=(6,6))

df["Survived"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    labels=["Not Survived","Survived"]
)

plt.title("Survival Percentage")

plt.savefig("pie_chart.png")
plt.show()

#Line Chart
plt.figure(figsize=(8,5))

df["Age"].sort_values().reset_index(drop=True).plot()

plt.title("Age Distribution Line Chart")
plt.xlabel("Passengers")
plt.ylabel("Age")

plt.savefig("line_chart.png")
plt.show()

#Histogram
plt.figure(figsize=(6,4))

plt.hist(df["Fare"], bins=20)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")

plt.savefig("histogram.png")
plt.show()

#Scatter Plot
plt.figure(figsize=(6,4))

plt.scatter(df["Age"], df["Fare"])

plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")

plt.savefig("scatter_plot.png")
plt.show()