#Importing Libraries
import numpy as np

str_matrix = [["H", "H", "H", "-1", "-1", "-1", "B"],
              ["H", "H", "H", "-1", "-1", "B", "B"],
              ["-1", "H", "H", "-1", "-1", "-1", "B","B","-1"]];

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Replacing "-1" values
  # 1)"-1" s should not be the start of the day
  # 2)Continuous occurance >= 2
  # 3) Then, it will be replaced with the previous String tag

for row in str_matrix:

    count=0;  #For counting number of consequetive -1
    current= None;  #Initiate current value to None
    previous_value = None;  # Initialize to None before the first element in each row

    for i in range(len(row)):
        if row[i] == "-1":  #Counting number of -1
            if previous_value is not None:
                count+=1;

        else:
            current=i;
            previous_value=row[current-count-1];
            if(count>=2):
              for k in range((current-count),(current)):  # Replace -1 with the previous value
                row[k]=previous_value;
            count=0;  #set back to 0

# Printing the updated matrix
for row in str_matrix:
    print(row);

#-----------------------------------------------------------------------------------------------------------------------------------------

