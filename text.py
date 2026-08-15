from collections import Counter

class Text:
    """
    A class to analyze text data in a pandas DataFrame.
    """
    
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
        
        self.longest = self.__longest()
        self.shortest = self.__shortest()
        self.count_empty = self.__count_empty()
        self.count_occur = self.__count_occur()
        self.has_symbol = self.__has_symbol()
        
    def __longest(self):
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
        
    def __shortest(self):
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
        """
        Count occurence of every text in every column with string data.
        
        Args:
            -
        
        Returns:
            dict: column name and counter of text occurence.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Calculate total occurence of each text.
        """
        
        return {key: Counter(self.exp.data[key]) for key in self.columns}
        
    def __has_symbol(self):
        """
        Check if any text in every column with string data contains symbols.

        Args:
            -

        Returns:
            dict: column name and boolean indicating if any text contains symbols.
        """
        
        """
        Dict comprehension structure:
        1. Getting key (column name) from every column.
        2. Check if any text contains symbols using regex.
        """

        return {key: self.exp.data[key].str.contains('[^a-zA-Z0-9]', regex=True).any() for key in self.columns}

    def __str__(self):
        """
        String representation of the Text class.

        Returns:
            str: A string representation of the Text class.
        """
        return f"Columns with text values: {self.columns}\n\n" \
                f"shortest text: {self.shortest}\n\n" \
                f"longest text: {self.longest}\n\n" \
                f"Count of Empty Text: {self.count_empty}\n\n" \
                f"Count of Text Occurrences: {self.count_occur}\n\n" \
                f"Has Symbols: {self.has_symbol}"