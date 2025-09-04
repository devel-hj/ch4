# 다음 코드를 보고 예상되는 실행 결과를 작성하세요

temp = ('bird', 'cat', 'dog')

# 변수 여러개 = 튜플
# 튜플의 요소가 순차적으로 변수에 저장됨
b,c,d = temp
print(b,c,d) # bird cat dog


fruits = ('사과', '배', '포도', '귤', '딸기')
# 1) 첫 번째 과일만 a에 넣고, 나머지는 rest에 담으세요
# 변수를 나열할때, 나머지 변수는 항상 맨 마지막에 두기
# 여러 변수, 나머지 변수 = 튜플
a, *rest = fruits
print(a, rest) # 사과 ['배', '포도', '귤', '딸기']

# 2) 앞 2개만 x,y에 넣고, 나머지는 others에 담으세요
x, y, *others = fruits
print(x, y, others) # 사과 배 ['포도', '귤', '딸기']