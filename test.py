# def duplicate_count(data):
#     return ["Senior" if i >= 55 and j > 7 else "Open" for (i, j) in data]
    
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

# print(duplicate_count(input)) 



# import re

# def to_camel_case2(text):
#     # print(re.split("-|_", text))
#     return ''.join (i.capitalize() for i in re.split("-|_", text))

# def to_camel_case(text):
#     d = re.split("-|_", text)
#     return ''.join (d[i].capitalize() if i > 0 else d[i] for i in range(0, len(d)))


# print(to_camel_case("the-stealth-warrior"))
# print(to_camel_case("The_Stealth_Warrior"))

# print(to_camel_case2("the-stealth-warrior"))
# print(to_camel_case2("The_Stealth_Warrior"))

# def is_prime(num):
#     if num <=1: return False
#     if num % 2 == 0:
#         return num == 2
#     d = 3
#     while d * d <= num and num % d != 0:
#         d += 2
#     return d * d > num

# print(is_prime(75))

# from curses.ascii import isalpha


# def alphabet_position(text):
#     return " ".join(str((ord(letter)-96)) for letter in text.lower() if letter.isalpha())
#     pass


# print(alphabet_position("The sunset sets at twelve o' clock."))

# print(ord("t")-96)

# def find_it(seq):
#     # return (seq.count(num) for num in seq)
#     return [num for num in seq if seq.count(num)%2 != 0][0]
#     # return {i for i in seq if seq.count(i)%2 != 0}
#     a = seq.count(5)
#     return a

# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

# def pig_it(text):
#     return ' '.join(word[1:]+word[0]+"ay" if word.isalpha() else word for word in text.split())
#     pass

# print(pig_it('Pig latin is cool'))
# print(pig_it("O tempora o mores !"))

# import time


# def make_readable(seconds):
#     return time.strftime("{:02}".format(seconds//3600)+":%M:%S", time.gmtime(seconds))
#     pass

# print(make_readable(0))
# print(make_readable(86399))
# print(make_readable(359999))

# def valid_parentheses(string):
#     a = 0
#     for i in string:
#         if i == "(": a += 1
#         if i == ")": a +=-1
#         if a < 0: return False
#     return True if a == 0 else False


# print(valid_parentheses("hi())("))
# print(valid_parentheses("hi(hi)()"))
# print(valid_parentheses("  )'"))
# print(valid_parentheses(""))
# print(valid_parentheses("())(()"))

# def sum_of_intervals(intervals):
#     a = list(sum(sorted(intervals), ()))
#     i = 0
#     while i < len(a)-2:
#         if a[i] >= a[i+1] and a[i] >= a[i+2]:
#             a.pop(i+2)
#             a.pop(i+1)
#             i=0
#         elif a[i] >= a[i+1] and a[i] < a[i+2]:
#             a.pop(i+1)
#             a.pop(i)
#             i=0
#         else:
#             i+=1
#     return sum(a[i+1]-a[i] for i in range(0, len(a), 2))

# print(sum_of_intervals([(1, 5)]))                                   # 4
# print(sum_of_intervals([(1, 5), (6, 10)]))                          # 8
# print(sum_of_intervals([(1, 5), (1, 5)]))                           # 4
# print(sum_of_intervals([(1, 5), (2, 4)]))                           # 4
# print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))                  # 7
# print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]))    # 100_000_030
# print(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]))


# def strip_comments(strng, markers):
#     a = strng.split("\n")
#     for i in markers:
#         a = [text.split(i)[0].rstrip() for text in a]
#     return "\n".join(a)



# print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))   # 'apples, pears\ngrapes\nbananas'
# print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))                                      # 'a\nc\nd'
# print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))                                     # ' a\nc\nd'

# from textwrap import wrap

# def sum_strings(x, y):
#     number = 10
#     if len(x) and len(y) <= number:
#         return str(sum([int("0"+x),int("0"+y)]))
#     else:
#         a = wrap(x.zfill((max(len(x),len(y))//number+1)*number),number)
#         b = wrap(y.zfill((max(len(x),len(y))//number+1)*number),number)
#         c = [int(a[i])+int(b[i]) for i in range(0, len(a))]
#         c.append("0")
#     return ''.join(str(c[i-1])[-number:] if len(str(c[i])) <= number else str(c[i-1]+1)[-number:] for i in range(1,len(c)))



# print(sum_strings("1", "1"))
# print(sum_strings("123", "456"))
# print(sum_strings("1", ""))
# print(sum_strings("45678910111236567891011", "1234512345678910111236567891011"))

array1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# print(len(array1))
# print(array1[i][j])

array2 = [[1,2,3],
          [8,9,4],
          [7,6,5]]



def snail(snail_map):
    # if len(snail_map) ** 2 == 1:
    #     return [[]]
    result = []
    i,j = 0,0
    if len(snail_map [i]) == 0:
        return []
    while len(result) != len(snail_map) ** 2:
        result.append(snail_map [i][j])
        if i <= j + 1 and i + j < len(snail_map) - 1:
            j+=1
        elif i < j and i + j >= len(snail_map) - 1:
            i+=1
        elif i >= j and i + j > len(snail_map) - 1:
            j-=1
        else:
            i-=1
    return result
    pass


print(snail(array1)) # [1,2,3,6,9,8,7,4,5]
print(snail(array2)) # [1,2,3,4,5,6,7,8,9]
print(snail([[]]))
print(snail([[1]]))


# int[,] GetArraySpiral(int number)
# {
#     int[,] result = new int[number, number];
#     int count = 1;
#     int i = 0;
#     int j = 0;
#     while (count <= number * number)
#     {
#         result [i, j] = count;
#         count++;
#         if (i <= j + 1 && i + j < number - 1)
#             j++;
#         else if (i < j && i + j >= number - 1)
#             i++;
#         else if (i >= j && i + j > number - 1)
#             j--;
#         else
#             i--;
#     }
#     return result;
# }



# Это тестовое задание, изменение