import pandas

def normalize_df(df, target_feature):
    if type(df) == pandas.core.frame.DataFrame:
        ndf = df.copy()
        features = list(ndf.columns)
        if target_feature in features:
            features.remove(target_feature)
        min_dict = {}
        base_dict = {}
        for f in features:
            column = list(ndf[f])
            min_dict[f] = min(column)
            base_dict[f] = max(column) - min(column)
        for f in features:
            for n in range(len(ndf)):
                base = base_dict[f]
                min_v = min_dict[f]
                temp = ndf.loc[n, f]
                if base == 0:
                    ndf.loc[n, f] = 0
                else:
                    ndf.loc[n, f] = (temp - min_v) / base
        return ndf

def normalize_point(df, target_feature, dictionary):
    ndf = df.copy()
    features = list(ndf.columns)
    if target_feature in features:
        features.remove(target_feature)
    min_dict = {}
    base_dict = {}
    for f in features:
        column = list(ndf[f])
        min_dict[f] = min(column)
        base_dict[f] = max(column) - min(column)
    test_point = {}
    for f in features:
        if f in dictionary:
            min_v = float(min_dict[f])
            base = float(base_dict[f])
            temp = float(dictionary[f])
            if base == 0:
                test_point[f] = 0
            else:
                test_point[f] = (temp - min_v) / base

    return test_point