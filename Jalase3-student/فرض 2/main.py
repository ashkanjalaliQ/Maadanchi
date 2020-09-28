import pandas as pd

def myfunc(n):
    return n[0]

data = pd.read_csv('student-mat.csv')
len(data)
data['pass'] = data.apply(lambda row: 1 if (row['G1'] + row['G2'] + row['G3']) >= 35 else 0, axis=1)
data = data.drop(['G1', 'G2', 'G3'], axis=1)
data.head()
print(data)

k = 5

print('Passed Student: ', len(data[data['pass'] == 1]) / len(data))
print('Failed Student: ', len(data[data['pass'] == 0]) / len(data))
print(data['reason'].unique())
data = pd.get_dummies(data, columns = [
        'sex',
        'school',
        'address',
        'famsize',
        'Pstatus',
        'Mjob',
        'Fjob',
        'reason',
        'guardian',
        'schoolsup',
        'famsup',
        'paid',
        'activities',
        'nursery',
        'higher',
        'internet'
])
print(data)
data.to_csv('test.csv', header=True, index=False)
student_file = open('FeatureOfStudent.txt')

feature_of_student = student_file.readline()
feature_of_student = feature_of_student.split(',')
feature_of_student = feature_of_student[:-1]


student_file.close()
for i in range(len(feature_of_student)):
    feature_of_student[i] = int(feature_of_student[i])
    
#property_stu = open('test.csv')

#property_stu = property_stu.readline()
property_stu = 'age,Medu,Fedu,traveltime,studytime,failures,famrel,freetime,goout,health,absences,pass,sex_F,sex_M,school_GP,school_MS,address_R,address_U,famsize_GT3,famsize_LE3,Pstatus_A,Pstatus_T,Mjob_at_home,Mjob_health,Mjob_other,Mjob_services,Mjob_teacher,Fjob_at_home,Fjob_health,Fjob_other,Fjob_services,Fjob_teacher,reason_course,reason_home,reason_other,reason_reputation,guardian_father,guardian_mother,guardian_other,schoolsup_no,schoolsup_yes,famsup_no,famsup_yes,paid_no,paid_yes,activities_no,activities_yes,nursery_no,nursery_yes,higher_no,higher_yes,internet_no,internet_yes'
property_stu = property_stu.split(',')

student_data = open('test.csv', 'r')
student_data = student_data.readlines()[1:]
for i in range(len(student_data)):
    student_data[i] = student_data[i].split(',')
    for j in range(len(student_data[i])):
        student_data[i][j] = int(student_data[i][j])
print(student_data)

result = 0

distance = []

for i in range(len(student_data)):
    result = 0
    for j in range(len(student_data[i])):
        result += student_data[i][j]
    distance.append([result, i])

distance.sort(key = myfunc)
distance = distance[:k]

student_data = open('student-mat.csv', 'r')
student_data = student_data.readlines()[1:]

neighbor = []

for i in range(len(distance)):
    neighbor.append(student_data[distance[i][1]][:-1].split(','))

passeds = 0
faileds = 0

print(neighbor)
print(distance)

scores  = 0

for i in range(len(neighbor)):
    scores = int(neighbor[i][-1]) + int(neighbor[i][-2]) + int(neighbor[i][-3])
    if scores >= 35:
        passeds += 1
    else:
        faileds += 1
print(passeds)
print(faileds)
if passeds > faileds:
    print('Pass!')
else:
    print('Failed!')