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

class Tree:

    def eval(self,env={}):
        pass

    def derive(self,v):
        pass

    def simplify(self):
        pass

    def is_valid_name(self,name):    # any nonempty string for now
        return isinstance(name,str) and len(name) > 0
        # None must not be valid name!

    def is_valid_value(self,value):  # any number for now
        return isinstance(value,(int,float,complex))
        # None must not be valid value!

    def __repr__(self):
        return "Tree: Not intended to be instantiated"



class Sum(Tree):

    def __init__(self, l, r): 
        self.left  = l if isinstance(l,Tree) else None
        self.right = r if isinstance(r,Tree) else None
        # self.left  = (isinstance(l,Tree) and l) or None
        # self.right = (isinstance(r,Tree) and r) or None

    def eval(self,env={}):
        lv = self.left.eval(env)  if self.left  else None
        rv = self.right.eval(env) if self.right else None
        return lv + rv if lv is not None and rv is not None else None
        # lv = self.left  and self.left.eval(env)
        # rv = self.right and self.right.eval(env)
        # if lv is not None and rv is not None: 
        #     return lv + rv
        # else:
        #     return None

    def derive(self,v):
        dl = self.left.derive(v)  if self.left  else None
        dr = self.right.derive(v) if self.right else None
        return Sum(dl,dr) if dl and dr else None
        # dl = self.left  and self.left.derive(v)
        # dr = self.right and self.right.derive(v)
        # return dl and dr and Sum(dl,dr)

    def simplify(self):
        sl = self.left.simplify()  if self.left  else None
        sr = self.right.simplify() if self.right else None
        # sl = self.left  and self.left.simplify()
        # sr = self.right and self.right.simplify()
        lc, rc = isinstance(sl,Const), isinstance(sr,Const)
        if lc and rc:
            return Const(sl.value + sr.value)
        elif lc and sl.value == 0: # Additive identity
            return sr
        elif rc and sr.value == 0: # Additive identity
            return sl
        return Sum(sl,sr) if sl and sr else None
        # return sl and sr and Sum(sl,sr)
    
    def __repr__(self):
        return f"Sum({repr(self.left)},{repr(self.right)})"


class Var(Tree):

    def __init__(self, n):
        self.name = n if self.is_valid_name(n) else None
        # if self.is_valid_name(n):
        #     self.name = n
        # else:
        #     self.name = None

    def eval(self,env={}):
        return env.get(self.name)

    def derive(self,v):
        if self.is_valid_name(v) and v == self.name:
            return Const(1)
        elif self.name is not None:
            return Const(0)
        else:
            return None

    def simplify(self):
        return self if self.name is not None else None
        # if self.name is not None:
        #     return self
        # else:
        #     return None

    def __repr__(self):
        return f"Var({self.name})"

    
class Const(Tree):

    def __init__(self, v):
        self.value = v if self.is_valid_value(v) else None
        # if self.is_valid_value(v):
        #     self.value = v
        # else:
        #     self.value = None

    def eval(self, env={}):
        return self.value

    def derive(self, v):
        return Const(0) if self.value is not None else None
        # if self.value is not None:
        #     return Const(0)
        # else:
        #     return None

    def simplify(self):
        return self if self.value is not None else None
        # if self.value is not None:
        #    return self
        # else:
        #     return None

    def __repr__(self):
        return f"Const({self.value})"


