import pandas as pd

# Load the Excel file
file_path = "villageid.xlsx"  
data = pd.read_excel(file_path)

sql_queries = [
    f"INSERT INTO Village (VillageName, TalukaId) VALUES ('{row['VillageName']}', {row['TalukaId']});"
    for _, row in data.iterrows()
]


with open('output_queries.sql', 'w') as file:
    file.write('\n'.join(sql_queries))

with open('output_queries.txt', 'w') as file:
    file.write('\n'.join(sql_queries))



print("SQL queries have been saved to output_queries.sql")
print("SQL queries have been saved to output_queries.txt")