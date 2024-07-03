'''Example 1: Define a function that takes an argument.
    Call the function. 
    Identify what code is the argument and what code is the parameter.
'''
'''def greetings(name):#function definition,name is the parameter
    print('Hello '  + name + ', How are you?') # should be indented  to tell python that this print belongs to the function
    
#first call
greetings("Beth")

#second call  with a variable name
name = "Mirriam"
greetings(name)

#third call with  an expression
greetings(str(8 + 9))
'''
  
'''def add(result):
    result = " done"
    print(result)
    
result = "I am done"
add(result)
'''       

'''def greet(name):#takes one argument named name
        print(f"The value of our parameter is {name}") #prints the value of name  
greet ("Nyarie")  #call the function
print(name)   #trying to acess the parameter outside the function                                                                                           
'''




name = "global variable" #variable declared out of the function - global variable
def Var():#function defination
    name = 'local variable'#local variable
    print(f'im the variable inside the function' )#print local var
    print()#skip line
    
print('hello from ', name) #print out of function
print()
Var()#calling function
print('After calling function print:', name)#printing global variable