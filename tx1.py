import jieba
txt=input("请输入一段文字")
ls=jieba.lcut(txt)
for i in ls[::-1]:
    print(i,end="")