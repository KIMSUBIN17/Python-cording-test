# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보 2차원 리스트 자료형으로 표현
# 노드1부터 시작하는 경우 많음->인덱스0 비워두고 인덱스1(노드1)부터시작)
graph = [
  [],
  [2, 3, 8],    #1번노드와 연결된 노드2,3,8
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 1차원 리스트 자료형으로 표현
# 모든 노드 1개도 방문하지 않은 기본 리스트 설정_인덱스0+인덱스1~8=9
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)