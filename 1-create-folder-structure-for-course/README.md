## Folder and subfolder creation

## Brief description
Script able to create folders and subfolders based on a json file taken from a specific course on Coursera platform

## How to get this necessary json file
This json file needs to be pulled from Coursera's website once logged in the course:
- Go to the main menu for the course
- Right click in an empty space on the website and then select "Page source"
- Look for *window.App={*
    - Copy the entire line and paste it in a code editor
- Remove *window.App={* and the last character ( ";" ). Save the file. Name it *course1.json*, for example
- Run python script
- Your folder(s) should be created

> Note 1: Inside main.py file there is a list of files to be processed: Their filenames are *course1.json* and *course2.json*. Change them as needed

> Note 2: Each folder and subfolder contains a README.md file in order to be able to upload the entire structure to GitHub

## Example
An execution example is provided. See [output_example.txt](https://github.com/mvarrone/coursera-scripts/blob/master/1-create-folder-structure-for-course/output_example.txt) for more information
