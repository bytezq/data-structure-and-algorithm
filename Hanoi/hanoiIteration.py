# 需要一个堆栈，记录递归环境
# 出栈和入栈的操作
# 堆栈中要记录的信息：n source destination auxiliary

# 这是一个网上常见的版本，但是不容易理解
def towerOfHanoi(n, source, destination, auxiliary):
    stack = [(n, source, destination, auxiliary)]

    while stack:
        n, source, destination, auxiliary = stack.pop()

        if n == 1:
            print("Move disk", n, "from source", source, "to destination", destination)
        else:
            stack.append((n - 1, auxiliary, destination, source))
            stack.append((1, source, destination, auxiliary))  # 这一步其实是移动第n个盘
            stack.append((n - 1, source, auxiliary, destination))


def printHanoi(n, source, destination, auxiliary):
    # 最后一位标志位表示是否移动，0为false，1为true，仅为了方便打印
    stack = [(n, source, destination, auxiliary, False)]

    while stack:
        n, source, destination, auxiliary, move = stack.pop()

        if move:
            print("Move disk", n, "from source", source, "to destination", destination)
        else:
            stack.append((n - 1, auxiliary, destination, source, n - 1 == 1))
            stack.append((n, source, destination, auxiliary, True))
            stack.append((n - 1, source, auxiliary, destination, n - 1 == 1))


n = 4
printHanoi(4, 'A', 'B', 'C')

'''
其实是一个分解的过程：
n: src -> dst
可以分解为：
n-1: src -> aux
n: src -> dst
n-1: aux -> src

栈的操作顺序是先进后出，所以入栈的顺序是相反的
递归转为迭代的难点在于：递归的顺序是正向的，迭代的顺序是反向的
分解保存每一个计算过程，然后从栈顶计算
'''
