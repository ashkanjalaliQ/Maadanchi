import pandas as pd

def to_one_list(ls):
    all_train = []
    for i in range(len(train)):
        all_train += train[i]
    return all_train
def main(filename, main_flower_class, attributes, t):
    data = pd.read_csv(filename)

    data.head()

    sepal_length = data[attributes[0]].to_list()
    sepal_width = data[attributes[1]].to_list()
    petal_length = data[attributes[2]].to_list()
    petal_width = data[attributes[3]].to_list()
    class_flower = data[attributes[4]].to_list()
    
    
    iris_setosa = []
    iris_versicolor = []
    iris_virginica = []
    
    for i in range(len(sepal_length)):
        if class_flower[i] == main_flower_class[0]:
            iris_setosa.append([sepal_length[i], sepal_width[i], petal_length[i], petal_width[i], 'Iris-setosa'])
        
        elif class_flower[i] == main_flower_class[1]:
            iris_versicolor.append([sepal_length[i], sepal_width[i], petal_length[i], petal_width[i], 'Iris-versicolor'])
        
        elif class_flower[i] == main_flower_class[2]:
            iris_virginica.append([sepal_length[i], sepal_width[i], petal_length[i], petal_width[i], 'Iris-virginica'])
    
    test_and_train = []
    
    
    
    
    
    
    tedad = len(sepal_length) // t
    tedad = tedad // 3
    
    
    
    for i in range(t):
        test_and_train.append(iris_setosa[i * tedad : i * tedad + tedad] + iris_versicolor[i * tedad : i * tedad + tedad] + iris_virginica[i * tedad : i * tedad + tedad])
    #print(len(test_and_train[0]))

    trains = []
    tests = []
    
    for i in range(t):
        tests.append(test_and_train[i])
        ls = []
        for j in range(t):
            if j != i:
                ls += test_and_train[j]
        trains.append(ls)
    print(len(trains[0]))
    print(len(tests[0]))
    
    
    
    return [trains, tests]