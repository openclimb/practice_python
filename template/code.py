# 入力ファイルを読み込む
input1 = list(map(int,input().split()))
input2 = list(map(int,input().split()))
input3 = input()
input4 = int(input())

# コードを記述する
output1 = [[] for i in range(input4)]
output1_2 = [set() for i in range(input4)]
output2 = [[]] * input4

print(output1)
print(output2)
print("\n")

output1[1].append(1)
output2[1].append(1)

print(*output1)
print(*output2)
print("\n")

output1_2[1].add(1)
output1_2[1].add(2)
print(*output1_2)
output1_2[1].add(1)
print(*output1_2)

