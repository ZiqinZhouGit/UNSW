from filter import filt_into_df
from normalize import normalize_df, normalize_point
from prediction import predict
import math
import matplotlib.pyplot as plt

filename = 'autos.arff'
target_feature = 'price'
k_range = range(1,23)


def cross_validation_p(filename, target_feature, k_range):
    df = filt_into_df(filename, target_feature)
    # apply 0-1 normalization to the filtered data
    normalized_df = normalize_df(df, target_feature)

    list_mape = []
    list_sde = []
    list_r_mape = []
    list_r_sde = []
    for k in k_range:
        for n in range(len(normalized_df)):
            test_point = dict(normalized_df.loc[n])
            true_value = test_point[target_feature]
            del test_point[target_feature]
            df = normalized_df.drop([n])
            predict_value = predict(df, test_point, target_feature, k)

            mape = abs(1 - predict_value/true_value)
            sde = (true_value - predict_value)**2
            list_mape.append(mape)
            list_sde.append(sde)

        list_r_mape.append(sum(list_mape) / len(list_mape))
        list_r_sde.append(math.sqrt(sum(list_sde) / len(list_sde)))
    result_dict = {'MAPE':list_r_mape,"SDE":list_r_sde}
    return result_dict

