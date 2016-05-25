#!/usr/bin/python3
# Version: A.1
# Author: Adrianus Saga Ekakristi (saga.ekakristi@gmail.com)
# Fakultas Ilmu Komputer, Universitas Indonesia

from sorter import MergeInsertionSorter

# Main class
class Debugger:
    def __init__(self, **kwargs):
        sorter_class = MergeInsertionSorter()
        test_array_1 = [0,0,1,7,8,9,10]
        test_array_2 = [2,3,4,5,6,0,0]
        test_array = test_array_1 + test_array_2
        threshold = 3
        print(test_array)
        sorter_class.merge(test_array, 2, 6, 11)
        print(test_array)


# Main method of this .py file
def main():
    # Start the program by creating the class
    mainObject = Debugger()
    
# Control the flow for when this .py file is executed
if __name__ == "__main__": main()