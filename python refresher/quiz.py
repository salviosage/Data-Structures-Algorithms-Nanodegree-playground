def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form 
            # the conditional statement, although this was
            # not introduced above. 
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None


# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# In this exercise, you will need to complete the function 
# when_offered(courses, course). This function accepts a "courses" 
# data structure and a "course" string. 
# The function should return a list of strings representing the semesters 
# when the input course is offered. See the two test cases below for examples 
# of correct results.


def when_offered(courses, course):
    # TODO: Fill out the function here.
    semesters = []
    for semester in courses:
        if course in courses[semester]:
            semesters.append(semester)
    # TODO: Return list of semesters here.
    return semesters



print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []
