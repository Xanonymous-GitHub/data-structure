from typing import Final, List, Tuple
from string import digits


class Term:
    def __init__(self, coefficient: int, exponent: int):
        self.__coefficient = coefficient
        self.__exponent = exponent

    @property
    def coefficient(self) -> int:
        return self.__coefficient

    @property
    def exponent(self) -> int:
        return self.__exponent

    def __add__(self, other):
        assert self.__exponent == other.exponent
        return Term(self.__coefficient + other.coefficient, self.__exponent)

    def __cmp__(self, other):
        return self.__coefficient == other.coefficient and self.__exponent == other.exponent

    def __str__(self) -> str:
        if self.__exponent == 0:
            gap_str = ''
            exponent = ''
            coefficient = str(self.__coefficient) if self.__coefficient > 0 else ''
        elif self.__coefficient and self.__exponent == 1:
            gap_str = 'x'
            exponent = ''
            if self.__coefficient == 1:
                coefficient = ''
            else:
                coefficient = str(self.__coefficient)
        elif self.__coefficient:
            gap_str = 'x^'
            exponent = str(self.__exponent)
            if self.__coefficient == 1:
                coefficient = ''
            else:
                coefficient = str(self.__coefficient)
        else:
            coefficient = gap_str = exponent = ''

        return coefficient + gap_str + exponent


class Polynomial:
    def __init__(self, terms: Tuple[Term]):
        self.__terms = terms
        self.__simplification()

    def __str__(self) -> str:
        return ''.join(
            (str(term) if index == 0 else (('+' if term.coefficient > 0 else '') + str(term)))
            for index, term in enumerate(self.__terms)
        )

    __repr__ = __str__

    def __simplification(self):
        sorted_terms = sorted(self.__terms, key=lambda term: term.exponent, reverse=True)
        length_of_sorted_terms = len(sorted_terms)
        sorted_terms.append(Term(0, -2))

        simplified_terms: List[Term] = list()

        previous_exponent = -1
        same_exponent_terms: List[Term] = list()

        for index, sorted_term in enumerate(sorted_terms):

            if index == length_of_sorted_terms - 1 or \
                    sorted_term.exponent != previous_exponent and \
                    len(same_exponent_terms) != 0:

                merged_term = same_exponent_terms[0]

                for same_exponent_term in same_exponent_terms[1:]:
                    print(same_exponent_term)
                    merged_term += same_exponent_term

                simplified_terms.append(merged_term)
                same_exponent_terms.clear()

            same_exponent_terms.append(sorted_term)
            previous_exponent = sorted_term.exponent

        self.__terms = simplified_terms

    @property
    def raw_terms(self) -> Tuple[Term]:
        return self.__terms

    @property
    def leading_exponent(self) -> int:
        return self.__terms[0].exponent

    def __add__(self, other):
        return Polynomial(tuple([ours for ours in self.__terms] + [his for his in other.raw_terms]))


def str_to_terms(polynomial_str: str) -> Tuple[Term]:
    terms: List[Term] = list()
    negative_sign: Final[str] = '-'
    positive_sign: Final[str] = '+'

    coefficient_str = str()
    coefficient = None

    exponent_str = str()
    exponent = None

    prefix = 1

    length = len(polynomial_str)

    for index, char in enumerate(polynomial_str):
        if char in digits:
            if coefficient is None:
                coefficient_str += char
            else:
                exponent_str += char

            if index == length - 1:
                coefficient = prefix * (int(coefficient_str) if coefficient_str else 0)
                exponent = 0

        elif coefficient_str:
            coefficient = prefix * int(coefficient_str)
            coefficient_str = str()
            prefix = 1

        elif exponent_str:
            exponent = prefix * int(exponent_str)
            exponent_str = str()
            prefix = 1

        elif char == 'x' and coefficient is None and exponent is None:
            coefficient = prefix
            coefficient_str = str()
            prefix = 1

        if char in (negative_sign, positive_sign):
            if char == negative_sign:
                prefix = -1
            if coefficient is not None and exponent is None:
                exponent = 1

        if coefficient is not None and exponent is not None:
            terms.append(Term(coefficient, exponent))
            coefficient = None
            exponent = None

    return tuple(terms)


def run():
    a = Polynomial(str_to_terms('-8x^5+3x^7-9x^5+2x^3-4x^1+7x+89'))
    b = Polynomial(str_to_terms('4x^8+3x^5-12x^5+3x^7-2x^2-77+24+54'))
    print(a)
    print(b)
    print(a + b)