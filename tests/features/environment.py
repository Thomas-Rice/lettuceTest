import sys
sys.path.append('C:\\Users\\twr_000\\PycharmProjects\\test\\GUI_Tester\\')

import testRunner
from paths_and_messages import *
import time


def before_all(context):
    context.testObject = testRunner.returnTestObjects()
    context.bboxes = PM_bboxes
    context.fileToOpen = PM_fileToOpen


def before_feature(context, feature):
    context.testName = feature.name
    context.refBBOX = context.bboxes[context.testName]
    context.x = context.testObject[context.testName]

def after_feature(context, feature):
    #To allow for Nuke to fully close
    time.sleep(3)

def after_step(context, step):
    #Close the application if the test has not failed and on the last step.
    if not step.status == 'failed' and step.step_type is 'then':
        context.x.tearDown('')
    elif step.status == 'failed':
        context.x.tearDown('Step Failed, Shutting Down Application')

def after_all(context):
    pass