#매번 배열 A에서 가장 작은 원소 골라서, 배열 B에서 가장 큰 원소와 교체
#조건:배열A에서 가장 작은 원소가 배열 B에서 가장 큰 원소보다 작을 때에만 교체 수행해야함
#이 과정 K번 반복
#1.배열A와 B의 정보 입력, 
#2.배열A의 원소 오름차순 정렬 & 배열B원소 내림차순 정렬
#3.두 배열 원소를 가장 첫번째 인덱스부터 차례대로 비교. A의 원소가 B의 원소보다 작을 때에만 교체->o(nlogn)보장 정렬 알고리즘 사용해야함

#N,K입력(두개의 배열은 N개의 원소, 최대 K번의 바꿔치기연산)
n,k = map(int,input().split())
#배열 A의 모든 원소 입력받기
a = list(map(int,input().split()))
#배열 B의 모든 원소 입력받기
b = list(map(int,input().split()))

#배열A의 원소 오름차순 정렬
a.sort()
#배열B의 원소 내림차순 정렬
b.sort(reverse=True)

#첫번재 인덱스부터 차례대로 비교, 두 배열의 원소 최대 K번 수행
for i in range(k):
  #A의 원소<B의 원소 일 때 교체
  if a[i]<b[i]:
    #두 원소 교체
    a[i], b[i] = b[i], a[i]     #swap
  else: #A의 원소>=B의 원소
    break

#배열 A의 모든 원소의 합 출력
print(sum(a))



'''
5 3
1 2 5 4 3
5 5 6 6 5
->출력=26
'''
'''
swap
a[i], b[i] = b[i], a[i]     
'''
