import pymel.core as pm

from PyFlow.Packages.PyFlowMaya.Nodes import EVENT_NODE_HEADER_COLOR
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper


class scriptEntry(NodeBase):
    def __init__(self, name):
        super(scriptEntry, self).__init__(name)
        self.evaluatePin = self.createOutputPin("Exec", "ExecPin")
        self.headerColor = EVENT_NODE_HEADER_COLOR

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addOutputDataType('ExecPin')
        helper.addOutputStruct(PinStructure.Single)
        return helper

    @staticmethod
    def category():
        return 'Events'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Can be used as entry point for anything'

    def compute(self, *args, **kwargs):
        self.evaluatePin.call()
