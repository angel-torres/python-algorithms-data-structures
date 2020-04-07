import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# O(n^2) because we are having to loop twice
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

names_dictionary = {}

# this solution is O(n) which is much faster- making a dictionary makes search much faster than having to loop over array for every item in the array
for name_1 in names_1:
    if name_1 in names_dictionary:
        names_dictionary[name_1] += 1
    else:
        names_dictionary[name_1] = 1

for name_2 in names_2:
    if name_2 in names_dictionary:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")