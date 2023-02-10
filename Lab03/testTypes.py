# testTypes.py
# playing with variable types

int1 = 12
var1 = type(int1)
#print (f"int1 is of type ",(var1), "and value is",int1)

float1 = 12.75
var2 = type(float1)
#print (f"int1 is of type ",(var2), "and value is",float1)

boolean1 = True
var3 = type(boolean1)
#print (f"int1 is of type ",(var3), "and value is",boolean1)

str1 = "Hello"
var4 = type(str1)
#print (f"int1 is of type ",(var4), "and value is",str1)

list1 = [1,2,3]
var5 = type(list1)
#print (f"int1 is of type ",(var5), "and value is",list1)


print('\nvariable {} is of type:{} and value: {}'.format('int', type(int1), int1))
print('variable {} is of type:{} and value: {}'.format('float1', type(float1), float1))
print('variable {} is of type:{} and value: {}'.format('boolean1', type(boolean1), boolean1))
print('variable {} is of type:{} and value: {}'.format('str1', type(str1), str1))
print('variable {} is of type:{} and value: {}'.format('list1', type(list1), list1))
# Or we could use the following to print using the f string
print(f"\nvariable Int1 is of type {var1} and value: {int1}")
print(f"variable float1 is of type {var2} and value: {float1}")
print(f"variable boolean1 is of type {var3} and value: {boolean1}")
print(f"variable str1 is of type {var4} and value: {str1}")
print(f"variable list1 is of type {var5} and value: {list1}")