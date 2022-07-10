# Purple in Gold GUI for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DonRP/PG-GUI)
![License](https://img.shields.io/github/license/DonRP/PG-GUI)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>

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

![Main_menu](https://user-images.githubusercontent.com/67595890/178162718-3494db8e-b6f6-4ff4-b200-0e44e049ef68.jpg)

![Options](https://user-images.githubusercontent.com/67595890/178162725-559735e0-2177-4610-aeb3-3c3e8e4f8111.jpg)

![Options-Russian](https://user-images.githubusercontent.com/67595890/178162730-ab4a4a06-aed6-45d7-8cd0-43c8bdbd3805.jpg)

![Choice_menu](https://user-images.githubusercontent.com/67595890/178162734-3b72f2c4-3326-4ed1-b4b9-c7272e1bfd20.jpg)

![Save](https://user-images.githubusercontent.com/67595890/178162738-9eb6e2d8-700d-40eb-839e-aef047f1488f.jpg)

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
