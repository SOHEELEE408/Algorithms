import sys

input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    parent, child1, child2 = map(str, input().split())
    tree[parent] = [child1, child2]

# 전위 순회: 중간 - 왼쪽 - 오른쪽
def preOrder(node):
    if node == '.':
        return
    print(node,end='')
    preOrder(tree[node][0])
    preOrder(tree[node][1])

# 중위 순회: 왼쪽 - 중간 - 오른쪽
def inOrder(node):
    if node == '.':
        return
    inOrder(tree[node][0])
    print(node,end='')
    inOrder(tree[node][1])

# 후위 순회: 왼쪽 - 오른쪽 - 중간
def postOrder(node):
    if node == '.':
        return
    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print(node,end='')



preOrder('A')
print()
inOrder('A')
print()
postOrder('A')