if __name__ == '__main__':
    print("Begin smoke testing expression tree program")
    env = { "x":5, "y":7 }

    x   = Var("x")
    y   = Var("y")
    z   = Var("z")  # no value in env

    c0  = Const(0.0)
    c1  = Const(1.0)
    c3  = Const(3.0)
    c6  = Const(6.0)
    c7  = Const(7.0)
    cm3 = Const(-3.0)

    print(f"Expression: {c0}")
    print(f"Evaluation with x=5, y=7:\n  {c0.eval(env)}")
    print(f"Derivative relative to x:\n  {c0.derive('x')}")
    print(f"Derivative relative to y:\n  {c0.derive('y')}")
    print(f"Derivative relative to None:\n  {c0.derive(None)}")
    print(f"Simplification:\n  {c0.simplify()}")
    print("")

    print(f"Expression:\n  {cm3}")
    print(f"Evaluation with x=5, y=7:\n  {cm3.eval(env)}")
    print(f"Derivative relative to x:\n  {cm3.derive(f'x')}")
    print(f"Derivative relative to y:\n  {cm3.derive(f'y')}")
    print(f"Derivative relative to None:\n  {cm3.derive(None)}")
    print(f"Simplification:\n  {cm3.simplify()}")
    print("")

    x = Var("x")
    y = Var("y")
    z = Var("z")  # no value in env

    print(f"Expression:\n  {x}")
    print(f"Evaluation with x=5, y=7:\n  {x.eval(env)}")
    print(f"Derivative relative to x:\n  {x.derive('x')}")
    print(f"Derivative relative to y:\n  {x.derive('y')}")
    print(f"Derivative relative to None:\n  {x.derive(None)}")
    print(f"Simplification:\n  {x.simplify()}")
    print("")

    print(f"Expression:\n  {y}")
    print(f"Evaluation with x=5, y=7:\n  {y.eval(env)}")
    print(f"Derivative relative to x:\n  {y.derive('x')}")
    print(f"Derivative relative to y:\n  {y.derive('y')}")
    print(f"Derivative relative to None:\n  {y.derive(None)}")
    print(f"Simplification:\n  {y.simplify()}")
    print("")

    print(f"Expression:\n  {z}")
