import os

print(os.listdir())

print(os.getcwd())

print("The table of 5 is given below:")
for i in range(1,11): 
    print(f"5x{i} = {5*i}")
