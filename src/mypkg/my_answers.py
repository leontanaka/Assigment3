#!/usr/bin/python

"""
Python Core object Types
"""

import numpy as np


def reform_array_dimension_col_wise(arr, nRow, nCol):
	new_arr = arr.reshape(nRow,nCol,order='F') 					# write your code here
	return new_arr


#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### append_sum_of_array(arr) is to stack the column summation below the bottom of the array
def append_sum_of_array(arr):
	new_arr = np.vstack((arr, arr.sum(0))) 					# write your code here
	return new_arr


#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### remove_topRow_endCol_from_array(arr) is to delete the top row and ending column from the array
def remove_topRow_endCol_from_array(arr):
	new_arr = arr[1:,:-1] 					# write your code here
	return new_arr

#### arr: 		the input array
#### new_arr:	the new generated array as the output
#### add_row_product_to_array(arr) is to calculate the product of each row and append to the array
def add_row_product_to_array(arr):
	row_product = arr.prod(1)[...,None]				# write your code here
	new_arr = np.hstack((arr, row_product)) 		# write your code here
	return new_arr









