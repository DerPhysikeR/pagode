# pagode

This is a tool for pair programming based on samba.

Just run `pagode directory/to/share` in the terminal and a samba server will be
started, sharing your work with others over the network.

## reasoning

### why?

The usual workflow of passing the keyboard around frustrated me to no end,
because of differences in OS, IDE and even keyboard layout.

### why samba?

Every major OS (Linux, Mac OS and Windows) supports samba natively without the
necessity to install any software, therefore only the person sharing the code
has to install `pagode`.

## installation

Currently, you have to clone the code and run `poetry install` to create a
virtual environment and install all dependencies.

## plans for the future

 - [ ] make this package installable via pypi
 - [ ] share link to samba share using a minimal web server
 - [ ] add some kind of usermanagement for mob programming
