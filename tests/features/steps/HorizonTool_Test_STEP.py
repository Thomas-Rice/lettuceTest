from behave import given, when, then



@given('Nuke is open with a C_CameraSolver setup and on horizon mode')
def step_impl(context):
    context.x.setup()

@when('we ctrl + alt drag on the viewer')
def step_impl(context):
    context.x.execute()

@then('the viewer should move according to the mouse moves')
def step_impl(context):
    context.x.evaluate(context.testName, context.refBBOX)
    context.x.tearDown()