import json
import maya.OpenMaya as om

from PyFlow.Core import PinBase
from PyFlow.Core.Common import *

# Patch some python methods
def MVectorRepr(self):
    return "[{0} {1} {2}]".format(self.x, self.y, self.z)

om.MVector.__repr__ = MVectorRepr


class MVectorEncoder(json.JSONEncoder):
    def default(self, vec3):
        if isinstance(vec3, om.MVector):
            return {om.MVector.__name__: [vec3.x, vec3.y, vec3.z]}
        json.JSONEncoder.default(self, vec3)


class MVectorDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(MVectorDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, vec3Dict):
        values = vec3Dict[om.MVector.__name__]
        return om.MVector(values[0], values[1], values[2])


class MVectorPin(PinBase):
    """doc string for MVectorPin"""
    def __init__(self, name, parent, direction, **kwargs):
        super(MVectorPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(om.MVector(0.0, 0.0, 0.0))

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('MVectorPin',)

    def defaultValue(self):
        if self.isArray():
            return []
        else:
            return om.MVector()

    @staticmethod
    def pinDataTypeHint():
        return 'MVectorPin', om.MVector()

    @staticmethod
    def color():
        return (10, 50, 120, 255)

    @staticmethod
    def internalDataStructure():
        return om.MVector

    @staticmethod
    def processData(data):
        return MVectorPin.internalDataStructure()(data)

    @staticmethod
    def jsonEncoderClass():
        return MVectorEncoder

    @staticmethod
    def jsonDecoderClass():
        return MVectorDecoder