#   Variable not in environment
    print(f"Evaluation with x=5, y=7:\n  {z.eval(env)}")
    print(f"Derivative relative to x:\n  {z.derive('x')}")
    print(f"Derivative relative to y:\n  {z.derive('y')}")
    print(f"Derivative relative to None:\n  {z.derive(None)}")
    print(f"Simplification:\n  {z.simplify()}")
    print("")

    s0L = Sum(c0,c3)
    s0R = Sum(c3,c0)
    s1  = Sum(c7,cm3)
    s2  = Sum(c1,y)
    s3  = Sum(x,c3)
    s4  = Sum(x,y)
    s5  = Sum(s1,s0L)
    s6  = Sum(Sum(s1,s2),Sum(s1,s4))
    print("Expr1")
    print(f"Expression:\n  {s0L}")
    print(f"Evaluation with x=5, y=7:\n  {s0L.eval(env)}")
    print(f"Derivative relative to x:\n  {s0L.derive('x')}")
    print(f"Derivative relative to y:\n  {s0L.derive('y')}")
    print(f"Derivative relative to None:\n  {s0L.derive(None)}")
    print(f"Simplification:\n  {s0L.simplify()}")
    print("")
    
    print("Expr2")
    print(f"Expression:\n  {s0R}")
    print(f"Evaluation with x=5, y=7:\n  {s0R.eval(env)}")
    print(f"Derivative relative to x:\n  {s0R.derive('x')}")
    print(f"Derivative relative to y:\n  {s0R.derive('y')}")
    print(f"Derivative relative to None:\n  {s0R.derive(None)}")
    print(f"Simplification:\n  {s0R.simplify()}")
    print(f" ")

    print("Expr3")
    print(f"Expression:\n  {s1}")
    print(f"Evaluation with x=5, y=7:\n  {s1.eval(env)}")
    print(f"Derivative relative to x:\n  {s1.derive('x')}")
    print(f"Derivative relative to y:\n  {s1.derive('y')}")
    print(f"Derivative relative to None:\n  {s1.derive(None)}")
    print(f"Simplification:\n  {s1.simplify()}")
    print("")

    print("Expr4")
    print(f"Expression:\n  {s2}")
    print(f"Evaluation with x=5, y=7:\n  {s2.eval(env)}")
    print(f"Derivative relative to x:\n  {s2.derive('x')}")
    print(f"Derivative relative to y:\n  {s2.derive('y')}")
    print(f"Derivative relative to None:\n  {s2.derive(None)}")
    print(f"Simplification:\n  {s2.simplify()}")
    print("")

    print("Expr5")
    print(f"Expression:\n  {s3}")
    print(f"Evaluation with x=5, y=7:\n  {s3.eval(env)}")
    print(f"Derivative relative to x:\n  {s3.derive('x')}")
    print(f"Derivative relative to y:\n  {s3.derive('y')}")
    print(f"Derivative relative to None:\n  {s3.derive(None)}")
    print(f"Simplification:\n  {s3.simplify()}")
    print("")

    print("Expr6")
    print(f"Expression:\n  {s4}")
    print(f"Evaluation with x=5, y=7:\n  {s4.eval(env)}")
    print(f"Derivative relative to x:\n  {s4.derive('x')}")
    print(f"Derivative relative to y:\n  {s4.derive('y')}")
    print(f"Derivative relative to None:\n  {s4.derive(None)}")
    print(f"Simplification:\n  {s4.simplify()}")
    print("")

    print("Expr7")
    print(f"Expression:\n  {s5}")
    print(f"Evaluation with x=5, y=7:\n  {s5.eval(env)}")
    print(f"Derivative relative to x:\n  {s5.derive('x')}")
    print(f"Derivative relative to y:\n  {s5.derive('y')}")
    print(f"Derivative relative to None:\n  {s5.derive(None)}")
    print(f"Simplification:\n  {s5.simplify()}")
    print("")

    print("Expr8")
    print(f"Expression:\n  {s6}")
    print(f"Evaluation with x=5, y=7:\n  {s6.eval(env)}")
    print(f"Derivative relative to x:\n  {s6.derive('x')}")
    print(f"Derivative relative to y:\n  {s6.derive('y')}")
    print(f"Derivative relative to None:\n  {s6.derive(None)}")
    print(f"Simplification:\n  {s6.simplify()}")
    print("")

    exp = Sum(Sum(x,x),Sum(c7,y))
    print("Expr9")
    print(f"Expression:\n  {exp}")
    print(f"Evaluation with x=5, y=7:\n  {exp.eval(env)}")
    print(f"Derivative relative to x:\n  {exp.derive('x')}")
    print(f"Derivative relative to y:\n  {exp.derive('y')}")
    print(f"Derivative relative to None:\n  {exp.derive(None)}")
    print(f"Simplification:\n  {exp.simplify()}")
    print("")
 
    exp2 = Sum(Sum(Const(0),Const(0)),Sum(Const(0),Const(1)))
    print("Expr10")
    print(f"Expression:\n  {exp2}")
    print(f"Evaluation with x=5, y=7:\n  {exp2.eval(env)}")
    print(f"Derivative relative to x:\n  {exp2.derive('x')}")
    print(f"Derivative relative to y:\n  {exp2.derive('y')}")
    print(f"Derivative relative to None:\n  {exp2.derive(None)}")
    print(f"Simplification:\n  {exp2.simplify()}")
    print("")

    n1 = Const(None)
    n2 = Var(None)
    n3 = Sum(None,None)

    print("Expr11")
    print(f"Expression:\n  {n1}")
    print(f"Evaluation with x=5, y=7:\n  {n1.eval(env)}")
    print(f"Derivative relative to x:\n  {n1.derive('x')}")
    print(f"Derivative relative to y:\n  {n1.derive('y')}")
    print(f"Derivative relative to None:\n  {n1.derive(None)}")
    print(f"Simplification:\n  {n1.simplify()}")
    print("")

    print("Expr12")
    print(f"Expression:\n  {n2}")
    print(f"Evaluation with x=5, y=7:\n  {n2.eval(env)}")
    print(f"Derivative relative to x:\n  {n2.derive('x')}")
    print(f"Derivative relative to y:\n  {n2.derive('y')}")
    print(f"Derivative relative to None:\n  {n2.derive(None)}")
    print(f"Simplification:\n  {n2.simplify()}")
    print("")

    print("Expr13")
    print(f"Expression:\n  {n3}")
    print(f"Evaluation with x=5, y=7:\n  {n3.eval(env)}")
    print(f"Derivative relative to x:\n  {n2.derive('x')}")
    print(f"Derivative relative to y:\n  {n3.derive('y')}")
    print(f"Derivative relative to None:\n  {n3.derive(None)}")
    print(f"Simplification:\n  {n3.simplify()}")
    print("")

