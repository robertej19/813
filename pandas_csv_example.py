import pandas as pd

title = "cubedata.csv" #You can also specify a full path, e.g. "data/files/cubedata.csv"

""" df is the normal variable name for a pandas dataframe object. 
By default, pandas reads in the first row as column labels, use header=None to use
the first row as data instead of labels"""
df = pd.read_csv(title,header=None) 

"If you want to check what names you do have of your columns, do the following"
column_names = list(df.columns) 
print("\nThe column names in {} are {} \n".format(title,column_names))

"""The below demonstrates one way to access elements in your dataframe. 
The syntax is df.iloc[row number, column number]
Currently this prints out every value
Here we select to print out only one element; cell [5,5]"""
for row_i in df.index: #df.index is the number of rows in the dataframe
    for column_j in range(len(df.columns)): #len counts the number of elements in a list
        value = df.iloc[row_i,column_j]
        if (row_i == 3 and column_j == 5):
            print("The value of cell at row {} and column {} is {}\n".format(row_i,column_j,value))


"""Here is a quick way to check if you have any  null values (None or NaN) in your data
df.isnull() returns a boolean check of if each cell is null or not (TRUE if NULL)
.sum() then sums over all rows to give a count of how many null values exist in each column"""
print("Number of null values in each column: (column: nulls) \n{} \n".format(df.isnull().sum()))

"""Finally, here is a simple way to remove null values from your data
(Warning: do not do this blindly, you should be sure that this is in fact
what you want to be doing with your data)"""

length_before_filtering = len(df.index) #Just saving the original number of rows of the dataframe as a sanity check

for row_i in df.index:
    if (df.loc[row_i,column_names].isnull().sum()):
        print("Row {} has a null value, dropping from dataframe".format(row_i))
        df.drop(df.index[row_i], inplace=True) #inplace=True is needed as df.drop() otherwise won't return anything

"""The below is not needed, and just included to demonstrate that a row has actually
been dropped from the table (not that this does not change the csv file itself)"""
length_after_filtering = len(df.index)
print("""\n The dataframe originally had {} rows, now it has {} rows""".format(
    length_before_filtering,length_after_filtering))