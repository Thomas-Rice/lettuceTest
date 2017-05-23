Feature: SuperTool_Test
  The user wants to be able to add user matches.
  When adding sniper windows appear to show the cameras that are matches with the custom point.


  Scenario: SuperTool_Case_TEST
    Given Nuke is open with a C_CameraSolver setup
    When I ctrl + alt on the an overlapping section of the viewer
    And we ctrl + alt drag on the viewer
    And I ctrl + alt drag on the viewer with camera 1 selected
    Then the a user match should be added with sniper windows present in the top left