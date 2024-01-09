from timeit import timeit

def enumerate_func(values:list) -> list:
    temp_list:list = []
    for i,value in enumerate(values,start=1):
        temp_list.append((i,value))

    return temp_list

def normal_func(values:list) -> list:
    temp_list:list = []
    for i,value in enumerate(values):
        temp_list.append((i+1,value))

    return temp_list

if __name__=="__main__":
    fifty_numbers =  list(range(50))

    normal_time = timeit(f'normal_func({fifty_numbers})',globals=globals(), number=1_000_000)
    enum_time = timeit(f'enumerate_func({fifty_numbers})',globals=globals(), number=1_000_000)

    print('i+1:',normal_time)
    print('start=1:',enum_time)

    print('Output is same:', normal_func(fifty_numbers)==enumerate_func(fifty_numbers))


