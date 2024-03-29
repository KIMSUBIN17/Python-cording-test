# 이진 탐색 소스 구현
def binary_search(array, target, start, end):
  while start<=end:
    mid = (start+end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    #중간점 값보다 찾으려는 값이 작으면 왼쪽 탐색
    elif array[mid] > target:
      end = mid -1
    #중간점 값보다 찾으려는 값이 크면 오른쪽 탐색
    else:
      start = mid + 1
  return None

#원소의 개수n과 찾고자 하는 문자열 target입력
n, target = list(map(int,input().split()))
#전체 원소 입력받기
array = list(map(int,input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array,target,0,n-1)
if result == None:
  print("해당하는 원소가 존재하지 않습니다.")
else:
  print(result + 1)