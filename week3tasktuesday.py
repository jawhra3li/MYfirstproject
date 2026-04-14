records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]
result = {}
subjects = {}
for name, subject, mark in records:
    if name not in result:
        result[name] = {}
    result[name][subject] = mark
    if subject not in subjects:
        subjects[subject] = []
    subjects[subject].append(mark)
for name in result:
    total = sum(result[name].values())   
    count = len(result[name])            
    avg = total / count                 
    print(name, avg)
for subject in subjects:
    total = sum(subjects[subject])      
    count = len(subjects[subject])      
    avg = total / count                 
    print(subject, avg)