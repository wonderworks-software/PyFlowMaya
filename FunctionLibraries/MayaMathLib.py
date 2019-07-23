import pymel.core.datatypes as dt

from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE


class MayaMathLib(FunctionLibraryBase):
    def __init__(self, packageName):
        super(MayaMathLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=('MayaVectorPin', dt.Vector(0.0, 0.0, 0.0)), nodeType=NodeTypes.Pure, meta={'Category': 'Math', 'Keywords': ["vec", "new", "v3"]})
    def CreateVector(x=('FloatPin', 0.0), y=('FloatPin', 0.0), z=('FloatPin', 0.0)):
        """New pymel Vector"""
        return dt.Vector(x, y, z)
