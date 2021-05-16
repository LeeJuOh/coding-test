def my_solution(n):
    result = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if "3" in f"{str(h)}{str(m)}{str(s)}":
                    result += 1
    return result


n = int(input())
print(my_solution(n))
