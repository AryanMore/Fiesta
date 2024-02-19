import csv

# Specify the paths of your input and output CSV files
input_file_path = 'Reviews Data.csv'
output_file_path = 'reduced_File.csv'

# Specify the columns you want to extract (replace with your desired column names)
columns_to_extract = ['SKU', 'PRODUCT_NAME', 'PRICE', 'PRODUCT_CATEGORY', 'REVIEW_COUNT', 'REVIEW_DATE']

def extract_columns(csv_reader, columns_to_extract):
    extracted_columns = []
    header_row = next(csv_reader)  # Read the header row to get column names
    
    for row in csv_reader:
        extracted_row = [row[header_row.index(column_name)] for column_name in columns_to_extract]
        extracted_columns.append(extracted_row)
    
    return extracted_columns

# Read data from input CSV file
with open(input_file_path, 'r', encoding='utf-8-sig') as input_file:
    csv_reader = csv.reader(input_file)
    
    # Extract the specified columns
    extracted_columns = extract_columns(csv_reader, columns_to_extract)

# Write the extracted columns to a new CSV file
with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Write the header row
    csv_writer.writerow(columns_to_extract)
    
    # Write the extracted rows
    csv_writer.writerows(extracted_columns)

print(f"Columns {columns_to_extract} extracted from {input_file_path} and saved to {output_file_path}.")