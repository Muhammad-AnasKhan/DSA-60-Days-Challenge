# TODO: Bonus points: trim any char which is not an alphabet or digit
def is_punctuation(char): 
    return (
        33 <= ord(char) <= 47 
        or 58 <= ord(char) <= 64 
        or 91 <= ord(char) <= 96 
        or 123 <= ord(char) <= 126
    )

def is_white_space(char):
    return True if char == ' ' else False

def trim_sen(sen):
    start = 0
    end = len(sen) - 1

    while start < end and (is_white_space(sen[start]) or is_punctuation(sen[start])):
        start += 1

    while end > start and (is_white_space(sen[end]) or is_punctuation(sen[end])):
        end -= 1

    return sen[start:end+1]

print(trim_sen('  !!bye ## '))
# print(is_punctuation('#'))
