import pymel.core as pm

from PyFlow.Packages.PyFlowMaya.Nodes import EVENT_NODE_HEADER_COLOR
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper


class eventCurrentFrameChanged(NodeBase):
    def __init__(self, name):
        super(eventCurrentFrameChanged, self).__init__(name)
        self.evaluatePin = self.createOutputPin("Exec", "ExecPin")
        self.currentFramePin = self.createOutputPin("frame", "IntPin")
        self.headerColor = EVENT_NODE_HEADER_COLOR
        self.lastFrame = pm.currentTime(q=True)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addOutputDataType('ExecPin')
        helper.addOutputDataType('IntPin')
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
        return 'Fired when current time is changed'

    def Tick(self, deltaTime):
        super(eventCurrentFrameChanged, self).Tick(deltaTime)
        currentFrame = pm.currentTime(q=True)
        if self.lastFrame != currentFrame:
            self.compute()
        self.lastFrame = pm.currentTime(q=True)

    def compute(self, *args, **kwargs):
        currentFrame = pm.currentTime(q=True)
        self.currentFramePin.setData(currentFrame)
        self.evaluatePin.call()
