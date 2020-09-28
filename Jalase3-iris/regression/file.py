iris_file_1 = open('C://Users//lenovo//Desktop//Maadanchi//Jalase3-iris//regression//iris.txt', 'r')
iris_file = iris_file_1.readlines()
iris_file_1.close()
#iris_file = iris_file[1:]
for i in range(1, len(iris_file)):
    iris_file[i] = iris_file[i].split(',')
    if iris_file[i][-1][:-1] in 'Iris-virginica':
        iris_file[i][-1] = str(0)
    elif iris_file[i][-1][:-1] in 'Iris-versicolor':
        iris_file[i][-1] = str(1)
    elif iris_file[i][-1][:-1] in 'Iris-setosa':
        iris_file[i][-1] = str(2)
result = 'sepal length,sepal width,petal length,petal width,class' + '\n'
res = ''
print(len(iris_file))
for i in range(1, len(iris_file)):
    res = ''
    for j in range(len(iris_file[i])):
        if j == len(iris_file[i]) - 1:
            res += iris_file[i][j] + '\n'
        else:
            res += iris_file[i][j] + ','
    result += res
print(result)
iris_write = open('iris.txt', 'w')
iris_write.write(result)