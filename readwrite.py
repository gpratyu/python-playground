#1: reads name.txt into a variable my_name and then,
with open('name.txt') as f:
    my_name = f.read()

introduction = "Hello, my name is " + my_name

#2. writes a new file named hello.txt with the contents
with open('hello.txt', 'w') as f:
    f.write(introduction)
    f.write('\n')

print(introduction)

