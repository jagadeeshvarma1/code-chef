money=int(input())
acost, ocost = map(int, input().split())
if money >= (acost + ocost):
  print("Yes")
else:
  print("No")