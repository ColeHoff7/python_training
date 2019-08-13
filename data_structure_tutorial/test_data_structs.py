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

