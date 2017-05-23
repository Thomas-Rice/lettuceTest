Feature: HorizonTool_Test
  The user wants to be able to move the horizon with ctrl/cmd + alt drag on the viewer.


  Scenario: HorizonTool layout drag
    Given Nuke is open with a C_CameraSolver setup
    When I double click on the C_CameraSolver
    And I double click on the Horizon Tool
    And I ctrl + alt drag on the viewer
    Then the viewer should move according to the mouse moves