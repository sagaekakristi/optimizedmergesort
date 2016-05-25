#!/usr/bin/python3
# Version: A.1
# Author: Adrianus Saga Ekakristi (saga.ekakristi@gmail.com)
# Fakultas Ilmu Komputer, Universitas Indonesia

import random
import math

# Main class
class ArrayGenerator:
	def __init__(self, **kwargs):
		pass
	
	def generate_random(self, size):
		random_array = []
		for index in range(0, size):
			random_array.append(index)
		random.shuffle(random_array)
		return random_array

	def generate_sorted(self, size):
		sorted_array = []
		for index in range(0, size):
			sorted_array.append(index)
		return sorted_array

	def generate_reversed_sorted(self, size):
		rev_sorted_array = list(reversed(self.generate_sorted(size)))
		return rev_sorted_array

	def generate_nearly_sorted(self, size):
		near_sorted_array = []
		for index in range(0, size):
			near_sorted_array.append(index)

		# randomly swap 10% of data
		for i in range(math.floor(size * 0.1)):
			random_id_a = random.randint(0, size - 1)
			random_id_b = random.randint(0, size - 1)
			while(random_id_a == random_id_b):
				random_id_a = random.randint(0, size - 1)
				random_id_b = random.randint(0, size - 1)
			self.swap(near_sorted_array, random_id_a, random_id_b)

		return near_sorted_array

	def generate_spiky_dist_array(self, size):
		spiky_array = []
		for index in range(size):
			if(index % 2 == 0):
				big_number = random.randint(0, size * 10000)
				spiky_array.append(big_number)
			else:
				small_number = random.randint(0, size * 10)
				spiky_array.append(small_number)
		return spiky_array


	def swap(self, array, index_a, index_b):
		temp = array[index_a]
		array[index_a] = array[index_b]
		array[index_b] = temp