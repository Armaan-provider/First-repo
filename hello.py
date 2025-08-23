import os

print(os.listdir())

print(os.getcwd())

num = int(input("Enter the number you want the table of:"))
print(f"The table of {num} is given below:")
for i in range(1,11): 
    print(f"{num}x{i} = {num*i}")


