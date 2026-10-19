import pandas as pd
df = pd.read_csv("restaurant_data.csv")
print(df[["Latitude", "Longitude"]].head())
import matplotlib.pyplot as plt
plt.scatter(df["Longitude"], df["Latitude"], s=10)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographic Distribution of Restaurants")
plt.show()
print("Observations: ")
print("Restaurants are concentrated in certain geographic areas, forming visible clusters.")
print("Some locations have a higher concentration of restaurants, while others have fewer scattered restaurants.")