import calendar
l = list(input().split())
d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(d[calendar.weekday(2009, int(l[1]), int(l[0]))])
