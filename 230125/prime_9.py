def if_prime(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        for i in range(2,n-1):
            if n%i==0:
                return 0
        return 1

l=[]
i=0
while True: # 無限ループ（あまりよくないがちゃんと終了条件を用意しておけば使っても良い）
    if if_prime(i): # 素数ならば
        if str(i)[-1]=='9': # 1桁目（数値を文字列に変換し、最後から1個目）が9ならば
            l.append(i) # リストに追加
            if len(l)==1400: # リストが1400個あれば
                break
    i+=1
print(l[-1]) # 1400個目（1400個あるリストのうち、最後から1個目）を出力

# test if_prime
# for i in range(100):
#     if if_prime(i):
#         print(i)

# not use list
# cnt=0
# i=0
# while cnt<1400:
#     if if_prime(i):
#         if str(i)[-1]=='9':
#             cnt+=1
#     i+=1
# print(i-1)
