import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import seaborn as sns
from utils.Constants import *


def continuous_variable_analysis(df, column_name):
    """
    :param df: Dataframe
    :param column_name: Column Name
    """

    font_name = "simhei"
    mpl.rcParams['font.family'] = font_name
    mpl.rcParams['axes.unicode_minus']=False

    if column_name not in df.columns:
        return

    data = df[column_name]

    desc_stats = data.describe()
    print(f"Column Name: {column_name}")
    print("Discriptive Analysis:")
    print(desc_stats)

    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    sns.histplot(data, kde=True, color='blue', bins=30)
    plt.title(f"{column_name} Histplot")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    sns.boxplot(x=data, color='orange')
    plt.title(f"{column_name} Boxplot")
    plt.xlabel(column_name)

    plt.tight_layout()

    if not os.path.exists('./output'):
        os.mkdir('./output')
    if not os.path.exists('./output/continuous'):
        os.mkdir('./output/continuous')
    plt.savefig(f"./output/continuous/{column_name}_distribution.png")

