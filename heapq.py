#heapq라이브러리
import heapq

def heapsort(iterable):
  h = []
  result = []

  #모든 원소 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h,value)
  print("정렬 전 : " + str(h))
  #힙에 삽입된 모든 원소 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))

  return result

result = heapsort([1,3,5,7,9,2,4,6,8,10])
print("정렬 후 : " + str(result))

#heapq : 다익스트라 최단 경로 알고리즘 포함해 우선순위 큐 기능 구현
#파이썬의 힙은 최소힙으로 구성->최소힙 자료구조의 최상단 원소는 항상 '가장 작은'원소
#파이썬에서는 최대힙 제공X, 최대힙 구현 시 원소의 부호 일시적으로 변경하는 방식 사용
#최대힙:힙에 원소 삽입 전에 value값의 부호를 반대로 바꾸었다가, 힙에서 원소 꺼낸 뒤 다시 원소의 부호 바꿔줌