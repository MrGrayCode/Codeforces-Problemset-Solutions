n = int(input())
id = {}
for _ in range(n):
    name = input()
    try:
        id[name] += 1
        print(name + str(id[name]))
    except KeyError:
        id[name] = 0
        print("OK")