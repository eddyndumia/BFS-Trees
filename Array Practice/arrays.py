"""
 Copyright 2023 Eddy Ndumia

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """


from array import *


#1. Create array and traverse

my_array = array('i', [1,2,3,4,5,6]) # O(n) space and time complexity

# traverse

for i in my_array:
    print(i) # O(n) time complexity, O(1) space complexity
    
# 2. Access individual array elements using indexes

print('Second item is:')
print(my_array[1]) # O(1) time and space complexity

# 3. Appending(inserting) an element to the end of the array using append()

my_array.append(6) # O(1) time complexity
print('You inserted:', my_array[len(my_array) - 1])

# 4. Inserting element into array using insert() method

# insert() adds an element at a given index, which is very time consuming since the other elements have to shift

my_array.insert(1, 8)

print('You inserted:', my_array[1])

# 5. Extending an array from another array using .extend()

extension_array = array('i', [10, 11, 12, 13, 11])

my_array.extend(extension_array)

print('There have been changes to your array:', my_array)

# 6. Inserting array element at the end of an array from a list using fromList()

tempList = [20,21,22,23,24,25]

my_array.fromlist(tempList)

print('There have been changes to you array. Added Items: ', my_array)


# 7. Removing an element using remove()

my_array.remove(11)

# removes the first occurrence of the element in the array and pushes the other elements to the left
# uses O(n) time complexity, O(1) space complexity
print(my_array)

#. 8 Removing the last element from the array

my_array.pop()

# very time efficient as no elements are pushed to the left, O(1) time and space complexity
print(my_array)


# 9. Fetching an elements index 

print(my_array.index(21))
print(my_array[13])


# 10. Reversing an array sequence using reverse method

my_array.reverse()
print(my_array)

# 11. Gettting buffer_info using buffer method

print("buffer info:", my_array.buffer_info())


# 12. Count method counts the number of times an element has occurred in an array

my_array.append(21)

print('21 has occurred', my_array.count(21),'times')


# 13. Converting an array to string using tostring 

'''
There is no difference, tostring they are both aliases to the same method, tostring was renamed to tobytes for the purposes for clarity 
in Python 3.2, as mentioned in the documentation

tostring has been kept for backwards compatibility, but the use of tostring is deprecated.
'''

strTemp = my_array.tobytes()

ints = array('i')
ints.frombytes(strTemp)
print(ints)
