import pytest
from lib.most_often import MostOften

def test_check_if_starting_list_type_is_valid():
    with pytest.raises (TypeError) as e:
        obj_most_often = MostOften(12345)
    error_message = str(e.value)
    assert error_message == "Error: invalid type"

def test_add_new_element_in_list():
    og_list = MostOften([1, 2, 3])
    og_list.add_new(4)
    assert og_list.starting_list == [1, 2, 3, 4]

def test_add_new_array_in_list():
    og_list = MostOften([1, 2, 3, 4])
    og_list.add_new([5, 6])
    assert og_list.starting_list == [1, 2, 3, 4, [5, 6]]
    
def test_if_highest_count_is_one():
    obj_most_often = MostOften([1,1,1,2,3])
    result = obj_most_often.get_most_often()
    assert result == 1
    
def test_given_two_element_with_same_highest_count():
    obj_most_often = MostOften([1,1,1,2,2,2,3])
    result = obj_most_often.get_most_often()
    assert result == "no clear winner"

def test_given_empty_list():
    obj_most_often = MostOften([])
    result = obj_most_often.get_most_often()
    assert result == "no clear winner"

def test_mixed_list():
    obj_most_often = MostOften([1, 2, "cat", "dog", 3, 7, "dog"])
    result = obj_most_often.get_most_often()
    assert result == "dog"

def test_add_new_and_get_most_often():
    obj_most_often = MostOften([1, 2, 3])
    obj_most_often.add_new("hello world")
    obj_most_often.add_new(2)
    result = obj_most_often.get_most_often()
    assert result == 2