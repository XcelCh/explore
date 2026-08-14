from collections import Counter

class Text:
    
    def __init__(self, exp):
        self.exp = exp
        
        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name, data type)) from dtypes attribute.
        2. Filter whether key (character code) belong to 'OST' (object, byte string, and StringDType).
        3. Getting val (column name) from vals (list of tuple(column name, data type)).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'OST' for val in vals if val[1] == 'str']
        
        """
        Dict comprehension structure:
        1. Getting the length of every text from every column.
        """
        self.length = {key: self.exp.data[key].str.len() for key in self.columns}
        
        self.longest_text = self.__longest_text()
        self.shortest_text = self.__shortest_text()
        self.count_empty = self.__count_empty()
        self.count_occur = self.__count_occur()
        self.has_symbol = self.__has_symbol()
        
    def __longest_text(self):
        """
        Retrieve the longest text by length for every row from every column with string data.

        Args:
            -
        
        Returns:
            dict: column name and list of text with the longest length.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting every val (text) with the longest text and put it in a set.
        """
        
        return {key: {val for val in self.exp.data[self.length[key] == self.length[key].max()][key]} for key in self.columns}    
        
    def __shortest_text(self):
        """
        Retrieve the shortest text by length for every row from every column with string data.

        Args:
            -
        
        Returns:
            dict: column name and list of text with the shortest length.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting every val (text) with the shortest text and put it in a set.
        """
        
        return {key: {val for val in self.exp.data[self.length[key] == self.length[key].min()][key]} for key in self.columns}
    
    def __count_empty(self):
        """
        Count empty text in every column with string data.

        Args:
            -
        
        Returns:
            dict: column name and total count of row with emtpy text.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Calculate total number of empty text.
        """
        
        return {key: (self.exp.data[key] == '').sum() for key in self.columns}
        
    def __count_occur(self):
        
        return {key: Counter(self.exp.data[key]) for key in self.columns}
        
    def __has_symbol(self):
        
        return {key: self.exp.data[key].str.contains('[^a-zA-Z0-9]', regex=True).any() for key in self.columns}