import re

def add(numbers: str) -> int:

    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter_line, numbers_part = numbers.split("\n", 1)
        delimiter = delimiter_line[2:]
        numbers = numbers_part.replace(delimiter, ",")
    number_list = re.split(r'[\n,]', numbers)
    negative_numbers = [num for num in number_list if int(num) < 0]