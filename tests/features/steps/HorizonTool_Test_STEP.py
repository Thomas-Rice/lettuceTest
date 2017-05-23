from behave import given, when, then



@given('Nuke is open with a C_CameraSolver setup')
def step_impl(context):
    #Load Nuke and confirm it's open
    context.x.setup()
    #Open specified file.
    context.x.openFile(context.fileToOpen)

@when('I double click on the C_CameraSolver')
def step_impl(context):
    context.x.clickCameraSolver()

@when('I double click on the Horizon Tool')
def step_impl(context):
    context.x.clickHorizonTool()

@when('I ctrl + alt drag on the viewer')
def step_impl(context):
    context.x.clickAndDrag()

@then('the viewer should move according to the mouse moves')
def step_impl(context):
    context.x.evaluate(context.testName, context.refBBOX)
