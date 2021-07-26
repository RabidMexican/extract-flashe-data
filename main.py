import pyreadstat as py

DATA_FILES = ['demographic', 'diet', 'physical']
DATA_DIRECTORY = "data"
RESULTS_DIRECTORY = "results"

print('STARTING...')

for data_file in DATA_FILES:
    print('Starting next file...')

    df, meta = py.read_sav(f"{DATA_DIRECTORY}/{data_file}.sav")
    df.to_csv(f'{RESULTS_DIRECTORY}/{data_file}.csv')
