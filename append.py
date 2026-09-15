# append function in python is used to add an element at the end of the list. 
# It takes a single argument, which is the element to be added.
#  The syntax for the append function is as follows:

# Example 1:
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

#Example 2:
high_level_languages = ['Python', 'Java', 'C++']
high_level_languages.append('JavaScript')
print(high_level_languages)  # Output: ['Python', 'Java', 'C++', 'JavaScript']

#Example 3:
pakistani_foods = ['Nihari', 'Biryani', 'Karahi']
pakistani_foods.append('jaliebi')
print(pakistani_foods)  # Output: ['Nihari', 'Biryani', 'Karahi', 'jaliebi']


# Example 4:
# if you want to append multiple elements to a list, you can use the extend() method instead of append(). 

operating_systems = ['Windows', 'Linux', 'macOS']
operating_systems.extend(['Android', 'iOS'])
print(operating_systems)  # Output: ['Windows', 'Linux', 'macOS', 'Android', 'iOS']