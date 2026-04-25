from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.pyplot import ylabel

df = pd.read_csv('avgIQperCountry.csv')

nobel_prizes_by_continent = df.groupby('Continent')['Nobel Prizes'].sum()

no_of_continents = nobel_prizes_by_continent()
print(no_of_continents) #Output: 8

colors = ['gold', 'lightcoral', 'yellow', 'thistle', 'lightskyblue', 'orange', 'aquamarine', 'burlywood']
plt.figure(figsize=(10,10))

nobel_prizes_by_continent.plot(kind='pie', colors='colors', autopct='%1.1f%')
plt.title('Distribution of Nobel Prizes by Continent')

plt.axis('equal')
plt.ylabel('')

plt.tight_layout()
plt.show()
