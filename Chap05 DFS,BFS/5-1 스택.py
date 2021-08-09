stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)    #최하단 원소부터 출력
print(stack[::-1])    #최상단_가장 늦게 들어온 원소부터 출력(리스트 원소 순서 뒤집어서 출력)