# Exercise 3
from pathlib import Path
# import functions from utils here

data_dir = Path("data")
output_dir = Path("solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

base_dir = Path("C:/Users/CSeimn/Documents/Master/2._Semester/Python_Kurs") # create the base directory
exc_dir = base_dir / "exercise-3-CSeimn" # create a subdirectory to the specific exercise
txt_dir = exc_dir / "data/cars.txt"

# 2. Read the text file [2P]
with open (txt_dir, "r") as file:
    txt = file.readlines()
    lines =  [line.rstrip('\n') for line in txt]
print(lines)

# 3. Count the occurences of each item in the text file [2P]
from collections import Counter
counter = Counter(lines)


# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]
sol_dir = exc_dir / "solutions"
sol_dir.exists()
sol_dir.mkdir(parents = True, exist_ok = True)


# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
with open("solution.csv", "w") as file:
    file.writelines("item", "count")
    for i in counter:
    file.write(counter.items(i))