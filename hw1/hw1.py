def sum_even_squares(n: int) -> int:
    result = int()
    while n > 0:
        n -= 1
        if not n % 2:
            result += n ** 2
    return result


def sum_even_squares_simple(n: int) -> int:
    return sum([x ** 2 for x in range(n - (1 if n % 2 else 2), 0, -2)])


def odd_pair_linear(nums, t=0) -> bool:
    for _, num in enumerate(nums):
        if num % 2:
            t += 1
        if t > 1:
            return True
    return False


def odd_pair_bf(nums: [int]) -> bool:
    for i, m in enumerate(nums):
        for j, n in enumerate(nums[i + 1:]):
            if m * n % 2:
                return True
    return False


def get_list() -> [int]:
    def generate_list(seed: int, gap: int) -> [int]:
        for _ in range(10):
            seed += gap
            gap += 2
            yield seed

    return [x for x in generate_list(0, 0)]


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.sides = [a, b, c]

    @property
    def perimeter(self) -> float:
        return sum(self.sides)

    @property
    def area(self) -> float:
        s = self.perimeter * 0.5
        a, b, c = self.sides
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def remove_punctuation(sentence: str) -> str:
    return (lambda x: ''.join([i for i in x if i not in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""]))(sentence)


def run():
    print('Problem 1')
    print(sum_even_squares(int(input('please provide n: '))))

    print()

    print('Problem 1(use sum function)')
    print(sum_even_squares_simple(int(input('please provide n: '))))

    print()

    print('Problem 2(linear)')
    print(odd_pair_linear(
        list(map(int, input('please provide a sequence of integer values separated by spaces: ').split()))))

    print()

    print('Problem 2(brute-force)')
    print(
        odd_pair_bf(list(map(int, input('please provide a sequence of integer values separated by spaces: ').split()))))

    print()

    print('Problem 3')
    print(get_list())

    print()

    print('Problem 4')
    t = Triangle(3, 4, 5)
    print(t.perimeter)
    print(t.area)

    print()

    print('Problem 5')
    print(remove_punctuation(input('please provide a sentence: ')))

    print()
