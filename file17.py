# Modules in Python
# Use modules to organize codes into different files

import file17converter # One way
from file17converter import kg_to_lbs # Separately
from file17converter import lbs_to_kg

#file17converter.lbs_to_kg() "When importing the whole file"

kg_to_pounds_10 = kg_to_lbs(10)
print(kg_to_pounds_10)

lbs_to_kg_10 = lbs_to_kg(10)
print(lbs_to_kg_10)


