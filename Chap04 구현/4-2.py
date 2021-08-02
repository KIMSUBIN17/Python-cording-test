h = int(input())

count = 0
for i in range(h + 1):   # 시
  for j in range(60):    # 분
    for k in range(60):  # 초
      # 매 시각에 3이 있으면 카운트 증가
      # 시분초 안에 3이 하나라도 있는지 확인하기 위해 문자열 형태로 저장해서 체크(그냥 문자열로 붙여버림)
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)