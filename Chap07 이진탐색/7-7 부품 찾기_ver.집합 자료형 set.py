#특정한 수가 한 번이라도 등장했는지를 검사하면 되므로 집합 자료형을 이용해서 풀 수 있음
#set()함수 : 집합 자료형을 초기화할 때 사용
#집합 자료형은 단순히 특정한 데이터가 존재하는지 검사할 때 매우 효과적으로 사용 가능
#이진탐색, 계수정렬보다 간단

#N(가게의 부품 개수) 입력받기
n = int(input())

#가게에 있는 전체 부품 번호를 입력받아 집합(set)자료형에 기록
array = set(map(int,input().split()))

#M(손님이 확인 요청한 부품 개수)입력받기
m = int(input())
#손님이 확인요청한 전체 부품 번호를 공백으로 구분해 입력
check = list(map(int,input().split()))

#손님이 확인 요청한 부품 번호 하나씩 확인
for i in check:
  #해당 부품이 존재하는지 확인
  if i in array:
    print('yes', end =' ')
  else:
    print('no', end=' ')