# IMPORT NECESSARY LIBRARIES
import pandas as pd
import os
import glob
import re

# def Create_DataFrame(key_,val_):
#     data_ = {'key_': key_,
#              'value_': val_}
#     data_df = pd.DataFrame(data_)
#     print(data_df)
#     return data_df


path_num = "C:\AI4Covid\DATA\clusters\eps1minPTS5"   #CLUSTER DATA FOLDER PATH
csv_files_num = glob.glob(os.path.join(path_num, "*.csv"))

path_catalog = "C:\AI4Covid\DATA\catalogues\csv_files\eps1minPTS5"   #CATALOG FOLDER PATH
csv_files_catalog = glob.glob(os.path.join(path_catalog, "*.csv"))

# LOOP OVER THE LIST OF CSV FILES
for f in csv_files_num:
    # read the csv file
    df = pd.read_csv(f)

    f_name=f.split("\\")[-1]

    # CLUSTER NUMBER COLUMN NAME
    numbered_cluster = df["Cluster_DBSCAN_0.0001_5"].values.tolist()


    for fl in csv_files_catalog:
        fl_name=fl.split("\\")[-1]                  #CATALOG FILE NAME SPLIT
        epsminPTS=fl_name.split("_")[-1]            #EPSMINPTS VALUE

        csv_name=f_name.split("_")[0]
        catalog_name = fl_name.split("_")[0]

        # EXTRACT UNIQUE DATES
        df_conv = pd.to_datetime(df['Date'])
        unique_dates = df_conv.dt.date.unique()

        if(csv_name==catalog_name):
            numbered_cluster_copy=[]
            TIME_STAMP=[]
            dic_val=[]
            data_dict=[]
            print(csv_name,"=",catalog_name,"----->",epsminPTS)
            df_tag=pd.read_csv(fl,header=None)
            key=df_tag.iloc[:, [0]].values.tolist()
            tag= df_tag.iloc[:, [1]].values.tolist()

            date_ = df['Date'][0]
            print(date_)

            for i in range(len(numbered_cluster)):
                if(df['Date'][i]!=date_):

                    # #DATAFRAME FORMAT OUTPUT
                    # Create_DataFrame(TIME_STAMP,numbered_cluster_copy)


                    # SEPERATE LISTS OUTPUT
                    print(numbered_cluster_copy)
                    # print(TIME_STAMP)
                    date_=df['Date'][i]
                    print(date_)

                    #CLEARING THE LISTS
                    numbered_cluster_copy.clear()
                    # TIME_STAMP.clear()

                if(numbered_cluster[i]==-1):    #Replacing cluster number -1 (Outliers) with O_L
                    numbered_cluster_copy.append("O_L")
                    # TIME_STAMP.append(df.Time[i])

                else:                           #If not an outlier; replacing with the relavent tags
                    end = len(key)
                    for j in range(end):

                        if(numbered_cluster[i]==key[j][0]):
                            numbered_cluster_copy.append(tag[j][0])
                            # TIME_STAMP.append(df.Time[i])

            # Create_DataFrame(TIME_STAMP, numbered_cluster_copy)         #DATAFRAME OUTPUT
            # print(TIME_STAMP)                                           #LIST OUTPUT
            print(numbered_cluster_copy)



