# 删除重复的元素
def dedupe(items):
    seen = set()
    for i in items:
        if i not in seen:
            yield i  #输出i
            seen.add(i)

if __name__ == "__main__":
    y = [1,4,9,5,5,8,3]
    print (y)
    print(list(dedupe(y)))