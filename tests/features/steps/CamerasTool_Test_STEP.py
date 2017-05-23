from behave import when, then


#given, and -> located in HorizonTool

@when('I double click on the Cameras Tool')
def step_impl(context):
    context.x.clickCamerasTool()

@then('the cameras selected should move according to the mouse moves')
def step_impl(context):
    context.x.evaluate(context.testName, context.refBBOX)
