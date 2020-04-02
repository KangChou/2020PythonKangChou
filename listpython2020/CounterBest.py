#计算元素出现次数最多的的名人
import collections 
Celebrity = ['Platon','Platon','O’Henry','司马迁','Curie','Curie','','Picasso','司马迁','司马迁','Qin Shi Huang','Curie','司马迁','Qin Shi Huang','霍去病']
from collections import Counter
Celebrity_counters = Counter(Celebrity)
TOP_threecounter = Celebrity_counters.most_common(4)#输出四个名人
print (TOP_threecounter)

