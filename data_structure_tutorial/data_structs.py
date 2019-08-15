class ListTutorial():

    def length(self, l):
        """
        This function returns the length of list l
        """
        pass

    def add_item(self, l, i):
        """
        This function add item i to the end of l and returns l
        """
        pass

    def remove_item(self, l, i):
        """
        This function removes item i from l if it exists, if there are multiples of that item, remove them all
        """
        pass

    def sum_items(self, l):
        """
        This function adds all of the elements of a list and returns them. 
        You can assume all items are numbers.
        For an empty list, return 0 as the sum
        """
        pass
    
    def combine_two_lists(self, a, b):
        """
        This function returns a list that contains all items contained in lists a and b
        The items from a should always come first. 
        Example:
          a = [1, 2, 3]
          b = [4, 5, 6]
          you should return [1, 2, 3, 4, 5, 6]
        """
        pass
    
    def sum_list(self, a, b):
        """
        This function returns a list that consists of the sum of items in the same index of list a and b
        Example:
          a = [1, 2, 3]
          b = [2, 4, 5]
          you would return [3, 6, 8]
        When one list is longer than the other, the sum of that index will just be the value of the item from the longer list
        """
        pass
    
    def zip_list(self, a, b):
        """
        This function returns a list that consists of the items of a and b 'zipped up', alternating between items of the lists
        Example:
          a = [1, 2, 3]
          b = [4, 5, 6]
          you would return [1, 4, 2, 5, 3, 6]
        if one list runs out of items to zip, the rest of the list will be the remaining elements of the longer list
        """
        pass
    
class DictionaryTutorial():

    def add_item(self, d, key, value):
        """
        This function adds an item {key: value} to dictionary dict and returns the new dictionary
        """
        pass
    
    def remove_item(self, d, key):
        """
        This function removes an item from a dictionary and returns the new dictionary
        """
        pass
    
    def dog_dict(self, dogs):
        """
        Given a list of strings defining dog ownership that looks like:
        ['John owns Fido', 'Bill owns Rover', 'Woof belongs to Man']
        (you can expect both formats, {human} owns {dog} and {dog} belongs to {human})
        Return a dictionary of {owners: dogs}
        so for the list above the dictionary would be:
        {
            'John': 'Fido',
            'Bill': 'Rover',
            'Man': 'Woof'
        }
        """
        pass

    def create_biography(self, people):
        """
        Given a list of people described by the following dictionary format:
        [{
            first_name: 'John',
            last_name: 'Smith',
            age: 101,
            occupation: 'Blacksmith',
            children: ['Joe', 'Jill']
        },
        {
            first_name: 'Elliot',
            last_name: 'Brosef',
            age: 15,
            occupation: 'Student',
            children: []
        }]

        Return a list of biographies comprised of their information. The biography for John and Elliot would be:
        ['John Smith, 101, is a Blacksmith with 2 children: Joe and Jill', 'Elliot Brosef, 15, is a Student with 0 children']
        This is an odd problem, but is similar to stuff you'll have to do with data sets
        """
        pass
    
class StringTutorial():

    def combine_strings(self, a, b):
        """
        This function returns the combination (concatenation) of strings a and b
        """
        pass

    def count_characters(self, s, c):
        """
        This function returns the number of times character c appears in string s
        """
        pass

    def get_range(self, s, a, b):
        """
        This function returns the substring of s from indices a->b
        Example:
          s = 'hello there'
          a = 3
          b = 5
          return 'lo'
        """
        pass

    def is_palindrome(self, s):
        """
        This function returns True if string s is a palindrome, and returns False if it is not
        """
        pass
    
    def replace(self, s, a, b):
        """
        This function replaces all instances of substring a with substring b in string s
        """
        pass
    
    def capitalize(self, s):
        """
        This function capitalizes the first letter in every word in string s
        Example:
            s = 'this is a string, it's pretty cool'
            return 'This Is A String, It's Pretty Cool'
        """
        pass

    