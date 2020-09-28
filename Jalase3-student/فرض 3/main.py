import pandas as pd
import numpy as np
from sklearn import linear_model, model_selection

################################
#########accuracy >= 82#########
################################

def student():
    
    data = pd.read_csv("student-mat.csv")

    predict_column = "G3"
    
    ## studytime = Important student data
    study_data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
    
    features = np.array(study_data.drop([predict_column], axis=1))
    #print(features)
    labels = np.array(data[predict_column])
    #print(labels)
    features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size = 0.2)
    #print(len(features_train))
    linear = linear_model.LinearRegression()
    linear.fit(features_train, labels_train)

    accuracy = linear.score(features_test, labels_test)
    #print(accuracy * 100)
    dispute = []
    predictions = linear.predict(features_test)
    #print(predictions)
    for i in range(len(predictions)):
        print("real :", labels_test[i])
        print("predicted :", predictions[i])
        dispute.append(abs(labels_test[i] - predictions[i]))
        print("------------------------------")
    print('average dispute :', sum(dispute) / len(dispute))
    return 'Accuracy : ' + str(accuracy * 100) + '%'
print(student())

'''j = 0
num = 2000
for i in range(num):
    j += float(predict()[11:-1])
print(j / num)'''