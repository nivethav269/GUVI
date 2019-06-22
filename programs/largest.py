a=(input())
b=a.split()
if int(max(b))<0:
  print(min(b))
else:
  print(max(b))
