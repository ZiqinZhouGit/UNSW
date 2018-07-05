def add(a, b):  # do not change the heading of the function
    return a + b


##########################################################################
# Question No. 1:
def gallop_to(input_list, target):
    gap = 1
    while not input_list.cur > len(input_list.data):

        original_index = input_list.cur
        input_list.cur += gap
        temp_index = input_list.cur
        print(input_list.cur)

        if input_list.eol():
            return
        if input_list.elem() > target:
            return bs(original_index, temp_index, target, input_list)
        if input_list.elem() == target:
            return
        if input_list.elem() < target:
            gap += gap
    # return len(input_list) -1

def bs(start, end, target, array):
    if start - end >= 0:
        return

    current = (start + end)//2

    if end - start == 1:
        current = end
        return
    if array.data[current] == target:
        return
    if array.data[current]>target:
        return bs(start, current, target, array)
    if array.data[current] < target:
        return bs(current, end, target, array)


##########################################################################
# Question No. 2:

# do not change the function heading

def Logarithmic_merge(index, cut_off, buffer_size):
    def process(LL):
        L_copy = LL[:]
        if len(LL) == 1:
            return L_copy
        for i in range(len(L_copy) - 1):
            if len(L_copy[i]) == len(L_copy[i+1]):
                i_copy = sorted(L_copy[i] + L_copy[i+1])
                L_copy.pop(i)
                L_copy.pop(i)
                L_copy.insert(i, i_copy)
                return L_copy
        return L_copy
    result = [[]]
    index = index[:cut_off]
#     print(index)
    while len(index) != 0:
        j = index.pop(0)
        while 1:
            new = process(result)
            if result == new:
                break
            else:
                result = new
        if len(result[0]) < buffer_size:
            result[0].append(j)
        if len(result[0]) == buffer_size:
            # result.insert(0, [])
            while True:
                new = process(result)
                if result == new:
                    break
                else:
                    result = new
            result.insert(0, [])
    RR = result[:]
    for k in range(len(result)):
        RR[k] = sorted(result[k])
    return RR

def decode_gamma(input_str):# do not change the function heading
    output_list = []
    while len(input_str) > 0:
        first_index = input_str.find('0')
        indicator = input_str[:first_index]
        count = 1 + len(indicator)
        binary_str = input_str[len(indicator) + 1: len(indicator) + count]
        binary_str = "1" + binary_str
        output = int(binary_str, 2)
        output_list.append(output)
        input_str = input_str[count:]
        input_str = input_str[len(binary_str) - 1:]
    return output_list

def decode_delta(input_str):# do not change the function heading
    output_list = []
    while len(input_str) > 0:
        first_index = input_str.find('0')
        unary_bin_indicator = input_str[:first_index]
        length_bin_indicator = len(unary_bin_indicator)
        bin_indicator = input_str[first_index + 1: 2*first_index + 1]
        input_str = input_str[2*first_index + 1:]
        bin_indicator = "1" + bin_indicator
        indicator = int(bin_indicator, 2)
        indicator = indicator - 1
        bin_output = "1" + input_str[:indicator]
        output = int(bin_output, 2)
        input_str = input_str[indicator:]
        output_list.append(output)

    return output_list

def decode_rice(inputs, b):# do not change the function heading
    from math import log
    output_list = []
    while len(inputs) > 0:
        first_index = inputs.find('0')
        indicator = first_index
        # print(indicator)
        q = int(log(b, 2))
        # print(q)
        bin_remain = inputs[indicator + 1: indicator + 1 + q]
        # print(bin_remain)
        remain = int(bin_remain, 2)
        # print(remain)
        output = indicator * b + remain
        # print(output)
        inputs = inputs[first_index + q + 1:]
        # print(inputs)
        output_list.append(output)
    return output_list

##########################################################################
# Question No. 1:
def binary_search(c, start, end, val):
    index = (start + end) // 2
    current = c.data[index]
    if current == val:
        c.cur = index
        return
    if end - start == 1:
        c.cur = end
        return
    if current < val:
        return binary_search(c, index, end, val)
    else:
        return binary_search(c, start, index, val)


def gallop_to(c, val):
    gap = 1
    while True:
        temp = c.cur
        c.cur += gap
        if c.eol():
            c.cur = len(c.data)-1
            if c.elem() < val:
                c.cur += 1
                return
        current = c.cur
        value = c.elem()
        if value > val:
            return binary_search(c, temp, current, val)
        if value == val:
            return
        gap += gap
