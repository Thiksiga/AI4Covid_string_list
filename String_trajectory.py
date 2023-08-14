# import necessary libraries
import pandas as pd
import os
import glob
import re


#Variable initializtion
string_list=[]


# use glob to get all the csv files
# in the folder
path_num = "C:\AI4Covid\DATA\clusters\eps1minPTS5"   #os.getcwd() //MANUALLY SET FOLDER PATH//
csv_files_num = glob.glob(os.path.join(path_num, "*.csv"))

path_catalog = "C:\AI4Covid\DATA\catalogues\csv_files"   #os.getcwd() //MANUALLY SET FOLDER PATH//
csv_files_catalog = glob.glob(os.path.join(path_catalog, "*.csv"))

# loop over the list of csv files
for f in csv_files_num:
    # read the csv file
    df = pd.read_csv(f)

    # print the location and filename
    # print('Location:', f)
    f_name=f.split("\\")[-1]

    # # print the content
    # print('Content:')
    # print(df)
    # print()
    numbered_cluster = df["Cluster_DBSCAN_0.0001_5"].values.tolist()        #CLUSTER NUMBER COLUMN NAME
    # print(numbered_cluster)

    for fl in csv_files_catalog:
        fl_name=fl.split("\\")[-1]  #CATALOG FILE NAME SPLIT
        epsminPTS=fl_name.split("_")[-1]    #EPSMINPTS VALUE

        csv_name=f_name.split("_")[0]
        catalog_name = fl_name.split("_")[0]
        # print(csv_name)
        # print(catalog_name)
        if(csv_name==catalog_name):
            numbered_cluster_copy=[]
            print(csv_name,"=",catalog_name,"----->",epsminPTS)
            df_tag=pd.read_csv(fl,header=None)
            key=df_tag.iloc[:, [0]].values.tolist()
            tag= df_tag.iloc[:, [1]].values.tolist()
            # print(type(key[0]))
            # print(key)
            # print(tag)
            # print(numbered_cluster[1])

            for i in range(len(numbered_cluster)):
                # print(i,"val:=",numbered_cluster[i])
                if(numbered_cluster[i]==-1):
                    # print("O_L")
                    numbered_cluster_copy.append("O_L")

                else:
                    end = len(key)
                    # print(end)
                    for j in range(end):
                        # print("j=",j)
                        # print("key=",(key[j][0]))
                        # print("num_cl=",numbered_cluster[i])
                        if(numbered_cluster[i]==key[j][0]):
                            # print("tag=",tag[j-1][0])
                            numbered_cluster_copy.append(tag[j][0])
                            # print(numbered_cluster_copy)

            print(numbered_cluster_copy)


