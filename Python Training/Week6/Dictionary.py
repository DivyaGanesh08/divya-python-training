#frequency count
my_list = [1, 2, 2, 3, 3,7,90,90,3]
freq = {}
for x in my_list:
    freq[x] = my_list.count(x)
print(freq)


#return max key value

my_dict = {'a': 10, 'b': 0, 'p':2}
max_key = max(my_dict)
print(max_key) 

#find avg
students = [
    {'id': 211, 'name': 'John', 'dept': 'CSE', 'score': 85},
    {'id': 212, 'name': 'Vijay', 'dept': 'EEE', 'score': 90},
    {'id': 213, 'name': 'Anu', 'dept': 'CSBS', 'score': 78},
    {'id': 214, 'name': 'Raji', 'dept': 'MECH', 'score': 92},
    {'id': 215, 'name': 'Mani', 'dept': 'EEE', 'score': 88},
    {'id': 216, 'name': 'Hari', 'dept': 'IT', 'score': 95},
    {'id': 217, 'name': 'Praveen', 'dept': 'CIVIL', 'score': 80},
    {'id': 218, 'name': 'Moni', 'dept': 'EEE', 'score': 89},
    {'id': 219, 'name': 'Divya', 'dept': 'CSE', 'score': 82},
    {'id': 220, 'name': 'Arjun', 'dept':'AI&DS', 'score': 91}
]

total_score = sum(student['score'] for student in students)
avg_score = total_score / len(students)


print("Average Score:", avg_score)
