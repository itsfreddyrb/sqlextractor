# SQL Table Extractor

This Python script extracts a specific table's CREATE statement and all related INSERT statements from a .sql or .sql.gz file and writes them to a new .sql file. This tool is useful for extracting specific table data from large SQL dump files.

## Features

- Works with both .sql and .sql.gz files
- Extracts the CREATE statement for the specified table
- Extracts all related INSERT statements for the specified table
- Writes the extracted statements to a new .sql file

## Requirements

- Python 3.6+

## Usage

1. Clone this repository or download the extract_table.py script.

2. Open a terminal or command prompt and navigate to the directory where the script is saved.

3. Run the script with the following command:

```python extract_table.py path/to/input_file.sql_or_gz table_name output_file.sql```

Replace path/to/input_file.sql_or_gz with the actual path to your input .sql or .sql.gz file, table_name with the name of the table you want to extract, and output_file.sql with the desired output file name.

## Example

To extract the THISTABLE table from example.gz.sql and write the output to result.sql, run the following command:

```python extract_table.py path/to/example.gz.sql THISTABLE result.sql```

Replace path/to/example.gz.sql with the actual path to your example.gz.sql file.

## License

This project is licensed under the terms of the MIT License. See the LICENSE file for more information.
