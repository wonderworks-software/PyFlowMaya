import pymel.core.datatypes as dt
import json

from PyFlow.Core import PinBase
from PyFlow.Core.Common import *


class MVectorEncoder(json.JSONEncoder):
    def default(self, vec3):
        if isinstance(vec3, dt.Vector):
            return {dt.Vector.__name__: [vec3.x, vec3.y, vec3.z]}
        json.JSONEncoder.default(self, vec3)


class MVectorDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(MVectorDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, vec3Dict):
        values = vec3Dict[dt.Vector.__name__]
        return dt.Vector(values[0], values[1], values[2])


class MayaVectorPin(PinBase):
    """doc string for MayaVectorPin"""
    def __init__(self, name, parent, direction, **kwargs):
        super(MayaVectorPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(dt.Vector(0.0, 0.0, 0.0))

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('MayaVectorPin',)

    def defaultValue(self):
        if self.isArray():
            return []
        else:
            return dt.Vector()

    @staticmethod
    def pinDataTypeHint():
        return 'MayaVectorPin', dt.Vector()

    @staticmethod
    def color():
        return (10, 50, 120, 255)

    @staticmethod
    def internalDataStructure():
        return dt.Vector

    @staticmethod
    def processData(data):
        return MayaVectorPin.internalDataStructure()(data)

    @staticmethod
    def jsonEncoderClass():
        return MVectorEncoder

    @staticmethod
    def jsonDecoderClass():
        return MVectorDecoder
