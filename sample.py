import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./data/train.csv", nrows=10)
    df.to_csv("./data/sample.csv")
