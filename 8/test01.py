def test_colors_enum():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
    assert ColorsEnum.BLACK == "BLACK"

def test_sizes_enum():
    assert SizesEnum.XL == "XL"
    assert SizesEnum.L == "L"
    assert SizesEnum.M == "M"
    assert SizesEnum.S == "S"
    assert SizesEnum.XS == "XS"

def test_duplicate_keys():
    class DuplicateEnum(metaclass=SimplifiedEnum):
        __keys = ("A", "B", "C", "A")
    assert hasattr(DuplicateEnum, "A") is True
    assert hasattr(DuplicateEnum, "B") is True
    assert hasattr(DuplicateEnum, "C") is True
    assert hasattr(DuplicateEnum, "D") is False
    assert DuplicateEnum.A == "A"
    assert DuplicateEnum.B == "B"
    assert DuplicateEnum.C == "C"

def test_empty_keys():
    class EmptyEnum(metaclass=SimplifiedEnum):
        __keys = ()
    assert hasattr(EmptyEnum, "") is False
    assert hasattr(EmptyEnum, "A") is False
    assert hasattr(EmptyEnum, "B") is False
    assert hasattr(EmptyEnum, "C") is False

def test_inherited_class():
    class MyEnum(Enum):
        X = "X"
        Y = "Y"
    class InheritedEnum(MyEnum, metaclass=SimplifiedEnum):
        __keys = ("Z",)
    assert hasattr(InheritedEnum, "X") is True
    assert hasattr(InheritedEnum, "Y") is True
    assert hasattr(InheritedEnum, "Z") is True
    assert InheritedEnum.X == "X"
    assert InheritedEnum.Y == "Y"
    assert InheritedEnum.Z == "Z"