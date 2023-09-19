


source = 55055
source_str = str(source)
length = len(source_str)
digit_to_add = 0
n = 1
i = 0
while i < length:
    digit_to_add += (source // n) % 10
    n *= 10
    i += 1

i = 0
while i < length:
    i += 1 


i = 0
j = 0
n = 1
digit_to_add = 0
counter = 0
target = 0
while i < length:
    j = i + 1
    while j < length:
        digit_to_add += (source // n) % 10
        if digit_to_add + int(source_str[i]) == 10:
            counter += 1
        digit_to_add = 0
        n *= 10
        j += 1
    i += 1
    n = 1 

# iterative solution
def count_ten_pairs(n):
    str_n = str(n)
    length_n = len(str_n)
    digit_to_add_n = 0
    m = 1
    i = 0
    j = 0
    counter = 0
    while i < length_n:
        j = i + 1
        while j < length_n:
            digit_to_add_n += (source // m) % 10
            if digit_to_add_n + int(str_n[i]) == 10:
                counter += 1
            digit_to_add_n = 0
            m *= 10
            j += 1
        i += 1
        m = 1

    return counter

a = count_ten_pairs(55055)

print(a)
