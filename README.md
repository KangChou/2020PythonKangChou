# 2020PythonKangChou
详细请看上面的.py文件
 python 3
# 算法基础与数据结构
[每日算法之旅(第一天):枚举算法的平凡与伟大](https://mp.weixin.qq.com/s?__biz=MzIwNzUwOTY1Nw==&mid=2247485927&idx=1&sn=b7724bfd20e306a72d2b23f795315169&chksm=97100811a06781073b4c99fda4cbc4fd904752d4076641dc5246a1a9130529531a80d1189c53&token=1006181174&lang=zh_CN#rd)

# 递归的思想
您见过一套俄罗斯娃娃吗？最初，您只会看到一个通常为彩绘木头的雕像，看起来像这样：

![image](https://upload-images.jianshu.io/upload_images/15863171-782f2379558bd6da.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

您可以移除第一个玩偶的上半部分，并且在里面看到什么？另一个稍小的俄罗斯娃娃！

![image](https://upload-images.jianshu.io/upload_images/15863171-e00f6450bc007061.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

您可以删除该洋娃娃并将其上半部分和下半部分分开。然后您会看到另一个甚至更小的娃娃：

![image](https://upload-images.jianshu.io/upload_images/15863171-75c524c491823fff.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

再一次：

![image](https://upload-images.jianshu.io/upload_images/15863171-dd0462557218cf67.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

而且您可以继续。最终，您找到了最年轻的俄罗斯娃娃。它只是一件，因此无法打开：

![image](https://upload-images.jianshu.io/upload_images/15863171-8a10710b7e16bce0.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我们从一个大俄罗斯玩偶开始，然后看到越来越小的俄罗斯玩偶，直到我们看到一个很小的玩偶无法容纳另一个。

俄罗斯玩偶与算法有什么关系？就像一个俄罗斯娃娃里面有一个较小的俄罗斯娃娃，里面还有一个甚至更小的俄罗斯娃娃一样，一直到一个很小的俄罗斯娃娃（太小而无法容纳另一个），我们将看到如何设计一种算法来通过解决相同问题的较小实例来解决问题，除非问题很小，以至于我们只能直接解决它。我们称这种技术为递归。

递归有很多应用程序。在本模块中，我们将看到如何使用递归来计算阶乘函数，确定单词是否是回文式，计算数字的幂，绘制类型的分形以及解决古老的河内塔问题。以后的模块将使用递归来解决其他问题，包括排序。



## 一、数据结构基础
### 1、创建数字列表
使用方法range()

    number=list(range(1,4)) %不包括右端点4
### 2、访问表中的值

<span style="color: green">  
    >>> number=list(range(1,2021))
</span>

    >>> 
    number
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, ..., 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 
    2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]


    >>>> number[2019]
    2020
    >>> number[0]    
     1
    >>> list1 = ['2020','Python','baidu','douyin']
    >>> list1[3]
    'douyin'
    
   
    >>> print (list1[3])
    douyin
    >>> list2 = [1,2,3,4,5,6,7,8,9,]    
    >>> list2[1:4]
    [2, 3, 4] 
### 3、删除中重复的元素并使得列表元素保持不变
    [1,4,9,5,5,8,3]


    1)
    
    # 删除可散列重复的元素（可散列就是列表的元素是一个随便放的数值，反之就是不可散列）
    #思想：构造一个函数或模块来进行调用
    def dedupe(items):
        seen = set()#判定i元素在items中
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


     [1, 4, 9, 5, 5, 8, 3]
     [1, 4, 9, 5, 8, 3]


 
 

    2)删除不可散列表中重复的元素，例如：列表里有字典
    def funha(items, key=None):
    seen = set()
    for i in items:
    a = i if key is None else key(i)
    if a not in seen:
    yield i
    seen.add(a)
    
    if __name__ == "__main__":
    b = [{'x': 6, 'y': 72},
    {'x': 16, 'y': 12},
    {'x': 26, 'y': 52},
    {'x': 36, 'y': 32}]
    print (b)
    print(list(funha(b, key=lambda b: (b['x'], b['y']))))
       
       [{'x': 36, 'y': 32}, {'x': 16, 'y': 12}, {'x': 26, 'y': 52}, {'x': 36, 'y': 32}]
    [{'x': 6, 'y': 72}, {'x': 16, 'y': 12}, {'x': 26, 'y': 52}] 

#### 附加说明 `if __name__ == 'main__':` 的作用
Python文件通常有两种使用方法:
第一是作为脚本直接执行;
第二是 import 导入其他的 python 脚本程序中被调用时（模块重用）被执行。
因此 `if __name__ == 'main__':` 的作用就是控制这两种情况执行代码的过程，在 `if __name__ == 'main__': `下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而 import 到其他脚本中是不会被执行的。

下面举例说明：
#### 例1 首先我们先建立一个pybianlie.py文件，运行代码如下

![bianlie.JPG](https://upload-images.jianshu.io/upload_images/18578734-0e08838eafbdcb9c.JPG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 例2 建立第二个test.py文件，运行代码如下
![test.JPG](https://upload-images.jianshu.io/upload_images/18578734-0b627e8dcd4846e5.JPG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

书写小技巧：图片先在简书转为MK.md文件语法，再放入github的.md文件中。

### 4、计算元素出现次数最多的元素

![Counter.JPG](https://upload-images.jianshu.io/upload_images/18578734-c24f6f477a6523a4.JPG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
    
    #计算元素出现次数最多的名人
    import collections 
    Celebrity = ['Platon','Platon','O’Henry','司马迁','Curie','Curie','','Picasso','司马迁','司马迁','Qin Shi Huang','Curie','司马迁','Qin Shi Huang','霍去病']
    from collections import Counter
    Celebrity_counters = Counter(Celebrity)
    TOP_threecounter = Celebrity_counters.most_common(4)#输出四个名人
    print (TOP_threecounter)
    
    执行结果：
    [('司马迁', 4), ('Curie', 3), ('Platon', 2), ('Qin Shi Huang', 2)]

