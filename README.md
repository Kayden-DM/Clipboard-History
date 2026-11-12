## Clipboard History Manager
A desktop clipboard history tracker built with CustomTkinter and pyperclip. It silently monitors your clipboard in the background, saves every new item to a JSON file, and displays them in a scrollable list where you can re-copy or delete entries with a single click.

## Features
Auto Monitoring — A daemon thread polls pyperclip.paste() every second and saves any new, non-duplicate content to the history.

Persistent Storage — History is stored in clipboard.json and reloaded on every launch, so nothing is lost between sessions.

One-Click Re-Copy — Each entry is a button; clicking it copies that item straight back to the system clipboard.

Individual Delete — An ✕ button on each row removes that specific entry and saves the updated list.

Clear All — A single button wipes the entire history and resets the status counter to zero.

Duplicate Guard — New clipboard content is only saved if it isn't already in the history, preventing repeated entries.

Truncated Preview — Long entries are trimmed to 50 characters in the UI, keeping rows compact while the full text is preserved in storage.

Dark Theme — CustomTkinter's dark appearance mode with the blue default color theme applied to all widgets.

Status Label — Shows a live count of saved items and confirms actions like "Copied".

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Window, scrollable frame, buttons, labels |
| `pyperclip` | Reads and writes the system clipboard |
| `json` | Serialises history to and from `clipboard.json` |
| `os` | Checks whether the history file exists before loading |
| `threading` | Runs the clipboard watcher loop in the background |
| `time` | Paces the watcher loop with a one-second sleep |
## How to Use It
Install Python 3.8 or newer from python.org and make sure it's added to your PATH.

Install the dependencies by running pip install customtkinter pyperclip.

Save the code as clipboard_history.py.

Open a terminal in the folder containing the file.

Run python clipboard_history.py.

Copy anything as you normally would — it appears at the top of the history list automatically. Click an item to copy it again, click ✕ to delete it, or press Clear All to wipe the history.

## Improvements
Add search/filtering — the list only grows; a search box would make finding an old entry much faster.

Add pinning or favourites — frequently used snippets could be pinned to the top so they aren't pushed down by new copies.

Add a configurable poll interval — the watcher is hardcoded to one second; exposing this would let users reduce CPU usage or catch faster copy bursts.

Allow custom storage location — clipboard.json is fixed to the script directory; a settings option would let users move it elsewhere.

Show full text on hover or click — rows are truncated to 50 characters with no way to preview the complete entry before copying it.

Cap the history size — there's no limit on stored items; a maximum length with automatic trimming would prevent unbounded growth.
