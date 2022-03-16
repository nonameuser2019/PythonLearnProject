
ans = 0
object = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
for i in range(len(object)):
    for j in range(i + 1, len(object)):
        if object[i] is object[j]:
            ans += 1
            break
        else:
            if i == len(object) - 1:
                ans += 1


assert ans == 5