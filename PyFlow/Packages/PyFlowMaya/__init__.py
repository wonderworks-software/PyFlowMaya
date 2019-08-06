PACKAGE_NAME = 'PyFlowMaya'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Nodes
from PyFlow.Packages.PyFlowMaya.Nodes.EventCurrentFrameChanged import eventCurrentFrameChanged
from PyFlow.Packages.PyFlowMaya.Nodes.ScriptEntry import scriptEntry

# Pins
from PyFlow.Packages.PyFlowMaya.Pins.MayaVectorPin import MayaVectorPin

# Function based nodes
from PyFlow.Packages.PyFlowMaya.FunctionLibraries.MayaMathLib import MayaMathLib
from PyFlow.Packages.PyFlowMaya.FunctionLibraries.MayaGeneralLib import MayaGeneralLib
from PyFlow.Packages.PyFlowMaya.FunctionLibraries.MayaDisplayLib import MayaDisplayLib
from PyFlow.Packages.PyFlowMaya.FunctionLibraries.MayaSelectionLib import MayaSelectionLib

# Tools
from PyFlow.Packages.PyFlowMaya.Tools.RunScriptTool import RunScriptTool

# Factories

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_NODES[eventCurrentFrameChanged.__name__] = eventCurrentFrameChanged
_NODES[scriptEntry.__name__] = scriptEntry

_FOO_LIBS[MayaMathLib.__name__] = MayaMathLib(PACKAGE_NAME)
_FOO_LIBS[MayaGeneralLib.__name__] = MayaGeneralLib(PACKAGE_NAME)
_FOO_LIBS[MayaDisplayLib.__name__] = MayaDisplayLib(PACKAGE_NAME)
_FOO_LIBS[MayaSelectionLib.__name__] = MayaSelectionLib(PACKAGE_NAME)

_PINS[MayaVectorPin.__name__] = MayaVectorPin

_TOOLS[RunScriptTool.__name__] = RunScriptTool


class PyFlowMaya(IPackage):
	def __init__(self):
		super(PyFlowMaya, self).__init__()

	@staticmethod
	def GetExporters():
		return _EXPORTERS

	@staticmethod
	def GetFunctionLibraries():
		return _FOO_LIBS

	@staticmethod
	def GetNodeClasses():
		return _NODES

	@staticmethod
	def GetPinClasses():
		return _PINS

	@staticmethod
	def GetToolClasses():
		return _TOOLS
