from typing import NamedTuple
from cached_property import cached_property as cached1
from property_cached import cached_property as cached2


class A(NamedTuple):
    a0: int

    @cached1
    def a1(self):
        return self.a0 + 1

    @cached2
    def a2(self):
        return self.a0 + 2

    @classmethod
    def try_cache(cls):
        a = cls(a0=0)
        print("Given a NamedTuple A with a slotted int:\n")
        try:
            print(a.a1)
        except AttributeError as e:
            print(f"  cached_property fails with \n\tAttributeError: {e}\n")

        try:
            print(a.a2)
        except TypeError as e:
            print(f"  property_cached fails with \n\tTypeError: {e}\n")


class B(NamedTuple):
    class B0:
        def __init__(self):
            self.b = 0

    b0: B0

    @cached1
    def b1(self):
        return self.b0.b + 1

    @cached2
    def b2(self):
        return self.b0.b + 2

    @classmethod
    def try_cache(cls):
        b = cls(b0=cls.B0())
        print("Given a NamedTuple B with a slotted class:\n")
        try:
            print(b.b1)
        except AttributeError as e:
            print(f"  cached_property fails with \n\tAttributeError: {e}\n")

        try:
            print(b.b2)
        except TypeError as e:
            print(f"  property_cached fails with \n\tTypeError: {e}\n")


if __name__ == "__main__":
    A.try_cache()
    B.try_cache()
