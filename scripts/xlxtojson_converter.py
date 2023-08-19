import pandas as pd
import json

# Load the Excel file into a pandas DataFrame
excel_file = 'C:\Users\sunil\Desktop\Hackathon\ElectricityProductionFromCoalSources.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# Convert the DataFrame to a JSON object
json_data = df.to_json(orient='records')

# Save the JSON data to a file
output_json_file = 'ElectricityProductionFromCoalSources.json'
with open(output_json_file, 'w') as json_file:
    json_file.write(json_data)

print("Conversion completed. JSON data saved to", output_json_file)
