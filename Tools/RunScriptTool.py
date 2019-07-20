from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Packages.PyFlowMaya.Tools import RESOURCES_DIR

from Qt import QtGui


class RunScriptTool(ShelfTool):
    """docstring for RunScriptTool."""
    def __init__(self):
        super(RunScriptTool, self).__init__()

    @staticmethod
    def toolTip():
        return "Finds all scriptEntry nodes and executes them"

    @staticmethod
    def getIcon():
        return QtGui.QIcon(RESOURCES_DIR + "runScript.png")

    @staticmethod
    def name():
        return str("RunScriptTool")

    def do(self):
        entryPointNodes = self.pyFlowInstance.graphManager.get().getAllNodes(classNameFilters=["scriptEntry"])
        for entryNode in entryPointNodes:
            entryNode.compute()
