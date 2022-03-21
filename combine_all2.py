import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd)  

# load chapter .csv files and append
df = pd.DataFrame()
source = pd.DataFrame()
book = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        source = pd.concat(pd.read_excel(os.path.join(cwd, file),sheet_name=None))
        df = pd.concat([df,source])
        
df.head()
