import random
import time
import matplotlib.pyplot as plt
import numpy as np
# content = file.read()
# print(content)


def dp(string1, string2, values):
    
    len_string1 = len(string1)
    len_string2 = len(string2)
    
    dp = [[0 for _ in range(len_string2 + 1) ]for _ in range(len_string1 + 1)] 

    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):
            
            if(string1[i - 1] == string2[j - 1]):
                dp[i][j]= dp[i - 1][j - 1] + values[string1[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp

def backtracking(dp, string1, string2):
    i = len(string1)
    j = len(string2)
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

def test():
    print("Testing File")
    file = open("tests/example.in","r")
    
    content = file.readlines()

    K = int(content[0])
    print(f'Number of characters in dictionary: {K}')

    values = {}
    for i in range(1, K + 1):
        pair = content[i].split()
        values[pair[0]] = int(pair[1])

    string1 = content[K + 1]
    print("String1 " + string1)
    print(type(string1))

    string2 = content[K + 2]
    print("String2 " + string2)
    print(type(string2))

    print(values)
    print(type(values))

    file.close()
    
    len_string1 = len(string1)
    len_string2 = len(string2)
    
    
    start_time = time.time()
    table = dp(string1, string2, values)
    
    subsequence = backtracking(table, string1, string2)
    
    end_time = time.time() 
    print(end_time - start_time)
    
    print(subsequence)
    
    final_value = table[len_string1][len_string2]
    print(final_value)
    
    
    output = open("tests/example.out", "w")
    output.write(str(final_value) + "\n")
    output.write(subsequence + "\n")
    output.write(str(end_time - start_time))
    output.close()
    
    
if __name__ == "__main__":
    #test()
    # for i in range(10):
    #     with open(f"input/{i + 1}.in", "w") as file:
    #         pass
        
    #     file = open(f"input/{i + 1}.in","w")
        
    #     K = random.randint(1,27)
        
    #     file.write(f'{K}\n')
    #     alphabet = 'abcdefghijklomnopqrstuvwxyz'
        
    #     letters = []
    
    #     for j in range(K):
    #         letter = random.choice(alphabet)
    #         value = random.randint(1,100)
            
    #         letters.append(letter)
    #         file.write(f'{letter} {value}\n')


    #     string1 = ""
    #     string2 = ""
        
    #     len_string1= random.randint(25,100)
    #     len_string1= random.randint(25,100)
        
    #     for i in range(len_string1):
    #         index = random.randint(0,len(letters) - 1)
    #         string1 += letters[index]
        
    #     for i in range(len_string1):
    #         index = random.randint(0,len(letters) - 1)
    #         string2 += random.choice(letters)
        
    #     file.write(f'{string1}\n')
    #     file.write(f'{string2}\n')
        
    #     file.close()

    
    for i in range(10):
        file = open(f"input/{i + 1}.in","r")

        content = file.readlines()
        K = int(content[0])
        

        values = {}
        for j in range(1, K + 1):
            pair = content[j].strip().split(" ")
            values[pair[0]] = int(pair[1])

        string1 = content[K + 1].strip()

        string2 = content[K + 2].strip()

        file.close()
    
        start_time = time.time()
        table = dp(string1, string2, values)
    
        subsequence = backtracking(table, string1, string2)
   
        end_time = time.time() 
        final_value = table[len(string1)][len(string2)]
        
        output = open(f"output/{i + 1}.out", "w")
        
        output.write(str(final_value) + "\n")
        output.write(str(subsequence) + "\n")
        output.write(str(end_time - start_time))
        output.close()
        
        print(f"File {i + 1} results: \n")
        print(f"Subsequence: {subsequence}")
        print(f"Final Value: {final_value}")
        print(f"Time: {end_time - start_time}")
        print("\n")

    
    x = []
    y = []
    for i in range(10):
        output = open(f"output/{i + 1}.out", "r")
        
        content = output.readlines()
        
        final_value = content[0].strip()
        subsequence = content[1].strip()
        duration = content[2].strip()
        
        x.append(i + 1)
        y.append(float(duration))
        
        output.close()
    
    print(x)
    print(y)


    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    ax.set(
        xlim=(0, 11),
        xticks=np.arange(1, 11),
        ylim=(0, max(y) * 1.2),
        yticks=np.arange(0, max(y) * 1.2, max(y)/5)
    )
    
    plt.show()
    
    