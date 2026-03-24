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

#find the 1st non repecting ch in a str

s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found")

# group of anagrams 

words = input("Enter words separated by space: ").split()

anagram_dict = {}

for word in words:
    
    key = ''.join(sorted(word))
    
    if key in anagram_dict:
        anagram_dict[key].append(word)
    else:
        anagram_dict[key] = [word]

print("Grouped Anagrams:")
for group in anagram_dict.values():
    print(group)

# find index of 2 nums that sums up the target (input list)

nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

num_dict = {}

for i in range(len(nums)):
    diff = target - nums[i]
    
    if diff in num_dict:
        print("Indices are:", num_dict[diff], "and", i)
        break
    
    num_dict[nums[i]] = i
else:
    print("No solution found")

# merging the 2 dictionarys

dict1 = {"a": 1, "y": 2}
dict2 = {"a": 3, "p": 4}

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    if key in merged:
        
        merged[key] = [merged[key], dict2[key]]
    else:
        merged[key] = dict2[key]

print("Merged Dictionary:", merged)
