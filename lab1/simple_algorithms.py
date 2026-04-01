"""Simple algorithms and recursion."""


def recursion_example(x: int) -> None:
    if x <= 0:
        return
    print("hello world")
    recursion_example(x - 1)


def factorial(x: int) -> int | None:
    if x < 0:
        return None
    if x in (0, 1):
        return 1
    return x * factorial(x - 1)


def fibonacci(x: int) -> int:
    if x < 0:
        raise ValueError("x must be non-negative")
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


def binary_search(mylist: list[int], x: int, start: int, stop: int) -> int | bool:
    if start > stop:
        return False
    mid = (start + stop) // 2
    if x == mylist[mid]:
        return mid
    if x < mylist[mid]:
        return binary_search(mylist, x, start, mid - 1)
    return binary_search(mylist, x, mid + 1, stop)


def gcd(a: int, b: int) -> int:
    """Find the greatest common divisor using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def main() -> None:
    print("--- Recursion Example---", "recursion_example(4) = ")
    recursion_example(4)

    print("--- Factorial Example---", "factorial(5) =")
    print(factorial(5))

    print("--- Fibonacci Example---", "fibonacci(10) = ")
    print(fibonacci(10))

    print("--- Binary Search Example---")
    mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 73, 77, 81]
    target = 20
    start = 0
    stop = len(mylist) - 1
    print("Searching for", target, "in", mylist)
    x = binary_search(mylist, target, start, stop)

    if x is False:
        print("Item", target, "Not Found")
    else:
        print("Item", target, "Found at Index", x)

    print("--- GCD Example---", "gcd(36, 45) =")
    print(gcd(36, 45))


if __name__ == "__main__":
    main()
