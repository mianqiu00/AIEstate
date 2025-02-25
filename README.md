# Beijing Second-hand Housing Data Analysis

This project aims to analyze second-hand housing listing data in Beijing for predicting housing price trends and analyzing the factors influencing housing prices.

## Environment Requirements

* Python 3.9.
* [Anaconda](https://www.anaconda.com/) containing all necessary packages.
* [PyTorch](https://pytorch.org/) version  2.6.0.
* For details, please refer to [Environment](./env.yaml).

## Install Dependencies

* Create and activate a virtual environment (recommended to use  `conda` or `venv`): 

```bash
conda env create -f env.yaml
conda activate estate
```

## Run the Project

* Run the project using the following script:

```bash
./run.sh
```

* Run in the background:

```bash
nohup ./run.sh > output.log 2>&1 &
```

# License

This project is licensed under the MIT License, which allows for free use, modification, and distribution of the code for academic and non-commercial purposes. For more details, please refer to the  [LICENSE](./LICENSE) file.