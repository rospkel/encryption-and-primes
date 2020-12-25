import math

# generates all numbers up to and including n
def gen_nums(n):
    i = 2
    nums = []
    while i <= n :
        nums.append(i)
        i += 1
    return nums

# generates all prime numbers up to and including n
def eratosthenes(n):
    i = 0
    nums = gen_nums(n)
    while nums[i] <= math.sqrt(n) :
        for x in nums :
            if x != nums[i] and x % nums[i] == 0 :
                nums.remove(x)
        i += 1
    print(nums)

# stolen code; from wikipedia I think
def sieve_of_Sundaram(n):
    """The sieve of Sundaram is a simple deterministic algorithm for finding all the
    prime numbers up to a specified integer."""
    k = (n - 2) // 2
    integers_list = [True] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            integers_list[i + j + 2 * i * j] = False
            j += 1
    if n > 2:
        print(2, end=' ')
    for i in range(1, k + 1):
        if integers_list[i]:
            print(2 * i + 1, end=' ')
