Feature: HorizonTool_Test
  The user wants to be able to move the horizon with ctrl/cmd + alt drag on the viewer.


  Scenario: HorizonTool layout drag
    Given Nuke is open with a C_CameraSolver setup and on horizon mode
    When we ctrl + alt drag on the viewer
    Then the viewer should move according to the mouse moves