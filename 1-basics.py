
# Variable: A storage location identified by its name, containing some value.
# Question: Assign a value of 10 to variable a and 20 to variable b
# Question: Store the result of a + b in a variable c and print it. What is the result of a + b?

s = '  Some string '
# Question: How do you remove the empty spaces in front of and behind the string s?
print(s.strip())
print(s.rstrip(' '))
print(s.lstrip(' '))


# Data Structures are ways of representing data, each has its own pros and cons and places that they are the right fit.
## List: A collection of elements that can be accessed by knowing the location (aka index) of the element
l = [1, 2, 3, 4]

# Question: How do you access the elements in index 0 and 3? Print the results.
## NOTE: lists retain the order of elements in it but dictionary doesn't
print(l[0], l[3])
## Dictionary: A collection of key-value pairs, where each key is mapped to a value using a hash function. Provides fast data retrieval based on keys.
d = {'a': 1, 'b': 2}

# Question: How do you access the values associated with keys 'a' and 'b'?
## NOTE: The dictionary cannot have duplicate keys
print(d['a'], d['b'])
## Set: A collection of unique elements that do not allow duplicates
my_set = set()
my_set.add(10)
my_set.add(10)
my_set.add(10)

# Question: What will be the output of my_set?
#(10)
## Tuple: A collection of immutable (non-changeable) elements, tuples retain their order once created.
my_tuple = (1, 'hello', 3.14)

# Question: What is the value of my_tuple?
print(my_tuple)
# Accessing elements by index
print(my_tuple[1])
# Question: How do you access the elements in index 0 and 1 of my_tuple?
print(my_tuple[0:1])
# Counting occurrences of an element
count_tuple = (1, 2, 3, 1, 1, 2)

# Question: How many times does the number 1 appear in count_tuple?
count=0
for i in count_tuple:
    if i == 1:
        count=count+1
print(f'the count of 1 in tuple is {count}')
# Finding the index of an element
# Question: What is the index of the first occurrence of the number 2 in count_tuple?
print(count_tuple.index(2))
# Loop allows a specific chunk of code to be repeated a certain number of times
# Example: We can use a loop to print numbers 0 through 10
for i in range(11):
    print(i)

# We can loop through our data structures as shown below
# Question: How do you loop through a list and print its elements?
for i in l:
    print(i)
# Dictionary loop
# Question: How do you loop through a dictionary and print its keys and values?
for k,v in enumerate(d.items()):
    print(k,v)
# Comprehension is a shorthand way of writing a loop
# Question: Multiply every element in list l with 2 and print the result
multiply = [ x*2 for x in l]
print(multiply)
# Functions: A block of code that can be re-used as needed. This allows for us to have logic defined in one place, making it easy to maintain and use.
## For example, let's create a simple function that takes a list as an input and returns another list whose values are greater than 3

def gt_three(input_list):
    return [elt for elt in input_list if elt > 3]
## NOTE: we use list comprehension with filtering in the above function

list_1 = [1, 2, 3, 4, 5, 6]
# Question: How do you use the gt_three function to filter elements greater than 3 from list_1?
print(gt_three(list_1))
list_2 = [1, 2, 3, 1, 1, 1]
# Question: What will be the output of gt_three(list_2)?
#[3]
# Classes and Objects
# Think of a class as a blueprint and objects as things created based on that blueprint
# You can define classes in Python as shown below
class DataExtractor:

    def __init__(self, some_value):
        self.some_value = some_value

    def get_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

    def close_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

# Question: How do you create a DataExtractor object and print its some_value attribute?
obj1 = DataExtractor(10)
# Libraries are code that can be reused.

# Python comes with some standard libraries to do common operations, 
# such as the datetime library to work with time (although there are better libraries)
from datetime import datetime  # You can import library or your code from another file with the import statement

# Question: How do you print the current date in the format 'YYYY MM DD'? Hint: Google strftime
print(datetime.now().strftime("%Y-%m-%d"))
# Exception handling: When an error occurs, we need our code to gracefully handle it without just stopping. 
# Here is how we can handle errors when the program is running
try:
    # Code that might raise an exception
    pass
except Exception as e: 
    # Code that runs if the exception occurs
    pass
else:
    # Code that runs if no exception occurs
    pass
finally:
    # Code that always runs, regardless of exceptions
    pass

# For example, let's consider exception handling on accessing an element that is not present in a list l
l = [1, 2, 3, 4, 5]
try:
    print(l[5])
except Exception as e:
    print(f'the error we are facing is {e}')
else:
    print(l[4])
finally:
    print([x*2 for x in l if x > 1])
# Question: How do you handle an IndexError when accessing an invalid index in a list?
# NOTE: in the except block its preferred to specify the exact erro/exception that you want to handle
