# pagode

This is a tool for pair programming based on samba.

In the future you should be able to share a specific directory using samba, to
pair program in.

## reasoning

### why?

The usual workflow of passing the keyboard around frustrated me to no end,
because of differences in OS, IDE and even keyboard layout.

### why samba?

Every major OS (Linux, Mac OS and Windows) supports samba natively without the
necessity to install any software.
Therefore only the person sharing the code hast to install `pagode`.

## installation

Probably via pipx, but you can always just clone the repository and start it
from there.

## how it works

Run `pagode directory/to/share` in the terminal.
This will open a browser window pointing to a minimal web server on localhost.
On this website you will find a link, for the other person to open in a browser
window, to connect to your session.
It will also show a link, the other person can click to open the created samba
share in their file explorer.
With the button "take control"/"give control" write access to the directory can
be given or taken away, so that only one person can edit the code at a time.
