from collections import Counter
import numpy as np

class Category:
    def __init__(self, exp):
        self.exp = exp

        """
        List comprehension structure: 
        1. Getting key (character code) and vals (list of tuple(column name, data type)) from dtypes attribute.
        2. Filter whether key (character code) belong to 'OST' (object, byte string, and StringDType).
        3. Getting val (column name) from vals (list of tuple(column name, data type)).
        """
        self.columns = [val[0] for key, vals in self.exp.dtypes.items() if key in 'O' for val in vals if val[1] == 'category']

        self.occur = self.__occur()
        self.common = self.__common()
        self.rarest = self.__rarest()

    def __occur(self):
        """
        Count the occurrence of every category in every column with category data.

        Args:
            -
        
        Returns:
            dict: column name and dictionary of category and its occurrence.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting every val (category) and its occurrence from the column and put it in a dictionary.
        """
        
        return {key: Counter(self.exp.data[key]) for key in self.columns}

    def __common(self):
        """
        Retrieve the most occurred category for every column with category data.

        Args:
            -
        
        Returns:
            dict: column name and most occurred category.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting the most occurred category from the column and put it in a dictionary.
        """
        
        return {key: self.occur[key].most_common(2)[0][0] if self.occur[key].most_common(2)[0][0] is not np.nan else self.occur[key].most_common(2)[1][0] for key in self.columns}

    def __rarest(self):
        """
        Retrieve the rarest category for every column with category data.

        Args:
            -
        
        Returns:
            dict: column name and most rare category.
        """

        """
        Dict comprehension structure: 
        1. Getting key (column name) from every column.
        2. Getting the most rare category from the column and put it in a dictionary.
        """
        
        return {key: self.occur[key].most_common()[-1][0] if self.occur[key].most_common()[-1][0] is not np.nan else self.occur[key].most_common()[-2][0] for key in self.columns}

    def __str__(self):
        """
        String representation of the Category class.

        Returns:
            str: A string representation of the Category class.
        """
        return f"Columns with category values: {self.columns}\n\n" \
                f"Categories occurrence: {self.occur}\n\n" \
                f"Most Common Categories: {self.common}\n\n" \
                f"Rarest Categories: {self.rarest}"