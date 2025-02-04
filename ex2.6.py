import timeit

def pow2(n: int) -> int:
    return 2 ** n

def time_pow2_single():
    execution_time = timeit.timeit("pow2(10000)", globals=globals(), number=10000)
    print(f"Time for 10000 calls of pow2(10000): {execution_time:.5f}s")

def pow2_for_loop():
    result = []
    for i in range(1001):
        result.append(2 ** i)
    return result

def pow2_list_comprehension():
    return [2**i for i in range(1001)]

def time_for_loop():
    execution_time = timeit.timeit("pow2_for_loop()", globals=globals(), number=1000)
    print(f"Time for 1000 calls of pow2_for_loop: {execution_time:.5f}s")

def time_list_comprehension():
    execution_time = timeit.timeit("pow2_list_comprehension()", globals=globals(), number=1000)
    print(f"Time for 1000 calls of pow2_list_comprehension: {execution_time:.5f}s")

if __name__ == "__main__":
    time_pow2_single()
    time_for_loop()
    time_list_comprehension()
