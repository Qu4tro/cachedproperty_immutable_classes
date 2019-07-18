from typing import NamedTuple
from collections import namedtuple
from cached_property import cached_property


class A(NamedTuple):
    a1: int

    @cached_property
    def a2(self):
        return self.a1 + 1


if __name__ == "__main__":
    a = A(a1=0)
    print(a.a2)
