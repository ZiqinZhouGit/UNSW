import numpy as np
from collections import Counter
from filter import filt_into_df
from sklearn.metrics import f1_score
from normalize import normalize_df, normalize_point

# according to the E-distance, using the default parameter k=5, we build our own knn algorithm
def knn(data, sample, k=5):
    for n in range(len(sample)):
        t = float(sample[n])
        sample[n] = t
    EDs = []
    for group in data:
        for features in data[group]:
            ED = np.linalg.norm(np.array(features)-np.array(sample))
            EDs.append([ED,group])
    votes = []
    for i in sorted(EDs)[:k]:
        vote = i[1]
        votes.append(vote)
    votes_result = Counter(votes).most_common(1)[0][0]

    return votes_result

def handle_file(filename, target_feature):
    df_1 = filt_into_df(filename,target_feature)
    df_final = normalize_df(df_1, target_feature)
    full_data = df_final.values.tolist()
    return full_data

# using f1_score mwthod to evaluate the algorithm, by changing the value of k, we can get different result
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


