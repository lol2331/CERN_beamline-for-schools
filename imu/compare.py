import pandas as pd

# read the two sheets into separate dataframes
df1_value = pd.read_excel('imu1.xlsx', sheet_name="Sheet1")
df2_value = pd.read_excel('imu2.xlsx', sheet_name="Sheet1")

df1_bytes = pd.read_excel('imu1.xlsx', sheet_name="Sheet2")
df2_bytes = pd.read_excel('imu2.xlsx', sheet_name="Sheet2")
# iterate over each row in the first dataframe and compare to corresponding row in second dataframe
for index, row in df1_value.iterrows():
    error_of_value = abs(df1_value.iloc[index] - df2_value.iloc[index])
    print("The error of values is " + error_of_value)

    error_of_bytes = abs(df1_bytes.iloc[index] - df2_bytes.iloc[index])
    print("The error of bytes is " + error_of_bytes)