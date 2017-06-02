from behave import when, then


@when('I ctrl + alt drag on the viewer with camera 1 selected')
def step_impl(context):
    context.x.ctrlAltCam1()

@when('I ctrl + alt on the an overlapping section of the viewer for SuperTool')
def step_impl(context):
    context.x.clickUserMatch()

