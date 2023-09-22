import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"D:\Python\PythonFiles\Datasets\spotify-2023.csv", encoding='latin-1')
plt.hist(df["released_year"],edgecolor = "black")
plt.show()
plt.bar(df.loc[1:10,"track_name"],df.loc[1:10,"in_spotify_playlists"])
plt.show()
plt.scatter(df["in_spotify_playlists"],df["in_apple_playlists"])
plt.show()

