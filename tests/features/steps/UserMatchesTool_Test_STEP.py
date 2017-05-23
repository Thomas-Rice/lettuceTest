from behave import when, then

#given, and -> located in HorizonTool

@when('And I Match/Solve/SetupRig')
def step_impl(context):
    context.x.matchAndSolveSetupRig()

@when('I click on the User Matches Tool')
def step_impl(context):
    context.x.clickUserMatchesTool()

@when('I ctrl + alt on the an overlapping section of the viewer')
def step_impl(context):
    context.x.clickAndDrag()

@then('the a user match should be added with sniper windows present in the top left')
def step_impl(context):
    context.x.evaluate(context.testName, context.refBBOX)
