import json
import os, csv

DATA_DIRECTORY = "test_data"
RESULTS_DIRECTORY = "test_results"

print('Starting treatment of data files : \n')

# treat every file in DATA_DIRECTORY
for data_file in os.listdir(DATA_DIRECTORY):
    f = open(f"{DATA_DIRECTORY}/{data_file}")
    row_nbr = 1

    reader = csv.reader(f)
    headers = next(reader, None)
    print(headers)

    for row in reader:
        print(row)
        i = 0
        json_answers = []

        for col in row:
            answer = {
                "question_label": headers[i],
                "value": col,
                "timestamp": {
                    "$date": 1627487674703
                }
            }
            json_answers.append(answer)
            i += 1

        print(f"WRITING FILE FOR ROW { row_nbr }")
        with open(f"{RESULTS_DIRECTORY}/{row_nbr}_{data_file}", 'w') as outfile:
            json.dump(json_answers, outfile)

        row_nbr += 1

