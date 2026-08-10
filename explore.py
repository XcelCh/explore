import pandas as pd
import seaborn as sns

class explore:
    
    def __init__(self, data):
        self.data = data

        self.dtypes = self.pdtypes(data)
        self.null = data.isnull().sum()
        self.min = self.get_min(data)
        #self.max = data.max()
    
    def pdtypes(self, data):
        """
        Parse data type of every column in the DataFrame.

        Args:
            data (pandas.DataFrame): data to be parsed.

        Returns:
            dict: key value object of data type and lists of column names.
        """

        """
        Keys: Every data type that exists in the data.
        Vals: Every column that belongs to that data type in a list structure. 
        """
        dtypes = data.dtypes
        out_key = [(key.kind, key.name) for key in dtypes.unique().tolist()]
        print(out_key)
        return {keyk.kind:[{keyv.name:[val for val in dtypes.index.to_list() if dtypes[val].name == keyv.name] for keyv in dtypes.unique().tolist()} for valk in dtypes.index.to_list() if dtypes[valk].kind == keyk.kind] for keyk in dtypes.unique().tolist()}

    def get_min(self, data):
        return []#data[self.dtypes['int64']].min()
    

df = sns.load_dataset('titanic')
exp = explore(df)

#print(exp.dtypes)