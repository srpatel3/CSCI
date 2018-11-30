# CSci 556, Multiparadigm Programming, Fall 2018
# Calculator Expression Tree Parser and AST Builder
# H. Conrad Cunningham

# 345678901234567890123456789012345678901234567890123456789012345678901234567890

# 2018-11-13: Developed prototyupe

# GRAMMAR

# Expr     ::=  Term { TermOp Term }
# Term     ::=  Factor { FactorOp Factor }
# Factor   ::=  Func | Var | Val | ( Expr )
# Func     ::=  Name ( [ Exp { , Expr } ] )
# TermOp   ::=  + | -
# FactorOp ::=  * | /
# Var      ::=  Name
# Val      ::=  Unsigned | - Unsigned
# Name     ::=  Leading alpabetic or underscore followed by zero or
#               more alphabetic, numeric, or underscore characters
# Unsigned ::=  One or more decimal digits with optional leading -

from __future__ import annotations  # 3.7 deferred annotations
from typing import Optional

from parsita import *
from calc_ast import Expr, Call, Add, Sub, Mul, Div, Var, Val


def make_Val(dstr: str) -> Val:
    return Val(int(dstr))


def make_nVal(dstr: str) -> Val:
    return Val(-int(dstr))


def make_Call(call) -> Call:
    return Call(call[0], call[1])


# [left, [ [op1, right1], [op2, right2] ...] ]
# Called with only + and - ... or * and /, not mixed
# Assume tight binding from right
def make_binop(parse_res) -> Optional[Expr]:
    left = parse_res[0]
    rest = parse_res[1]
    print(left)
    print(rest)
    if len(rest) == 0:
        return left
    first = rest[0]
    if len(first) != 2:
        print(f"Error in make_binop({parse_res})")
        return None
    oper = first[0]
    right = first[1]
    if oper == "*":
        return Mul(left, make_binop([right, rest[1:]]))
    if oper == "/":
        return Div(left, make_binop([right, rest[1:]]))
    if oper == "+":
        return Add(left, make_binop([right, rest[1:]]))
    if oper == "-":
        return Sub(left, make_binop([right, rest[1:]]))
    print(f"Unknown operator {oper} in make_binop")
    return None


# Parsita TextParser
class TreeParsers(TextParsers):

    # Grammar rules using Parsita, with semantic routines
    expr = term & rep(termop & term) > make_binop
    term = factor & rep(factorop & factor) > make_binop
    factor = func | var | val | "(" >> expr << ")"
    func = name & "(" >> repsep(expr, ",") << ")" > make_Call
    termop = lit("+") | lit("-")
    factorop = lit("*") | lit("/")
    var = name > Var
    val = (lit("-") >> unsigned > make_nConst) | (unsigned > make_Val)
    name = reg(r"[_A-Za-z][_A-Za-z0-9]*")
    unsigned = reg(r"[+-]?\d+")

tree = TreeParsers().expr.parse('6**9')
print(tree)
# assert TreeParsers.expr.parse('6+7') == Success('Hello World!')
# assert TreeParsers.expr.parse('a=b+c') == Failure("Hello World! expected but Goodbye found")

