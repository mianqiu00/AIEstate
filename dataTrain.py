import time
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import seed_everything, convert_date_format, SEED
from ml import train_xgboost, train_random_forest, train_linear_regression, train_elasticnet_regression, train_mlp

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
    print(f"({end_time - start_time:.2f}s)") 

    # df = df.loc[:, ~df.columns.str.match(r'text_embedding_\d+')]  # drop text_embedding

    print("Loading Training Testing Data", end=" ")
    start_time = time.time()
    drop_columns = ['baseUrl', 'url', 'title', 'priceUnit', 'roomInfo', 
                    'typeInfo', 'areaInfo', 'aroundInfo', 'introContent', 'transaction', 
                    'baseInfo', "is_garage", "estate_name", "mortgage_bank"]
    df = df.drop(columns=drop_columns)

    X = df.drop(columns=['priceTotal'])
    y = df['priceTotal']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)
    end_time = time.time()
    print(f"({end_time - start_time:.2f}s)") 

    train_xgboost(X_train, X_test, y_train, y_test, plot=True, save_model=True)
    train_random_forest(X_train, X_test, y_train, y_test, save_model=True)
    train_linear_regression(X_train, X_test, y_train, y_test, save_model=True)
    train_elasticnet_regression(X_train, X_test, y_train, y_test, save_model=True)
    train_mlp(X_train, X_test, y_train, y_test)
    

if __name__ == '__main__':
    print("Start Training!")
    start_time = time.time()
    file_path = './data/processed_data.csv'
    main(file_path, NROWS)
    end_time = time.time()
    print(f"All Training Finished! ({end_time - start_time:.2f}s)") 