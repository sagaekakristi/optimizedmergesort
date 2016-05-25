#!/usr/bin/python3
# Version: A.1
# Author: Adrianus Saga Ekakristi (saga.ekakristi@gmail.com)
# Fakultas Ilmu Komputer, Universitas Indonesia

import math
import time

# Main class
class MergeInsertionSorter:
	def __init__(self, **kwargs):
		self.vars = kwargs

	# Driver Class Family
	def optimized_sort(self):
		array = self.vars.get('array')
		start = 0
		end = len(array) - 1
		threshold = self.vars['threshold']
		self.vars['swap_number'] = 0
		self.vars['comparison_number'] = 0
		self.vars['start_time'] = time.time()
		self.opt_merge_sort(array, start, end, threshold)
		self.vars['finish_time'] = time.time()
		self.vars['running_time'] = self.vars.get('finish_time') - self.vars.get('start_time')

	def standard_merge_sort(self):
		array = self.vars.get('array')
		start = 0
		end = len(array) - 1
		self.vars['swap_number'] = 0
		self.vars['comparison_number'] = 0
		self.vars['start_time'] = time.time()
		self.std_merge_sort(array, start, end)
		self.vars['finish_time'] = time.time()
		self.vars['running_time'] = self.vars.get('finish_time') - self.vars.get('start_time')

	def standard_insertion_sort(self):
		array = self.vars.get('array')
		start = 0
		end = len(array) - 1
		self.vars['swap_number'] = 0
		self.vars['comparison_number'] = 0
		self.vars['start_time'] = time.time()
		self.pure_insertion_sort(array, start, end)
		self.vars['finish_time'] = time.time()
		self.vars['running_time'] = self.vars.get('finish_time') - self.vars.get('start_time')

	# Framework Class Family
	def opt_merge_sort(self, array, start, end, threshold):
		evaluated_length = end - start + 1
		if(evaluated_length > threshold):
			mid = math.floor((start + end) / 2)
			self.opt_merge_sort(array, start, mid, threshold)
			self.opt_merge_sort(array, mid + 1, end, threshold)			
			self.merge(array, start, mid, end)
		else:
			self.insertion_sort(array, start, end)

	def std_merge_sort(self, array, start, end):
		evaluated_length = end - start + 1
		if(evaluated_length > 1):
			mid = math.floor((start + end) / 2)
			self.std_merge_sort(array, start, mid)
			self.std_merge_sort(array, mid + 1, end)
			self.merge(array, start, mid, end)
		else:
			pass

	def pure_insertion_sort(self, array, start, end):
		self.insertion_sort(array, start, end)

	# Helper & Algorithm Class Family
	def merge(self, array, start, mid, end):
		# create sorted array that will be filled
		sorted_subarray = []
		left_pointer = start
		right_pointer = mid + 1
		sorted_pointer = 0

		# build sorted part of array
		while(left_pointer <= mid and right_pointer <= end):
			# if left is smaller
			if(array[left_pointer] < array[right_pointer]):
				self.addComparison()
				# print(array[left_pointer])
				sorted_subarray.append(array[left_pointer])
				left_pointer += 1
			# if right is smaller
			else:
				self.addComparison()
				# print(array[right_pointer])
				sorted_subarray.append(array[right_pointer])
				right_pointer += 1
			sorted_pointer += 1

		# take all left array if remain
		if(left_pointer <= mid):
			while(left_pointer <= mid):
				self.addComparison()
				sorted_subarray.append(array[left_pointer])
				left_pointer += 1

		# take all right array if remain
		if(right_pointer <= end):
			while(right_pointer <= end):
				self.addComparison()
				sorted_subarray.append(array[right_pointer])
				right_pointer += 1

		# transfer sorted subarray to original array
		sorted_pointer = 0
		array_pointer = start
		sorted_length = len(sorted_subarray)
		while(sorted_pointer < sorted_length):
			# print(sorted_subarray[sorted_pointer])
			array[array_pointer] = sorted_subarray[sorted_pointer]
			sorted_pointer += 1
			array_pointer += 1

		# print(sorted_subarray)

	def insertion_sort(self, array, start, end):
		# print(end - start + 1)
		for i in range(start + 1, end + 1):
			j = i
			while(array[j-1] > array[j] and (j > start)):
				self.addComparison()
				self.swap(array, j, j - 1)
				j = j - 1

	def swap(self, array, index_a, index_b):
		temp = array[index_a]
		array[index_a] = array[index_b]
		array[index_b] = temp
		self.vars['swap_number'] += 1

	def addComparison(self):
		self.vars['comparison_number'] += 1

	def set_test_array(self, test_data):
		self.vars['array'] = test_data

	def set_threshold(self, threshold):
		self.vars['threshold'] = threshold

	def get_result_data(self):
		return (self.vars.get('array'), self.vars.get('comparison_number'), self.vars.get('swap_number'), self.vars.get('running_time'))

	def clean(self):
		self.vars = dict()

	def _print_array(self, array):
		print(array)

	def _print_sub_array(self, array, start, end):
		for i in range(len(array)):
			if(i >= start and i <= end):
				print("{} ".format(array[i]), end="")
		#print(" || ", end="")
		print("")