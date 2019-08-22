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


if __name__ == "__main__":
    A.try_cache()
