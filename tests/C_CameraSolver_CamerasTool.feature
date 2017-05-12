Feature: CamerasTool_Test
  The user wants to be able to move individual cameras in the C_CameraSolver.


  Scenario: Camera layout drag
    Given Nuke is open with a C_CameraSolver setup and on cameras mode
    When I ctrl + alt drag on the viewer with camera 1 selected
    Then the cameras selected should move according to the mouse moves