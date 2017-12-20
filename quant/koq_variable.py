class KOQVariable():

    def __init__(self, registry, varName, quantity):
        self._registry = registry
        self._name = varName
        self._quantity = quantity
        
    def __repr__(self):
        self._registry.clear_terms()
        return self._quantity.__repr__();
    
    def __add__(self, other):
        self._registry.check_type1_error(self, other)
        self._registry.add_term(self)
        if (self.get_type_name(self) == None or self.get_type_name(other) == None):
            self._registry.add_term(other)
            self._registry.add_term("+")
        lhs = self._quantity if hasattr(self, '_quantity') else self
        rhs = other._quantity if hasattr(other, '_quantity') else other
        return KOQVariable(self._registry, None, lhs + rhs);
    
    __radd__ = __add__
    __iadd__ = __add__
    
    def __sub__(self, other):
        self._registry.check_type1_error(self, other)
        self._registry.add_term(self)
        if (self.get_type_name(self) == None or self.get_type_name(other) == None):
            self._registry.add_term(other)
            self._registry.add_term("-")
        lhs = self._quantity if hasattr(self, '_quantity') else self
        rhs = other._quantity if hasattr(other, '_quantity') else other
        return KOQVariable(self._registry, None, lhs - rhs);
                 
    __rsub__ = __sub__
    __isub__ = __sub__

    def __mul__(self, other):
        self._registry.add_term(self)
        self._registry.add_term(other)
        self._registry.add_term("*")
        lhs = self._quantity if hasattr(self, '_quantity') else self
        rhs = other._quantity if hasattr(other, '_quantity') else other
        return KOQVariable(self._registry, None, lhs * rhs);
    
    __rmul__ = __mul__
    __imul__ = __mul__

    def __truediv__(self, other):
        self._registry.add_term(self)
        self._registry.add_term(other)
        self._registry.add_term("/")
        lhs = self._quantity if hasattr(self, '_quantity') else self
        rhs = other._quantity if hasattr(other, '_quantity') else other
        return KOQVariable(self._registry, None, lhs / rhs);
    
    __div__ = __truediv__
    __rdiv__ = __truediv__
    __idiv__ = __truediv__

    def __pow__(self, other):
        self._registry.add_term(self)
        self._registry.add_term(other)
        self._registry.add_term("**")
        lhs = self._quantity if hasattr(self, '_quantity') else self
        rhs = other._quantity if hasattr(other, '_quantity') else other
        return KOQVariable(self._registry, None, lhs ** rhs);
    
    __rpow__ = __pow__
    __ipow__ = __pow__
    
    def get_type_name(self, variable):
        return self._registry.get_type_name(variable)
    