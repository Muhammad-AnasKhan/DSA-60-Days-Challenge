input = "Find the awesomes substrings in this string";
substringToFind = " awesome";

def find_substring(input, substring):
    input_len = len(input)
    substring_len = len(substring)
    word_start_index = -1

    for i in range(input_len):
        if input[i] == substring[0]: #  If current character is  same as first character of substring       
            chars_count = 0
            for j in range(i, i + substring_len): #  Checking each character of the current word with characters
                if  j >= input_len:
                    break
                if input[j] != substring[j-i]: #  If characters don't match
                    break
                chars_count += 1
                print(chars_count)

            if chars_count == substring_len:
                word_start_index = i
                break

    if (word_start_index != -1):
        print(f"Found '{substring}' at index {word_start_index}.")
    else:
        print(f"Could not find '{substring}' in the input.")


find_substring(input, substringToFind)
