import pandas as pd, numpy as np, math
from sklearn import linear_model, model_selection
def iris():
    data = pd.read_csv("iris.csv")
    predict_column = "class"
    iris_data = data[["sepal length", "sepal width", "petal length", "petal width", "class"]]
    features = np.array(iris_data.drop([predict_column], axis=1))
    labels = np.array(data[predict_column])
    features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size = 0.2)
    linear = linear_model.LinearRegression()
    linear.fit(features_train, labels_train)
    dispute = []
    predictions = linear.predict(features_test)
    for i in range(len(predictions)):
        predictions[i] = round(predictions[i])
        print("real :", labels_test[i])
        print("predicted :", int(predictions[i]))
        dispute.append(abs(labels_test[i] - predictions[i]))
        print("------------------------------")
    accuracy = 100 - ((sum(dispute) / len(dispute) * 100) / 2)
    return 'average dispute :' + str(sum(dispute) / len(dispute)) + '\n' + 'Accuracy : ' + str(accuracy) + '%'
print(iris())