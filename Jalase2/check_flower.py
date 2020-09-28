import pandas as pd

def myfunc(n):
    return n[0]

def main(feature_of_flowers, train_data, k):

    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    class_flower = []
    for i in range(150 // k * (k - 1)):
        sepal_length.append(train_data[i][0])
        sepal_width.append(train_data[i][1])
        petal_length.append(train_data[i][2])
        petal_width.append(train_data[i][3])
        class_flower.append(train_data[i][4])
        
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
        return 'Iris-virginica'
    elif number_of_flower[1] > number_of_flower[0] >= number_of_flower[2] or number_of_flower[1] > number_of_flower[2] >= number_of_flower[0]:
        return 'Iris-versicolor'
    elif number_of_flower[2] > number_of_flower[0] >= number_of_flower[1] or number_of_flower[2] > number_of_flower[1] >= number_of_flower[0]:
        return 'Iris-setosa'
