
user_string=input("Enter comma-separated elements: ")

comma_separated=user_string.split(',')


my_dict={}

for words in comma_separated:
    ordinal_value=0
    for char in words:
        ordi=ord(char)
        ordinal_value+=ordi
    my_dict[words]=ordinal_value
    assert words in my_dict #check if words is in my_dict or not. if available then add only one


#iterating through the dictionary
for key, value in my_dict.items():
    print(f"'{key}' -> {value}")
