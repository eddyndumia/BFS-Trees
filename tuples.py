


# creating tuples without brakcets 

mytuple = '1', '2', '3', '4', '5', '6', '7', '8', '9'

print(mytuple)

# creating with brackets

mytuple2 = ('1', '2', '3', '4', '5', '6', '7', '8')

print(mytuple2)

# creating a tuple using the in-built function

newtuple = tuple('my name is eddy ndumia')

print(newtuple)

# slicing cuts the tuple from the first index to the last, excluding the last index
# used to print tuple elements easily

print(mytuple2[0:5])

# traversing through a tuple
# for i in mytuple2:
        #print(i)
        
go_signal = '3' in mytuple2

if go_signal:
    print("GO GO GO GO")