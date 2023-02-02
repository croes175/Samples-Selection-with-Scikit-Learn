import pandas as pd
from sklearn.model_selection import train_test_split

DATASET_NAME="EnergyEfficiency.data.txt"

dataset = pd.read_csv(DATASET_NAME,
                      skiprows=0)

#Variable estratificada

dataset_train, dataset_test = train_test_split(dataset, test_size=0.2, stratify=dataset["Y2"])