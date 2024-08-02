

#method 1

def index_the_first_occurance(str1, str2):
    print(str1, str2)
    if str2 not in str1:
        return -1
    else:
        return str1.find(str2)


haystack = "notsadbutnotsad"
needle = "sad"
call_function = index_the_first_occurance(haystack, needle)
print(call_function)

#method 2

def index_the_first_occurance(str1, str2):
    for index in range(len(str1)):
        if str1[index:index+len(str2)] == str2:
            return index
        


haystack = "notsadbutnotsad"
needle = "sad"
call_function = index_the_first_occurance(haystack, needle)
print(call_function)