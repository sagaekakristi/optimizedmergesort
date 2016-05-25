#!/usr/bin/python3
# Version: A.1
# Author: Adrianus Saga Ekakristi (saga.ekakristi@gmail.com)
# Fakultas Ilmu Komputer, Universitas Indonesia

from sorter import MergeInsertionSorter
from data_generator import ArrayGenerator
import time

# Main class
class Main:
	def __init__(self, **kwargs):
		start_time = time.time()
		base_path = "results/"
		result_filename = "result.txt"
		self.result_file = open(base_path + result_filename, 'w')
		for data_size in [50, 100, 150, 250, 400, 500, 750, 1000, 2500, 3500, 5000, 6000, 7500, 10000, 15000]: #, 250000, 500000, 1000000]:
			for array_type in ['random', 'almost_sorted', 'reversed_sorted', 'sorted', 'spiky']:
				# generate test array
				generator_class = ArrayGenerator()
				test_array = []
				if(array_type == 'random'):
					test_array = generator_class.generate_random(data_size)
				elif(array_type == 'almost_sorted'):
					test_array = generator_class.generate_nearly_sorted(data_size)
				elif(array_type == 'reversed_sorted'):
					test_array = generator_class.generate_reversed_sorted(data_size)
				elif(array_type == 'sorted'):
					test_array = generator_class.generate_sorted(data_size)
				elif(array_type == 'spiky'):
					test_array = generator_class.generate_spiky_dist_array(data_size)
				else:
					print("Test array type undefined. Eg: random / almost_sorted / reversed_sorted / sorted / spiky")

				# threshold
				threshold = 6

				# print test array to file
				filename = "{}_{}.txt".format(data_size, array_type)
				self.save_array(test_array, base_path + filename)

				# do optimized sort, pure merge sort, pure insertion sort
				for sort_type in ['optimized', 'pure_merge', 'pure_insertion']: #['pure_insertion']:
					info = "Size = {} | ArrayType = {} | SortType = {} ".format(data_size, array_type, sort_type)
					print(info)
					self.write_info(info)
					clone_array = list(test_array)
					self.experiment(sort_type, clone_array, data_size, threshold)
		
		finish_time = time.time()
		experiment_time = finish_time - start_time
		info = "Total experiment time = {} second | start_time = {} | finish_time = {}".format(str(experiment_time), time.asctime(time.localtime(start_time)), time.asctime(time.localtime(finish_time)))
		self.write_info(info)
		print(info)
		self.result_file.close()

	def experiment(self, sort_type, test_array, data_size, threshold, **kwargs):
		sorter_class = MergeInsertionSorter()		

		sorter_class.set_test_array(test_array)
		sorter_class.set_threshold(threshold)

		if(sort_type == 'optimized'):
			sorter_class.optimized_sort()
		elif(sort_type == 'pure_merge'):
			sorter_class.standard_merge_sort()
		elif(sort_type == 'pure_insertion'):
			sorter_class.standard_insertion_sort()
		else:
			print("Sorting algorithm undefined. Eg: optimized, pure_merge, pure_insertion")

		(result, comparison, swap, running_time) = sorter_class.get_result_data()

		# print(result)
		if(self.is_sorted(result)):
			info = "Result: comparison = {} | swap = {} | running time = {} second".format(comparison, swap, running_time)
			print(info)
			self.write_info(info)
		else:
			info = 'Sort fail detected!'
			print(info)
			self.write_info(info)

	def is_sorted(self, array):
		is_sorted = True
		for index in range(len(array) - 1):
			if(array[index] <= array[index + 1]):
				pass
			else:
				is_sorted = False
				break
		return is_sorted

	def write_info(self, info):
		self.result_file.write(info + '\n')

	def save_array(self, array, filename):
		file_object = open(filename, 'w')
		to_write = ''
		for item in array:
			to_write = to_write + str(item) + "\n"
		file_object.write(to_write)
		file_object.close()

# Main method of this .py file
def main():
	# Start the program by creating the class
	mainObject = Main()
	
# Control the flow for when this .py file is executed
if __name__ == "__main__": main()