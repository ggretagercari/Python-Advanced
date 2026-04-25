from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.lines import lineStyles

from kaggle_data.kaggl4e_dataset import average_iq_per_continent

df = pd.read_csv['avgIQperCountry.csv']

avg_iq_by_continent = df.groupby('Continent')('Average IQ'). mean()

plt.figure(figsize=(10,0))

average_iq_by_continent.plot(kind='lie', marker='o', color='skyblue')

plt.title("Average IQ by Continent")
plt.xlabel('Continent')
plt.ylabel('Average IQ')

plt.grid(axis='both', lineStyle='--', alpha=0.7)

plt.show()