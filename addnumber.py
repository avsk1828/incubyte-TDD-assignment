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
    if negative_numbers:
        raise ValueError(f"Negative numbers not allowed: {', '.join(negative_numbers)}")
    return sum(map(int, number_list))

print(add(""))           
print(add("1"))          
print(add("1,5")) 
print(add("1,8"))       
print(add("1\n2,3"))     
print(add("//;\n1;2"))   
print(add("//|\n1|2|3")) 
print(add("//|\n2|2|333"))
print(add("//|\n2|2|311133"))

try:
    print(add("//;\n1;-2"))  
except ValueError as e:
    print(e)  

try:
    print(add("//;\n1;-2;-3")) 
except ValueError as e:
    print(e) 