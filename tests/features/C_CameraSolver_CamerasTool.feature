Feature: CamerasTool_Test
  The user wants to be able to move individual cameras in the C_CameraSolver.


  Scenario: Camera layout drag
    Given Nuke is open with a C_CameraSolver setup
    When I double click on the C_CameraSolver
    And I double click on the Cameras Tool
    And I ctrl + alt drag on the viewer
    Then the cameras selected should move according to the mouse moves