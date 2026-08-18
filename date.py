from dateutil.relativedelta import relativedelta

class Date:
    """
    A class to analyze date data in a pandas DataFrame.
    """
    
    def __init__(self, exp):
        self.exp = exp

        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name, data type) from Explore class dtypes attribute.
        2. Filter whether key (character code) belong to 'mM' (datetime and timedelta objects).
        3. Getting val (column name) from vals (list of tuple(column name, data type).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'mM' for val in vals]

        self.min = self.__min()
        self.max = self.__max()
        self.range = self.__range()

    def __min(self):
        """
        Parse minimum value of column with relevant data types E.g. datetime and timedelta.

        Args:
            -
        
        Returns:
            dict: column name and minimum value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from columns attribute as key.
        2. Accessing the corresponding column in the DataFrame to get the minimum value as value.
        """
        return {key: self.exp.data[key].min() for key in self.columns}

    def __max(self):
        """
        Parse maximum value of column with relevant data types E.g. datetime and timedelta.

        Args:
            -
        
        Returns:
            dict: column name and maximum value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from columns attribute as key.
        2. Accessing the corresponding column in the DataFrame to get the maximum value as value.
        """
        return {key: self.exp.data[key].max() for key in self.columns}

    def __range(self):
        """
        Parse datetime range between oldest and newest datetime of column with relevant data types E.g. datetime and timedelta.

        Args:
            -
        
        Returns:
            dict: column name and range value parsed.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from columns attribute as key 
        2. Accessing the corresponding column in the DataFrame to get the date or time range.
        """
        
        rdelta = {key: relativedelta(self.exp.data[key].max(), self.exp.data[key].min()) for key in self.columns}
        
        return {key: f'{val.years} years {val.months} months {val.days} days' for key, val in rdelta.items()}

    def __str__(self):
        """
        String representation of the Date class.

        Returns:
            str: String representation of the Date class.
        """
        return f"Columns with datetime values: {self.columns}\n\n" \
                f"Minimum datetime: {self.min}\n\n" \
                f"Maximum datetime: {self.max}\n\n" \
                f"Datetime ranges between oldest and newest data: {self.range}\n\n"