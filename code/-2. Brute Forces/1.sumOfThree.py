x, y, z = 1, 1, 1
n = int(input())
ans = "NO"
for i in range(1, n):
    for j in range(1, n):
        if i + j < n and i % 3 != 0 and j % 3 != 0 and (n - i - j) % 3 != 0 and i != j and j != n - i - j and n - i - j != i:
            x, y, z = i, j, n - i - j
            ans = "YES"
            break
    if ans == "YES": break
print(ans)
print(x, y, z) if ans == "YES" else None    