array = [7,5,9,0,3,1,6,2,4,8]
#print("정렬 전", array)

for i in range(1, len(array)):
  for j in range(i,0,-1): # 인덱스i부터 1까지 1씩 감소하면서 반복
    if array[j] < array[j-1] : # 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
  else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
    break


print("정렬 후", array)

#range함수에서 마지막 숫자는 range에 지정한 끝나는 숫자보다 1이 더 큼
