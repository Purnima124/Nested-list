# marks=[[78, 76, 94, 86, 88],
#   [91, 71, 98, 65, 76],
#   [95, 45, 78, 52, 49]]
# i=0
# s=0
# count=0
# while i<len(marks):
#   a=0
#   while a<len(marks[i]):
#     s=s+marks[i][a]
#     a=a+1
#   i=i+1
#   count=count+1
#   print("marks",s,":",count)
# question no. 2
# marks=[[78, 76, 94, 86, 88,],[91, 71, 98, 65,],[95, 45, 78]]
# i=0
# s=0
# count=0
# while i<len(marks):
#   a=0
#   while a<len(marks[i]):
#     s=s+marks[i][a]
#     a=a+1
#   i=i+1
#   count=count+1
#   print("marks",s,":",count)

# marks=[[78, 76, 94, 86,88,],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
# i=0
# s=0
# count=0
# while i<len(marks):
#   a=0
#   while a<len(marks[i]):
#     s=s+marks[i][a]
#     a=a+1
#   i=i+1
#   count=count+1
#   print("marks",s,":",count)

marks=[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
avg=0
count=0
while i<len(marks):
  sum=0
  a=0
  s=0
  while a<len(marks[i]):
    s=s+marks[i][a]
    a=a+1
  sum=sum+s
  avg=sum//len(marks[i])
  i=i+1
  count=count+1
  print("marks",avg,":",count)





