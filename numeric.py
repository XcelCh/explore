class Numeric:
    """
    Numeric class to parse minimum, maximum, median, and mean value of column with relevant data types E.g. int, float.
    """

    def __init__(self, exp):
        self.exp = exp

        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name, data type)) from dtypes attribute.
        2. Filter whether key (character code) belong to 'iuf' (int and float).
        3. Getting val (column name) from vals (list of tuple(column name, data type)).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'iuf' for val in vals]

        self.min = self.__min()
        self.max = self.__max()
        self.median = self.__median()
        self.mean = self.__mean()
        self.mode = self.__mode()
        self.count_zero = self.__count_zero()
        self.count_negative = self.__count_negative()
        self.count_unique = self.__count_unique()

    def __min(self):
        """
        Parse minimum value of column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and minimum value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the minimum value as value.
        """
        return {val: self.exp.data[val].min() for val in self.columns}

    def __max(self):
        """
        Parse maximum value of column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and maximum value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the maximum value as value.
        """
        return {val: self.exp.data[val].max() for val in self.columns}

    def __median(self):
        """
        Parse median value of column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and median value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the median value as value.
        """
        return {val: self.exp.data[val].median().round(2) for val in self.columns}

    def __mean(self):
        """
        Parse mean value of column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and mean value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the mean value as value.
        """
        return {val: self.exp.data[val].mean().round(2) for val in self.columns}

    def __mode(self):
        """
        Parse mode value of column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and mode value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the mode value as value.
        """
        return {val: self.exp.data[val].mode()[0] for val in self.columns}

    def __count_zero(self):
        """
        Count 0 values in column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and count of zero values parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to check whether it has zero value as value.
        """
        return {val: (self.exp.data[val] == 0).sum() for val in self.columns}

    def __count_negative(self):
        """
        Count negative values in column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and count of negative values parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to check whether it has negative value as value.
        """
        return {val: (self.exp.data[val] < 0).sum() for val in self.columns}

    def __count_unique(self):
        """
        Count unique values in column with relevant data types E.g. int, float.

        Args:
            -
        
        Returns:
            dict: column name and count of unique values parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting val (column name) from columns attribute as key and accessing the corresponding column in the DataFrame to get the count of unique values as value.
        """
        return {val: self.exp.data[val].nunique() for val in self.columns}

    def __str__(self):
        return f"Columns with numeric values: {self.columns}\n\n" \
                f"Minimum Values: {self.min}\n\n" \
                f"Maximum Values: {self.max}\n\n" \
                f"Median Values: {self.median}\n\n" \
                f"Mean Values: {self.mean}\n\n" \
                f"Mode Values: {self.mode}\n\n" \
                f"Count of Zero Values: {self.count_zero}\n\n" \
                f"Count of Negative Values: {self.count_negative}\n\n" \
                f"Count of Unique Values: {self.count_unique}"