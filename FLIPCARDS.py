card = int(input())
for c in range(card):
  left,right= map(int,input().split())
  print(min(left-right,right))