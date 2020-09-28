iris_file = open('iris_train.csv')
iris_file = iris_file.readlines()


def sort_by_0(n):
    return n[0]
def sort_by_1(n):
    return n[1]
def sort_by_2(n):
    return n[2]
def sort_by_3(n):
    return n[3]

setosa_range = []
versicolor_range = []
virginica_range = []

for i in range(len(iris_file)):
    iris_file[i] = iris_file[i].split(',')
    iris_file[i][-1] = iris_file[i][-1][:-1]
    if iris_file[i][-1] == 'Iris-setosa':
        setosa_range.append([iris_file[i][0], iris_file[i][1], iris_file[i][2], iris_file[i][3]])
    elif iris_file[i][-1] == 'Iris-versicolor':
        versicolor_range.append([iris_file[i][0], iris_file[i][1], iris_file[i][2], iris_file[i][3]])
    elif iris_file[i][-1] == 'Iris-virginica':
        virginica_range.append([iris_file[i][0], iris_file[i][1], iris_file[i][2], iris_file[i][3]])
        
        
setosa_range.sort(key=sort_by_0)
versicolor_range.sort(key=sort_by_0)
virginica_range.sort(key=sort_by_0)

print('setosa : ', setosa_range[0][0], ' < ', 'range', ' < ', setosa_range[-1][0])
print('versicolor : ', versicolor_range[0][0], ' < ', 'range', ' < ', versicolor_range[-1][0])
print('virginica : ', virginica_range[0][0], ' < ', 'range', ' < ', virginica_range[-1][0])


print()


setosa_range.sort(key=sort_by_1)
versicolor_range.sort(key=sort_by_1)
virginica_range.sort(key=sort_by_1)

print('setosa : ', setosa_range[0][1], ' < ', 'range', ' < ', setosa_range[-1][1])
print('versicolor : ', versicolor_range[0][1], ' < ', 'range', ' < ', versicolor_range[-1][1])
print('virginica : ', virginica_range[0][1], ' < ', 'range', ' < ', virginica_range[-1][1])


print()


setosa_range.sort(key=sort_by_2)
versicolor_range.sort(key=sort_by_2)
virginica_range.sort(key=sort_by_2)

print('setosa : ', setosa_range[0][2], ' < ', 'range', ' < ', setosa_range[-1][2])
print('versicolor : ', versicolor_range[0][2], ' < ', 'range', ' < ', versicolor_range[-1][2])
print('virginica : ', virginica_range[0][2], ' < ', 'range', ' < ', virginica_range[-1][2])


print()


setosa_range.sort(key=sort_by_3)
versicolor_range.sort(key=sort_by_3)
virginica_range.sort(key=sort_by_3)

print('setosa : ', setosa_range[0][3], ' < ', 'range', ' < ', setosa_range[-1][3])
print('versicolor : ', versicolor_range[0][3], ' < ', 'range', ' < ', versicolor_range[-1][3])
print('virginica : ', virginica_range[0][3], ' < ', 'range', ' < ', virginica_range[-1][3])
