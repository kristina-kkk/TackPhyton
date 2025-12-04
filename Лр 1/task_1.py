numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
none_index = numbers.index(None)
numbers_without_none = [num for num in numbers if num is not None]
sum_without_none = sum(numbers_without_none)
total_count = len(numbers)
average = sum_without_none / total_count
numbers[none_index] = average# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
