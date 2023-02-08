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

# 3. Appending(inserting) an element to the end of the array

my_array.append(6) # O(1) time complexity
print('You inserted:', my_array[len(my_array) - 1])

    
