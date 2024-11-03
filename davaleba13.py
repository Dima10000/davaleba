import csv
from statistics import mean

def add_student_info(filepath, student_data):
    records = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        records = list(reader)
    
    records.append(student_data)
    records.sort(key=lambda x: int(x['id']))

    with open(filepath, mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

def fetch_students(filepath, student_id=None):
    results = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for entry in reader:
            if student_id is None or entry['id'] == str(student_id):
                results.append(entry)
    
    return results

def average_marks(filepath, subject):
    marks = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for entry in reader:
            if entry['subject_name'] == subject:
                marks.append(float(entry['mark']))
    
    return mean(marks) if marks else 0

def modify_student_mark(filepath, student_id, subject, updated_mark):
    records = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        records = list(reader)
    
    for entry in records:
        if entry['id'] == str(student_id) and entry['subject_name'] == subject:
            entry['mark'] = str(updated_mark)
            break

    with open(filepath, mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
