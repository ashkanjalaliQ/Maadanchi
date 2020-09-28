def tree(flower_file):
    feature_of_flowers = flower_file.split(',')
    feature_of_flowers = feature_of_flowers[:-1]
    
    for i in range(len(feature_of_flowers)):
        feature_of_flowers[i] = float(feature_of_flowers[i])

    if 0.1 <= feature_of_flowers[3] <= 0.6:
        if 1 <= feature_of_flowers[2] <= 1.9:
            if 4.3 <= feature_of_flowers[0] <= 5.8:
                if 2.3 <= feature_of_flowers[1] <= 4.4:
                    return 'Iris-setosa'
            
    elif 1 <= feature_of_flowers[3] <= 1.8:
        if 3 <= feature_of_flowers[2] <= 5.1:
            if 4.9 <= feature_of_flowers[0] <= 7:
                if 2 <= feature_of_flowers[1] <= 3.4:
                    return 'Iris-versicolor'
    
    if 1.4 <= feature_of_flowers[3] <= 2.5:
        if 4.5 <= feature_of_flowers[2] <= 6.9:
            if 4.9 <= feature_of_flowers[0] <= 7.9:
                if 2.2 <= feature_of_flowers[1] <= 3.8:
                    return 'Iris-virginica'
file_address = 'iris_test.csv'
flower_file = open(file_address)
flower_file = flower_file.readlines()
flower_name = flower_file.copy()
for i in range(len(flower_name)):
    flower_name[i] = flower_name[i].split(',')
    flower_name[i][-1] = flower_name[i][-1][:-1]
    flower_name[i] = flower_name[i][-1]

correct = 0
incorrect = 0

for i in range(len(flower_file)):
    if tree(flower_file[i]) == flower_name[i]:
        correct += 1
    else:
        incorrect += 1
        
print('Correct : ', correct)
print('Incorrect : ', incorrect)

print(correct * 100 / len(j))