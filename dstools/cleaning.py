import pandas as pd
import numpy as np

def check_dtypes(df:pd.DataFrame=None)-> dict:
    '''
    Check the types of columns

    Parameters:
            df (pandas.dataframe): A data frame that will be analysed          
    Returns:
            column_types (dict): A dictionary whose keys are the types found and values are lists containing the name of columns whose type is equal to the key they are in.
            
    '''
    column_types = {}
    for col, type_ in zip(df.columns.tolist(), df.dtypes):
        try:
            column_types[str(type_)].append(col)
        except:
            column_types[str(type_)] = [col]
    return column_types

def check_missing(df:pd.DataFrame=None, list_columns:list=None, list_of_missing=None) -> pd.Series:
    '''
    Check missing values in the columns

    Parameters:
            df (pandas.dataframe): A data frame that will be analysed
            list_columns (list): A list containing the columns to be analysed
            list_of_missing (list): A list containing the missing values types to be checked. If None, the function will look only for None and np.nan          
    Returns:
            series_missing (pd.Series): A pandas series whose keys are the columns and values are the rate of missing values [0, 1].
            
    '''
  if list_of_missing is not None:
      for missing in list_of_missing:
          df = df.replace({missing:None})

  if list_columns is None:
    series_missing = (df.isna().sum()/len(df))
    series_missing = series_missing.sort_values(ascending=False)
  else:
    series_missing = (df[list_columns].isna().sum()/len(df))
    series_missing = series_missing.sort_values(ascending=False)
  return series_missing

def check_constant_columns(df:pd.DataFrame=None, list_columns:list=None, threshold:float=0.85) -> tuple: 
    '''
    Finds and remove constant and quasi-constant columns

    Parameters:
            df (pandas.dataframe): A data frame that will be analysed
            threshold (float): A float number [0,1] indicating the maximum accepted ratio of unique values in the same column
            

    Returns:
            constant_columns (list): A list with the name of constant columns found
            quasi_constant_columns (list): A list with the name of quasi-constant columns
    '''
    print('Analysing Constant Columns')
    constant_columns = []
    quasi_constant_columns = []
    
    for i in df.columns: 
        
        if len(df[i].unique()) == 1:
            constant_columns.append(i)
        else:
            continue
            
            
    if len(constant_columns) > 0:
        print(f'{len(constant_columns)} Constant Columns Found')
        print(constant_columns)
    else:
        print('No Constant Column Found')
        
        
    for i in df.columns:
      series_value_counts = df[i].value_counts(normalize=True)
      if series_value_counts.iloc[0] > threshold:
          quasi_constant_columns.append(i)
      else:
          continue
  
    if len(quasi_constant_columns)> 0:
        print(f'{len(quasi_constant_columns)} Quasi-Constant Columns Found')
        print(quasi_constant_columns)
    else:
      print('No Quasi-Constant Column Found')
        
        
    return constant_columns, quasi_constant_columns