import pandas as pd


data = pd.read_csv('student-por.csv', sep=';')

scores = []

for j in range(len(data['school'])):
    grade = int(data['G1'].to_list()[j]) + int(data['G2'].to_list()[j]) + int(data['G3'].to_list()[j])
    if grade >= 35:
        scores.append(1)
    else:
        scores.append(0)
data.head()        


dataset = {
    'school' : data['school'].to_list(),
    'sex' : data['sex'].to_list(),
    'age' : data['age'].to_list(),
    'address' : data['address'].to_list(),
    'famsize' : data['famsize'].to_list(),
    'Pstatus' : data['Pstatus'].to_list(),
    'Medu' : data['Medu'].to_list(),
    'Fedu' : data['Fedu'].to_list(),
    'Mjob' : data['Mjob'].to_list(),
    'Fjob' : data['Fjob'].to_list(),
    'reason' : data['reason'].to_list(),
    'guardian' : data['guardian'].to_list(),
    'traveltime' : data['traveltime'].to_list(),
    'studytime' : data['studytime'].to_list(),
    'failures' : data['failures'].to_list(),
    'schoolsup' : data['schoolsup'].to_list(),
    'famsup' : data['famsup'].to_list(),
    'paid' : data['paid'].to_list(),
    'activities' : data['activities'].to_list(),
    'nursery' : data['nursery'].to_list(),
    'higher' : data['higher'].to_list(),
    'internet' : data['internet'].to_list(),
    'romantic' : data['romantic'].to_list(),
    'famrel' : data['famrel'].to_list(),
    'freetime' : data['freetime'].to_list(),
    'goout' : data['goout'].to_list(),
    'Dalc' : data['Dalc'].to_list(),
    'Walc' : data['Walc'].to_list(),
    'health' : data['health'].to_list(),
    'absences' : data['absences'].to_list(),
    'G1' : data['G1'].to_list(),
    'G2' : data['G2'].to_list(),
    'G3' : data['G3'].to_list(),
    'Pass' : scores
    
}

df = pd.DataFrame(dataset)

df.to_csv('main.csv', index=False)

