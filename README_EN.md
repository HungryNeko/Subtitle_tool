A collection of Python tools for managing and processing subtitle files.

## Feature Overview
### Subtitle renaming — Automatically rename subtitle files to match the corresponding video filenames, so the player can load them automatically.

Usage

    Run renamefiles.py in the command line.
    
    Drag the folder containing videos and subtitle files into the terminal window.
    
    The script will automatically rename the subtitles (natural order) to match the corresponding video filenames (natural order).
    
    Example
    [vid1.mp4, vid2.mp4, sub1.ass, sub2.ass] 
    → [vid1.mp4, vid2.mp4, vid1.ass, vid2]
