# CSci 556, Multiparadigm Programming, Fall 2018
# Expression Tree Calculator; Basic OO
# H. Conrad Cunningham

# This program was based partially on my Scala code from 2008, which
# was itself based on Section 6 of _A Scala Tutorials for Java
# Programmers_, but reimplemented in an object-oriented style in 2008.

#2345678901234567890123456789012345678901234567890123456789012345678901234567890

# 2018-09-09: Python 3.7 version based on 2008 Scala version
# 2018-09-10: Comparisons against None changed to "is" and "is not"
# 2018-09-11: Use conditional expressions instead of and/or combinations

# Note: This program uses None in place of invalid Tree instances in
# many casses.

import math
from typing import cast
from typing import Optional
from typing import Union
from typing import Any, Dict, SupportsFloat
from dataclasses import dataclass
from typing import cast

class Tree:

    def eval(self,env : Dict = {}) -> Optional[Union[int,float,complex]]:
        pass

    def derive(self,v) -> Optional['Tree']:
        pass

    def simplify(self) -> Optional['Tree']:
        pass

    def is_valid_name(self,name : Optional[str]) -> bool:    # any nonempty string for now
        return isinstance(name,str) and len(name) > 0
        # None must not be valid name!

    # Have to update this function for accepting multiple types of values
    def is_valid_value(self,value : Optional[Union[int,float,complex]]) -> bool:  # any number for now
        return isinstance(value,(int,float,complex))
        # None must not be valid value!

    def __repr__(self) -> str:
        return "Tree: Not intended to be instantiated"

# @dataclass
class Var(Tree):

    def __init__(self, n : Optional[str]) -> None:
        self.name : Optional[str] = n if self.is_valid_name(n) else None
        # if self.is_valid_name(n):
        #     self.name = n
        # else:
        #     self.name = None

    def eval(self,env : Dict = {})-> Optional[Union[int,float,complex]]:
        return env.get(self.name)

    def derive(self,v : Optional[str]) -> Optional['Const'] :
        if self.is_valid_name(v) and v == self.name:
            return Const(1)
        elif self.name is not None:
            return Const(0)
        else:
            return None

    def simplify(self) -> Optional['Var']:
        return self if self.name is not None else None
        # if self.name is not None:
        #     return self
        # else:
        #     return None

    def __repr__(self) -> str:
        return f"Var({self.name})"


class Const(Tree):

    def __init__(self, v : Optional[Union[int,float,complex]]) -> None:
        self.value : Optional[Union[int,float,complex]] = v if self.is_valid_value(v) else None
        # if self.is_valid_value(v):
        #     self.value = v
        # else:
        #     self.value = None

    def eval(self, env : Dict ={}) -> Optional[Union[int,float,complex]]:
        return self.value

    def derive(self, v : Optional[str]) -> Optional['Const']:
        return Const(0) if self.value is not None else None
        # if self.value is not None:
        #     return Const(0)
        # else:
        #     return None

    def simplify(self) -> Optional['Const']:
        return self if self.value is not None else None
        # if self.value is not None:
        #    return self
        # else:
        #     return None

    def __repr__(self) -> str:
        return f"Const({self.value})"

class Sub(Tree):
    def __init__(self, l : Optional['Tree'], r: Optional['Tree']) -> None:
        self.left : Optional['Tree']  = l if isinstance(l,Tree) else None
        self.right: Optional['Tree']  = r if isinstance(r,Tree) else None

    def eval(self,env : Dict={}) -> Optional[Union[int,float,complex]]:
        lv : Optional[Union[int,float,complex]] = self.left.eval(env)  if self.left  else None
        rv : Optional[Union[int,float,complex]]= self.right.eval(env) if self.right else None
        return lv - rv if lv is not None and rv is not None else None

    def derive(self,v : Optional[str]) -> Optional['Sub']:
        dl : Optional['Tree']  = self.left.derive(v)  if self.left  else None
        dr : Optional['Tree'] = self.right.derive(v) if self.right else None
        return Sub(dl,dr) if dl and dr else None

    def simplify(self) -> Union['Sub','Tree','Var','Const',None]:
        sl : Optional["Tree"] = self.left.simplify()  if self.left  else None
        sr : Optional["Tree"]= self.right.simplify() if self.right else None
        lc : bool = isinstance(sl,Const)
        rc : bool = isinstance(sr,Const)
        if lc and rc:
            if self.is_valid_value(cast('Const',sl).value) and self.is_valid_value(cast('Const',sr).value):
                return Const(cast(Union[int,float,complex],cast('Const',sl).value) - cast(Union[int,float,complex],cast('Const',sr).value))
        elif lc and cast(Union[int,float,complex],cast('Const',sl).value) == 0:
            return sr
        elif rc and cast(Union[int,float,complex],cast('Const',sr).value) == 0:
            return sl
        return Sub(sl,sr) if sl and sr else None

    def __repr__(self) -> str:
        return f"Sub({repr(self.left)},{repr(self.right)})"

