import pandas as pd
import glob
import os
import csv

# path_num = "C:\AI4Covid\DATA\clusters\eps1minPTS5"   #os.getcwd() //MANUALLY SET FOLDER PATH//
# csv_files_num = glob.glob(os.path.join(path_num, "*.csv"))
f=f"C:\AI4Covid\DATA\clusters\eps1minPTS5\Avishka_Perera.xlsx_ClusterData.csv"
# for f in csv_files_num:
df=pd.read_csv(f)
# print(df.Date)

# Extract unique dates
df_conv=pd.to_datetime(df['Date'])
unique_dates = df_conv.dt.date.unique()

# print(unique_dates)
# print(type(unique_dates))

for i in df.Date:
    I=pd.to_datetime(i)
    for j in unique_dates:
        if(j==I.date()):
            print('Same same same same same')


