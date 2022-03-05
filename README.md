
## Features

* Main screen
    * campaign selector (default option new)
    * campaign label
    * start/end button (when pressed with no map selected, pop error message)
    * map select box (maps displayed in created order)
    * room select box
    * toggle game screen button
    * edit button (opens edit mode)
    * maximize game screen toggle button

### Edit screen
    * campaign Name label
    * campaign select box
    * map select box 
    * room select box
    * for each asset select box put two buttons below it for new and delete
    * button for exiting edit mode
    * toolbox (move map, add room boundary, subtract room boundary)
    * CRUD for rooms, maps, and campaigns. (right click to delete)

    * New Map Flow
        * Structure process for creating a new map and defining rooms. (Possibly a dedicated dialog box for this process.)
        1. Click new map.
        2. Select map image file from file system.
        3. opens up the game screen and displays the game map and calibration square with the calibration square in the top left corner and a slider that will scale the map  image up and down.
        4. User select 'Ok' when they're done and a scaled version of the map image is generated for the game to use going forward.
        5. User is directed back to room building screen (edit screen).

### Calibraton square
    This is visual reference tool to help DMs scale their maps so that each tile displays correct size. The maps needs to fit minis properly (the map is a physical game board).
    * 1 x 1 square displayed over top the map image
    * click and drag

### Game Screen
    * separate window to display map image.
    * control for this will be present in the main window.
    * borderless in full screen mode.
    * otherwise it is non interactible

## Fuctions

    * When a campaign is selected, you can click 'start' to to launch the game screen. 'End' to stop the stop the game screen (this can be a toggle). Once a campaign is selected then you can select maps and rooms.
    * When room is selected. The game screen will move the map so that the selected room is cetnered and update the mask so that all areas ouside of the room are obscured.
    * When a map is selected, the selected map will be displayed with no room selected. by default the whole map is obscured.



    
        