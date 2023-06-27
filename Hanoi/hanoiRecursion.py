
def towerOfHanoi(n, source, destination, auxiliary):
    if n==1:
        print("move disk 1 from source", source, "to destination", destination) # 移动
        return
    else:
        towerOfHanoi(n-1, source, auxiliary, destination)
        print("Move disk", n, "from source", source, "to destination", destination) # 移动
        towerOfHanoi(n-1, auxiliary, destination, source)


n = 4
towerOfHanoi(4, 'A', 'B', 'C')