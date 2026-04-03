
file = open("test.in","r")

# content = file.read()
# print(content)

content = file.readlines()

print(content)
K = int(content[0])
print(K)
print(type(K))

values = {}
for i in range(1, K + 1):
    pair = content[i].split()
    print(pair)
    values[pair[0]] = int(pair[1])

string1 = content[K + 1]
print(string1)
print(type(string1))

string2 = content[K + 2]
print(string2)
print(type(string2))

print(values)
print(type(values))

file.close()

len_string1 = len(string1)
len_string2 = len(string2)

dp = [[0 for _ in range(len_string2 + 1) ]for _ in range(len_string1 + 1)] 
    


for i in range(1, len_string1 + 1):
    for j in range(1, len_string2 + 1):
        
        if(string1[i - 1] == string2[j - 1]):
            dp[i][j]= dp[i - 1][j - 1] + values[string1[i - 1]]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            

def backtracking():
    i = len_string1
    j = len_string2
    res = ""
    while(i > 0 and j > 0):
        if(string1[i - 1] == string2[j - 1]):
            res = string1[i - 1] + res
            i -= 1
            j -= 1
        elif(dp[i - 1][j] > dp[i][j - 1]):
            i -= 1
        else:
            j -= 1
    return res

print(backtracking())

final_value = dp[len_string1][len_string2]
print(final_value)

