#删除不可散列表中重复的元素，例如：列表里有字典
def funha(items, key=None):
    seen = set()
    for i in items:
        a = i if key is None else key(i)
        if a not in seen:
            yield i
            seen.add(a)

if __name__ == "__main__":
    b = [{'x': 36, 'y': 32},
        {'x': 16, 'y': 12},
        {'x': 26, 'y': 52},
        {'x': 36, 'y': 32}] 
    print (b)
    print(list(funha(b, key=lambda b: (b['x'], b['y']))))
  