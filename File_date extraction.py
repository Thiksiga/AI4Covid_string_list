import pandas as pd
import glob
import os
import csv

# path_num = "C:\AI4Covid\DATA\clusters\eps1minPTS5"   #os.getcwd() //MANUALLY SET FOLDER PATH//
# csv_files_num = glob.glob(os.path.join(path_num, "*.csv"))
f=f"C:\AI4Covid\DATA\clusters\eps1minPTS5\Avishka_Perera.xlsx_ClusterData.csv"
# for f in csv_files_num:
df=pd.read_csv(f)
f_name=f.split("\\")[-1]
print(f_name)

# Extract unique dates
df_conv=pd.to_datetime(df['Date'])
unique_dates = df_conv.dt.date.unique()

# print(unique_dates)
# print(type(unique_dates))
summary=pd.DataFrame(columns=['cluster_num'])

cluster=df['Cluster_DBSCAN_0.0001_5']

for i in df.Date:
    I=pd.to_datetime(i)

    for j in unique_dates:
        if(j==I.date()):
            print('Same',i)
            summary = summary._append({'cluster_num':cluster},ignore_index=True)

    print(summary)

    mapfolder_path = f"C:\AI4Covid\DATA\clusters\eps1minPTS5\date_sep"
    mapfile_path = f"{mapfolder_path}\{i}.csv"

    summary.to_csv(mapfile_path, index=False)

