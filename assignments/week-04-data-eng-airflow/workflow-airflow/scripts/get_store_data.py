import pandas as pd
from pathlib import Path

#path = Path(__file__).parent.parent.resolve()
#filename = 'dat/train_comb.csv'
#data = pd.read_csv(path.joinpath(filename)) 
data = pd.read_csv('/Users/toyosibamidele/Desktop/FourthBrainMLELocal/FourthBrainMLE/assignments/week-04-data-eng-airflow/dat/train_comb.csv')
data_store1 = data[data.Store==1]
#ofname = filename.replace('train_comb', 'train-store1')
#data_store1.to_csv(path.joinpath(ofname), index=False)
data_store1.to_csv('train-store1.csv', index=False)

#/Users/toyosibamidele/Desktop/FourthBrainMLELocal/FourthBrainMLE/assignments/week-04-data-eng-airflow/dat/train_comb.csv
#/Users/toyosibamidele/Desktop/FourthBrainMLELocal/FourthBrainMLE/assignments/week-04-data-eng-airflow/dat