my_list = [1, 'hello', 3, 'world', 5,3.14]

check_type = lambda x: isinstance(x, (int,str))
result = all(map(check_type, my_list))

print(result)