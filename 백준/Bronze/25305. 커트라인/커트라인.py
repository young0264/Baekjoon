n,k = map(int,input().split())
grade = list(map(int,input().split()))

grade.sort(reverse=True)

print(grade[k-1])