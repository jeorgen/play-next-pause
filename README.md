play-next-pause
===============

A simple remote control that should be able to play, pause, stop and skip on DNLA/UPnP devices it finds on the subnet. Tested on Ubuntu &amp; WinXP

play-next-pause

play-next-pause is a very simple remote control application that can stop, pause, resume, play and skip on a UPnP/DLNA-compliant media player, at least if the Media Player is Rhythmbox with the UPnP/DLNA plugin enabled. The source code is currently around 55 lines of code. It is very much in alpha status and has been developed just to the "works for me" point.

[screenshot](https://raw.github.com/jeorgen/play-next-pause/master/docsfiles/Sc_ubuntu.png)

play-next-pause on Ubuntu 9.10


No other player than Rhythmbox tested at this moment. play-next-pause should be able to detect several media players on the network if there are several, and open a remote control for each one.

The personal goal with play-next-pause from the author's side is for it to be a way of controlling a central media player from any computer or operating system I happen to be on at the moment on the subnet. Currently this is instead solved by using the Music Player Daemon (mpd) as as server and Ario clients on the various Linux and Win32 machines.

[screenshot](https://raw.github.com/jeorgen/play-next-pause/master/docsfiles/Sc_win.png)

play-next-pause on Windows XP Home


KNOWN BUGS

Remotes do not close when the corresponding media player disappears from the net.


LINUX AND WINDOWS BINARIES

This is the first time the author ever tries to build python binaries. It is a learning experience :-) The binaries can be downloaded here.
https://sourceforge.net/projects/play-next-pause/files/

LINUX BINARIES

The Linux binary is one file made with Pyinstaller. It runs on my Ubuntu 9.10, and should hopefully run on Linux desktops with glibc 2.8 or newer. On Ubuntu that seems to be 8.10 and onwards. CentOS 5 does not work. Pyinstaller builds it with glibc 2.5 from CentOS 5 (I think) but something in there seems to want 2.8.

The single file release unpacks in and uses files from the /tmp directory. If you are running SELINUX or has mounted /tmp with noexec, the single file binary distribution will not work. There is now a multi file binary soon that has been tested on Ubuntu 9.10 with /tmp mounted with noexec.

WINDOWS BINARY

The Windows binary is a slew of files in a directory and has been made with Py2exe. It has been tested to run on a netbook with Windows XP home. It outputs error messages now and again and sometimes does not start. It needs some care and attention. There seems to be around 50MB of doc and similar files in there that could safely be removed.

CREDITS

play-pause-next is currently around 55 lines of code. This is thanks to the fantastic Coherence framework behind it and the GTK GUI framework.

UPnP Inspector from Coherence is a great tool for seeing what devices are on your subnet and what capabilities they have. If you are running Linux, check the repositories of your distribution for it, or if you are a pythonista, use easy_install to install it.

Update: I just realised that in UPnP Inspector you can right click the devices in the tree, and you get a remote control for that device! Not only that, but you can drag songs from a media server to a media renderer and it plays the song. Amazing. It may nullify the need for the remote play-next-pause for many use cases.
