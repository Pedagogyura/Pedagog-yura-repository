import pandas as pd

file_path = '/mnt/data/airport-codes_csv.csv'

df = pd.read_csv(file_path)

ukraine_airports = df[df['iso_country'] == 'UA']

airport_names = ukraine_airports['name']

print("Названия аэропортов в Украине:")
for name in airport_names:
    print(name)
