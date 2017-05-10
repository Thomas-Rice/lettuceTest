from behave import given, when, then



@given('Nuke is open with a C_CameraSolver setup')
def step_impl(context):
    context.x.setup()

@when('I ctrl + alt on the an overlapping section of the viewer')
def step_impl(context):
    context.x.execute()

@then('the a user match should be added with sniper windows present in the top left')
def step_impl(context):
    context.x.evaluate(context.testName, context.refBBOX)
