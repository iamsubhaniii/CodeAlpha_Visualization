import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SalesRec.csv")

# Show columns
print(df.columns)

# 1. Bar Chart (Top 10 Sales)
df.head(10).plot(kind='bar')
plt.title("Top 10 Records")
plt.show()

# 2. Histogram (Numeric column)
df.select_dtypes(include=['int64','float64']).hist(figsize=(10,8))
plt.suptitle("Histogram of Numeric Columns")
plt.show()

# 3. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()