class Neg(Tree):
    def __init__(self, n : Optional['Tree']) -> None:
        self.val  = n if isinstance(n,Tree) else None

    def eval(self,env : Dict={}) -> Optional[Union[int,float,complex]]:
        nv = self.val.eval(env)  if self.val  else None
        return  -1*nv if nv is not None else None

    def derive(self,v : Optional[str]) -> Optional['Neg']:
        dn = self.val.derive(v)  if self.val  else None
        return Neg(dn) if dn else None

    def simplify(self) -> Union['Tree', 'Const', 'Neg',None]:
        nl : Optional['Tree'] = self.val.simplify()  if self.val  else None
        nc= isinstance(nl,Const)
        if nc:
            return Const(-1*cast(Union[int,float,complex],cast('Const',nl).value))
        return Neg(nl) if nc else None

    def __repr__(self):
        return f"Neg({repr(self.val)})"

class Cos(Tree):
    def __init__(self, n : Optional[Union['Const','Var','Tree']]) -> None:
        self.val : Optional[Union['Const','Var','Tree']]  = n if isinstance(n,Tree) else None

    def eval(self,env : Dict={}) -> Optional[Union[int,float,complex]]:
        nv : Optional[Union[int,float]] = cast(Union[int,float],self.val.eval(env))  if self.val  else None
        return  math.cos(nv) if nv is not None else None

    def derive(self,v : Optional[str]) -> Optional['Cos']:
        dn : Optional['Tree'] = self.val.derive(v)  if self.val  else None
        return Cos(dn) if dn else None

    def simplify(self) -> Union['Tree','Const','Var','Cos',None]:
        nl : Optional['Tree'] = self.val.simplify()  if self.val  else None
        nc : bool= isinstance(nl,Const)
        if nc and cast('Const',nl).value == 0:
            return Const(1)
        elif nc and cast('Const',nl).value == 90:
            return Const(0)
        elif nc:
            return Const(math.cos(cast(Union[int,float],cast('Const',nl).value)))
        return Cos(nl) if nc else None

    def __repr__(self) -> str:
        return f"Cos({repr(self.val)})"

class Sin(Tree):
    def __init__(self, n : Optional[Union['Tree','Const','Var']]) -> None:
        self.val : Optional[Union['Const','Var','Tree']] = n if isinstance(n,Tree) else None

    def eval(self,env : Dict ={}) -> Optional[Union[int,float,complex]]:
        nv : Optional[Union[int,float]] = cast(Union[int,float],self.val.eval(env))  if self.val  else None
        return  math.sin(nv) if nv is not None else None

    def derive(self,v : Optional[str]) -> Optional['Sin']:
        dn : Optional['Tree'] = self.val.derive(v)  if self.val  else None
        return Sin(dn) if dn else None

    def simplify(self) -> Union['Tree', 'Const', 'Var', 'Sin', None]:
        nl : Optional['Tree'] = self.val.simplify()  if self.val  else None
        nc : bool = isinstance(nl,Const)
        if nc and cast('Const',nl).value == 0:
            return Const(0)
        elif nc and cast('Const',nl).value == 90:
            return Const(1)
        elif nc:
            return Const(math.sin(cast(Union[int,float],cast('Const',nl).value)))
        return Sin(nl) if nc else None

    def __repr__(self) -> str:
        return f"Sin({repr(self.val)})"

class Div(Tree):
    def __init__(self, l : Optional['Tree'], r : Optional['Tree']) -> None:
        self.left  : Optional['Tree']  = l if isinstance(l,Tree) else None
        self.right : Optional['Tree'] = r if isinstance(r,Tree) else None

    def eval(self,env : Dict={}) -> Optional[Union[int,float,complex]]:
        lv : Optional[Union[int,float,complex]] = self.left.eval(env)  if self.left  else None
        rv : Optional[Union[int,float,complex]] = self.right.eval(env) if self.right else None
        if not rv == 0:
            return lv / rv if lv is not None and rv is not None else None
        else:
            return None
    def derive(self,v : Optional[str]) -> Optional['Div']:
        dl : Optional['Tree'] = self.left.derive(v)  if self.left  else None
        dr : Optional['Tree'] = self.right.derive(v) if self.right else None
        return Div(dl,dr) if dl and dr else None

    def simplify(self) -> Union['Tree','Const','Div','Var',None]:
        sl : Optional['Tree']= self.left.simplify()  if self.left  else None
        sr : Optional['Tree']= self.right.simplify() if self.right else None
        lc : bool = isinstance(sl,Const)
        rc : bool = isinstance(sr,Const)
        if lc and rc:
            if not cast('Const',sr).value == 0:   
              return Const(cast(Union[int,float,complex],cast('Const',sl).value) / cast(Union[int,float,complex],cast('Const',sr).value))
            else:
                return None
        elif lc and cast('Const',sl).value == 0:
            return Const(0)
        elif rc and cast('Const',sr).value == 0:
            return None
        elif rc and cast('Const',sr).value == 1:
            return sl
        return Div(sl,sr) if sl and sr else None

    def __repr__(self) -> str:
        return f"Div({repr(self.left)},{repr(self.right)})"


