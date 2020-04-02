# 删除可散列重复的元素（可散列就是列表的元素是一个随便放的数值，反之就是不可散列）
#思想：构造一个函数或模块来进行调用
def dedupe(items):
    seen = set()
    #判定i元素在items中
    #判定i元素不在seen中,注意：这里的seen被赋予一个集合列表的形象
    #如果i元素都在列表items中，那么就输出i
    for i in items:
        if i not in seen:
            yield i  #输出i
            seen.add(i)
    #下面给出要判断的元素和列表
if __name__ == "__main__":
    y = [1,4,9,-5,-5,8,3] #这里的y=items
    print (y)           #打印列表y与后面的进行对比
    print(list(dedupe(y))) #调用上面dedupe函数的方法

