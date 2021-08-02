data = input()
result = []
value = 0

for x in data :
  #알파벳이면 결과 리스트에 삽입
  if x.isalpha():
    result.append(x)
  #숫자는 따로 더하기
  else :
    value += int(x)

#알파벳을 오름차순 정렬
result.sort()

#숫자가 하나라도 있으면 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

#결과 출력_리스트를 문자열로 변환해 출력
print(''.join(result))