#Task 1 - Define a function that returns a list of random numbers between 2 values.

#Steps 
#1   - I import the random module. 
#1.1 - What is a module? - A module is a file that contains pre-written Python code. Essentialy - It's an easy way to re-use code!
#1.2 - Name some other modules - NumPy, Pandas, math, random, datetime..
#1.3 - Some of these modules are built-in. Others need to be installed.
#1.4 - To install NumPy for example, you can run the following code: 
#      pip install numpy

#2   - I will define the 'random_numbers_homework' variable using the snake_case naming style.
#2.1 - What other naming styles are there? - camelCaseStyle, PascalCaseStyle, UPPERCASE_STYLE, lowercase_style... 


import random
def random_numbers_homework(start, end, chilli_pepper):

    """    
    function: I will generate a list of random numbers between 'start' and 'end'. 
    args:
        start (int) the lower number
        end (int) the higher number
        chilli_pepper (int) the number of random numers for our list

    Returns:
        list: a list of random numbers

    """  
    my_first_list = []     #Here I created an empty list to store the random numbers we will generate for the list. 
    for _ in range(chilli_pepper): #This line starts a loop that will execute 'chilli_pepper' number of times. The underscore is a placeholder variable (which is a variable to be determined later TBC!!!)
        random_number = random.randint(start, end) #Inside the loop a random number is generated using the randint function form the random module. 'Start' and 'End' values specify the range of the no.s to be generated for the list. 
        my_first_list.append(random_number) #The generated random number is added to the 'my_first_list' list using the append method. 
    return my_first_list #After the loop completes the 'my_first_list' list, is returned as the output function

first_list_output_variable = random_numbers_homework(1, 1000, 7) #The variable 'first_list_output_variable' is assigned the result of calling random_number_homework. I call the function using the 'start' and 'end' variables which I give the values '1' and '1000'. I also set the variable 'chilli_pepper' to the value 7, meaning the loop will execute 7 times. 
print(first_list_output_variable) #Finally.... the value of 'first_list_output_variable' is printed. displaying 7 random numbers between 1 and 1000 !!!!!! 