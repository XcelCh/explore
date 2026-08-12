import pandas as pd

def min(exp):
    """
    Parse minimum value of column with relevant data types E.g. int, float, datetime.

    Args:
        -
    
    Returns:
        pandas.DataFrame: column name and minimum value parsed, similar to pandas.DataFrame.min.
    """

    """
    Dict comprehension structure: 
    1. Getting key (character code) and vals (list of tuple(column name, data type)) from dtypes attribute.
    2. Filter whether key (character code) belong to 'iufmM' (int, float, or datetime).
    3. Getting val (tuple(column name, data type)) from vals (list of tuple(column name, data type)).
    """
    return pd.DataFrame({val[0]:exp.data[val[0]].min() for key, vals in exp.dtypes.items() if key in 'iufmM' for val in vals}, index=[0])

def max(exp):
    """
    Parse maximum value of column with relevant data types E.g. int, float, datetime.

    Args:
        -
    
    Returns:
        pandas.DataFrame: column name and maximum value parsed, similar to pandas.DataFrame.max.
    """

    """
    Dict comprehension structure: 
    1. Getting key (character code) and vals (list of tuple(column name, data type)) from dtypes attribute.
    2. Filter whether key (character code) belong to 'iufmM' (int, float, or datetime).
    3. Getting val (tuple(column name, data type)) from vals (list of tuple(column name, data type)).
    """
    return pd.DataFrame({val[0]:exp.data[val[0]].max() for key, vals in exp.dtypes.items() if key in 'iufmM' for val in vals}, index=[0])