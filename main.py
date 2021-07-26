import os

import pyreadstat as py

DATA_DIRECTORY = "data"
RESULTS_DIRECTORY = "results"

print('Starting treatment of data files : \n')

for data_file in os.listdir(DATA_DIRECTORY):

    file_name = os.path.splitext(data_file)[0]
    print(f"=== {file_name} ===")

    df, meta = py.read_sav(f"{DATA_DIRECTORY}/{data_file}")
    df.to_csv(f'{RESULTS_DIRECTORY}/{file_name}.csv')

    print(f"{data_file}.csv created successfully !\n")
