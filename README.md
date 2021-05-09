# Purple in Gold GUI for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DonRP/PG-GUI)
![License](https://img.shields.io/github/license/DonRP/PG-GUI)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>
<span class="badge-buymeacoffee">
<a href="https://www.buymeacoffee.com/p/59760" title="Donate to this project using Buy Me A Coffee"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg" alt="Buy Me A Coffee donate button" /></a>
</span>

This GUI is meant to have Visual Novel/Game developers who have little experience with Ren'py.
This repo is public to help and to give the opportunity to help me.

## Instructions to insert GUI in your repo 
I recommend the following ways to include it in your project:
- [**Pull branch**](https://github.com/DonRP/PG-GUI#pull-branch) (to **insert** it into your game and **update** it easily)
- **Fork** (to improve the repo or create a GUI based on mine)

### Pull branch
To **insert** or **update** the GUI in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **GUI-xxxxp**

##### Version 3840p

`git checkout GUI-3840p`

`git pull https://github.com/DonRP/PG-GUI.git GUI-only --allow-unrelated-histories`

At the end make a merge inside the arm of the project.

##### Version 1080p

`git checkout GUI-1080p`

`git pull https://github.com/DonRP/PG-GUI.git GUI-only-1080p --allow-unrelated-histories`

At the end make a merge inside the arm of the project.

##### Version 720p

`git checkout GUI-720p`

`git pull https://github.com/DonRP/PG-GUI.git GUI-only-720p --allow-unrelated-histories`

At the end make a merge inside the arm of the project.

## Images
![alt text](https://github.com/DonRP/PG-GUI/blob/master/images/Main_menu.webp "Main menu")

![alt text](https://github.com/DonRP/PG-GUI/blob/master/images/Options.webp "Options")

![alt text](https://github.com/DonRP/PG-GUI/blob/master/images/Options-Russian.webp "Options Russian")

![alt text](https://github.com/DonRP/PG-GUI/blob/master/images/Choice_menu.webp "Choice menu")

![alt text](https://github.com/DonRP/PG-GUI/blob/master/images/Save.webp "Save")

## Goals
- Create a complete, but minimal GUI
- Style: imaginative suitable for various uses
- Speed is intuitiveness
- Always updated to the latest version of Ren'py
- Compatible with various types of devices

## Additional tools
- Text bar transparency controls
- Choice of menu on the bottom side
- Languages menu
- Ambient sound (looped)
