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