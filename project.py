import json
import pandas as pd

# Load the JSON data
json_data = '''
{
    "main": [
        {
            "a": {
                "b": "1",
                "c": "2"
            },
            "d": "3"
        },
        {
            "a": {
                "b": "4",
                "c": "5"
            },
            "d": "6"
        }
    ]
}
'''

# Convert JSON to DataFrame
df = pd.json_normalize(json.loads(json_data), "main")

# Save DataFrame to Excel file
excel_file = "output.xlsx"
df.to_excel(excel_file, index=False)

print(f"JSON data has been successfully converted to Excel: {excel_file}")
