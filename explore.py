import pandas as pd
import numeric

class Explore:
    
    def __init__(self, data):
        self.data = data

        self.dtypes = self.pdtypes()
        
        self.null = data.isnull().sum()

        self.min = numeric.min(self)
        self.max = numeric.max(self)
    
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