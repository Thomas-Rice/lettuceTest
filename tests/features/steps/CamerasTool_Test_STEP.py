from behave import given, when, then



@given('Nuke is open with a C_CameraSolver setup and on cameras mode')
def step_impl(context):
    context.x.setup()

@when('I ctrl + alt drag on the viewer with camera 1 selected')
def step_impl(context):
    context.x.execute()

@then('the cameras selected should move according to the mouse moves')
def step_impl(context):
    context.x.evaluate(context.testName, context.refBBOX)
    context.x.tearDown()