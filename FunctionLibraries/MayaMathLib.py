import maya.OpenMaya as om

from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE


class MayaMathLib(FunctionLibraryBase):
    def __init__(self, packageName):
        super(MayaMathLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=('MVectorPin', om.MVector(0.0, 0.0, 0.0)), nodeType=NodeTypes.Callable, meta={'Category': 'MayaMath', 'Keywords': ["vec", "new", "v3"]})
    def CreateMVector(x=('FloatPin', 0.0), y=('FloatPin', 0.0), z=('FloatPin', 0.0)):
        """New MVector"""
        return om.MVector(x, y, z)
