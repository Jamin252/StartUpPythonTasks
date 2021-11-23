"""a = {"A": 0, "B": 1}
print(a.items())
values = sorted(a.items(), key=lambda item: item[0])
for i in values:
    print(i[1], type(i))

print("value = ", values)
a.va"""
def apptemp(a):
    a[0] = "b"

a= ["a"]
apptemp(a)
print(a)