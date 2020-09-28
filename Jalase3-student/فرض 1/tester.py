import pandas as pd


data = pd.read_csv('main.csv')

print(data)

#print('Pass', len(data[data['Pass'] == 1]) / len(data))
#print('Fail', len(data[data['Pass'] == 0]) / len(data))

school = data['school'].to_list()




pass_stu = data['Pass'].to_list()
sex = data['sex'].to_list()
address = data['address'].to_list()
famsiza = data['famsize'].to_list()
pstatus = data['Pstatus'].to_list()

status_gp = [[0, 0], [0, 0], [[0, 0], [0, 0]], 0, 0]
status_ms = [[0, 0], [0, 0], [[0, 0], [0, 0]]]

## [0] : Grade
## [1] : Sex
## [2] : R or U
## [3] : Famsize
## [4] : Pstatus
for i in range(len(school)):
    if school[i] == 'GP':
        if pass_stu[i] == 1:
            status_gp[0][0] += 1
            if sex[i] == 'M':
                status_gp[1][0] += 1
                if address[i] == 'R':
                    status_gp[2][0][0] += 1
                else:
                    status_gp[2][0][1] += 1
            else:
                status_gp[1][1] += 1
                if address[i] == 'R':
                    status_gp[2][1][0] += 1
                else:
                    status_gp[2][1][1] += 1
                    if famsiza[i] == 'GT3':
                        status_gp[3] += 1
                        if pstatus[i] == 'T':
                            status_gp[4] += 1
                        
        else:
            status_gp[0][1] += 1
    else:
        if pass_stu[i] == 1:
            status_ms[0][0] += 1
            if sex[i] == 'M':
                status_ms[1][0] += 1
                if address[i] == 'R':
                    status_ms[2][0][0] += 1
                else:
                    status_ms[2][0][1] += 1
            else:
                status_ms[1][1] += 1
                if address[i] == 'R':
                    status_ms[2][1][0] += 1
                else:
                    status_ms[2][1][1] += 1
        else:
            status_ms[0][1] += 1
print(status_gp)
print(status_ms)