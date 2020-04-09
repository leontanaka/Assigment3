import pytest

from mypkg.my_answers import *
import numpy as np

arr_ori = np.arange(15)
arr_1 = reform_array_dimension_col_wise(arr_ori, 3, 5)
arr_2 = append_sum_of_array(arr_1)
arr_3 = remove_topRow_endCol_from_array(arr_1)
arr_4 = add_row_product_to_array(arr_1)
a1 = np.array([12,13,14])
a2 = np.array([9,10,11,30])
a3 = np.array([1,4,7,10])
a4 = np.array([2,5,8,11,14,12320])


def test_reform():
    assert(arr_1[:,-1].all() == a1.all())


def test_sum():
    assert(arr_2[:,-2].all()==a2.all())


def test_remove():
    assert(arr_3[0,:].all() == a3.all() and arr_3.shape == (2,4))


def test_product():
    assert(arr_4[-1,:].all() == a4.all())
