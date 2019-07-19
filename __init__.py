PACKAGE_NAME = 'PyFlowMaya'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.PyFlowMaya.Pins.MayaVectorPin import MayaVectorPin

# Function based nodes
from PyFlow.Packages.PyFlowMaya.FunctionLibraries.MayaMathLib import MayaMathLib

# Factories

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_FOO_LIBS[MayaMathLib.__name__] = MayaMathLib(PACKAGE_NAME)

_PINS[MayaVectorPin.__name__] = MayaVectorPin


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
