import csv

# Input CSV file path
input_file = 'C:/Users/Kamalkant More/Documents\Hackathon_work\Fiesta\Reviews Data_Origial.csv'
# Output CSV file path
output_file = 'C:/Users/Kamalkant More/Documents\Hackathon_work\Fiesta\Reviews Data.csv'

# Function to remove white spaces from all blocks of a row
def remove_whitespace(row):
    return [block.strip() for block in row]

# Choose the row you want to modify
row_index = 4  # For example, to modify the first row, use 0

# Read input CSV file and write modified data to output CSV file
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for i, row in enumerate(reader):
        if i == row_index:
            modified_row = remove_whitespace(row)
            writer.writerow(modified_row)
        else:
            writer.writerow(row)

print("Whitespace removed from row {} and saved to {}.".format(row_index, output_file))
