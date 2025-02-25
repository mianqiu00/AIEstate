import os
import pandas as pd

all_data = pd.DataFrame()

for root, dirs, files in os.walk('./data_page'):
    for file in files:
        if file.endswith('.csv'):
            if 'output_data' in file:
                continue
            file_path = os.path.join(root, file)
            data = pd.read_csv(file_path)
            all_data = pd.concat([all_data, data], ignore_index=True)

all_data = all_data.drop_duplicates()
all_data.to_csv('./train.csv', index=False)