class Prod(Tree):
    def __init__(self, l : Optional['Tree'], r : Optional['Tree']) -> None:
        self.left : Optional['Tree']  = l if isinstance(l,Tree) else None
        self.right: Optional['Tree'] = r if isinstance(r,Tree) else None

    def eval(self,env : Dict ={}) -> Optional[Union[int,float,complex]]:
        lv : Optional[Union[int,float,complex]] = self.left.eval(env)  if self.left  else None
        rv : Optional[Union[int,float,complex]] = self.right.eval(env) if self.right else None
        return lv * rv if lv is not None and rv is not None else None

    def derive(self,v : Optional[str]) -> Optional['Prod']:
        dl : Optional['Tree'] = self.left.derive(v)  if self.left  else None
        dr : Optional['Tree'] = self.right.derive(v) if self.right else None
        return Prod(dl,dr) if dl and dr else None

    def simplify(self)-> Union['Tree','Const','Var','Prod',None]:
        sl : Optional['Tree'] = self.left.simplify()  if self.left  else None
        sr : Optional['Tree'] = self.right.simplify() if self.right else None
        lc : bool = isinstance(sl,Const)
        rc : bool = isinstance(sr,Const)        
        if lc and rc:
            return Const(cast(Union[int,float,complex],cast('Const',sl).value) * cast(Union[int,float,complex],cast('Const',sr).value))
        elif lc and cast('Const',sl).value == 1:
            return sr
        elif rc and cast('Const',sr).value == 1:
            return sl
        elif lc and cast('Const',sl).value == 0:
            return Const(0)
        elif rc and cast('Const',sr).value == 0:
            return Const(0)
        return Prod(sl,sr) if sl and sr else None

    def __repr__(self) -> str:
        return f"Prod({repr(self.left)},{repr(self.right)})"

