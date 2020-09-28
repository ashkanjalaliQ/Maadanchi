import pandas as pd

def myfunc(n):
    return n[0]

data = pd.read_csv("iris.csv")

flower_file = open('Featureflowers.txt')

feature_of_flowers = flower_file.readline()
feature_of_flowers = feature_of_flowers.split(',')
feature_of_flowers = feature_of_flowers[:-1]


flower_file.close()
for i in range(len(feature_of_flowers)):
    feature_of_flowers[i] = float(feature_of_flowers[i])
    


data.head()
print(data)
k = 7

sepal_length = data['sepal length'].to_list()
sepal_width = data['sepal width'].to_list()
petal_length = data['petal length'].to_list()
petal_width = data['petal width'].to_list()
class_flower = data['class'].to_list()
res = []

for i in range(len(sepal_length)):
    res.append([abs(sepal_length[i] - feature_of_flowers[0]) + abs(sepal_width[i] - feature_of_flowers[1]) + abs(petal_length[i] - feature_of_flowers[2]) + abs(petal_width[i] - feature_of_flowers[3]), class_flower[i]])

res.sort(key=myfunc)
res = res[:k]

number_of_flower = [0, 0, 0]

## number_of_flower[0] : virginica
## number_of_flower[1] : versicolor
## number_of_flower[2] : setosa

for i in range(len(res)):
    if res[i][1] == 'Iris-virginica':
        number_of_flower[0] += 1
    elif res[i][1] == 'Iris-versicolor':
        number_of_flower[1] += 1
    elif res[i][1] == 'Iris-setosa':
        number_of_flower[2] += 1

if number_of_flower[0] > number_of_flower[1] >= number_of_flower[2] or number_of_flower[0] > number_of_flower[2] >= number_of_flower[1]:
    print('Iris-virginica')
elif number_of_flower[1] > number_of_flower[0] >= number_of_flower[2] or number_of_flower[1] > number_of_flower[2] >= number_of_flower[0]:
    print('Iris-versicolor')
elif number_of_flower[2] > number_of_flower[0] >= number_of_flower[1] or number_of_flower[2] > number_of_flower[1] >= number_of_flower[0]:
    print('Iris-setosa')
