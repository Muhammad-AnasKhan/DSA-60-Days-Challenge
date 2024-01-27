def count_words_in_string(string=""):
    count = 0
    string = string.strip()
    
    for i in range(len(string)):
        if string[i] == " " or "  ":
            count += 1
    return count + 1  # added 1 for last word


string = " Be grateful! Be Patient! Be Smart! "
print(count_words_in_string(string))