if __name__ == '__main__':
    env = { "x":5, "y":7 }
    x   = Var("x")
    y   = Var("y")
    z   = Var("z")
    c0  = Const(0.0)
    c1  = Const(1.0)
    c3  = Const(3.0)
    c6  = Const(6.0)
    c7  = Const(7.0)
    cm3 = Const(-3.0)
    print("Test Starts from Here")

    # print("\n\n###Sub TESTS STARTS FROM HERE:###\n\n")
    # s0L = Sub(c0,c3)
    # s0R = Sub(c3,c0)
    # s1  = Sub(c7,cm3)
    # s2  = Sub(c1,y)
    # s3  = Sub(x,c3)
    # s4  = Sub(x,y)
    # s5  = Sub(s1,s0L)
    # s6  = Sub(Sub(s1,s2),Sub(s1,s4))
    # print("Expr1")
    # print(f"Expression:\n  {s0L}")
    # print(f"Evaluation with x=5, y=7:\n  {s0L.eval(env)}")
    # print(f"Derivative relative to x:\n  {s0L.derive('x')}")
    # print(f"Derivative relative to y:\n  {s0L.derive('y')}")
    # print(f"Derivative relative to None:\n  {s0L.derive(None)}")
    # print(f"Simplification:\n  {s0L.simplify()}")
    # print("")
    # print("Expr2")
    # print(f"Expression:\n  {s0R}")
    # print(f"Evaluation with x=5, y=7:\n  {s0R.eval(env)}")
    # print(f"Derivative relative to x:\n  {s0R.derive('x')}")
    # print(f"Derivative relative to y:\n  {s0R.derive('y')}")
    # print(f"Derivative relative to None:\n  {s0R.derive(None)}")
    # print(f"Simplification:\n  {s0R.simplify()}")
    # print(f" ")
    
    # print("Expr3")
    # print(f"Expression:\n  {s1}")
    # print(f"Evaluation with x=5, y=7:\n  {s1.eval(env)}")
    # print(f"Derivative relative to x:\n  {s1.derive('x')}")
    # print(f"Derivative relative to y:\n  {s1.derive('y')}")
    # print(f"Derivative relative to None:\n  {s1.derive(None)}")
    # print(f"Simplification:\n  {s1.simplify()}")
    # print("")
    
    # print("Expr4")
    # print(f"Expression:\n  {s2}")
    # print(f"Evaluation with x=5, y=7:\n  {s2.eval(env)}")
    # print(f"Derivative relative to x:\n  {s2.derive('x')}")
    # print(f"Derivative relative to y:\n  {s2.derive('y')}")
    # print(f"Derivative relative to None:\n  {s2.derive(None)}")
    # print(f"Simplification:\n  {s2.simplify()}")
    # print("")
    
    # print("Expr5")
    # print(f"Expression:\n  {s3}")
    # print(f"Evaluation with x=5, y=7:\n  {s3.eval(env)}")
    # print(f"Derivative relative to x:\n  {s3.derive('x')}")
    # print(f"Derivative relative to y:\n  {s3.derive('y')}")
    # print(f"Derivative relative to None:\n  {s3.derive(None)}")
    # print(f"Simplification:\n  {s3.simplify()}")
    # print("")
    
    # print("Expr6")
    # print(f"Expression:\n  {s4}")
    # print(f"Evaluation with x=5, y=7:\n  {s4.eval(env)}")
    # print(f"Derivative relative to x:\n  {s4.derive('x')}")
    # print(f"Derivative relative to y:\n  {s4.derive('y')}")
    # print(f"Derivative relative to None:\n  {s4.derive(None)}")
    # print(f"Simplification:\n  {s4.simplify()}")
    # print("")
    
    # print("Expr7")
    # print(f"Expression:\n  {s5}")
    # print(f"Evaluation with x=5, y=7:\n  {s5.eval(env)}")
    # print(f"Derivative relative to x:\n  {s5.derive('x')}")
    # print(f"Derivative relative to y:\n  {s5.derive('y')}")
    # print(f"Derivative relative to None:\n  {s5.derive(None)}")
    # print(f"Simplification:\n  {s5.simplify()}")
    # print("")
    
    # print("Expr8")
    # print(f"Expression:\n  {s6}")
    # print(f"Evaluation with x=5, y=7:\n  {s6.eval(env)}")
    # print(f"Derivative relative to x:\n  {s6.derive('x')}")
    # print(f"Derivative relative to y:\n  {s6.derive('y')}")
    # print(f"Derivative relative to None:\n  {s6.derive(None)}")
    # print(f"Simplification:\n  {s6.simplify()}")
    # print("")
    
    # exp = Sub(Sub(x,x),Sub(c7,y))
    # print("Expr9")
    # print(f"Expression:\n  {exp}")
    # print(f"Evaluation with x=5, y=7:\n  {exp.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp.derive(None)}")
    # print(f"Simplification:\n  {exp.simplify()}")
    # print("")
    
    # exp2 = Sub(Sub(Const(0),Const(0)),Sub(Const(0),Const(1)))
    # print("Expr10")
    # print(f"Expression:\n  {exp2}")
    # print(f"Evaluation with x=5, y=7:\n  {exp2.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp2.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp2.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp2.derive(None)}")
    # print(f"Simplification:\n  {exp2.simplify()}")
    # print("")

    # n1 = Const(None)
    # n2 = Var(None)
    # # n3 = Sum(None,None)

    # print(f"Expression:\n  {n1}")
    # print(f"Evaluation with x=5, y=7:\n  {n1.eval(env)}")
    # print(f"Derivative relative to x:\n  {n1.derive('x')}")
    # print(f"Derivative relative to y:\n  {n1.derive('y')}")
    # print(f"Derivative relative to None:\n  {n1.derive(None)}")
    # print(f"Simplification:\n  {n1.simplify()}")
    # print("")

    # print(f"Expression:\n  {n2}")
    # print(f"Evaluation with x=5, y=7:\n  {n2.eval(env)}")
    # print(f"Derivative relative to x:\n  {n2.derive('x')}")
    # print(f"Derivative relative to y:\n  {n2.derive('y')}")
    # print(f"Derivative relative to None:\n  {n2.derive(None)}")
    # print(f"Simplification:\n  {n2.simplify()}")
    # print("")

    # print(f"Expression:\n  {n3}")
    # print(f"Evaluation with x=5, y=7:\n  {n3.eval(env)}")
    # print(f"Derivative relative to x:\n  {n2.derive('x')}")
    # print(f"Derivative relative to y:\n  {n3.derive('y')}")
    # print(f"Derivative relative to None:\n  {n3.derive(None)}")
    # print(f"Simplification:\n  {n3.simplify()}")
    # print("")


    print("\n\n###Prod TESTS STARTS FROM HERE:###\n\n")
    p0L = Prod(c0,c3)
    p0R = Prod(c3,c0)
    p1  = Prod(c7,cm3)
    p2  = Prod(c1,y)
    p3  = Prod(x,c3)
    p4  = Prod(x,y)
    p5  = Prod(p1,p0L)
    p6  = Prod(Prod(p1,p2),Prod(p1,p4))
    print("Expr1")
    print(f"Expression:\n  {p0L}")
    print(f"Evaluation with x=5, y=7:\n  {p0L.eval(env)}")
    print(f"Derivative relative to x:\n  {p0L.derive('x')}")
    print(f"Derivative relative to y:\n  {p0L.derive('y')}")
    print(f"Derivative relative to None:\n  {p0L.derive(None)}")
    print(f"Simplification:\n  {p0L.simplify()}")
    print("")
    print("Expr2")
    print(f"Expression:\n  {p0R}")
    print(f"Evaluation with x=5, y=7:\n  {p0R.eval(env)}")
    print(f"Derivative relative to x:\n  {p0R.derive('x')}")
    print(f"Derivative relative to y:\n  {p0R.derive('y')}")
    print(f"Derivative relative to None:\n  {p0R.derive(None)}")
    print(f"Simplification:\n  {p0R.simplify()}")
    print(f" ")
    
    print("Expr3")
    print(f"Expression:\n  {p1}")
    print(f"Evaluation with x=5, y=7:\n  {p1.eval(env)}")
    print(f"Derivative relative to x:\n  {p1.derive('x')}")
    print(f"Derivative relative to y:\n  {p1.derive('y')}")
    print(f"Derivative relative to None:\n  {p1.derive(None)}")
    print(f"Simplification:\n  {p1.simplify()}")
    print("")
    
    print("Expr4")
    print(f"Expression:\n  {p2}")
    print(f"Evaluation with x=5, y=7:\n  {p2.eval(env)}")
    print(f"Derivative relative to x:\n  {p2.derive('x')}")
    print(f"Derivative relative to y:\n  {p2.derive('y')}")
    print(f"Derivative relative to None:\n  {p2.derive(None)}")
    print(f"Simplification:\n  {p2.simplify()}")
    print("")
    
    print("Expr5")
    print(f"Expression:\n  {p3}")
    print(f"Evaluation with x=5, y=7:\n  {p3.eval(env)}")
    print(f"Derivative relative to x:\n  {p3.derive('x')}")
    print(f"Derivative relative to y:\n  {p3.derive('y')}")
    print(f"Derivative relative to None:\n  {p3.derive(None)}")
    print(f"Simplification:\n  {p3.simplify()}")
    print("")
    
    print("Expr6")
    print(f"Expression:\n  {p4}")
    print(f"Evaluation with x=5, y=7:\n  {p4.eval(env)}")
    print(f"Derivative relative to x:\n  {p4.derive('x')}")
    print(f"Derivative relative to y:\n  {p4.derive('y')}")
    print(f"Derivative relative to None:\n  {p4.derive(None)}")
    print(f"Simplification:\n  {p4.simplify()}")
    print("")
    
    print("Expr7")
    print(f"Expression:\n  {p5}")
    print(f"Evaluation with x=5, y=7:\n  {p5.eval(env)}")
    print(f"Derivative relative to x:\n  {p5.derive('x')}")
    print(f"Derivative relative to y:\n  {p5.derive('y')}")
    print(f"Derivative relative to None:\n  {p5.derive(None)}")
    print(f"Simplification:\n  {p5.simplify()}")
    print("")
    
    print("Expr8")
    print(f"Expression:\n  {p6}")
    print(f"Evaluation with x=5, y=7:\n  {p6.eval(env)}")
    print(f"Derivative relative to x:\n  {p6.derive('x')}")
    print(f"Derivative relative to y:\n  {p6.derive('y')}")
    print(f"Derivative relative to None:\n  {p6.derive(None)}")
    print(f"Simplification:\n  {p6.simplify()}")
    print("")
    
    exp = Prod(Prod(x,x),Prod(c7,y))
    print("Expr9")
    print(f"Expression:\n  {exp}")
    print(f"Evaluation with x=5, y=7:\n  {exp.eval(env)}")
    print(f"Derivative relative to x:\n  {exp.derive('x')}")
    print(f"Derivative relative to y:\n  {exp.derive('y')}")
    print(f"Derivative relative to None:\n  {exp.derive(None)}")
    print(f"Simplification:\n  {exp.simplify()}")
    print("")
    
    exp2 = Prod(Prod(Const(0),Const(0)),Prod(Const(0),Const(1)))
    print("Expr10")
    print(f"Expression:\n  {exp2}")
    print(f"Evaluation with x=5, y=7:\n  {exp2.eval(env)}")
    print(f"Derivative relative to x:\n  {exp2.derive('x')}")
    print(f"Derivative relative to y:\n  {exp2.derive('y')}")
    print(f"Derivative relative to None:\n  {exp2.derive(None)}")
    print(f"Simplification:\n  {exp2.simplify()}")
    print("")

    # print("\n\n###Div TESTS STARTS FROM HERE:###\n\n")
    # d0L = Div(c0,c3)
    # d0R = Div(c3,c0)
    # d1  = Div(c7,cm3)
    # d2  = Div(c1,y)
    # d3  = Div(x,c3)
    # d4  = Div(x,y)
    # d5  = Div(d1,d0L)
    # d6  = Div(Div(d1,d2),Div(d1,d4))
    # print("Expr1")
    # print(f"Expression:\n  {d0L}")
    # print(f"Evaluation with x=5, y=7:\n  {d0L.eval(env)}")
    # print(f"Derivative relative to x:\n  {d0L.derive('x')}")
    # print(f"Derivative relative to y:\n  {d0L.derive('y')}")
    # print(f"Derivative relative to None:\n  {d0L.derive(None)}")
    # print(f"Simplification:\n  {d0L.simplify()}")
    # print("")
    # print("Expr2")
    # print(f"Expression:\n  {d0R}")
    # print(f"Evaluation with x=5, y=7:\n  {d0R.eval(env)}")
    # print(f"Derivative relative to x:\n  {d0R.derive('x')}")
    # print(f"Derivative relative to y:\n  {d0R.derive('y')}")
    # print(f"Derivative relative to None:\n  {d0R.derive(None)}")
    # print(f"Simplification:\n  {d0R.simplify()}")
    # print(f" ")
    
    # print("Expr3")
    # print(f"Expression:\n  {d1}")
    # print(f"Evaluation with x=5, y=7:\n  {d1.eval(env)}")
    # print(f"Derivative relative to x:\n  {d1.derive('x')}")
    # print(f"Derivative relative to y:\n  {d1.derive('y')}")
    # print(f"Derivative relative to None:\n  {d1.derive(None)}")
    # print(f"Simplification:\n  {d1.simplify()}")
    # print("")
    
    # print("Expr4")
    # print(f"Expression:\n  {d2}")
    # print(f"Evaluation with x=5, y=7:\n  {d2.eval(env)}")
    # print(f"Derivative relative to x:\n  {d2.derive('x')}")
    # print(f"Derivative relative to y:\n  {d2.derive('y')}")
    # print(f"Derivative relative to None:\n  {d2.derive(None)}")
    # print(f"Simplification:\n  {d2.simplify()}")
    # print("")
    
    # print("Expr5")
    # print(f"Expression:\n  {d3}")
    # print(f"Evaluation with x=5, y=7:\n  {d3.eval(env)}")
    # print(f"Derivative relative to x:\n  {d3.derive('x')}")
    # print(f"Derivative relative to y:\n  {d3.derive('y')}")
    # print(f"Derivative relative to None:\n  {d3.derive(None)}")
    # print(f"Simplification:\n  {d3.simplify()}")
    # print("")
    
    # print("Expr6")
    # print(f"Expression:\n  {d4}")
    # print(f"Evaluation with x=5, y=7:\n  {d4.eval(env)}")
    # print(f"Derivative relative to x:\n  {d4.derive('x')}")
    # print(f"Derivative relative to y:\n  {d4.derive('y')}")
    # print(f"Derivative relative to None:\n  {d4.derive(None)}")
    # print(f"Simplification:\n  {d4.simplify()}")
    # print("")
    
    # print("Expr7")
    # print(f"Expression:\n  {d5}")
    # print(f"Evaluation with x=5, y=7:\n  {d5.eval(env)}")
    # print(f"Derivative relative to x:\n  {d5.derive('x')}")
    # print(f"Derivative relative to y:\n  {d5.derive('y')}")
    # print(f"Derivative relative to None:\n  {d5.derive(None)}")
    # print(f"Simplification:\n  {d5.simplify()}")
    # print("")
    
    # print("Expr8")
    # print(f"Expression:\n  {d6}")
    # print(f"Evaluation with x=5, y=7:\n  {d6.eval(env)}")
    # print(f"Derivative relative to x:\n  {d6.derive('x')}")
    # print(f"Derivative relative to y:\n  {d6.derive('y')}")
    # print(f"Derivative relative to None:\n  {d6.derive(None)}")
    # print(f"Simplification:\n  {d6.simplify()}")
    # print("")
    
    # exp = Div(Div(x,x),Div(c7,y))
    # print("Expr9")
    # print(f"Expression:\n  {exp}")
    # print(f"Evaluation with x=5, y=7:\n  {exp.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp.derive(None)}")
    # print(f"Simplification:\n  {exp.simplify()}")
    # print("")
    
    # exp2 = Div(Div(Const(0),Const(0)),Div(Const(0),Const(1)))
    # print("Expr10")
    # print(f"Expression:\n  {exp2}")
    # print(f"Evaluation with x=5, y=7:\n  {exp2.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp2.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp2.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp2.derive(None)}")
    # print(f"Simplification:\n  {exp2.simplify()}")
    # print("")
    
    

    # n0L = Neg(c0)
    # n0R = Neg(c3)
    # n1  = Neg(c7)
    # n2  = Neg(c1)
    # n3  = Neg(x)
    # n4  = Neg(y)
    # n5  = Neg(n1)
    # n6  = Neg(Neg(n1))
    # print("Expr1")
    # print(f"Expression:\n  {n0L}")
    # print(f"Evaluation with x=5, y=7:\n  {n0L.eval(env)}")
    # print(f"Derivative relative to x:\n  {n0L.derive('x')}")
    # print(f"Derivative relative to y:\n  {n0L.derive('y')}")
    # print(f"Derivative relative to None:\n  {n0L.derive(None)}")
    # print(f"Simplification:\n  {n0L.simplify()}")
    # print("")
    # print("Expr2")
    # print(f"Expression:\n  {n0R}")
    # print(f"Evaluation with x=5, y=7:\n  {n0R.eval(env)}")
    # print(f"Derivative relative to x:\n  {n0R.derive('x')}")
    # print(f"Derivative relative to y:\n  {n0R.derive('y')}")
    # print(f"Derivative relative to None:\n  {n0R.derive(None)}")
    # print(f"Simplification:\n  {n0R.simplify()}")
    # print(f" ")
    
    # print("Expr3")
    # print(f"Expression:\n  {n1}")
    # print(f"Evaluation with x=5, y=7:\n  {n1.eval(env)}")
    # print(f"Derivative relative to x:\n  {n1.derive('x')}")
    # print(f"Derivative relative to y:\n  {n1.derive('y')}")
    # print(f"Derivative relative to None:\n  {n1.derive(None)}")
    # print(f"Simplification:\n  {n1.simplify()}")
    # print("")
    
    # print("Expr4")
    # print(f"Expression:\n  {n2}")
    # print(f"Evaluation with x=5, y=7:\n  {n2.eval(env)}")
    # print(f"Derivative relative to x:\n  {n2.derive('x')}")
    # print(f"Derivative relative to y:\n  {n2.derive('y')}")
    # print(f"Derivative relative to None:\n  {n2.derive(None)}")
    # print(f"Simplification:\n  {n2.simplify()}")
    # print("")
    
    # print("Expr5")
    # print(f"Expression:\n  {n3}")
    # print(f"Evaluation with x=5, y=7:\n  {n3.eval(env)}")
    # print(f"Derivative relative to x:\n  {n3.derive('x')}")
    # print(f"Derivative relative to y:\n  {n3.derive('y')}")
    # print(f"Derivative relative to None:\n  {n3.derive(None)}")
    # print(f"Simplification:\n  {n3.simplify()}")
    # print("")
    
    # print("Expr6")
    # print(f"Expression:\n  {n4}")
    # print(f"Evaluation with x=5, y=7:\n  {n4.eval(env)}")
    # print(f"Derivative relative to x:\n  {n4.derive('x')}")
    # print(f"Derivative relative to y:\n  {n4.derive('y')}")
    # print(f"Derivative relative to None:\n  {n4.derive(None)}")
    # print(f"Simplification:\n  {n4.simplify()}")
    # print("")
    
    # print("Expr7")
    # print(f"Expression:\n  {n5}")
    # print(f"Evaluation with x=5, y=7:\n  {n5.eval(env)}")
    # print(f"Derivative relative to x:\n  {n5.derive('x')}")
    # print(f"Derivative relative to y:\n  {n5.derive('y')}")
    # print(f"Derivative relative to None:\n  {n5.derive(None)}")
    # print(f"Simplification:\n  {n5.simplify()}")
    # print("")
    
    # print("Expr8")
    # print(f"Expression:\n  {n6}")
    # print(f"Evaluation with x=5, y=7:\n  {n6.eval(env)}")
    # print(f"Derivative relative to x:\n  {n6.derive('x')}")
    # print(f"Derivative relative to y:\n  {n6.derive('y')}")
    # print(f"Derivative relative to None:\n  {n6.derive(None)}")
    # print(f"Simplification:\n  {n6.simplify()}")
    # print("")
    
    # exp = Neg(Neg(c7))
    # print("Expr9")
    # print(f"Expression:\n  {exp}")
    # print(f"Evaluation with x=5, y=7:\n  {exp.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp.derive(None)}")
    # print(f"Simplification:\n  {exp.simplify()}")
    # print("")
    
    # exp2 = Neg(Neg(Const(1)))
    # print("Expr10")
    # print(f"Expression:\n  {exp2}")
    # print(f"Evaluation with x=5, y=7:\n  {exp2.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp2.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp2.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp2.derive(None)}")
    # print(f"Simplification:\n  {exp2.simplify()}")
    # print("")
    # cs0L = Cos(c0)
    # cs0R = Cos(c3)
    # cs1  = Cos(c7)
    # cs2  = Cos(c1)
    # cs3  = Cos(x)
    # cs4  = Cos(y)
    # cs5  = Cos(cs1)
    # cs6  = Cos(Cos(cs1))
    # print("Expr1")
    # print(f"Expression:\n  {cs0L}")
    # print(f"Evaluation with x=5, y=7:\n  {cs0L.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs0L.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs0L.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs0L.derive(None)}")
    # print(f"Simplification:\n  {cs0L.simplify()}")
    # print("")
    # print("Expr2")
    # print(f"Expression:\n  {cs0R}")
    # print(f"Evaluation with x=5, y=7:\n  {cs0R.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs0R.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs0R.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs0R.derive(None)}")
    # print(f"Simplification:\n  {cs0R.simplify()}")
    # print(f" ")
    
    # print("Expr3")
    # print(f"Expression:\n  {cs1}")
    # print(f"Evaluation with x=5, y=7:\n  {cs1.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs1.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs1.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs1.derive(None)}")
    # print(f"Simplification:\n  {cs1.simplify()}")
    # print("")
    
    # print("Expr4")
    # print(f"Expression:\n  {cs2}")
    # print(f"Evaluation with x=5, y=7:\n  {cs2.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs2.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs2.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs2.derive(None)}")
    # print(f"Simplification:\n  {cs2.simplify()}")
    # print("")
    
    # print("Expr5")
    # print(f"Expression:\n  {cs3}")
    # print(f"Evaluation with x=5, y=7:\n  {cs3.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs3.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs3.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs3.derive(None)}")
    # print(f"Simplification:\n  {cs3.simplify()}")
    # print("")
    
    # print("Expr6")
    # print(f"Expression:\n  {cs4}")
    # print(f"Evaluation with x=5, y=7:\n  {cs4.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs4.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs4.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs4.derive(None)}")
    # print(f"Simplification:\n  {cs4.simplify()}")
    # print("")
    
    # print("Expr7")
    # print(f"Expression:\n  {cs5}")
    # print(f"Evaluation with x=5, y=7:\n  {cs5.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs5.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs5.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs5.derive(None)}")
    # print(f"Simplification:\n  {cs5.simplify()}")
    # print("")
    
    # print("Expr8")
    # print(f"Expression:\n  {cs6}")
    # print(f"Evaluation with x=5, y=7:\n  {cs6.eval(env)}")
    # print(f"Derivative relative to x:\n  {cs6.derive('x')}")
    # print(f"Derivative relative to y:\n  {cs6.derive('y')}")
    # print(f"Derivative relative to None:\n  {cs6.derive(None)}")
    # print(f"Simplification:\n  {cs6.simplify()}")
    # print("")
    
    # exp = Cos(Cos(c7))
    # print("Expr9")
    # print(f"Expression:\n  {exp}")
    # print(f"Evaluation with x=5, y=7:\n  {exp.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp.derive(None)}")
    # print(f"Simplification:\n  {exp.simplify()}")
    # print("")
    
    # exp2 = Cos(Cos(Const(1)))
    # print("Expr10")
    # print(f"Expression:\n  {exp2}")
    # print(f"Evaluation with x=5, y=7:\n  {exp2.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp2.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp2.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp2.derive(None)}")
    # print(f"Simplification:\n  {exp2.simplify()}")
    # print("")
    # sn0L = Sin(c0)
    # sn0R = Sin(c3)
    # sn1  = Sin(c7)
    # sn2  = Sin(c1)
    # sn3  = Sin(x)
    # sn4  = Sin(y)
    # sn5  = Sin(sn1)
    # sn6  = Sin(Sin(sn1))
    # print("Expr1")
    # print(f"Expression:\n  {sn0L}")
    # print(f"Evaluation with x=5, y=7:\n  {sn0L.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn0L.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn0L.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn0L.derive(None)}")
    # print(f"Simplification:\n  {sn0L.simplify()}")
    # print("")
    # print("Expr2")
    # print(f"Expression:\n  {sn0R}")
    # print(f"Evaluation with x=5, y=7:\n  {sn0R.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn0R.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn0R.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn0R.derive(None)}")
    # print(f"Simplification:\n  {sn0R.simplify()}")
    # print(f" ")

    # print("Expr3")
    # print(f"Expression:\n  {sn1}")
    # print(f"Evaluation with x=5, y=7:\n  {sn1.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn1.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn1.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn1.derive(None)}")
    # print(f"Simplification:\n  {sn1.simplify()}")
    # print("")

    # print("Expr4")
    # print(f"Expression:\n  {sn2}")
    # print(f"Evaluation with x=5, y=7:\n  {sn2.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn2.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn2.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn2.derive(None)}")
    # print(f"Simplification:\n  {sn2.simplify()}")
    # print("")

    # print("Expr5")
    # print(f"Expression:\n  {sn3}")
    # print(f"Evaluation with x=5, y=7:\n  {sn3.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn3.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn3.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn3.derive(None)}")
    # print(f"Simplification:\n  {sn3.simplify()}")
    # print("")

    # print("Expr6")
    # print(f"Expression:\n  {sn4}")
    # print(f"Evaluation with x=5, y=7:\n  {sn4.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn4.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn4.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn4.derive(None)}")
    # print(f"Simplification:\n  {sn4.simplify()}")
    # print("")

    # print("Expr7")
    # print(f"Expression:\n  {sn5}")
    # print(f"Evaluation with x=5, y=7:\n  {sn5.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn5.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn5.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn5.derive(None)}")
    # print(f"Simplification:\n  {sn5.simplify()}")
    # print("")

    # print("Expr8")
    # print(f"Expression:\n  {sn6}")
    # print(f"Evaluation with x=5, y=7:\n  {sn6.eval(env)}")
    # print(f"Derivative relative to x:\n  {sn6.derive('x')}")
    # print(f"Derivative relative to y:\n  {sn6.derive('y')}")
    # print(f"Derivative relative to None:\n  {sn6.derive(None)}")
    # print(f"Simplification:\n  {sn6.simplify()}")
    # print("")

    # exp = Sin(Sin(c7))
    # print("Expr9")
    # print(f"Expression:\n  {exp}")
    # print(f"Evaluation with x=5, y=7:\n  {exp.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp.derive(None)}")
    # print(f"Simplification:\n  {exp.simplify()}")
    # print("")

    # exp2 = Sin(Sin(Const(1)))
    # print("Expr10")
    # print(f"Expression:\n  {exp2}")
    # print(f"Evaluation with x=5, y=7:\n  {exp2.eval(env)}")
    # print(f"Derivative relative to x:\n  {exp2.derive('x')}")
    # print(f"Derivative relative to y:\n  {exp2.derive('y')}")
    # print(f"Derivative relative to None:\n  {exp2.derive(None)}")
    # print(f"Simplification:\n  {exp2.simplify()}")
    # print("")
