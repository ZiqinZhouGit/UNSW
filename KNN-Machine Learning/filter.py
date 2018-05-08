from pandas import DataFrame
import arff


def all_digit(l):
    temp = 0
    while temp < len(l):
        if l[temp].lstrip('-+').isnumeric():
            temp += 1
        else:
            break
    if temp == len(l):
        return True
    else:
        return False


dict_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
            'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12}


def all_text_number(l):
    temp = 0
    while temp < len(l):
        if l[temp] in dict_num:
            temp += 1
        else:
            break
    if temp == len(l):
        return True
    else:
        return False


def filt_into_df(filename, target_feature):
    f = open(filename, 'r')
    data = arff.load(f)

    attributes = []
    index_removed_attr = []
    for i in range(len(data['attributes'])):
        a = data['attributes'][i]
        # pick all numerical features:
        if a[0] == target_feature:
            attributes.append(a[0])
        elif type(a[1]) == str and a[1] == 'REAL':
            attributes.append(a[0])
        # pick all features in digital string type:['one',] or ['-1']
        elif type(a[1]) == list:
            if all_digit(a[1]):  # or all_text_number(a[1]):
                attributes.append(a[0])
            else:
                index_removed_attr.append(i)

    for i in range(len(index_removed_attr)):
        index_removed_attr[i] -= i
    data_set = data['data']  # get all items
    filtered_data_set = []
    for i in range(len(data_set)):
        instance = data_set[i]
        for j in index_removed_attr:
            del instance[j]
        if not (None in instance):
            for i in range(len(instance)):
                if instance[i] in dict_num:
                    s = instance[i]
                    instance[i] = dict_num[s]
                if type(instance[i]) == str:
                    if instance[i].lstrip('-+').isnumeric():
                        s = instance[i]
                        instance[i] = int(s)

            filtered_data_set.append(instance)

    df = DataFrame(filtered_data_set, columns=attributes)
    return df
