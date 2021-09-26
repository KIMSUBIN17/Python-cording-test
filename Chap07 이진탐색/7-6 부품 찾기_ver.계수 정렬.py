#계수정렬 이용
#모든 원소의 번호를 포함할 수 있는 크기의 리스트 생성
#리스트의 인덱스에 직접 접근해 특정한 번호의 부품이 매장에 존재하는지 확인

#N(가게의 부품 개수) 입력받기
n = int(input())
array = [0] * 1000001

#가게에 있는 전체 부품 번호를 입력받아 기록
for i in input().split():
  array[int(i)] = 1

#M(손님이 확인 요청한 부품 개수)입력받기
m = int(input())
#손님이 확인요청한 전체 부품 번호를 공백으로 구분해 입력
check = list(map(int,input().split()))

#손님이 확인 요청한 부품 번호 하나씩 확인
for i in check:
  #해당 부품이 존재하는지 확인
  if array[i] == 1:
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
'''