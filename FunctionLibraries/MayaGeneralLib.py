import pymel.core as pm

from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE


class MayaGeneralLib(FunctionLibraryBase):
    def __init__(self, packageName):
        super(MayaGeneralLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=('BoolPin', False), nodeType=NodeTypes.Callable, meta={'Category': 'MayaGeneral', 'Keywords': []})
    def SetTranslation(dag=('StringPin', ""), vector=('MayaVectorPin', pm.datatypes.Vector())):
        """Sets node translation if node exists"""
        if pm.objExists(dag):
            node = pm.PyNode(dag)
            node.t.set(vector)
            return True
        return False
