# CSci 556, Multiparadigm Programming, Fall 2018
# Calculator Expression Abstract Syntax Tree
# H. Conrad Cunningham

# 345678901234567890123456789012345678901234567890123456789012345678901234567890

# 2018-11-13: Developed from Expression Tree Function Module Version
#             ExprFuncMod2.py and frozen Dataclass version ExprDC.py
# 2018-11-14: Added __post_init__ to Div and Var; Reformated with black -l 70

from __future__ import annotations  # 3.7 deferred annotations
from typing import cast, Any, List, Mapping, Optional, Union
from dataclasses import dataclass  # 3.7
from abc import ABC, abstractmethod

# Type aliases (module-level variables)
Name = str
Number = Union[int, float, complex]
NumberR = (
    int,
    float,
    complex,
)  # Union type Number not usable @runtime
Env = Mapping[Name, Number]

# Make validity checks module-level functions
def is_valid_name(name: Any) -> bool:  # any nonempty string for now
    return isinstance(name, str) and len(name) > 0
    # None must not be valid name!


def is_valid_value(value: Any) -> bool:  # any number now
    return isinstance(value, NumberR)
    # None must not be valid value!


# Expr hierarchy holds expression tree data for type checks;
class Expr(ABC):
    pass


# Added--not implemented in eval, derive, symplify
# Target for function calls
@dataclass(frozen=True)
class Call(Expr):
    opcode: str
    operand: List[Expr]


# Name changed from Sum
@dataclass(frozen=True)
class Add(Expr):
    left: Optional[Expr]
    right: Optional[Expr]


# Added--not implemented in eval, derive, symplify
@dataclass(frozen=True)
class Sub(Expr):
    left: Optional[Expr]
    right: Optional[Expr]


# Added--not implemented in eval, derive, symplify
@dataclass(frozen=True)
class Mul(Expr):
    left: Optional[Expr]
    right: Optional[Expr]


# Added--not implemented in eval, derive, symplify
@dataclass(frozen=True)
class Div(Expr):
    left: Optional[Expr]
    right: Optional[Expr]

    # Postprocess __init__, check for divide by 0 (frozen dataclass)
    def __post_init__(self):
        if isinstance(self.right, Val) and self.right.value == 0:
            print("Attempt to divide by 0 in Div")
            object.__setattr__(self, "left", None)
            object.__setattr__(self, "right", None)


@dataclass(frozen=True)
class Var(Expr):
    name: Optional[Name]

    # Postprocess __init__, checj for invalid name (frozen dataclass)
    def __post_init__(self):
        if not is_valid_name(self.name):
            print("Attempt to set Var to invalid name")
            object.__setattr__(self, "name", None)


# Name changed from Const
@dataclass(frozen=True)
class Val(Expr):
    value: Optional[Number]


# eval, derive, and simplify are module-level functions
# Use if-elif-else structure with isinstance checks


def eval(tree: Optional[Expr], env: Env = {}) -> Optional[Number]:
    if isinstance(tree, Add):
        lv = eval(tree.left, env) if tree.left else None
        rv = eval(tree.right, env) if tree.right else None
        return lv + rv if lv is not None and rv is not None else None
    elif isinstance(tree, Var):
        return env.get(cast(str, tree.name))
    elif isinstance(tree, Val):
        return tree.value
    else:
        return None


def derive(tree: Optional[Expr], n: Optional[Name]) -> Optional[Expr]:
    if isinstance(tree, Add):
        dl = derive(tree.left, n) if tree.left else None
        dr = derive(tree.right, n) if tree.right else None
        return Add(dl, dr) if dl and dr else None
    elif isinstance(tree, Var):
        if is_valid_name(n) and n == tree.name:
            return Val(1)
        elif tree.name is not None:
            return Val(0)
        else:
            return None
    elif isinstance(tree, Val):
        return Val(0) if tree.value is not None else None
    else:
        return None


def simplify(tree: Optional[Expr]) -> Optional[Expr]:
    if isinstance(tree, Add):
        sl = simplify(tree.left) if tree.left else None
        sr = simplify(tree.right) if tree.right else None
        lc, rc = isinstance(sl, Val), isinstance(sr, Val)
        if lc and rc:  # Note several casts for use of mypy
            # No change to result, just allow type checking
            # ints and reals are complex for addition
            return Val(
                cast(complex, cast(Val, sl).value)
                + cast(complex, cast(Val, sr).value)
            )
        elif lc and cast(Val, sl).value == 0:  # Additive identity
            return sr
        elif rc and cast(Val, sr).value == 0:  # Additive identity
            return sl
        return Add(sl, sr) if sl and sr else None
    elif isinstance(tree, Var):
        return tree if tree.name is not None else None
    elif isinstance(tree, Val):
        return tree if tree.value is not None else None
    else:
        return None


# Smoke testing code (should be recoded to compare against desired output)

if __name__ == "__main__":

    def smoke_test02(expr: Expr, envir: Env) -> None:
        print(f"Expression: {expr}")
        print(f"Evaluation with x=5, y=7:\n  {eval(expr,envir)}")
        print(f"Derivative relative to x:\n  {derive(expr,'x')}")
        print(f"Derivative relative to y:\n  {derive(expr,'y')}")
        print(f"Derivative relative to None:\n  {derive(expr,None)}")
        print(f"Simplification:\n  {simplify(expr)}")
        print("")

    print("\nBegin smoke testing expression tree program\n")

    env: Env = {"x": 5, "y": 7}

    x = Var("x")
    y = Var("y")
    z = Var("z")  # no value in env

    c0 = Val(0.0)
    c1 = Val(1.0)
    c3 = Val(3.0)
    c6 = Val(6.0)
    c7 = Val(7.0)
    cm3 = Val(-3.0)

    smoke_test02(c0, env)
    smoke_test02(cm3, env)

    smoke_test02(x, env)
    smoke_test02(y, env)
    smoke_test02(z, env)

    s0L = Add(c0, c3)
    s0R = Add(c3, c0)
    s1 = Add(c7, cm3)
    s2 = Add(c1, y)
    s3 = Add(x, c3)
    s4 = Add(x, y)
    s5 = Add(s1, s0L)
    s6 = Add(Add(s1, s2), Add(s1, s4))

    smoke_test02(s0L, env)
    smoke_test02(s0R, env)
    smoke_test02(s1, env)
    smoke_test02(s2, env)
    smoke_test02(s3, env)
    smoke_test02(s4, env)
    smoke_test02(s5, env)
    smoke_test02(s6, env)

    exp = Add(Add(x, x), Add(c7, y))
    exp2 = Add(Add(Val(0), Val(0)), Add(Val(0), Val(1)))

    smoke_test02(exp, env)
    smoke_test02(exp2, env)

    n1 = Val(None)
    n2 = Var(None)
    n3 = Add(None, None)

    smoke_test02(n1, env)
    smoke_test02(n2, env)
    smoke_test02(n3, env)
