from quant.koq_variable import KOQVariable
from _collections import defaultdict

class KOQRegistry():
    def __init__(self):
        self._type_names = defaultdict(list)
        self._relations = defaultdict(list)
        self.clear_terms()
        
    def KOQ(self, name, value):
        self.check_type2_error(name)
        self.clear_terms()
        self.__dict__[name] = KOQVariable(self, name, value)
        self._type_names[name].append(self.__dict__[name])
        return self.__dict__[name]
        
    def KOQRelation(self, name, relation):
        self._relations[name].append(relation.replace(" ", ""))

    def clear_terms(self):
        self._terms = []
        
    def check_type1_error(self, koq1, koq2):
        type1 = self.get_type_name(koq1)
        type2 = self.get_type_name(koq2)
        if (type1 != None and type2 != None and type1 != type2):
            raise TypeError('Type 1 Kind of Quantity error: {0} vs {1}'.format(type1, type2))
        
    def get_type_name(self, value):
        try:
            for key, values in self._type_names.items():
                for v in values:
                    if (v == value):
                        return key
        except AttributeError:
            return None
        return None

    def add_term(self, item):
        if (isinstance(item, list)):
            sub_terms = []
            for sub_item in item:
                if (isinstance(sub_item, KOQVariable)):
                    # Don't store unnamed intermediate results
                    if (sub_item._name != None):
                        sub_terms.append(sub_item._name)
                else:
                    sub_terms.append(sub_item)
            self._terms.append(list(sub_terms))
        else:
            if (isinstance(item, KOQVariable)):
                # Don't store unnamed intermediate results
                if (item._name != None):
                    self._terms.append(item._name)
            else:
                self._terms.append(item)
        #print(self._terms)
        
    def isEquivalent(self, infix_str, relation):
        # TODO: Improve this trivial implementation.
        # A real implementation needs to be able to recognise as equivalent, expressions that can be re-arranged 
        # and/or simplified to match one of the specified relations.
        return relation.replace(" ", "") == infix_str

    def check_type2_error(self, type_name):
        if (not self._terms):
            return
        if (not type_name in self._relations):
            return
        #print(self._terms)
        infix_str = self.to_infix_str(self._terms)
        #print(infix_str)
        for relation in self._relations[type_name]:
            if (self.isEquivalent(infix_str, relation)):
                return
        raise TypeError("Type 2 Kind of Quantity error: {0} = {1}".format(type_name, self._relations[type_name]))


    def generate_expression(self, operator, rhs, lhs):
        # Ignore multiplication by a constant 
        if (operator == "*"):
            if (not isinstance(lhs, str)):
                return rhs
            if (not isinstance(rhs, str)):
                return lhs
            
        return lhs.__str__() + operator.__str__() + rhs.__str__()

    def to_infix_str(self, terms):
        stack = []
        for t in terms:
            if(self.isOperator(t)):
                rhs = stack.pop()
                lhs = stack.pop()
                expression = self.generate_expression(t, rhs, lhs)
                stack.append(expression)
            else:
                stack.append(t)
        return stack[-1]
        
    def isOperator(self, t):
        return t == "+" or t == "-" or t == "*" or t == "/" or t == "**"
