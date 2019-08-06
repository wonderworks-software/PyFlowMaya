import pymel.core as pm

from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE


class MayaDisplayLib(FunctionLibraryBase):
    def __init__(self, packageName):
        super(MayaDisplayLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), meta={'Category': 'Display', 'Keywords': []})
    def currentLinearUnit(fullName=("BoolPin", False)):
        return pm.currentUnit(query=True, linear=True, f=fullName)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={'Category': 'Display', 'Keywords': []})
    def setCurrentLinearUnit(unit=("StringPin", "cm", {"ValueList": ["mm", "millimeter", "cm", "centimeter", "m", "meter", "km", "kilometer", "in", "inch", "ft", "foot", "yd", "yard", "mi", "mile"]})):
        return pm.currentUnit(linear=unit)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), meta={'Category': 'Display', 'Keywords': []})
    def currentAngularUnit(fullName=("BoolPin", False)):
        return pm.currentUnit(query=True, angle=True, f=fullName)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={'Category': 'Display', 'Keywords': []})
    def setCurrentAngularUnit(unit=("StringPin", "deg", {"ValueList": ["deg", "degree", "rad", "radian"]})):
        return pm.currentUnit(angle=unit)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", ""), meta={'Category': 'Display', 'Keywords': []})
    def currentTimeUnit():
        return pm.currentUnit(query=True, time=True)
