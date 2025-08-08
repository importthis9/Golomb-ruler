import itertools

def f(a: list | tuple) -> list[list]:
    # 生成标尺的所有排列
    l = list(itertools.permutations(a))
    for i in l:
        s = set()
        # 生成所有可能的子区间和
        for j in range(len(i)):
            for k in range(j + 1, len(i) + 1):
                s.add(sum(i[j:k]))
            for k in range(j - 1, -1, -1):
                s.add(sum(i[k:j + 1]))
        # 判断所有子区间和是否构成一个连续的整数集合
        if sorted(s) == list(range(1, max(s) + 1)):
            print(f"找到杜德尼标尺: {i}")
            with open('G:\\file.log', 'a') as fp:
                fp.write(f"找到杜德尼标尺: {i}")

def shengcheng(he: int, changdu: int) -> list:
    # 生成所有可能的标尺组合
    if changdu == 1:
        return [[he]]
    res = []
    for i in range(1, he):
        for j in shengcheng(i, 1):
            for k in shengcheng(he - i, changdu - 1):
                res.append([j[0]] + k)
    return res
def main():
    he = 22  # 总长度
    changdu = 7  # 段数
    # 生成所有可能的标尺组合
    
    l = shengcheng(he, changdu)
    print(len(l))
    # 遍历所有可能的排列
    i= 0
    for k in l:
        with open('H:\\files.log', 'w') as fp:
            fp.write(str(i))
        f(k)
        i += 1

if __name__ == "__main__":
    main()
    