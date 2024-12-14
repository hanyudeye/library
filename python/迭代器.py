# 迭代

for char  in "hello,world":
    print(char)

for item in ['array','bad','chat']:
    print(item)

tv={"name":"电视","function":"显示画面和声音"} 
for item in tv :
    print(tv[item])


for item in tv.values() :
    print(item)


## 迭代器
# 迭代器有两个基本的方法：iter() 和 next(),且字符串，列表或元组对象都可用于创建迭代器，迭代器对象可以使用常规 for 语句进行遍历，也可以使用 next() 函数来遍历。

# 1、字符创创建迭代器对象
str1 = 'hello'
iter1 = iter ( str1 )
while True:
    try:
        print(next(iter1))
    except StopIteration:
        print(StopIteration.value)
        break

