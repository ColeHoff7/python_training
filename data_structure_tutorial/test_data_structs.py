from data_structs import DictionaryTutorial,ListTutorial,StringTutorial

# Tests for Lists
l = ListTutorial()

def test_length():
    assert l.length([1,2,3,4,5]) == 5

def test_length_2():
    assert l.length([]) == 0

def test_add_item():
    a = ['a', 'b', 'c']
    new_a = l.add_item(a, 'd')
    assert new_a == ['a','b','c','d']

def test_remove_item():
    a = ['a', 'b', 'c']
    new_a = l.remove_item(a, 'b')
    assert new_a == ['a','c']

def test_remove_item_multiple():
    a = ['a', 'b', 'b', 'c']
    new_a = l.remove_item(a, 'b')
    assert new_a == ['a','c']

def test_sum_items():
    a = [1,4,6,8,2,3]
    s = l.sum_items(a)
    assert s == 24

def test_sum_items_empty():
    a = []
    s = l.sum_items(a)
    assert s == 0

def test_combine():
    a = [1,2,3]
    b = [4,5,6]
    n = l.combine_two_lists(a,b)
    assert n == [1,2,3,4,5,6]

def test_combine_2():
    a = [1,2,3]
    b = []
    n = l.combine_two_lists(a,b)
    assert n == [1,2,3]

def test_combine_3():
    a = []
    b = ['a', 'b']
    n = l.combine_two_lists(a,b)
    assert n == ['a', 'b']

def test_sum_list():
    a = [1,3,5]
    b = [2,6,9]
    n = l.sum_list(a, b)
    assert n == [3,9,14]

def test_sum_list_2():
    a = [1,3,5,3,3,3]
    b = [2,6,9]
    n = l.sum_list(a, b)
    assert n == [3,9,14,3,3,3]

def test_zip_list():
    a = [1, 2, 3]
    b = [4, 5, 6]
    n = l.zip_list(a,b)
    assert n == [1,4,2,5,3,6]

def test_zip_list_2():
    a = [1, 2, 3, 9, 10]
    b = [4, 5, 6]
    n = l.zip_list(a,b)
    assert n == [1,4,2,5,3,6,9,10]

# Tests for Dicts
d = DictionaryTutorial()

def test_add_item_dict():
    assert d.add_item({'a': 'b', 'c': 'd'}, 'e', 'f') == {'a': 'b', 'c': 'd', 'e': 'f'}

def test_remove_item_dict():
    assert d.remove_item({'a': 'b', 'c': 'd', 'e': 'f'}, 'e') == {'a': 'b', 'c': 'd'}

def test_dog_dict():
    assert d.dog_dict(['John owns Fido', 'Bill owns Rover', 'Woof belongs to Man']) == {'John': 'Fido', 'Bill': 'Rover', 'Man': 'Woof'}

def test_biography():
    people = [{'first_name': 'John', 'last_name': 'Smith', 'age': 101, 'occupation': 'Blacksmith', 'children': ['Joe', 'Jill']},{'first_name': 'Elliot','last_name': 'Brosef','age': 15,'occupation': 'Student','children': []}]
    assert d.create_biography(people) == ['John Smith, 101, is a Blacksmith with 2 children: Joe, Jill', 'Elliot Brosef, 15, is a Student with 0 children']

# Tests for Strings
s = StringTutorial()

def test_combine_string():
    assert s.combine_strings('abc','cba') == 'abccba'

def test_count_characters():
    assert s.count_characters('aabbbbbaccccccaaa','a') == 6

def test_count_characters():
    assert s.count_characters('','a') == 0

def test_get_range():
    assert s.get_range('abcdefg', 3, 6) == 'def'

def test_is_palindrome_true_odd():
    assert s.is_palindrome('racecar') == True

def test_is_palindrome_true_even():
    assert s.is_palindrome('raccar') == True

def test_is_palindrome_false():
    assert s.is_palindrome('asdfb') == False

def test_replace():
    assert s.replace('i love dogs', 'dogs', 'cats') == 'i love cats'

def test_replace():
    assert s.replace('my name is cole, cole is my name', 'cole', 'kevin') == 'my name is kevin, kevin is my name'

def test_capitalize():
    assert s.capitalize('this is a string, it\'s pretty cool') == 'This Is A String, It\'s Pretty Cool'

def test_capitalize_2():
    assert s.capitalize('   this is a string, it\'s pretty cool   ') == '   This Is A String, It\'s Pretty Cool   '

def test_capitalize_empty():
    assert s.capitalize('') == ''

def test_capitalize_already_capital():
    assert s.capitalize('This Is A String, It\'s Pretty Cool') == 'This Is A String, It\'s Pretty Cool'
