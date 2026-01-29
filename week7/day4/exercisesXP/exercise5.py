import pandas as pd
import openpyxl


data = {
        'Flower_Name': ['Rose', 'Tulip', 'Sunflower', 'Daisy'],
        'Color': ['Red', 'Pink', 'Yellow', 'White'],
        'Quantity': [10, 15, 7, 20]
    }

df = pd.DataFrame(data)
print(df)

excel_filename = "exported_flowers.xlsx"
df.to_excel(excel_filename, sheet_name='Sheet1')
print(f"\nSuccessfully exported to: {excel_filename}")


json_filename = "exported_flowers.json"
df.to_json(json_filename, orient='records')
print(f"Successfully exported to: {json_filename}")