from filter import filt_into_df
from normalize import normalize_df, normalize_point
import operator


def predict(normalized_df, test_point, target_feature, k):
    # filter the original data

    # get the features from data
    features = list(normalized_df.columns)
    if target_feature in features:
        features.remove(target_feature)
    # print("the features we select are:")
    # for f in features:
    #     print(f,end = ' ')

    # apply 0-1 normalization to the test data
    # test_point = normalize_point(df, target_feature, test_point)

    # get all distances from test points to all points in training data
    distance_dict = {}
    for n in range(len(normalized_df)):
        try:
            temp_point = dict(normalized_df.loc[n])
        except KeyError:
            continue
        dist_square = 0
        for f in features:
            dist_square += (temp_point[f] - test_point[f]) ** 2
        dist = dist_square ** 0.5
        distance_dict[n] = dist

    # sort the distance:
    sorted_distance = sorted(distance_dict.items(), key=operator.itemgetter(1))

    # get the nearest k points
    kNN_list = []
    for t in sorted_distance[:k]:
        index = t[0]
        neighbor_value = normalized_df.loc[index, target_feature]
        kNN_list.append(neighbor_value)

    # return the mean value of target feature of the nearest k points as result
    result = sum(kNN_list) / len(kNN_list)
    return result
