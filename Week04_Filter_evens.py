def filter_evens(number_list):
    even_numbers = []
    for number in number_list:
        if number > 0 and number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
    

nums = [0,-2,3,14]
print(filter_evens(nums))
