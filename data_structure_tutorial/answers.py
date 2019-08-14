class ListTutorial():

    def length(self, l):
        """
        This function returns the length of list l
        """
        return len(l)

    def add_item(self, l, i):
        """
        This function add item i to the end of l and returns l
        """
        l.append(i)
        return l

    def remove_item(self, l, i):
        """
        This function removes item i from l if it exists, if there are multiples of that item, remove them all
        """
        # fancy version
        new_l = list(filter((i).__ne__, l))
        return new_l

        # easier version
        new_l = []
        for item in l:
            if item != i:
                new_l.append(item)
        
        return new_l

    def sum_items(self, l):
        """
        This function adds all of the elements of a list and returns them. 
        You can assume all items are numbers.
        For an empty list, return 0 as the sum
        """
        s = 0
        for item in l:
            s += item
        return s
    
    def combine_two_lists(self, a, b):
        """
        This function returns a list that contains all items contained in lists a and b
        The items from a should always come first. 
        Example:
          a = [1, 2, 3]
          b = [4, 5, 6]
          you should return [1, 2, 3, 4, 5, 6]
        """
        return a+b
    
    def sum_list(self, a, b):
        """
        This function returns a list that consists of the sum of items in the same index of list a and b
        Example:
          a = [1, 2, 3]
          b = [2, 4, 5]
          you would return [3, 6, 8]
        """
        # There are multiple ways to do this, this isn't the most optimal but is easy to understand
        if len(a) > len(b):
            new_l = a
            small_list = b
        else:
            new_l = b
            small_list = a
        
        for i in range(len(small_list)):
            new_l[i] += small_list[i]
        
        return new_l
    
    def zip_list(self, a, b):
        """
        This function returns a list that consists of the items of a and b 'zipped up', alternating between items of the lists
        Example:
          a = [1, 2, 3]
          b = [4, 5, 6]
          you would return [1, 4, 2, 5, 3, 6]
        if one list runs out of items to zip, the rest of the list will be the remaining elements of the longer list
        """
        new_list = []
        i = 0
        while True:
            if i >= len(a) and i >= len(b):
                # i is past both of them, just return the new_list
                return new_list
            elif i >= len(a):
                # if i is only past a, then we need the rest of the items from b
                return new_list + b[i:]
            elif i >= len(b):
                # if i is only past b, then we need the rest of the items from a
                return new_list + a[i:]
            else:
                #otherwise, zip up the next two items
                new_list.append(a[i])
                new_list.append(b[i])
                i+=1
    
class DictionaryTutorial():

    def add_item(self, dict, key, value):
        """
        This function adds an item {key: value} to dictionary dict
        """
        pass
    
class StringTutorial():

    def combine_strings(self, a, b):
        """
        This function returns the combination (concatenation) of strings a and b
        """
        return a+b

    def count_characters(self, s, c):
        """
        This function returns the number of times character c appears in string s
        """
        # easy
        return s.count(c)

        # more fun
        count = 0
        for i in s:
            if i == c:
                count+=1
        return count

    def get_range(self, s, a, b):
        """
        This function returns the substring of s from indices a->b
        Example:
          s = 'hello there'
          a = 3
          b = 5
          return 'lo'
        """
        return s[a:b]

    def is_palindrome(self, s):
        """
        This function returns True if string s is a palindrome, and returns False if it is not
        """
        j = len(s)-1
        i = 0
        while i < j:
            if s[i] != s[j]:
                return False
            j-=1
            i+=1
        return True
    
    def replace(self, s, a, b):
        """
        This function replaces all instances of substring a with substring b in string s
        """
        # easy answer, there are much more fun ways to do this manually
        s = s.replace(a,b)
        return s
    
    def capitalize(self, s):
        """
        This function capitalizes the first letter in every word in string s
        Example:
            s = 'this is a string, it's pretty cool'
            return 'This Is A String, It's Pretty Cool'
        """
        # get a list of all of the words by splitting on spaces
        words = s.split(' ')
        new_string = ''
        for word in words:
            new_string += word.capitalize() + ' '
        return new_string[:-1] # we have this -1 here to remove the last space we added because it wasn't part of the original string