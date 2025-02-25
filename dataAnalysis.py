import time
import pandas as pd
from analysis import discrete_variable_analysis, continuous_variable_analysis
from utils import seed_everything, convert_date_format
from utils.Constants import *

NROWS = None

def main(file_path, nrows=None):
    seed_everything(SEED)

    print("Loading Macrofactor Data", end=" ")
    start_time = time.time()
    df = pd.read_csv(file_path, nrows=nrows)
    """reference: https://zjw.beijing.gov.cn/bjjs/fwgl/tzgg/436435234/index.shtml"""
    quota_policy_time = "2024年4月30日"
    quota_policy_time = convert_date_format(quota_policy_time)
    df['quota_policy'] = df.apply(lambda row: 1 if row['listing_time'] > quota_policy_time else 0, axis=1)
    """reference: www.gov.cn/yaowen/liebiao/202410/content_6982922.htm"""
    LPR_policy_time = "2024年9月29日"
    LPR_policy_time = convert_date_format(LPR_policy_time)
    df['LPR_policy'] = df.apply(lambda row: 1 if row['listing_time'] > LPR_policy_time else 0, axis=1)
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)\n") 
    
    print("Analysing Discrete Variables")
    start_time = time.time()
    for column_name in COLUMN_NAME_MAPPINGS.keys():
        discrete_variable_analysis(df, column_name)
    end_time = time.time()
    print(f"Analysing Discrete Variables ({end_time - start_time:.2f}s)\n") 

    print("Analysing Continuous Variables")
    start_time = time.time()
    continuous_columns = ["area", "area_in", "listing_time", "mortgage_amount"]
    for column_name in continuous_columns:
        continuous_variable_analysis(df, column_name)
    end_time = time.time()
    print(f"Analysing Continuous Variables ({end_time - start_time:.2f}s)\n") 

if __name__ == '__main__':
    print("Start Analysing!")
    start_time = time.time()
    file_path = './data/processed_data.csv'
    main(file_path, NROWS)
    end_time = time.time()
    print(f"All Analysis finished! ({end_time - start_time:.2f}s)\n") 