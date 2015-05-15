__author__ = 'jszheng'
"""
This is helper classes and interfaces for symbol scope
recording and identification
"""

from enum import Enum


class Scope:
    def getScopeName(self):
        pass

    def getEnclosingScope(self):
        pass

    def define(self, sym):
        pass

    def resolve(self, name):
        pass


class Symbol:
    class TypeEnum(Enum):
        INVALID = 1
        VOID = 2
        INT = 3
        FLOAT = 4

    def __init__(self, name='', stype=TypeEnum.INVALID):
        self.name = name
        self.type = stype
        self.scope = None

    def __str__(self):
        if self.type != Symbol.TypeEnum.INVALID:
            return '<'+self.name+':'+self.type.name+'>'
        else:
            return self.name


class BaseScope(Scope):
    def __init__(self, scope: Scope):
        self.enclosingScope = scope
        self.symbols = {}

    def resolve(self, name):
        s = self.symbols.get(name)
        if s is not None:
            return s
        if self.enclosingScope is not None:
            return self.enclosingScope.resolve(name)
        return None

    def define(self, sym: Symbol):
        self.symbols[sym.name] = sym

    def getEnclosingScope(self):
        return self.enclosingScope

    def __str__(self):
        buf = self.getScopeName() + ' : ' + list(self.symbols.keys()).__str__()
        return buf


class GlobalScope(BaseScope):
    def __init__(self, scope):
        super().__init__(scope)

    def getScopeName(self):
        return 'globals'


class LocalScope(BaseScope):
    def __init__(self, parent):
        super().__init__(parent)

    def getScopeName(self):
        return 'locals'


class FunctionSymbol(Symbol, Scope):
    def __init__(self, name='', stype=Symbol.TypeEnum.INVALID, scope=None):
        super().__init__(name, stype)
        self.enclosingScope = scope
        self.arguments = {}

    def resolve(self, name):
        s = self.arguments.get(name)
        if s is not None:
            return s
        if self.enclosingScope is not None:
            return self.enclosingScope.resolve(name)
        return None

    def define(self, sym: Symbol):
        self.arguments[sym.name] = sym
        sym.scope = self

    def getEnclosingScope(self):
        return self.enclosingScope

    def getScopeName(self):
        return self.name

    def __str__(self):
        buf = "function "
        buf += super().__str__()
        buf += " : "
        for par in self.arguments.values():
            buf += par.__str__() + ';'
        return buf


class VariableSymbol(Symbol):
    def __init__(self, name, stype):
        super().__init__(name, stype)