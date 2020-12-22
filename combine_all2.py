import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd)  

# load chapter .csv files and append
df = pd.DataFrame()
source = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        source = pd.read_csv(os.path.join(cwd, file), error_bad_lines=False)
        source['Chapter'] = file.split()[0]
        df = df.append(source) 
df.rename({'Indian Name':'blank'}) # rename culturally insensitive, unused column
df = df[ ['Chapter'] + [ col for col in df.columns] ]
df['Year'] = 2014
df = df[ ['Year'] + [ col for col in df.columns] ]
df.to_csv('summer2014_istarCamps.csv')