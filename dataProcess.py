import os
import json
import time
import numpy as np
import pandas as pd
from tqdm import tqdm
from process import *
from ml import reduce_embedding_aae, reduce_embedding_pca
from utils import update_dataframe_with_conflict_resolution, seed_everything, LOCATION_MAPPING, SEED
from api import get_location

NROWS = None
IS_REDUCE = 1
EMBEDDING_DIM = 256

def main(file_path, nrows=None):

    seed_everything(seed=SEED)

    print(f"Loading csv file: {file_path}", end=" ")
    start_time = time.time()
    df = pd.read_csv(file_path, nrows=nrows)
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n") 
    
    print("Processing: roomInfo", end=" ")
    start_time = time.time()
    df[['shi', 'ting', 'floor_loc', 'total_floors', 'is_garage']] = df['roomInfo'].apply(lambda x: pd.Series(roomInfo_split(x)))
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n") 

    print("Processing: typeInfo", end=" ")
    start_time = time.time()
    df[['east', 'west', 'south', 'north', 'floor_type', 'decoration_type']] = df['typeInfo'].apply(lambda x: pd.Series(typeInfo_split(x)))
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n") 

    print("Processing: areaInfo", end=" ")
    start_time = time.time()
    df[['area', 'construct_time', 'construct_type']] = df['areaInfo'].apply(lambda x: pd.Series(areaInfo_split(x)))
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n") 

    print("Processing: aroundInfo")
    start_time = time.time()
    df[['estate_name', 'location']] = df['aroundInfo'].apply(lambda x: pd.Series(aroundInfo_split(x)))
    estate_list = set(df['estate_name'].to_list())
    location_dict_path = './data/location_dict.json'
    if os.path.exists(location_dict_path):
        with open(location_dict_path, 'r') as f:
            location_dict = json.load(f)
    else:
        location_dict = {}
    for item in tqdm(estate_list, desc="Processing location"):
        input_str = '北京市' + item
        if item not in location_dict:
            location_dict[item] = get_location(input_str)
            time.sleep(0.1)
    with open(location_dict_path, 'w') as f:
        json.dump(location_dict, f, ensure_ascii=False, indent=4)
    df_location = pd.DataFrame.from_dict(location_dict, orient='index', columns=['lng', 'lat'])
    df_location.reset_index(inplace=True)
    df_location.rename(columns={'index': 'estate_name'}, inplace=True)
    df = df.merge(df_location, how='left', left_on='estate_name', right_on='estate_name')
    df['location'] = df['location'].apply(lambda x: LOCATION_MAPPING.get(x.split()[0]))
    end_time = time.time()
    print(f"Processing: aroundInfo ({end_time - start_time:.2f}s)\n") 

    print("Processing: introContent", end=" ")
    start_time = time.time()
    args = ["shi", "ting", "wei", 
            "area", "floor_type", "construct_type", "floor_loc", "total_floors", "area_in", 
            "east", "west", "south", "north", 
            "construct_instruct", "decoration_type", "villa_type", 
            "ti", "hu", 
            "heating_type", "elevator"]
    new_columns = df['introContent'].apply(lambda x: pd.Series(introContent_split(x)))
    df = update_dataframe_with_conflict_resolution(df, new_columns, args)
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n") 

    print("Processing: transaction", end=" ")
    start_time = time.time()
    args = ["listing_time", "ownership", "last_transaction", "application", "houselife", "house_property", 
            "mortgage", "mortgage_amount", "mortgage_bank", "mortgage_repay", "spare"]
    new_columns = df['transaction'].apply(lambda x: pd.Series(transaction_split(x)))
    df = update_dataframe_with_conflict_resolution(df, new_columns, args)
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n") 

    embedding_path = "./data/baseInfo_embedding.npy"
    start_time = time.time()
    if os.path.exists(embedding_path):
        print("Loading: baseInfo", end=" ")
        text_embedding = np.load(embedding_path)
    else:
        start_time = time.time()
        text_embedding = pd.DataFrame(
            [baseInfo_split(x) for x in tqdm(df['baseInfo'], desc="Processing baseInfo")]
        )
        text_embedding = text_embedding.to_numpy(dtype=np.float32)
        os.makedirs("./data", exist_ok=True)
        np.save(embedding_path, text_embedding)
        print("Processing: baseInfo", end=" ")
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n")

    if IS_REDUCE:
        reduced_embedding_path = "./data/reduced_baseInfo_embedding.npy"
        print("Processing: baseInfo embedding reducing")
        start_time = time.time()
        # reduced_text_embedding = reduce_embedding_aae(text_embedding, latent_dim=EMBEDDING_DIM)
        reduced_text_embedding = reduce_embedding_pca(text_embedding, low_dim=EMBEDDING_DIM)
        os.makedirs("./data", exist_ok=True)
        np.save(reduced_embedding_path, reduced_text_embedding)
        df_reduced_embedding = pd.DataFrame(reduced_text_embedding, columns=[f'text_embedding_{i}' for i in range(EMBEDDING_DIM)])
        df = pd.concat([df, df_reduced_embedding], axis=1)
        end_time = time.time()
        print(f"Processing: baseInfo embedding reducing ({end_time - start_time:.2f}s)\n") 
    else:
        df_embedding = pd.DataFrame(text_embedding, columns=[f'text_embedding_{i}' for i in range(768)])
        df = pd.concat([df, df_embedding], axis=1)
    
    df.to_csv("./data/processed_data.csv", index=False)

if __name__ == '__main__':
    print("Start Processing!")
    start_time = time.time()
    file_path = './data/data.csv'
    main(file_path, NROWS)
    end_time = time.time()
    print(f"All Processing Finished! ({end_time - start_time:.2f}s)") 