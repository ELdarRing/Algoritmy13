#Задание 1
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C'],
    'E': ['C']
}

#Задание 2
graph['F'] = ['A', 'E']

graph['A'].append('F')
graph['E'].append('F')

#Задание 3
def get_neighbors(graph, node):
    if node in graph:
        return graph[node]
    else:
        return "Вершина не найдена"

print(get_neighbors(graph, 'C'))

#Задание 4
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

dfs(graph, 'A')

#Задание 5
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            
            stack.extend(reversed(graph[node]))
    
    return visited

dfs_stack(graph, 'A')

#Задание 6
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            
            queue.extend(graph[node])
    
    return visited

bfs(graph, 'A')

#Задание 7
from collections import deque

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    
    return order

start = input("Введите стартовую вершину: ")

if start in graph:
    result = bfs_traversal(graph, start)
    print("Порядок обхода:", result)
else:
    print("Такой вершины нет в графе")

#Задание 8
def path_exists(graph, start, end):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node == end:
            return True
        
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    
    return False

print(path_exists(graph, 'A', 'E'))  

#Задание 9
def reachable_count(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    
    return len(visited)

print(reachable_count(graph, 'A'))

#Задание 10
from collections import deque

def shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])  
    
    while queue:
        node, path = queue.popleft()
        
        if node == end:
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    
    return None  

print(shortest_path(graph, 'A', 'E'))