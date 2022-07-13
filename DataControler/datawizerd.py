import numpy as np
import pandas as pd

def datawiz():
    data = pd.read_csv("dataSet/database.csv")
    #gets ride of column and row labled ID
    data = data.drop('ID', axis=1)
    #finds all columns where data has 66% or more null values
    null_columns = data.loc[:, data.isna().sum() > 0.66 * data.shape[0]].columns
    #gets ride of row with those null columns
    data = data.drop(null_columns, axis=1)
    # fills into the column Root Mean Square and fills in the mean of the root
    data['Root Mean Square'] = data['Root Mean Square'].fillna(data['Root Mean Square'].mean())
    #data drop row 0 not sure what rest_index does
    data = data.dropna(axis=0).reset_index(drop=True)
    # sets new column called month and adds second line of  date
    data['Month'] = data['Date'].apply(lambda x: x[0:2])
    data['Day'] = data['Date'].apply(lambda x: x[3:-5])
    # sets new column called year and fills it with last four line from data date column
    data['Year'] = data['Date'].apply(lambda x: x[-4:])
    # drops the Date column
    data = data.drop('Date', axis=1)
    # sets mounth as an int type using numpy
    data['Month'] = data['Month'].astype(np.int)
    # set year as a string type and adds a Z at the end  why add a Z a
    data[data['Year'].str.contains('Z')]
    # if Year has a Z in it....
    invalid_year_indices = data[data['Year'].str.contains('Z')].index
    data = data.drop(invalid_year_indices, axis=0).reset_index(drop=True)
    data['Year'] = data['Year'].astype(np.int)
    data['Day'] = data['Day'].astype(np.int)
    # creats a new column called Hours and fills it with the second line in Time and turns it into a int
    data['Hour'] = data['Time'].apply(lambda x: np.int(x[0:2]))
    data = data.drop('Time', axis=1)
    data['Status'].unique()
    data['Status'] = data['Status'].apply(lambda x: 1 if x == 'Reviewed' else 0)
    return data


datawiz()