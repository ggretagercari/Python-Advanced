import pandas as pd
from numpy.ma.extras import average

data = pd.read_csv('avgIQpercountry.csv')

#print(data)

first_rows = data.head(10)
print(first_rows)


last_rows = data.tail(10)
print(last_rows)

data.sample(n=5)
data.sample(frac=0.5)

country_data = data['Country']
print(country_data)

subset = data[['Country', 'Average IQ']]
print(subset)

filtered_data - subset[subset['Average IQ'] > 130]
print(filtered_data)

null_mask = data.isnull()
null_count - null_mask.sum()
print("\nCount of null in each column: ")
print(null_count)

data.dropna(inplace=true)
print('\nDataset information after removing null values')
print(data.info())

duplicated_count = data.duplicated().sum()
print("\nCount of duplicate rows: ")
print(duplicated_count)

data.drop_duplicates(keep='last', inplace=true)

data['Population -  2023'] = data['Population -  2023'].apply(lambda x:float(x.replace(',','')))
print(data.info())

#group by 'Continent' and calculate average IQ
average_iq_per_continent = data.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)

#Sorting the average IQ per continent in descending order
sorted_average_iq_per_continent = average_iq_per_continent.sort_values(ascending=false)
print(sorted_average_iq_per_continent)

#Calculate the total Nobel Prizes by Contry
total_nobel_by_contry = data.groupby('Country')['Nobel Prices'].sum()
#Sort the total Nobel Prizes by contry in descending order
sorted_total_nobel_by_country = total_nobel_by_contry.sort_values(ascending= False)
#print the sorted total Prizes by Contry
print('\nTotal Nobel Prizes by country', sorted_total_nobel_by_country)
sorted_total_nobel_nonzero = sorted_total_nobel_by_country[sorted_total_nobel_by_country !=0]
print("\nTotal Nobeol Prizes by Country, excluding countries with Zero Nobel Prizes\n", sorted_total_nobel_nonzero)
