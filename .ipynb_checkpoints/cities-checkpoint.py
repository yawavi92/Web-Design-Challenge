import pandas as pd

# Read the csv file in
df = pd.read_csv('Resources/assets/cities.csv')

# Save to file
df.to_html('datas.html', index=False)

# Assign to string
table = df.to_html()
print(table)