import os
import numpy as np
from abc import ABC, abstractmethod
from collections import deque, defaultdict
from typing import Optional


def reverse_read(filename: str) -> int:
    #read in each line of the text file in reverse order
    
    bottom_hash_map = defaultdict(lambda : 0)
    top_hash_map = defaultdict(lambda: 0)
    count = 0
    
    with open(filename, 'rb') as read_obj:
        end_pointer_location = read_obj.seek(0, os.SEEK_END)
        start_pointer_location = 0
        
        
        buffer = deque()
        top_buffer = deque()
        
        
        while end_pointer_location >= 0:
            read_obj.seek(end_pointer_location)
            end_pointer_location -= 1
            new_byte = read_obj.read(1)
            
            read_obj.seek(start_pointer_location)
            top_byte = read_obj.read(1)
            start_pointer_location += 1
            
            if new_byte == b'\n':
                # print("here")
                #end of line
                n = 0
                while buffer:
                    val = buffer.popleft()
                    if val > bottom_hash_map[n]:
                        count += 1
                        bottom_hash_map[n] = val
                        
                # while buffer:      
                #     print((buffer.pop(), "big"))                    
            elif new_byte:
                buffer.appendleft(int(new_byte.decode()))                
        return count
    
def count_trees(filename: str) -> Optional[int]:
    arr = np.genfromtxt(filename, delimiter=1, dtype=int)
    top_hash = defaultdict(lambda : -1)
    count_hash = set()
    
    for n1, row in enumerate(arr):
        max_val = -1
        for n, element in enumerate(row):            
            if element > max_val or element > top_hash[n]:
                count_hash.add((n1, n))
                
            top_hash[n] = max(top_hash[n], element)
            max_val = max(max_val, element)
            
    bottom_hash = defaultdict(lambda : -1)

    for n1 in range(len(arr)-1, -1, -1):
        row = arr[n1]
        max_val = -1
        for n in range(len(row)-1, -1, -1):
            element = row[n]
            
            if element > max_val or element > bottom_hash[n]:
                count_hash.add((n1, n))
                
            
            bottom_hash[n] = max(bottom_hash[n], element)
            max_val = max(max_val, element)
    return len(count_hash)
            
            
print("Number of trees: ", count_trees("input_8.txt"))
print("Time complexity: O(n^2)")
print("Space complexity: O(n ~ n^2)")
print("test")


### Part 2

def part_two(filename):
    arr = np.genfromtxt(filename, delimiter=1, dtype=int)
    vision = defaultdict(lambda : 1)
    #up->down and left->right loops
    
    
    top_hash = defaultdict(lambda : defaultdict(lambda : 0))
    for n1, row in enumerate(arr):
        row_hash = {}
        for n, element in enumerate(row):
            max_ix = 0
            top_max_ix = 0
            for i in range(element, 10):
                if i in row_hash:
                    max_ix = max(max_ix, row_hash[i])
                    
                if i in top_hash[n]:
                    top_max_ix = max(top_max_ix, top_hash[n][i])
                    
                    
            vision[(n1, n)] *= (n - max_ix)
            vision[(n1, n)] *= (n1 - top_max_ix)
            row_hash[element] = max(row_hash.get(element, 0), n)
            top_hash[n][element] = max(top_hash[n][element], n1)
            
    #down->up and right->left loops
    bottom_hash = defaultdict(lambda : defaultdict(lambda : len(arr[0])-1))
    for n1 in range(len(arr)-1, -1, -1):
        row = arr[n1]
        row_hash = {}
        for n in range(len(row)-1, -1, -1):
            element = row[n]
            min_ix = len(row) -1
            bottom_min_ix = len(row)-1
            for i in range(element, 10):
                if i in row_hash:
                    min_ix = min(min_ix, row_hash[i])
                    
                if i in top_hash[n]:
                    bottom_min_ix = min(bottom_min_ix, bottom_hash[n][i])
            vision[(n1, n)] *= min_ix - n
            vision[(n1, n)] *= bottom_min_ix - n1
            row_hash[element] = min(row_hash.get(element, len(row)-1), n)
            bottom_hash[n][element] = min(bottom_hash[n][element], n1)            
    return vision

import timeit

# print(timeit.timeit(lambda: part_two("input_8.txt"), number = 100))

vision = part_two("input_8.txt")
print("Largest Vision: ", max(vision.values()))

########################## Logic for Part 2 ##########################
#For each row: 
    #- as you iterate over the elements, create a hash map of elements you've seen
    #- {element: max_index} if iterating from the left
    #- {element: min_index} if iterating from the right
    
    #- for each element, you want to check if elements greater than it are in the set
    #- because we are between 0-9 we only have 10 possible numbers to check
    # because we hash the numbers we've seen, each check is O(1)
    #- max of 10 * O(1) * n elements in the row = O(n) cost one direction
    #- repeat for reverse direction
    #- repeat for up and down