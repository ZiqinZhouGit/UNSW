# Filename: kNN.py
from cv_of_prediction import cross_validation_p
from CV_classification import score,predict_class
from filter import filt_into_df
from normalize import normalize_df, normalize_point
from prediction import predict
import matplotlib.pyplot as plt
import csv
import sys
import collections

count_parameter = len(sys.argv)
if sys.argv[1] == '-r':
    if count_parameter == 6:
        filename = sys.argv[2]
        target_feature = sys.argv[3]
        k_range_low = int(sys.argv[4])
        k_range_up = int(sys.argv[5]) + 1
        k_range = list(range(k_range_low,k_range_up))
        if filename == 'autos.arff':
            result_list = cross_validation_p(filename, target_feature, k_range)
            print('===== SDE =====')
            t = k_range_low
            for i in result_list['SDE']:
                print('k =',t,end = ' | ')
                print('SDE =',i)
                t += 1
            print('===== MAPE =====')
            t = k_range_low
            for i in result_list['MAPE']:
                print('k =', t, end=' | ')
                print('MAPE =',i)
                t += 1
        elif filename == 'ionosphere.arff':
            print("===== F1 Score =====")
            t = k_range_low
            result_list = score(filename, target_feature, k_range)
            for i in result_list:
                print('k =', t, end=' | ')
                print('F1 Score = ',i)
                t += 1

    elif count_parameter == 5:
        filename = sys.argv[2]
        target_feature = sys.argv[3]
        k = int(sys.argv[4])
        k_range = [k,]
        if filename == 'autos.arff':
            result_list = cross_validation_p(filename, target_feature, k_range)
            print('===== SDE =====')
            for i in result_list['SDE']:
                print('k =', k, end=' | ')
                print('SDE =',i)
            print('===== MAPE =====')
            for i in result_list['MAPE']:
                print('k =', k, end=' | ')
                print('MAPE =',i)
        elif filename == 'ionosphere.arff':
            print("===== F1 Score =====")
            result_list = score(filename, target_feature, k_range)
            for i in result_list:
                print('k =', k, end=' | ')
                print('F1 Score = ', i)

elif sys.argv[1] == '-f':
    filename = sys.argv[2]
    target_feature = sys.argv[3]
    k_range_low = int(sys.argv[4])
    k_range_up = int(sys.argv[5]) + 1
    k_range = list(range(k_range_low, k_range_up))

    if filename == 'autos.arff':
        result = cross_validation_p(filename, target_feature, k_range)
        x = k_range
        y = result['SDE']
        plt.figure(1,figsize=(8, 4))
        plt.plot(x, y, label="$MAPE$", color="red", linewidth=1)
        plt.xlabel("K_value")
        plt.ylabel("MAPE")
        plt.title("Evaluate with different K")
        plt.legend()
        plt.show()

        y = result['MAPE']
        plt.figure(2,figsize=(8, 4))
        plt.plot(x, y, label="$MAPE$", color="red", linewidth=1)
        plt.xlabel("K_value")
        plt.ylabel("SDE")
        plt.title("Evaluate with different K")
        plt.legend()
        plt.show()

    elif filename == 'ionosphere.arff':
        x = k_range
        y = score(filename, target_feature, k_range)
        plt.figure(figsize=(8, 4))
        plt.plot(x, y, label="$f1_score$", color="red", linewidth=1)
        plt.xlabel("K_value")
        plt.ylabel("f1_score")
        plt.title("Performance with K")
        plt.legend()
        plt.show()

elif sys.argv[1] == '-v':
    filename = sys.argv[2]
    target_feature = sys.argv[3]
    testfile = sys.argv[4]
    k = int(sys.argv[5])
    list_dict = []
    with open(testfile) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            temp_dict = {}
            for n in range(len(row)):
                ind = headers[n]
                val = row[n]
                temp_dict[ind] = val
            list_dict.append(temp_dict)

    if filename == 'autos.arff':
        count = 0
        for d in list_dict:
            df = filt_into_df(filename, target_feature)
            normalized_df = normalize_df(df, target_feature)
            test_point = normalize_point(df, target_feature, d)
            r = predict(normalized_df, test_point, target_feature, k)
            print('Prediction of',target_feature,'for instance', count, 'is', r)
            count += 1

    elif filename == 'ionosphere.arff':
        count = 0
        for d in list_dict:
            instance = []
            od = collections.OrderedDict(sorted(d.items()))
            for i in od:
                instance.append(d[i])
            print(instance)
            r = predict_class(filename, target_feature, instance)
            print('Prediction of', target_feature, 'for instance', count, 'is', r)
            count += 1

