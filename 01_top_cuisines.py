import pandas as pd
df = pd.read_csv("restaurant_data.csv")
print(df.shape)
# top 3 most common cuisines
print(df["Cuisines"].head(3))

 #persentage of restaurants
cuisine_counts = df["Cuisines"].str.split(",").explode().value_counts()
total = len(df)
top3 = cuisine_counts.head(3)
for cuisine, count in top3.items():
    percentage = count / total *  100
    print(cuisine, round(percentage, 2), "%")
