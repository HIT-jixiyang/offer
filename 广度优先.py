graph = {
    "A": ["B","C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D","E"],
    "D": ["B", "C", "E","F"],
    "E": ["C", "D"],
    "F": ["D"],
}
def BFS(graph,vertex):
    # 使用列表作为队列
    queue = []
    # 将首个节点添加到队列中
    queue.append(vertex)
    # 使用集合来存放已访问过的节点
    looked = set()
    # 将首个节点添加到集合中表示已访问
    looked.add(vertex)
    # 当队列不为空时进行遍历
    while(len(queue)>0):
        # 从队列头部取出一个节点并查询该节点的相邻节点
        temp = queue.pop(0)
        nodes = graph[temp]
        # 遍历该节点的所有相邻节点
        for w in nodes:
            # 判断节点是否存在于已访问集合中,即是否已被访问过
            if w not in looked:
                # 若未被访问,则添加到队列中,同时添加到已访问集合中,表示已被访问
                queue.append(w)
                looked.add(w)
        print(temp,end=' ')

def DFS(graph,vertex):
    # 使用列表作为栈
    stack = []
    # 将首个元素添加到队列中
    stack.append(vertex)
    # 使用集合来存放已访问过的节点
    looked = set()
    # 将首个节点添加到集合中表示已访问
    looked.add(vertex)
    # 当队列不为空时进行遍历
    while len(stack)>0:
        # 从栈尾取出一个节点并查询该节点的相邻节点
        temp = stack.pop()
        nodes = graph[temp]
        # 遍历该节点的所有相邻节点
        for w in nodes:
            # 判断节点是否存在于已访问集合中,即是否已被访问过
            if w not in looked:
                # 若未被访问,则添加到栈中,同时添加到已访问集合中,表示已被访问
                stack.append(w)
                looked.add(w)
        print(temp,end=' ')
# 由于无向图无根节点，则需要手动传入首个节点，此处以"A"为例
print("BFS",end=" ")
BFS(graph,"A")
print("")
print("DFS",end=" ")
DFS(graph,"A")