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
        pass
    