#크기 상관없이 나열되어 있는 수열을 큰 수부터 작은 수의 순서로 정렬
#수열을 내림차순으로 정렬하는 프로그램

#기본적인 정렬문제
#수열에 속해있는 수의 개수가 500개 이하이므로 적은편이므로 코드가 간단한 파이썬 기본정렬 라이브러리 sorted()사용

n = int(input())

#n개의 정수 입력받아 리스트에 저장
array = []
for i in range(n):
  array.append(int(input()))

#파이썬 기본 정렬 라이브러리로 정렬 수행
array = sorted(array, reverse=True)

#정렬 결과 출력
for i in array:
  print(i, end=' ')


'''
3
15
27
12 입력시 27 15 12출력
'''