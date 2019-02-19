student1=["bilal","nemutlu","1155142"]
student2=["burcu","boluknasi","1154970"]
classroom = [student1,student2]
 

for student in classroom:
    print("first name: {} ------------ last name: {}".format(student[0],student[1]))
 
 
 
 # Loop over a single list with a regular for-in:

# for n in numbers:
    # print(n)
# Loop over multiple lists at the same time with zip:

# for header, rows in zip(headers, columns):
    # print("{}: {}".format(header, ", ".join(rows)))
# Loop over a list while keeping track of indexes with enumerate:

# for num, line in enumerate(lines):
    # print("{0:03d}: {}".format(num, line))
