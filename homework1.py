
def apply_all_func(int_list, *functions):
        result = {}
        for function in functions:
                result[function.__name__] = function(int_list)
        return result


int_list = [6, 20, 15, 9]
result = apply_all_func(int_list, min, max, len, sum, sorted)

print(result)



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
