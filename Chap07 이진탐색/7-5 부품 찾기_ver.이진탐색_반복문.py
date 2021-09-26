#다량의 데이터 검색은 이진탐색 알고리즘 이용

#이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
  while start<=end:
    mid = (start + end)//2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    #중간점 값보다 찾는 값이 작으면 왼쪽만 확인
    if array[mid] > target:
      end = mid - 1
    #중간점 값보다 찾는 값이 크면 오른쪽 확인
    else:
      start = mid + 1
  return None


#N(가게의 부품 개수)입력
n = int(input())
#가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int,input().split()))
array.sort()    #이진 탐색 수행위해 사전에 정렬

#M(손님이 확인을 요청한 부품 개수)입력
m = int(input())
#손님이 확인을 요청한 전체 부품 번호를 공백으로 구분하여 입력
check = list(map(int,input().split()))

#손님이 확인을 요청한 부품 번호를 하나씩 확인
for i in check:
  #해당 부품이 존재하는지 확인
  result = binary_search(array,i,0,n-1)
  if result != None:
    print('yes', end =' ')
  else:
    print('no', end=' ')



'''
>>입력
5
8 3 7 9 2
3
5 7 9
>>출력
no yes yes