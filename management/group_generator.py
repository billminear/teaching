
import os
import csv
from pprint import pprint
from random import randint

lab_directory = r'.\lab_01'
group_file_name = 'groups.csv'
group_file_path = os.path.join(lab_directory, group_file_name)

students = []

# to fill with groups of students.
pairs = []

# to fill with groups and their numbers.
groups = {}

# loop until student list is empty.
while students:

	pair = []

	# get number of students and append one to the group list.
	student_count = len(students)
	pair.append(students.pop(randint(0, student_count-1)))

	# add second student to the group list.
	# if there's an odd total of students, no need to append a second
	# student to the final list.
	if len(students) != 0:
		pair.append(students.pop(randint(0, student_count-2)))

	# append list of two students to the list of all groups.
	pairs.append(pair)

	# clear group list if a pair is reached.
	if len(pair) == 2:
		pair = []

# generate groups.
for group_number in range(1, len(pairs)+1):
	groups[group_number] = pairs.pop()

with open(group_file_path, 'w', newline='') as group_file:

	csv_writer = csv.writer(group_file)

	csv_writer.writerow(['Group Number','Group Member','Group Member','Notes'])

	for group in groups:
		csv_writer.writerow([group, groups[group][0], groups[group][1]])
		# print([group, group[group])





