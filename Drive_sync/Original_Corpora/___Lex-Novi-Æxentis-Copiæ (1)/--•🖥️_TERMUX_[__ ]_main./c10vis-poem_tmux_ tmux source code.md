---
title: "c10vis-poem_tmux_ tmux source code"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•🖥️_TERMUX_[__ ]_main./c10vis-poem_tmux_ tmux source code.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Watch
0
tmux source code
ISC License
Contributing
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from tmux/tmux
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is 682 commits behind tmux/tmux:master .
Contribute
Sync fork
ThomasAdam Merge branch 'obsd-master'
f07ac30 · last month
.github
github: update lock-threads to v6
last month
compat
Work around systemd killing panes ea…
4 months ago
fuzz
Add new fuzzers for command parsin…
4 months ago
logo
Icons, from someone on GitHub in iss…
5 years ago
presentations
Add a couple of presentations I wrote …
11 years ago
regress
Update copy mode vi test, from Max V…
last month
tools
Merge SIXEL branch.
3 years ago
.gitignore
Add .swp, from Nikola Tadic.
last year
.mailmap
mailcap: update entry for Thomas Ada…
5 months ago
.travis.yml
Add FreeBSD CI, from Jan Beich.
6 years ago
CHANGES
Add to CHANGES.
last month
COPYING
Make COPYING the same.
4 months ago
Makefile.am
Uninstall the man page too.
2 months ago
README
New bash completion URL, from David…
last year
README.ja
New bash completion URL, from David…
last year
SYNCING
portable: SYNCING: correct tmux-open…
last year
Merge branch 'obsd-master'
last year
c10vis-poem
tmux
Code
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Fork
0
T


alerts.c
arguments.c
Merge branch 'obsd-master'
2 years ago
attributes.c
Change noattr to be an explicit attribut…
8 months ago
autogen.sh
Bump automake and autoconf versions.
9 years ago
cfg.c
Merge branch 'obsd-master'
10 months ago
client.c
Merge branch 'obsd-master'
last year
cmd-attach-session.c
Tighten up read-only checks on attach…
2 months ago
cmd-bind-key.c
Fix documentation around optional ar…
last year
cmd-break-pane.c
Some more easy floating panes bits.
2 months ago
cmd-capture-pane.c
Add -H flag to capture-pane to show h…
last month
cmd-choose-tree.c
Add a -h flag to choose-tree and choo…
last month
cmd-command-prompt.c
Add -C flag to command-prompt to m…
3 months ago
cmd-confirm-before.c
Another memory leak, from Huihui Hu…
4 months ago
cmd-copy-mode.c
Fix scrollbar drag position when windo…
last month
cmd-detach-client.c
Tighten up read-only checks on attach…
2 months ago
cmd-display-menu.c
Merge branch 'obsd-master'
4 months ago
cmd-display-message.c
Free format on -a, reported by Huihui …
5 months ago
cmd-display-panes.c
Preserve the original text in the first lin…
last month
cmd-find-window.c
Only wrap pattern in *s if using a regul…
3 years ago
cmd-find.c
Merge branch 'obsd-master'
last month
cmd-if-shell.c
Do not leak on failure, GitHub 4565.
last year
cmd-join-pane.c
Merge branch 'obsd-master'
last month
cmd-kill-pane.c
Add a context for cell/palette/hyperlin…
last month
cmd-kill-server.c
Add args parsing callback for some fu…
5 years ago
cmd-kill-session.c
Add missing headers.
last month
cmd-kill-window.c
Add missing headers.
last month
cmd-list-buffers.c
Validate -O flags, from Dane Jensen in…
5 months ago
cmd-list-clients.c
Validate -O flags, from Dane Jensen in…
5 months ago
cmd-list-commands.c
Add sorting (-O flag) and a custom for…
5 months ago
cmd-list-keys.c
Make list-keys only use a message if -…
last month


cmd-list-panes.c
Add pane_x, y, z format variables and …
2 months ago
cmd-list-sessions.c
Validate -O flags, from Dane Jensen in…
5 months ago
cmd-list-windows.c
Validate -O flags, from Dane Jensen in…
5 months ago
cmd-load-buffer.c
Tweak error messages so that file na…
9 months ago
cmd-lock-server.c
Add args parsing callback for some fu…
5 years ago
cmd-move-window.c
Add args parsing callback for some fu…
5 years ago
cmd-new-session.c
Sanitize pane titles and window and s…
3 months ago
cmd-new-window.c
Fix documentation around optional ar…
last year
cmd-parse.y
Add a limit on maximum length of env…
3 months ago
cmd-paste-buffer.c
Merge branch 'obsd-master'
4 months ago
cmd-pipe-pane.c
Merge branch 'obsd-master'
3 months ago
cmd-queue.c
Merge branch 'obsd-master'
last year
cmd-refresh-client.c
Add a get-clipboard option which whe…
8 months ago
cmd-rename-session.c
Sanitize pane titles and window and s…
3 months ago
cmd-rename-window.c
Add args parsing callback for some fu…
5 years ago
cmd-resize-pane.c
Move the PANE_FLOATING flag into th…
last month
cmd-resize-window.c
Get rid of some warnings with GCC 10…
3 years ago
cmd-respawn-pane.c
Fix documentation around optional ar…
last year
cmd-respawn-window.c
Fix documentation around optional ar…
last year
cmd-rotate-window.c
Add args parsing callback for some fu…
5 years ago
cmd-run-shell.c
Allow run-shell arguments after a shell…
2 months ago
cmd-save-buffer.c
Merge branch 'obsd-master'
9 months ago
cmd-select-layout.c
Bring some new formats from the floa…
3 months ago
cmd-select-pane.c
Move the PANE_FLOATING flag into th…
last month
cmd-select-window.c
Add args parsing callback for some fu…
5 years ago
cmd-send-keys.c
tmux: tc can be NULL, so check before…
4 months ago
cmd-server-access.c
Use name as marker for failure not typ…
last month
cmd-set-buffer.c
Initialize bufname, reported by Mark K…
5 months ago
cmd-set-environment.c
Make some usages more consistent a…
last year


