## Folder and subfolder creation

Script able to create folders and subfolders based on a json file from specific courses

Each folder and subfolder contains a README.md file in order to upload the entire structure to GitHub

This json file needs to be pulled from website once logged in:
- Go to the main menu for the course
- Right click in an empty space on the website and then select "page source"
- Look for *window.App={*
    - Copy the entire line and paste it in a code editor
- Remove *window.App={* and the last character ( ";" ). Save the file. Name it *course1.json*, for example

> Note: Inside main.py file there is a list of files to be processed: Names are course1.json and course2.json. Change as needed