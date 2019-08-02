import pymel.core as pm
import pymel.core.datatypes as dt

from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE


class MayaSelectionLib(FunctionLibraryBase):
    def __init__(self, packageName):
        super(MayaSelectionLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", []), meta={'Category': 'Selection', 'Keywords': []})
    def getSelection():
        return [i.name() for i in pm.selected()]

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={'Category': 'Selection', 'Keywords': []})
    def select(pattern=("StringPin", "*"), bVisible=("BoolPin", False), bToggle=("BoolPin", False), bReplace=("BoolPin", False),
               bNoExpand=("BoolPin", False), bHierarchy=("BoolPin", False), bDeselect=("BoolPin", False),
               bContainerCentric=("BoolPin", False), bClear=("BoolPin", False), bAllDependencyNodes=("BoolPin", False),
               bAllDagObjects=("BoolPin", False), bAddFirst=("BoolPin", False), bAdd=("BoolPin", False),
               bResult=("Reference", ("BoolPin", False))):
        """Wrapper for **pm.select**"""
        if not pm.objExists(pattern):
            bResult(False)
        else:
            pm.select(pattern,
                      vis=bVisible,
                      tgl=bToggle,
                      r=bReplace,
                      ne=bNoExpand,
                      hi=bHierarchy,
                      d=bDeselect,
                      cc=bContainerCentric,
                      cl=bClear,
                      adn=bAllDependencyNodes,
                      ado=bAllDagObjects,
                      af=bAddFirst,
                      add=bAdd)
            bResult(True)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={'Category': 'Selection', 'Keywords': []})
    def clearSelection():
        pm.select(cl=True)

    @staticmethod
    @IMPLEMENT_NODE(returns=None, nodeType=NodeTypes.Callable, meta={'Category': 'Selection', 'Keywords': []})
    def pickWalk(direction=("StringPin", "left", {"ValueList": ["up", "down", "left", "right", "in", "out"]}),
                 bRecurse=("BoolPin", False),
                 typ=("StringPin", "nodes", {"ValueList": ["nodes", "instances", "edgeloop", "edgering", "faceloop", "keys", "latticepoints", "motiontrailpoints"]})):
        """The pickWalk command allows you to quickly change the selection list relative to the nodes that are currently selected. It is called pickWalk, because it walks from one selection list to another by unselecting what's currently selected, and selecting nodes that are in the specified direction from the currently selected list.\n\nIf you specify objects on the command line, the pickWalk command will walk from those objects instead of the selected list. If the -type flag is instances, then the left and right direction will walk to the previous or next instance of the same selected dag node."""
        pm.pickWalk(d=direction, r=bRecurse, type=typ)
