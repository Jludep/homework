class SimplifiedEnum(type):
    def __new__(mcls, name, bases, attrs):
        __keys = attrs.pop("__keys", ())
        enums = {}
        for key in __keys:
            enums[key] = key
        attrs.update(enums)
        return super().__new__(mcls, name, bases, attrs)

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")

class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")

assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"

# In this code, we define a SimplifiedEnum class that takes care of removing the duplications in variable declarations. The __new__ method of this class takes the __keys attribute from the class definition, removes it, and uses its values to create the enum variables.

# We apply this SimplifiedEnum class as the metaclass of ColorsEnum and SizesEnum classes. This results in these classes having enum variables without any duplications.

# Finally, we test the new classes by asserting that the values of their enum variables are what we expect them to be.