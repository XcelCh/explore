import pandas as pd

class Explore:
    
    def __init__(self, data):
        self.data = data

        self.dtypes = self.pdtypes()
        self.null = data.isnull().sum()
        self.min = self.pmin()
        self.max = self.pmax()
    
    def pdtypes(self):
        """
        Parse data type of every column in the DataFrame.

        Args:
            -

        Returns:
            dict: key value object of Numpy character code and lists of tuple that includes column name, data type, and category values if exist.
        """

        """
        Keys: numpy character code identifying the general data type E.g. one of 'biufcmMOSTUV'.
        Vals: Every column that belongs to the general data type in a list of tuples structure, 
              the tuple will contain column name, data type, and if exist category values.

        val_detail list comprehension structure:
        1. Getting idx (column name) from data.dtypes.
        2. Forming value of list comprehension consisting (column name, data type, and category values if exist) in a tuple data type.

        return dict comprehension structure:
        1. Getting available key (character code) from data.dtypes.
        2. Getting val (list of tuple(column name, data type, and category values if exist)) from val_detail with the same key (character code).
        """
        dtypes = self.data.dtypes
        val_detail = [(idx, dtypes[idx].name, dtypes[idx].categories.to_list()) if dtypes[idx].name == 'category' else (idx, dtypes[idx].name) for idx in dtypes.index.to_list()]
        
        return {key.kind:[val for val in val_detail if dtypes[val[0]].kind == key.kind] for key in dtypes.unique().tolist()}

    def pmin(self):
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
        return pd.DataFrame({val[0]:self.data[val[0]].min() for key, vals in self.dtypes.items() if key in 'iufmM' for val in vals}, index=[0])

    def pmax(self):
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
        return pd.DataFrame({val[0]:self.data[val[0]].max() for key, vals in self.dtypes.items() if key in 'iufmM' for val in vals}, index=[0])