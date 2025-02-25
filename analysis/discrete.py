import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import seaborn as sns
from utils.Constants import *


def discrete_variable_analysis(df, column_name):
    """
    :param df: Dataframe
    :param column_name: Column Name
    """

    font_name = "simhei"
    mpl.rcParams['font.family'] = font_name
    mpl.rcParams['axes.unicode_minus']=False

    if column_name not in COLUMN_NAME_MAPPINGS:
        return

    mapping = COLUMN_NAME_MAPPINGS[column_name]
    reverse_mapping = {v: k for k, v in mapping.items()} 

    value_counts = df[column_name].value_counts().sort_index()
    value_counts.index = value_counts.index.map(lambda x: reverse_mapping.get(x, f"暂无数据"))

    print(f"Column Name: {column_name}")
    print("Frequency:")
    print(value_counts)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=value_counts.index, y=value_counts.values, hue=value_counts.index, palette="viridis", legend=False)
    plt.title(f"{column_name} Distribution")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    if not os.path.exists('./output'):
        os.mkdir('./output')
    if not os.path.exists('./output/discrete'):
        os.mkdir('./output/discrete')
    plt.savefig(f"./output/discrete/{column_name}_distribution.png")
    print(f"Save figure ./output/discrete{column_name}_distribution.png\n")

