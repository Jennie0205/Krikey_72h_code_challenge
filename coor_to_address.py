import os
import time
from collections import defaultdict
from IPython.display import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.patches as mpatches
import seaborn as sns
from tabulate import tabulate
import reverse_geocoder as rg

df1_wVideos = pd.read_csv('./watchedVideo.csv',index_col = [0])

print(tabulate(df1_wVideos.head(3), headers='keys', tablefmt='psql'))


## Coordinate data column clean up
df1_wVideos['coordinates'] = df1_wVideos['coordinates'].apply(lambda x: x.replace("Decimal", ""))\
                            .apply(lambda x: x.replace("(", "")).apply(lambda x: x.replace(")", ""))\
                            .apply(lambda x: x.replace("'", ""))


df1_wVideos['address'] =''
df1_wVideos['country'] =''
df_temp = df1_wVideos['coordinates'].str.split(',', expand=True)
for i in range(len(df1_wVideos['address'])):
  if(i%10 == 0):
      print(i)
  addr = rg.search( (df_temp[0][i], df_temp[1][i]))   ## addr is ordered dict
  address_string = dict(addr[0]).get('cc')  + '  ' +   dict(addr[0]).get('admin1')  + '  ' +  dict(addr[0]).get('admin2') + '  ' +  dict(addr[0]).get('name')
  df1_wVideos['address'].iloc[i] = address_string
  df1_wVideos['country'].iloc[i] = dict(addr[0]).get('cc')

df1_wVideos.head(5)

df1_wVideos.to_csv('./df1_wVideo_w_addr.csv', index=False)
