def find_index_of_char(str, ch):
    for i in range(len(str)):
        if(str[i]==ch):
            return i
    return -1

# print(find_index_of_char("Assalam O Alaikum G!", "Z"))

def find_sub_string(main_string, sub_string):
    match = False 
    for i in range(len(main_string) - len(sub_string) + 1):
        match = True  # Assume a match
        for j in range(len(sub_string)):
            if main_string[i + j] != sub_string[j]: # checking if substring matches or not index by index
                match = False  # Mismatch found, set match to False
                break
        if match:
            return i  
    return -1  
sub_String_index = find_sub_string("Assalam O Alaikum G!", "!")
print(f"Substring starts at: {sub_String_index}")
