#!/usr/bin/python

"""
Python Core object Types
"""

import numpy as np


#### arr: 		the input array
#### nRow: 		the # of row in the reformed array
#### nCol: 		the # of column in the reformed array
#### new_arr:	the new reformed array as the output
#### reform the array to a new array with size(nRow,nCol)
def reform_array_dimension_col_wise(arr, nRow, nCol):
	new_arr =  arr.reshape((nRow, nCol),order = 'F')
	return new_arr


#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### stack the column summation below the bottom of the array
def append_sum_of_array(arr):
	new_arr =  np.vstack((arr,arr.sum(0)))
	return new_arr 


#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### delete the top row and ending column from the array
def remove_topRow_endCol_from_array(arr):
	new_arr = arr[1:,:-1]# write your code here
	return new_arr

#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### calculate the product of each row and append to the array, use row_product to save the product value and add to the new array
def add_row_product_to_array(arr):
	row_product = arr.prod(1)
	new_arr =  np.column_stack((arr,row_product))# write your code here
	return new_arr









