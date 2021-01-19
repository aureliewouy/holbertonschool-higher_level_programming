#!/usr/bin/python3
""" Task 1 - My list """


class MyList(list):
    """
    Class That inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints the list sorted
        """
        print(sorted(self))
