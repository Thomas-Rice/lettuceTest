import sys
sys.path.append('C:\\Users\\thomas.rice\\PycharmProjects\\GUI_Tester\\')

import baseTest
import testRunner
from paths_and_messages import *
import time


def before_all(context):
    context.testObject = testRunner.returnTestObjects()
    context.bboxes = PM_bboxes


def before_feature(context, feature):
    context.testName = feature.name
    context.refBBOX = context.bboxes[context.testName]
    context.x = baseTest.baseTest(context.testObject[context.testName])

def after_feature(context, feature):
    time.sleep(10)


def after_all(context):
    pass