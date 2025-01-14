def apply_all_func(int_list, *functions):
    results: dict = {}
    for fun in functions:
        results[fun.__name__] = fun(int_list)
    return results

if __name__ in '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))