cmd-set-option.c
Validate command argument types (st…
5 years ago
cmd-show-environment.c
Make some usages more consistent a…
last year
cmd-show-messages.c
Merge branch 'obsd-master'
8 months ago
cmd-show-options.c
Merge branch 'obsd-master'
last year
cmd-show-prompt-history.c
Free history entries properly, from Hui…
5 months ago
cmd-source-file.c
Merge branch 'obsd-master'
8 months ago
cmd-split-window.c
Merge branch 'obsd-master'
last month
cmd-swap-pane.c
Do not allow swapping floating panes …
last month
cmd-swap-window.c
Preserve marked pane with swap-wind…
9 months ago
cmd-switch-client.c
Tighten up read-only checks on attach…
2 months ago
cmd-unbind-key.c
Add args parsing callback for some fu…
5 years ago
cmd-wait-for.c
Add args parsing callback for some fu…
5 years ago
cmd.c
Merge branch 'obsd-master'
2 months ago
colour.c
Improve code readability in colour_pal…
8 months ago
compat.h
Turn off regular expressions when fuz…
3 months ago
configure.ac
Add a configure flag for ASAN.
2 months ago
control-notify.c
Some more easy floating panes bits.
2 months ago
control.c
Merge branch 'obsd-master'
2 months ago
environ.c
Merge branch 'obsd-master'
5 months ago
example_tmux.conf
Use terminal-features instead of termi…
2 years ago
file.c
Merge branch 'obsd-master'
2 months ago
format-draw.c
Add some new mouse ranges called "…
3 months ago
format.c
Merge branch 'obsd-master'
last month
grid-reader.c
When mode-keys is set to vi, do not all…
2 months ago
grid-view.c
When history-limit is changed, apply to…
6 months ago
grid.c
Replace refresh-from-pane in copy mo…
last month
hyperlinks.c
Merge branch 'obsd-master'
2 years ago
image-sixel.c
Avoid overshooting Sixel height in sixe…
2 months ago
image.c
Track which list (images or saved_ima…
3 months ago


input-keys.c
Merge branch 'obsd-master'
4 months ago
input.c
Merge branch 'obsd-master'
2 months ago
job.c
Merge branch 'obsd-master'
10 months ago
key-bindings.c
Replace refresh-from-pane in copy mo…
last month
key-string.c
Reorganize structure of key_code so t…
4 months ago
layout-custom.c
Move the PANE_FLOATING flag into th…
last month
layout-set.c
Move the PANE_FLOATING flag into th…
last month
layout.c
Allow floating panes to be created par…
last month
log.c
Some style nits.
4 years ago
mdoc2man.awk
Generate tmux.1 using mdoc2man.aw…
13 years ago
menu.c
Add a context for cell/palette/hyperlin…
last month
mode-tree.c
Return immediately if the list is empty …
last month
names.c
Sanitize pane titles and window and s…
3 months ago
notify.c
Merge branch 'obsd-master'
3 months ago
options-table.c
Merge branch 'obsd-master'
last month
options.c
When history-limit is changed, apply to…
6 months ago
osdep-aix.c
The AIX functions hang on 7300-01-01…
last year
osdep-cygwin.c
Look for libevent2 differently from libe…
6 years ago
osdep-darwin.c
Use MAC_OS_X_VERSION_MIN_REQUI…
last year
osdep-dragonfly.c
Look for libevent2 differently from libe…
6 years ago
osdep-freebsd.c
Look for libevent2 differently from libe…
6 years ago
osdep-haiku.c
The AIX functions hang on 7300-01-01…
last year
osdep-hpux.c
Look for libevent2 differently from libe…
6 years ago
osdep-linux.c
Look for libevent2 differently from libe…
6 years ago
osdep-netbsd.c
Remove unnecessary declarations.
4 years ago
osdep-openbsd.c
Use PATH_MAX instead of MAXPATH…
4 years ago
osdep-sunos.c
Looks like evports on SunOS are broke…
5 years ago
osdep-unknown.c
Look for libevent2 differently from libe…
6 years ago
paste.c
Merge branch 'obsd-master'
3 months ago


popup.c
Merge branch 'obsd-master'
last month
proc.c
Merge branch 'obsd-master'
last month
regsub.c
Do not read off end of buffer if it ends …
3 months ago
resize.c
Fix clients_calculate_size for manual t…
5 months ago
screen-redraw.c
Merge branch 'obsd-master'
last month
screen-write.c
Merge branch 'obsd-master'
last month
screen.c
Merge branch 'obsd-master'
last month
server-acl.c
Allow ACLs to use groups as well as u…
last month
server-client.c
Merge branch 'obsd-master'
last month
server-fn.c
Merge branch 'obsd-master'
2 months ago
server.c
Merge branch 'obsd-master'
last month
session.c
Merge branch 'obsd-master'
3 months ago
sort.c
Add a Z sort order in tree mode.
last month
spawn.c
Merge branch 'obsd-master'
last month
status.c
Do not cache format for status line be…
2 months ago
style.c
Add some new mouse ranges called "…
3 months ago
tmux-protocol.h
If a pane is killed, cancel reading from …
4 years ago
tmux.1
Merge branch 'obsd-master'
last month
tmux.c
Merge branch 'obsd-master'
3 months ago
tmux.h
Merge branch 'obsd-master'
last month
tty-acs.c
Fix a couple of rounded border charac…
3 years ago
tty-draw.c
Add a context for cell/palette/hyperlin…
last month
tty-features.c
Merge branch 'obsd-master'
2 months ago
tty-keys.c
Increase escape delay if the buffer co…
2 months ago
tty-term.c
Merge branch 'obsd-master'
3 months ago
tty.c
Merge branch 'obsd-master'
last month
utf8-combined.c
Two fixes for RI codepoints. Firstly, do…
last month
utf8.c
Merge branch 'obsd-master'
2 months ago
window-buffer.c
Merge branch 'obsd-master'
4 months ago


window-client.c
Add a -h flag to choose-tree and choo…
last month
window-clock.c
Merge branch 'obsd-master'
3 months ago
window-copy.c
Replace refresh-from-pane in copy mo…
last month
window-customize.c
Add a short builtin help text for each …
4 months ago
window-tree.c
Merge branch 'obsd-master'
last month
window.c
Merge branch 'obsd-master'
last month
xmalloc.c
Add xrecallocarray.
7 years ago
xmalloc.h
Merge branch 'obsd-master' into master
5 years ago
tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a
single screen. tmux may be detached from a screen and continue running in the background, then later reattached.
This release runs on OpenBSD, FreeBSD, NetBSD, Linux, macOS and Solaris.
tmux depends on libevent 2.x, available from this page.
It also depends on ncurses, available from this page.
To build tmux, a C compiler (for example gcc or clang), make, pkg-config and a suitable yacc (yacc or bison) are
needed.
Some platforms provide binary packages for tmux, although these are sometimes out of date. Examples are listed
on this page.
To build and install tmux from a release tarball, use:
tmux can use the utempter library to update utmp(5), if it is installed - run configure with --enable-utempter to
enable this.
Welcome to tmux!
Dependencies
Installation
Binary packages
From release tarball
./configure && make
sudo make install
README
Contributing
License


For more detailed instructions on building and installing tmux, see this page.
To get and build the latest from version control - note that this requires autoconf , automake and pkg-config :
Bug reports, feature suggestions and especially code contributions are most welcome. Please send by email to:
tmux-users@googlegroups.com
Or open a GitHub issue or pull request. Please read this document before opening an issue.
There is a list of suggestions for contributions. Please feel free to ask on the mailing list if you're thinking of
working on something or need further information.
For documentation on using tmux, see the tmux.1 manpage. View it from the source tree with:
A small example configuration is in example_tmux.conf .
And a bash(1) completion file at:
https://github.com/scop/bash-completion/blob/main/completions-core/tmux.bash
For debugging, run tmux with -v or -vv to generate server and client log files in the current directory.
The tmux mailing list for general discussion and bug reports is:
https://groups.google.com/forum/#!forum/tmux-users
Subscribe by sending an email to:
tmux-users+subscribe@googlegroups.com
Releases
No releases published
From version control
git clone https://github.com/tmux/tmux.git
cd tmux
sh autogen.sh
./configure && make
Contributing
Documentation
nroff -mdoc tmux.1|less
Support


Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
C 87.3%
Roff 7.2%
Shell 2.8%
Yacc 1.3%
M4 0.8%
Awk 0.3%
Other 0.3%
Suggested workflows
Based on your tech stack
C/C++ with Make
Build and test a C/C++ project using Make.
By GitHub Actions
Configure
CMake based, single-platform projects
Build and test a CMake based project on a single-platform.
By GitHub Actions
Configure
MSBuild based projects
Build a MSBuild based project.
By GitHub Actions
Configure
More workflows
