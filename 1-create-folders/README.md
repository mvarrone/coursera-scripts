## Folder and subfolder creation

Script able to create folders and subfolders based on a json file from specific courses

Each folder and subfolder contains a README.md file in order to upload the entire structure to GitHub

json file needs to be pulled from website once logged in:
    - Go to the main menu for the course
    - Right click in an empty space on the website and then go to "page source"
    - Look for "window.App={". Copy the entire line and paste it in a code editor
    - Remove "window.App={"" and the last character ( ";" ). Save file. Name it "course1.json", for example. Done