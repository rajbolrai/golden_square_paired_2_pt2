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