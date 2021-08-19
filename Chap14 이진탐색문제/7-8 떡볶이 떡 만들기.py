n,m = list(map(int,input().split(' ')))
#각 떡의 개별 높이 정보 입력
array = list(map(int,input().split()))

#이진탐색 시작점과 끝점 설정->높이 범위
start = 0
end = max(array)

#이진탐색 수행
result = 0
while(start<=end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    #잘랐을 때 떡의 양(현재의 높이로 잘랐을 때)
    #현재의 높이보다 떡의 높이가 더 클때만 결과(잘린부분)저장
    if x > mid:
      total += x - mid
  #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 탐색)->높이값이 줄어들때
  if total < m:
    end = mid - 1
  #떡의 양이 충분할 경우 덜 자르기(오른쪽 탐색)->높이값이 늘어날때
  else:
    result = mid
    #최대한 덜 잘랐을 때가 정답
    start = mid + 1

print(result) # 가장 마지막에 기록되어 있는 높이값 출력