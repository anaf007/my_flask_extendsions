#coding=utf-8
"""
有序图
"""

def searchGraph(graph,start,end):

    results = []

    generatePath(graph,[start],end,results) #生成路径

    results.sort(key=lambda x:len(x))

    return results


#生成路径
def generatePath(graph,path,end,results):
    state = path[-1]
    if state == end:
        results.append(path)
    else:
        for arc in graph[state]:
            if arc not in path:
                generatePath(graph,path+[arc],end,results)


if __name__ == '__main__':
    Graph = {'A':['B','C','D'],\
                'B':['E'],\
                'C':['D','F'],\
                'D':['B','E','G'],\
                'E':[],\
                'F':['D','G'],\
                'G':['E']\
            }

    r = searchGraph(Graph,'A','D')
    for i in r:
        print(i)
    print('====end====')

    r = searchGraph(Graph,'A','E')
    for i in r:
        print(i)
    print('====end====')

    r = searchGraph(Graph,'C','E')
    for i in r:
        print(i)
    print('====end====')




