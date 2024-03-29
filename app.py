import random
import find_specific_number as fsp

numbers = random.sample(range(0, 201, 2), 3)
print(numbers)

max_number_inList = fsp.find_max(numbers)