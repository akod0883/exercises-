numbers = input("Enter list of numbers seperated by spaces ").split(" ")
print(sorted(numbers, key=int))
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))