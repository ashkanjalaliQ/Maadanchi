##GP,F,18,U,GT3,A,4,4,at_home,teacher,course,mother,2,2,0,yes,no,no,no,yes,yes,no,no,4,3,4,1,1,3,4,0,11,11
feature_student = input().split(',')
grade = int(feature_student[-1]) + int(feature_student[-2]) + int(feature_student[-3])
if grade >= 35:
    feature_student.append(1)
else:
    feature_student.append(0)
    
if feature_student[-1] == 1:
    if feature_student[0] == 'GP':
        if feature_student[1] == 'F':
            if feature_student[3] == 'U':
                if feature_student[4] == 'GT3':
                    
        
        
    
else:
    