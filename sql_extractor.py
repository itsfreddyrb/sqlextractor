import gzip
import re
import sys

def read_file(file_path):
    if file_path.endswith('.gz'):
        with gzip.open(file_path, 'rt', encoding='utf-8') as f:
            content = f.read()
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    return content

def extract_table_data(input_file, table_name, output_file):
    # Read the input SQL file (compressed or not)
    content = read_file(input_file)

    # Extract the CREATE statement for the specified table
    create_table_pattern = r"CREATE TABLE `?" + table_name + r"`?\s?\(.*?\);"
    create_table = re.search(create_table_pattern, content, flags=re.DOTALL)

    if create_table is None:
        print(f"Table '{table_name}' not found.")
        return

    # Extract the INSERT statements for the specified table
    insert_pattern = r"INSERT INTO `?" + table_name + r"`? .*?;"
    inserts = re.findall(insert_pattern, content)

    # Write the extracted statements to the output SQL file
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(create_table.group(0) + "\n")

        for insert in inserts:
            f_out.write(insert + "\n")

    print(f"Table '{table_name}' data has been written to {output_file}")

if __name__ == "__main__":


    if len(sys.argv) != 4:
        print("Extract table from gz.sql or sql file")
        sys.exit(1)

    input_file = sys.argv[1]
    table_name = sys.argv[2]
    output_file = sys.argv[3]


    extract_table_data(input_file, table_name, output_file)
