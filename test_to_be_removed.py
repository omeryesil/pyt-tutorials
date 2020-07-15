import numpy
import pandas as pd 

from pandas_datareader import data as wb 

pg = wb.DataReader('PG', data_source='yahoo', start='2020-01-01')

print (pg)


