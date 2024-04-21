import csv
import os

def merge_csv_files(*paths, delimiter=';', only_shared_columns=False):
    
    data_list = []
    header_set = set()

    for path in paths:
        with open(path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            header_set.update(reader.fieldnames)
            data_list.extend([row for row in reader])

    if only_shared_columns:
        common_columns = set.intersection(*[set(row.keys()) for row in data_list])
        columns = ['name', 'id'] + [col for col in ['grade', 'age', 'email'] if col in common_columns]
    else:
        columns = ['name', 'id', 'grade', 'age', 'email']

    output_path = os.path.join(os.path.dirname(paths[0]), 'merged.csv')
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=delimiter)
        
        writer.writeheader()

        for entry in data_list:
            writer.writerow({col: entry.get(col, 'NaN') for col in columns})



# merge_csv_files('ex3_1.csv', 'ex3_2.csv', 'ex3_3.csv', delimiter=';', only_shared_columns=False)

# merge_csv_files('ex3_1.csv', 'ex3_2.csv', 'ex3_3.csv', delimiter=';', only_shared_columns=True)
