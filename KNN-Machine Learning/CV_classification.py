from classification import handle_file
from classification import knn
from sklearn.metrics import f1_score

def performance(file_name,target_feature,value):
    predict_class_list = []
    original_class_list = []
    full_data = handle_file(file_name,target_feature)
    for i in range(len(full_data)):
        full_data_copy = full_data[:i] + full_data[i+1:]
        target = full_data[i]
        train_set_cv = {'b':[],'g':[]}
        for ii in full_data_copy:
            train_set_cv[ii[-1]].append(ii[:-1])
        predict = knn(train_set_cv,target[:-1],k=value)
        original_class_list.append(target[-1])
        predict_class_list.append(predict)
    return f1_score(original_class_list,predict_class_list,average='macro')

def score(file_name,target_feature,r):
    score_list = []
    for k_value in list(r):
        score = performance(file_name,target_feature,k_value)
        score_list.append(score)
    return score_list

def predict_class(file_name, target_feature, instance):
    full_data = handle_file(file_name,target_feature)
    train_set_cv = {'b':[],'g':[]}
    for ii in full_data:
        train_set_cv[ii[-1]].append(ii[:-1])
    result = knn(train_set_cv,instance)
    return result

# instance = [1,0,0.64710,0.33533,0.74638,-0.07151,0.67873,0.08260,0.88928,-0.08139,0.78735,0.06678,0.60668,-0.01351,0.83262,-0.01054,0.85764,-0.04769,0.87170,-0.03615,0.81722,-0.09490,0.71002,0.04394,0.80467,-0.19114,0.61147,-0.04822,0.38207,-0.01703,0.75747,-0.09678,0.45764,-0.03151]
#
# print(predict('ionosphere.arff','class',instance))
