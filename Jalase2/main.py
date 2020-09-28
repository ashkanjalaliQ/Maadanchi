import Split_features, check_flower

k = 5

alltext = Split_features.main('iris.csv', ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'], k)
trains, tests = alltext[0], alltext[1]
incorrect = correct = 0
for j in range(len(tests)):
    for i in range(len(tests[j])):
        if check_flower.main(tests[j][i][:-1], trains[j], k) == tests[j][i][-1]:
            correct += 1
        else:
            incorrect += 1
print('Correct : ' + str((correct / k * 100) / 30) + '%')
#print('Incorrect : ', (incorrect / 5 * 100) / 30)