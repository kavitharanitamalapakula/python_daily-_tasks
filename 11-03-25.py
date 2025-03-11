# Assessment
def is_increasing(num):
    num_str = str(num) 
    for i in range(len(num_str) - 1): 
        if num_str[i] >= num_str[i + 1]:  
            return False
    return True
def check_numbers(lst):
    result = []
    for num in lst:
        result.append(is_increasing(num))
    return result
numbers = [568, 89, 112, 88, 571]
result = check_numbers(numbers)
print(result)
