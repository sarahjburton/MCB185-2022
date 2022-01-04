GUMPy
=====

Author: Ian Korf

## Introduction ##

GUMPy is a quick introduction to the tools of the trade for the emerging
bioinformatics programmer: GitHub, Unix, Markdown, and Python. Most of this
document is about Unix. Most of the accompanying coursework is Python.

Here's the overall path through the document

1. Get a GitHub account, create and fork repos
2. Install Unix/Linux
3. Learn some basics of the Unix/Linux command line
4. Learn about files and Markdown formatting
5. Interact with GitHub using the CLI
6. Create your first Python program
7. Learn about file permissions and paths

------------------------------------------------------------------------------

## GitHub Account ##

If you want people to believe you're a programmer, you have to act like one.
That starts with you having a GitHub account. Your repositories and activity
are part of your CV. If you don't have a GitHub account, it's time to point
your web browser to [https://github.com](GitHub) and create your account.

Choose a username. It's okay to be clever, but don't be silly. Remember, this
will be part of your CV. I use my full name. After setting your email and
password, choose the free plan and then answer a few questions about your
interests to create your account. Go to your email to verify your email
address.

### Create a Repository ###

It's time to create your first repository, which we often shorten to _repo_.
Before we begin, we need to talk a little about ownership, privacy, and
security.

When you create a repo, you own it. You can read it, write to it, or even
delete it. Later, you can invite collaborators who can join you in your
efforts, but by default, only you can make edits.

When a repo is created, it can be either _Public_ or _Private_. A Public
repository allows other people to download a copy of your repo. This is called
_cloning_. There is no security risk in cloning a Public repository (unless you
put sensitive info in there). If people modify their clones, it does not affect
your files. If you invite them as collaborators and give them write permission,
they can modify the files in your repo.

A Private repository is invisible to everyone but you. You can add
collaborators to Public or Private repos and specify what kinds of permissions
each collaborator may have. As the owner, you can change a repo from Public to
Private and back.

Now let's go make a repo. Go to the GitHub website and click on the green "New"
button to create a new repo. Name this _homework_ because this is where you'll
be submitting your homework. You can make this Public or Private as you like.
If you make it Private, you'll need to do some extra steps later to give your
instructor and TA permission to view your files. Click the boxes to initialize
with a README, add a .gitignore and add a license. Scroll through the
.gitignore options until you get to "Python". Choose whichever license you
like. I generally use MIT. Click the "Create Repository" and you will be
transported to your new mostly empty repo.

If you made your repo Private, you need to give your instructors permission to
view your repo. Go to the "Settings" link in your repo and then click on
"Manage access" on the left. Click on the green "Add People" button to add your
instructor and TA (you'll have to ask them for their GitHub handles).

### Forking a Repository ###

The next step is to fork the MCB185-2022 repo. Point your browser to
https://github.com/iankorf/MCB185-2022 and
then click on the "Fork" button in the upper left.

A _fork_ is different from a _clone_. When a person clones a repo, they do not
_own_ the repo. As such, they cannot make permanent changes to it. When a
person forks a repo, they own a copy of that. Meaning that they can make
permanent changes to their copy (but not yours). Here's a biological analogy. A
fork is like mitosis. After forking/mitosis, each cell is independent. Changes
made to one cell have no effect on the other. When cloning, everyone is working
on the same cell. Changes made in a clone go back to the original cell (but
again, only if they have permission). If you make changes to a clone when you
don't have permission, I guess that's a bit like editing an RNA: it doesn't
affect the genome. OK, it's not a great analogy.

You need to fork the MCB185-2022 repo because you'll want to be able to edit
some of the files inside. I need to clone your homework repo so I can see your
files (I don't need to edit your files).

------------------------------------------------------------------------------

## Unix/Linux Environment ##

Most professional bioinformatics is done in a Unix/Linux environment. You don't
have to love Unix/Linux, but you do have to be good at it.

### What's the deal with Unix vs. Linux? ###

Most people about to embark on an adventure in bioinformatics programming will
be using some flavor of Linux (e.g. Debian, Fedora, LinuxLite, Mint, Ubuntu,
etc.) and not actually Unix. Is there a difference between Linux and Unix?
Practically, no, but philisophically, yes. Linux was designed to behave just
like Unix, so they are supposed to be very similar. However, Unix has its roots
as a commercial product and Linux has its roots in open source free software.
In this document, the terms _Linux_ and _Unix_ are used somewhat
interchangeably.

### Where do I get Linux? ###

Before we begin, you need a command line Linux environment on your computer.
Why a CLI (command line interface) rather than a GUI (graphical user
interface)? When it comes to automating tasks, it's easier to automate text
commands than mouse clicks. Also, most computer clusters run Linux because it's
free and robust. For these reasons, most professional bioinformatics is done
with a Linux CLI. If you have any aspirations of becoming a bioinformatics
programmer, you need to become comfortable with the Linux CLI. But before we
get to that, you need Linux.

### Unix on Mac ###

If your computer is a Mac, you already have Unix installed, and your specific
flavor of Unix is called Darwin. You can get to the CLI with the _Terminal_
application. However, you might not have `git` and other developer tools
installed by default. To install these, type the following in your terminal:

	xcode-select --install

This will bring up a dialog box that will prompt you through the install. You
may want to install other Linux CLI software. For this, there is the
[https://brew.sh](Homebrew) project. This works similarly to other Linux
package managers. To install homebrew, type the following in your termins:

	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

In addition to the Mac's built-in Unix, you may like to run a Linux virtual
machine because compatibility is always best in Linux. See the Virtual Machine
section below for more information.

### Linux on PC ###

If your computer is a PC currently running Windows, you will have to install
Linux _somehow_ and you have several choices. Each of these has advantages and
disadvantages, which are described in more detail below.

+ Virtual machine - recommended
+ Install Linux on a PC - best if you have a spare PC
+ Windows Subsystem for Linux - official Microsoft solution
+ Cygwin - may be useful for advanced users
+ Git bash - may be useful for advanced users

### Virtual Machine ###

This is the current recommendation for Linux on a Windows computer.

A virtual machine (VM) is a _fictional_ computer running inside your normal
Windows operating system. The virtualization _host_ software (e.g. VirtualBox)
running on Windows tricks the new _guest_ operating system (Linux) into
thinking it is attached to its own motherboard, CPU, keyboard, mouse, monitor,
etc.

The upside of virtualization is that it's safe and inexpensive. It's hard to
destroy data on your computer and you don't have to buy any new hardware.
VirtualBox is free software that works very well. Other popular virtualization
products include VMware and Parallels. If you want commercial support, you may
like those.

The downside of a VM is that your virtual machines will take up some RAM, CPU,
and storage. RAM is the most critical resource because it isn't easily shared.
If you have 8 GB RAM, you could set up your VM with half. But that means both
your real and virtual machines are running on 4 GB each. Computers run more
efficiently with more RAM, especially if you're the type of person to have 20
browser tabs open. Adding more RAM to your computer will improve your VM
experience. You can also run a VM with less RAM if you use a lightweight Linux
distribution like Lubuntu or LinuxLite.

On the CPU side, your programs running in a VM will run slower than they could.
The difference is pretty negligible though. We're talking 1-10% slower. You
will also have to dedicate about 5-10 GB of hard disk space. Even with the
downsides, VMs are a great way to run Linux on your PC.

There are many distributions of Linux. The most obvious differences among them
is the desktop Graphical User Interface (GUI). Some look like old-school
Windows while others look like Mac OS, and still others offer their own unique
look and feel. As bioinformatics programmers, we're more interested in the CLI
than the GUI, so I don't concern myself too much with what the desktop looks
like. Here are some recommendations for setting up your VM.

+ Linux: Lubuntu
+ VM Memory: 2 GB
+ Disk: use default types, 40G variable size

Make sure you read the installation directions fully. There are some
post-install customizations you might need to do. On VirtualBox these include:

+ Install the Guest Additions "CD"
+ Switch the virtual video card if you can't resize the screen
+ Set up a shared folder if you want Linux and Windows to share files

If you're having problems with the install or post-install, ask help from the
instructor or TA.

### Install Linux on PC ###

This is the best way to run Linux, but it may change your PC permanently.

There are a variety of ways you can install Linux on a hard disk. This could be
an external hard disk you plug in when you want to run Linux (e.g. a flash
drive), or you can split your current hard disk into multiple partitions, or
you can wipe Windows and install Linux instead. All of these methods will give
you Linux with all of the RAM and CPU. Each one is slightly destructive,
however, and you may accidentally wipe your Windows partition even if you
didn't intend to. For these reasons, if you only have 1 computer, I don't
recommend installing Linux directly. Use VirtualBox, WSL, or Cygwin instead.
However if you do have a spare computer, installing Linux will give you that
fully immersive experience that helps you learn Linux faster.

You can sometimes pick up old PCs for $50. Old Macs make great Linux boxes. I
have a 2015 iMac and 2012 Mac Mini that are too old to work with the current
MacOS, but both continue to work flawlessly as Linux machines.

### Windows Subsystem for Linux ###

The official Microsoft solution for running Linux is called the Windows
Subsystem for Linux (WSL). There are two types of WSL, Type 1 and Type 2. Type
1 is older. It is also compatible with virtual machines like VirtualBox. If you
want to run both WSL and VBox on the same machine, you should use WSL Type 1.

If you want to be more up-to-date, then use WSL Type 2. Unfortunately,
installing WSL2 will stop VirtualBox from running. You can have WSL2 and VBox
on the same computer, but not running at the same time; you will have to edit
some settings and restart to switch between the two. This is a pain, so don't
do it.

The upside of WSL is that it is the official Microsoft product. Most of the
time it works great. It uses less resources than a VM, so your actual and
virtual computers will be faster with WSL. The downside of WSL is the Windows
and Linux filesystems do not play well together. When Windows programs save
files in the Linux filesystem, some permissions may get reset (meaning you
can't read or write files until until you `chmod`). It can be annoying. As WSL
matures, it may become the best way to run Linux on Windows, but as of now I
don't recommend it.

From WSL, your Windows C drive is conveniently mounted at `/mnt/c`. Finding
your Linux filesystem root from Windows is not so easy.

### Cygwin on Windows ###

Cygwin is a terminal with Unix commands. In use, it feels similar to WSL.

Cygwin is not an entire operating system but rather a terminal with POSIX
commands (POSIX is a standard for portable Unix). It does not come
pre-installed with Python, so you will have to run the Cygwin `Setup.exe` to
install it and possibly other programming tools. For basic Python programming,
I've found Cygwin to work great. However, when I tried to do a `pip3 install
numpy` it did not work out of the box. If you have a lot of previous Unix
experience and don't mind troubleshooting software installs, Cygwin can be
great. If you're more of a novice, use something else.

Your Windows C drive is mounted at `/cygdrive/c`. Your Cygwin root depends on
where you chose to install it (probably `C:\cygdrive`).

### Git Bash on Windows ###

Git Bash is another terminal with Unix commands.

Git Bash is software intended for running git commands on Windows PCs using a
command line interface. It can be used for more tasks, such as Python
programming. Some programming languages are built-in (e.g. Perl) but Python is
not by default. Git Bash feels very similar to Cygwin but software installation
is slightly more complex. Like Cygwin, experts may like Git Bash, but it's not
for novices.

### Remote Login ###

Another way to work with Linux is to use your computer as a terminal to another
computer located somewhere on the Internet. This might be part of a larger
cloud computing service (e.g. Google, Amazon, etc.) or a computer located at
your school. The downside here is that you'll need a network connection.

### Raspberry Pi ###

The Raspberry Pi is an inexpensive ($50-100) single board computer that is
about the size of a deck of cards. You can also get one built into a slim
keyboard. They use Linux as their OS. You just need to provide a mouse and
monitor. They work great as a learning platform, but can be limiting as some
useful bioinformatics software isn't compiled for the Pi.

### Linux on Chromebook ###

Chromebooks are some of the least expensive computers you can buy.
Conveniently, Linux is built right in. Select the time from the lower right
corner and then go to Settings->Advanced->Developers.

Scroll down to "Linux development environment" and turn it on. It takes a few
minutes to install. To get to the Linux CLI, use the Terminal application. This
takes a little while to launch the first time.

I don't really recommend Chromebooks because it's not a popular platform for
professional bioinformatics work. However, if that's all you have, it will work
fine for this course.

### Linux on Tablet ###

I don't have any experience with Linux on tablets. I've seen it done, and it
seems to work okay, but I expect there will be some issues with precompiled
binaries as there are with the other cellphone-chip-based solutions (Pi,
Chromebook).

------------------------------------------------------------------------------

## Terminal, Command Line, and Shell ##

To interact with Linux at the CLI you use a _terminal_ application. There are
many flavors of terminals, each with its own name. Most of them have the word
'term' in them somewhere. For example, `xterm`, `qterm`, or just `Terminal`.

Once you launch a terminal application, you are presented with a command prompt
where you type _stuff_. This environment is actually called a _shell_. There
are several flavors of shell, each one generally has 'sh' in the name. Examples
include `sh`, `bash`, `csh`, `ksh`, `tcsh`, and `zsh`.

Are you confused by terminals and shells? That would be normal. Let's have an
analogy to clear this up.

A _terminal_ is like a _word processor_. The default applications on Mac and
Windows are Pages and Word. But just because those are the defaults, doesn't
mean you can't install Open Office.

The terminal gives you access to the _shell_. Here is another place you have a
choice. Whatever form of Unix you're using will have a default shell. That may
be `bash` or `zsh` but you can switch from one to another easily. This is sort
of like changing the language preferences in your word processor from US
English to UK English. Some of the spellings and punctuation change, but there
are more similarities than differences.

### Terminal Basics ###

Launch the terminal application (the name of this will differ from one
operating system to another and even within a particular OS you will have
several options). Run the `date` command by typing in the terminal and ending
with the _return_ key.

	date

Congratulations, you just made your first Unix statement. You type words on the
command line (in this case just one) and then hit return to execute the
command. `date` is but one of many Unix commands you have at your fingertips
(literally). Like most Unix commands, `date` does more than simply output the
current date in the format you just witnessed. You can choose any number of
formats and even set the internal clock to a specific time. Let's explore this
a tiny bit. Commands can take _arguments_. Let's tell the `date` program that
we want the date to be formatted as year-month-day and with
hours-minutes-seconds also. The syntax below will seem arcane, but the various
abbreviations should be make sense. Type the command below and observe the
output.

	date "+%Y-%m-%d %H:%M:%S"

### Manual Pages ###

If you want to learn more information about what `date` can do, you can either
look online or use the Unix built-in manual pages. For a quick refresher on a
command, the manual pages are often easiest. But if you have no idea what the
command does, than you might want to look for assistance online where you might
find questions, answers, and examples. To read the manual pages for `date` you
use the `man` command.

	man date

You can page through this with the space bar and exit with `q`. In the above
statement, `man` was the command and `date` was the argument. The program that
let you page through the documentation was another Unix command that you didn't
intentionally invoke, it just happens automatically when you execute the `man`
command.

### Injury Prevention ###

Typing is bad for your health. Seriously, if you type all day, you will end up
with a repetitive stress injury. Don't type for hours at a time. Make sure you
schedule breaks. Unix has several ways to save your fingers. Let's go back and
run the `date` program again. Instead of typing it in, use the _up arrow_ on
your keyboard to go backwards through your command history. If you scroll back
too far, you can use the _down arrow_ to move forward through your history
(but not into the future, Unix isn't that smart).

	date "+%Y-%m-%d %H:%M:%S"

You can use the _left arrow_ and _right arrow_ to position the cursor so you
can edit the text on the command line.

To see your entire history of commands in this session, use the `history`
command.

	history

Probably the most important finger saver in Unix is **tab completion**. When
you hit the tab key, the shell completes the rest of the word for you if it can
guess what you want next. For example, instead of typing out `history` you can
instead type `his` followed by the tab key, the rest of the word will be
completed. If you use something less specific, you can hit the tab key a second
time and the shell will show you the various legal words. Try typing `h` and
then the tab key twice. Those are all the commands that begin with the letter
h. You should use tab completion constantly. Not only does it save you key
presses and time, it also ensures that your spelling is correct. Try
misspelling the `history` command to observe the error it reports.

	historie

### Variables ###

The shell defines various variables which are called _shell variables_ or
_environment variables_. For example, the `USER` variable contains your user
name. You can examine the contents of a variable with the `printenv` command.

	printenv USER

Another way to print the contents of an environment variable is to use the
`echo` command to dereference the `$USER` variable.

	echo Hello $USER, your shell is $SHELL

We won't use variables much, but it's important to know they exist because some
programs use them for configuration. If you want to see all your environment
variables, you can use the `printenv` command without any arguments.

	printenv

Don't worry if you find the topic of environment variables to be a little
confusing at this time. We will revisit the topic a little later when it
matters more.

### Setting Up Your Workspace ###

Depending on the specific flavor of your operating system, you may have various
folders in your home directory. For example, Mac, Windows, and Linux generally
have _Desktop_, _Documents_,  and _Downloads_ folders. These are default
locations for your point-n-click files. Let's set up a folder to do our
programming and bioinformatics work. Open a terminal and type the following
command.

	cd

The `cd` command is used to "change directory". If you don't give it any
specific place to go, it will take you to your home directory. There are two
other ways to get to your home directory: _tilde_ and `$HOME`. Both of these
commands do the same thing.

	cd ~
	cd $HOME

To examine the exact path to your home directory, use the `pwd` command, which
stands for "print working directory".

	pwd

To see the other files in your home directory, type the `ls` command.

	ls

You should see your Documents, Downloads, and other folders created by default
by the operating system. Now it's time to create a new working directory for
all of your bioinformatics programming stuff. Let's call it _Work_.

	mkdir Work

Note that all of the directories given to you by default were a single word
starting with a capital letter (e.g. Downloads). We followed this convention
when we chose _Work_. However, the typical Unix world is all lowercase. So once
we enter the Work directory, we'll follow Unix standards and go all lowercase.
Let's make another directory inside the _Work_ directory called _bin_. Then
`cd` to _Work_ and have a look around with the `ls` command.

	mkdir Work/bin
	cd Work
	ls

You should see _bin_ and nothing else. Let's create another directory in here
called _lib_.

	mkdir lib
	ls

Now you should see two things, _bin_ and _lib_. We won't be using these
directories right away, but we will be using them soon.

### Creating and Viewing Files ###

(For the this exercise and others that follow, it may be useful to have your
graphical desktop displaying the contents of your Work directory. That way you
can see that typing and clicking are related. You won't actually be using the
mouse though.)

There are a number of ways to create a file. The `touch` command will create a
file or change its modification time (Unix records when the last time a file
was edited) if it already exists. Let's first make sure we are in our Work
directory. Here you can see why we use the tilde to represent our home
directory: it saves typing.

	cd ~/Work
	touch foo

The file `foo` doesn't contain anything at all. It is completely empty. If your
graphical file browser was open to your Work directory, when you typed you
would have seen the file magically appear in the file browser. Now lets create
a file with some content in it.

	ls /bin > bar

This command listed the `/bin` directory and **redirected** the output to a
file named `bar`. The greater-than sign allows you to send a stream of
characters to a file. Those characters can be streamed from the `ls` command as
was done here, or you could type them at the keyboard. Let's try putting some
content into `foo` with the keyboard.

	cat > foo

After you type the line above, the shell appears to hang. It's waiting for you
to start typing. Go ahead and write a few lines of poetry. To close the stream
of data and save the file, type ^D. What the heck is ^D? In Unix parlance, that
means hit the _control_ key followed by the _d_ key. This is sometimes written
as control-D. Note that even though ^D and control-D have a capital D in them,
you don't actually use the shift key. So go ahead and type ^D.

The most useful ways to view a file are with `head`, `tail`, `more`, and
`less`. `head` shows you the first 10 lines of a file, while `tail` shows you
the last 10. Of course there are command line options to change the number of
lines. Let's try them out.

	head foo
	tail foo
	head -5 bar
	tail -5 bar

If you want to view a whole file you can do that with `cat` or `less`. We just
saw how `cat` could be used to create a file, but it can also be used to view
them.

	cat bar

This isn't very useful for viewing large files unless you're a speed reader. A
more useful way to look at files is with a _pager_. The `more` and `less`
commands let you see a file one terminal page at a time. This is what you used
before when viewing the manual page for the `date` command. Use the spacebar to
advance by one page, the _b_ key to go backwards by one page, and when you're
done, hit _q_ to quit. `more` and `less` do more or less the same thing, but
oddly enough `less` does more than `more`. There are a lot of silly jokes in
Unix culture.

	less bar

### Editing Files ###

Let's try editing a file with `nano`, which is a terminal-based editor.

	nano foo

This changes the entire look of your terminal. No longer are you typing
commands at a prompt. Now you're editing a file and can change the random text
you just wrote. Use the arrow keys to move the cursor around. Add some text by
typing. Remove some text with the delete key. At the bottom, you can see a menu
that uses control keys. To save the file you hit the ^O key (control and then
the letter o). You will then be prompted for the file name, at which point you
can overwrite the current file (bar) or make a new file with a different name.
To exit nano, hit ^X. Note, you don't need to give nano a file name when you
start it up.

Unix file names often have the following properties:

* all lowercase letters
* no spaces in the name (use underscores or dashes instead)
* an extension such as .txt

### Navigating Directories ###

Whenever you are using a terminal, the shell's command line is focused on a
particular directory. The files you just created above were in a specific
directory (~/Work). To determine what directory you are currently in, use the
`pwd` command (print working directory). Let's make sure you're in your home
directory and examine its path.

	cd
	pwd

Your home directory should be listed below based on your operating
system.

* MacOS -  `/Users/your_name`
* Ubuntu - `/home/your_name`
* Lubuntu - `/home/your_name`
* WSL - `/home/your_name`

A path that begins with a `/` is called an _absolute path_ (we saw this before
when we did `ls /bin`). Your location also has a _relative path_, which is
simply the dot `.` character. Your full name is like an absolute path while
pronouns are like a relative path. So "Ian Frederick Korf" describes the author
absolutely, while "me" describes me more relatively. If I want to reference
other people, I can use an absolute or relative path. "Mario Takechi Korf"
describes my brother in absolute terms while "twin brother" describes him in
relative terms.

If you want to know what files are in your home directory, you can do that with
an absolute path regardless of where your shell is currently focused. You can
type out the path you found above, or you can dereference the `HOME`
environment variable.

	echo $HOME
	ls $HOME

You can also list your home directory using a relative path. Read the dot as
"here" so the following command is "list here".

	ls .

`ls` will list your current directory if you don't give it an argument, so an
equivalent statement is simply:

	ls

Notice that `ls` reports both the files and directories in your current
directory. Without icons it's a little difficult to figure out which names
correspond to file and which to directories. So let's add a command line option
to the `ls` command that will decorate directories with a special character.

	ls -F

This command adds a character to the end of the file names to indicate what
kind of files they are. A forward slash character indicates that the file is a
directory. These directories inside your working directory are called
_sub-directories_. They are **below** your current location. There are also
directories **above** your current focus. There is at most one directory
immediately above you. We call this the **parent** directory, which in Unix is
called `..` (that wasn't a typo, it's two dots). You can list your parent
directory as follows:

	ls ..

The `ls` command has a lot of options. Try reading the `man` pages and trying
some of them out. Now is a good time to experiment with a few command line
options. Note that you can specify them in any order and collapse them if they
don't take arguments (some options have arguments).

	man ls
	ls -a
	ls -l
	ls -l -a
	ls -a -l
	ls -la
	ls -al

There are two ways to specify a directory: _relative_ path and _absolute_ path.
The command `ls ..` listed the directory above the current directory. The
command `nano bar` edited the file `bar` in the current directory. You could
also have written `nano ./bar`. What if you want to list some directory
somewhere else or edit a file somewhere else? We actually did that before with
`ls /bin > foo`. To specify the absolute path, you precede the path with a
forward slash. For example, to list the absolute root of the Unix file system,
you would type the following:

	ls /

To list the contents of /usr/bin you would do the following:

	ls /usr/bin

This works exactly the same from whatever your current working directory is
because `/usr/bin` is an absolute path. However, if you do `ls bin` it only
works if you happen to have a directory or file called `bin` in your current
focus.

To change your working directory, use the `cd` command. Try changing to the root
directory

	cd /
	pwd
	ls

Now return to your home directory by executing `cd` without any arguments.

	cd
	pwd
	ls

Now go back to the root directory and create a file in your Work directory.
That is, your shell will have its focus on the root directory, but the files
you create will be in your Work directory. Open your GUI file browser to your
Work directory before you begin these commands.

	cd /
	touch $HOME/Work/file1
	touch ~/Work/file2
	ls ~/Work

### Moving and Renaming Files ###

Your home directory is starting to fill up with a bunch of crap. Let's organize
that stuff. First off, let's create a new directory for `stuff` using the
`mkdir` command.

	cd ~/Work
	mkdir stuff

Let's move some files into that new directory with the `mv` (move) command.

	mv foo stuff

The file `foo` is now inside the directory `stuff`. You can observe this by
listing the current directory, which no longer contains `foo`, and `stuff`,
where it now resides.

	ls .
	ls stuff

The weird thing about the `mv` command is that it not only moves files into
directories, it can also rename them. Let's try renaming `bar` to `bark`.

	mv bar bark

The difference between `mv foo stuff` and `mv bar bark` is that in the former
case there was a directory called `stuff` and in the latter there wasn't. This
is the key to `mv` command. If the last argument exists, it tries moving the
first argument (the file) into the last argument (the directory). What if you
try moving a file onto an already existing file? Let's do that with the
previously created `file` and `file2`.

	mv file1 file2
	ls .

Whoops. `file1` just got renamed to `file2`. In other words, the contents of
`file2` just got permanently deleted. For this reason, sometimes people use the
`-i` flag to turn on interactive mode. Let's recreate the previous files and
try this again.

	touch file1 file2
	ls
	mv -i file1 file2

Now you get a warning before doing any destructive activities!

`mv` can move and rename a file at the same time. Let's put `bark` into the
`stuff` directory and change its name back to `bar`.

	mv bark stuff/bar
	ls stuff

`mv` can move multiple things at the same time. Let's move both `file1` and
`file2` into the `stuff` directory.

	mv file1 file2 stuff
	ls stuff

### Wildcards ###

One of the most useful time-saving tricks in the shell is the use of the `*`
character as a wildcard. The `*` character matches missing characters if it
can. If we want to list the files in `stuff` that start with the letter _f_ we
do the following:

	ls stuff/f*

A very common use of the wildcard is to match all files with a specific file
extension. Let's try that.

	touch a.txt b.txt
	ls *.txt
	mv *.txt stuff

### Copying and Aliasing ###

The `cp` command copies files. Let's say you wanted to make a copy of `bar`
which is currently in your Work directory. You have to tell `cp` where you want
that copy to exist. It can't exist in the exact same location. You'll either
have to give it a different location or change its name. Let's first try giving
it a new location.

	cp stuff/bar .

The previous command reads as "copy the bar file from the stuff directory to my
current location". We could also copy the file without changing its location,
but we have to give it a new name.

	cp stuff/bar stuff/bark
	ls stuff

### Deleting Files ###

You delete files with the `rm` command. Be careful, because once gone, files
are gone forever. If you want a safer, interactive version of `rm` use it with
the `-i` flag (we saw this earlier with `mv`).

	ls stuff
	rm stuff/file1
	ls stuff
	rm -i bar

As a reminder, you didn't type those file names completely, right? You used tab
completion, right?

You can delete multiple files at once too and even whole directories. Watch out
though, that can get dangerous. If you want to completely remove everything in
the `stuff` directory, you _could_ do the following (but please don't):

	rm stuff/*

That will still leave the `stuff` directory intact, but without any files. If
you want to remove the directory, you use the `rmdir` command. You can try
this, but it won't work because the directory isn't empty. `rmdir` only removes
empty directories.

	rmdir stuff

If you want to remove a directory and everything it contains, you can use the
`-r` flag to recursively delete everything inside and the `-f` flag to force
delete of protected files. This is highly, highly destructive, so maybe don't
do it.

	rm -rf stuff

The worst possible thing you could do is unintentionally use the wildcard `*`
with the `rm` command with slightly incorrect syntax. Here, let me show you how
to destroy everything. Maybe don't type this...

	rm -rf stuff *

You may have wanted to do `rm -rf stuff/*` but the space between `stuff` and
`*` means that `*` matches **EVERYTHING**. So that's how you delete everything
in your current directory. If you happen to be in your home directory, you just
deleted everything you own. Ask me how I know.

Since `mv`, `cp`, and `rm` can be so dangerous, many people create aliases that
force each command to be interactive. We'll see how to do this a little farther
below when we get to the more advanced Unix section.

------------------------------------------------------------------------------

## Markdown and Files ##

Most of the files we work with in Linux are plain text files. Many things
change in this world, but not the format of text files. Got some old poetry you
wrote in WriteNow? Well, that software doesn't exist anymore, so good luck
viewing it. However, any text file since the dawn of Unix still works just
fine. Markdown files, like this one, are plain text files. However, there are
Markdown processors that will turn you Markdown files into beautiful PDF, HTML,
etc.

### Text vs Binary ###

There are two main types of files you will encounter: text and binary. You can
view text files with `less` and edit them with `nano`, for example. All of the
programs we will write will be text files. You can also view and edit binary
files but they look like gobledygook, not English. If you want to see what a
binary file looks like, try the following.

	less /bin/ls

You're looking at the machine code for the `ls` program. It's not meant to be
human-readable. These are machine-specific instructions designed for machines,
not humans. So what makes a file text or binary? To answer that, we need to
delve into the world of bits and bytes.

### Bits, Bytes, and ASCII ###

A _bit_ is a single binary digit representing a 0 or 1. The number "1" is just
1 as we know it. The number "10" is 2 in decimal notation. There is a "1" in
the 2s place and a 0 in the "1s" place, so 2 + 0 = 2. Similarly, the number
"11" in binary is 3 in decimal and the number "101" in binary is "5" in decimal
(1 four, 0 two, 1 one).

A byte is 8 bits. Computers usually deal in bytes. So we don't normally talk
about a number like "101" to represent 5 but rather the 8-digit version of that
"00000101". So what number is "10000000"? Well that depends if you're working
in base 2, decimal, or something else entirely. In order to clarify these
things, people often put two characters at the front to signify the base when
it's not base-10. Prepending the numerals with "0b" tells people "I'm using
binary". So "0b10000000" means 128 and not ten million.

We actually use the "byte" more frequently than you might guess. However, when
we do so, it's usually in _hexidecimal_ notation. In base 2, there are 2
symbols: 0 and 1. In base 10 (ordinary decimal) there are 10 symbols: 0, 1, 2,
3, 4, 5, 6, 7, 8 , and 9. In base 16 (hexidecimal), there are 16 symbols: 0, 1,
2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, and F. So the symbol "B" in hexidecimal
means "11" in decimal. To specify that a number is in hex, it is proceeded with
"0x". Therefore "0x10" is 16 (1 value in the 16s and nothing in the 1s).

Have you ever seen internet addresses of the form 192.168.1.1? Ever wondered
what those 4 numbers are? Each one is a byte. So each one can have a value from
"0b00000000" to "0b11111111". In other words, each value can be from "0x00" to
"0xFF". Or more familiarly, from 0 to 255. These same byte notations are used
all over the place in computers. For example, you may have had to dig up the
MAC (media access control) address of your network adapater, which may have
looked like "f0:18:98:e9:f2:be". Each of those number-like things separated by
a colon is a byte in the range of 00-ff (upper and lowercase don't matter in
hexidecimal).

### Colorspace ###

Another place you may have seen hexidecimal notation is to represent colors. In
a computer, color is made by mixing three colors of light: red, green, and
blue. Each of those colors can have an intensity from 0 to 255, which in hex is
00-FF. For example, if you want to make bright red, you use FF in the red
channel, 00 in the green channel, and 00 in the blue channel. The most
efficient way to write this is to mash them all together as FF0000. This can
also be written as 0xFF0000 or even #FF0000.

Here are some common colors:

+ FF0000 Red (only the red channel)
+ 00FF00 Green (only the green channel)
+ 0000FF Blue (only the blue channel)
+ 000000 Black (all channels off)
+ FFFFFF White (all channels on)
+ 808080 Gray (all channels at half)

If you think about the color spectrum, yellow is halfway between red and green.
So how do we make a color halfway between the two? By turning on those two
channels. Similarly, halfway between green and blue is cyan. If you think of
the spectrum as a circle rather than a line, then halfway between blue and red
is magenta.

+ FFFF00 Yellow
+ 00FFFF Cyan
+ FF00FF Magenta

What about the other colors, such as orange? Orange isn't halfway between any
of the channels. However, it is halfway between red and yellow. To make orange,
we have to decrease the green channel so that the average is closer to red. How
about we cut the green in half? FF8000 = Orange.

At this point, you're probably asking yourself, "but what about all of that
stuff I learned in art class where red + green = brown?". Paints are pigments,
not sources of life. You have to think about those in the absorption spectrum.
Red pigment block green and blue, allowing red to come through. Similarly,
green pigment blocks red and blue, allowing green to come through. When you mix
pigments, you average the absorptive properties of the two. So red + green
pigments completely block the blue spectrum and allow about half of the red and
green to come through. If we were to express that in hex it would look like
808000, which is a dark yellow, which might as well be brown.

### Back to Binary ###

So now it's time to understand the difference between text and binary files. A
text file typically uses only the 7 bits defined by ASCII (American Standard
Code for Information Interchange). That is, each byte is confined to the range
from 0 to 127. In binary that's "0b00000000" to "0b01111111". In hex, that's
"0x00" to "0x7F". All of the numbers equal to or greater than than "0b10000000"
or "0x80" or 128 are outside the ACSII space. Any file using values outside of
ASCII is binary.

In a plain text file, every symbol (e.g letter or punctuation) has a
corresponding value in the range of 0-127. For example, captial "A" is
"0b01000001" or "0x41" or 65 (decimal). Similarly, capital "B" is "0b01000010"
or "0x42" or 66. The numbers from 0-9 are in ASCII slots 48-57, the capital
letters are 65-90, the lowercase letters are 97-122, and other symbols are in
various places (32-47, 58-64, 91-96, 123-127). Everything below 32 is
invisible.

At this point you may be wondering about other alphabets and how they get
encoded in a computer. Surely you can't fit all of the symbols in known human
language into the range of 0-127. You can't. However, there are multi-byte
encodings that offer many more symbols. But for now, we are only considering
ASCII.

### Formatting Plain Text ###

Text files are incredibly simple. There are no choices of ruler settings, font
family, font style, lists, or tables you expect to find in a word processing
document. However, sometimes you want part of a text file to look like a
heading, or boldface, or a list. There are lots of ways you can imagine doing
that from the use of capital letters to punctuation. Markdown is a global
standard for writing text files. If you follow the standard, you can turn your
plain text documents into beautifully formatted HTML or PDF that has actual
headings, hyperlinks, font styles, lists, etc.

To find out how to write Markdown, check out the website linked below. This is
the official home of vanilla Markdown. There are a few customizations of
Markdown that add a few more things like tables.

[https://daringfireball.net/projects/markdown](Markdown)

Another way to learn Markdown is to compare an HTML or PDF file to its original
Markdown plain text source document. If you're viewing this document on GitHub,
you're viewing it formatted as HTML. You can also look at the raw text either
on the website or in your forked repo.

Let's create our first Markdown document in `nano`.

	nano plans.md

Now let's enter some content.

	To Do List
	==========

	Here are some of the things I'm working on this week.

	+ Learn some Unix commands
	+ Learn how to write in Markdown **now**
	+ Learn how to program in Python
	+ Get my code into GitHub like all _professional_ developers

As you can see, even without the use of headings, font sizes, type faces,
rulers, etc. we are able to communicate document structure and emphasis. "To Do
List" is clearly the title. The plus signs are clearly a bulleted list. The use
of asterixes and underscores clearly show emphasis. Follow a few simple
Markdown rules and you'll end up with beautiful documents that are easy to
write and a pleasure to read as text, HTML, PDF, etc.

------------------------------------------------------------------------------

## GitHub CLI ##

### Personal Access Token ###

When you interact with the GitHub website, you use a username and password.
When you interact with GitHub using the Linux CLI, you cannot use your website
password. Instead you have to use a "personal access token" (PAT). So the first
thing we need to do is to generate a PAT.

Log into GitHub and then click on the icon in the top right corner. This will
drop down a menu where you will find "Settings". Follow that link and you will
get to your various account settings. Scroll down to the bottom to find
"Developer Settings". On the next page you will see "Personal access tokens".
Click on the link to "Generate a personal access token".

In the "Note" you might put in "programming" or something. It doesn't matter.

For "Expiration" you can use any of the values. If you don't want to do this
again, use the "No expiration" option.

Click on the "repo" checkbox, which will also check the subordiante boxes.

Your personal access token is given to you once. Copy it and save it somewhere
safe. You can never get to this PAT again. Ever. However, you can generate a
new one anytime you like, so if you lose your PAT, you can just generate a new
one. I put my PAT in a personal message to myself in Slack. I also keep it in
a file on Dropbox.

### Cloning Your Repos ###

Your current repos are locatd on GitHub, but are not in your Linux computer.
It's time to get them. You'll need a good place to keep all of your GitHub
repos. I use a directory called "Work" in my home directory. If you want to be
like me, open a terminal and do the following (substituting YOUR_GITHUB_HANDLE
for whatever your username is on GitHub).

	cd ~/Work
	git clone https://github.com/YOUR_GITHUB_HANDLE/homework
	ls

You should now see your homework directory. Go get your fork of MCB185-2022.

	git clone https://github.com/iankorf/MCB185-2022
	ls

You should see both your homework and MCB185-2022 directories.

### Git Commands ###

Enter your homework repository and check its status.

	cd homework
	git status

You will see that git reports that your repository is up to date. Let's modify
a file and see what happens. Edit the `README.md` file so that it has a little
more information. For example, you might add your name and someting about your
learning goals.

	nano README.md

After saving your changes, check your repository status again.

	git status

This shows that `README.md` has been changed. In order to put those changes
back into GitHub, you'll need to `add`, `commit`, and `push`.

	git add README.md
	git commit -m "update"
	git push

The `add` argument tells `git` we intend to put this file in our repo. Not all
files in your current directly need to go into your repo. For example, you may
have some temporary program outout you were using for debugging.

The `commit` tells `git` we are done with edits, and the `-m` provides a short
message about what work was done. The message might be as simple as "update" or
"edit" or "new", but might be more complex such as "finally squashed the
formatting bug".

The `push` tells git to upload the file back to GitHub.

When git prompts you for your username, use your GitHub username. For the
password, copy-paste your GitHub personal access token.

The general workflow with `git` is the following.

1. Create a file
2. `git add`
3. `git commit -m "something"`
4. `git push`
5. Time passes...
6. `git pull`
7. Edit files
8. Go back to step 2

------------------------------------------------------------------------------

## Python: Hello World ##

It's time to write your first Python program. We're going to do this with
`nano`. Start `nano` by typing the command name followed by the file you want
to create.

	cd ~/Work/homework
	nano 00helloworld.py

Now type the following line:

	print('hello world')

Hit ^O (that's the command key plus the o key) to save the file and the ^W to
exit nano. Now let's try running the command from the shell.

	python3 00helloworld.py

If everything worked okay, you should have seen 'hello world' in your terminal.
If not, don't go on. Ask for help fixing your computing environment.

---

Now it's time to add your new file to your repository. First let's check the
status of your repo.

	git status

This shows that `00helloworld.py` is not currently being tracked. So let's add,
commit, and push it.

	git add 00helloworld.py
	git commit -m "initial commit"
	git push

Check the GitHub website. You'll see that your changes to `README.md` are there
as well as the new file `00helloworld.py`.

It might seem like git is a lot of effor just to upload your code to a website.
If that's all git did, it would be too much effort, but git allows you to do a
lot more. Git tracks every change you make to a file, allowing you to rewind it
to any point in time. Git allows you to make a _branch_ of related work and
then later merge it back in with the main trunk if desired. More importantly,
git allows multiple developers to work simultaneously on the same project
without destroying each others work. We aren't using those advanced features
yet. Right now, our focus is on backing up our code and logging our programming
activity to the GitHub website.


## Unix Permissions and Paths ##

Unix file permissions are critical to understand, but a little obscure. To
understand how they work, we're going to turn our `00helloworld.py` program
into a proper executable. Be patient in this section, it's complex.

Previously, when we wanted to run the program `00helloworld.py` we had to
proceed that with the command `python3`. Most of the programs you've seen so
far, like `date` or `ls` did not require anything other than the name of the
program. We can change `00helloworld.py` to work in the same manner. While this
isn't really necessary, it's very important to understand how permissions work,
so we're going to modify `00helloworld.py` to be just like `ls`.

Go to your homework repot and use nano to edit the file.

	nano 00helloworld.py

Now modify it so that it looks like the following:

	#!/usr/bin/env python3
	print('hello world')

Line 1 has the "hash bang" _interpreter directive_. The first line of a text
file tells Unix which language to use. Make sure the first character of the
file is `#` and that there are no additional leading spaces. Line 2 is what you
had before. Save this file and then push the changes back to your repo. We're
not done yet. This is just the first step.

### Programs ###

In order for a text file to function as a program it needs 3 things.

1. An interpreter directive on the first line (we just did this)
2. Permission to be executed
3. Located in the executable path

### File Permissions ###

A file can have 3 kinds of permissions: read, write, and execute. These are
abbreviated as `rwx`. If a file has read permissions, you can view it. If it
has write permissions, you can edit it, which includes deleting it. If it has
execute permissions, you can run it as a program.

Directories are special kinds of files that also have the same permissions.
Here, read means you can view the files in the directory. Write means you can
add or delete files in the directory. Execute means you can enter the
directory.

Generally, you would like to be able to read, write, and execute the
directories you own. But this isn't always true of files. You may have
downloaded some important data and want to make sure you can't modify or delete
it. Permissions allow you to modify what actions can be taken by whom.

In addition to having 3 types of permissions (read, write, execute), every file
also has 3 types of people that can access it: the owner (you), the group you
belong to (e.g. a laboratory), or the public (everyone else who has access to
the computer).

Let's examine the file permissions on the directories and files you
currently have.

	cd ~/Work
	ls -lF

You should see something like the following:

	drwxr-xr-x  2 ian ian 4096 Feb 7 10:01 bin/
	drwxr-xr-x  2 ian ian 4096 Feb 7 10:01 lib/
	drwxr-xr-x  2 ian ian 4096 Feb 7 10:11 homework/

Let's break down what's happening with the first arcane set of symbols. The
first letter is `d` which indicates that the file is a directory. We can also
see this because of the trailing slash from the `ls -F`. The next 9 characters
are 3 triplets.

+ rwx the first triplet are your permissions
+ r-x the second triplet are group permissions
+ r-x the third triplet are public permissions

You may read, write, and execute the directory. That is, you have permission to
`ls` the directory, `rm` files in the directory, and `cd` into the directory.
Users who belong to your group can also read and enter your directories, but
they can't modify their contents.

Let's take a look at the permissions of `00helloworld.py`.

	cd homework
	ls -l 00helloworld.py

On Ubuntu, this is what I found, however the default permissions for your Linux
distribution may be different.

	-rw-r--r-- 1 ian ian 44 Feb 7 11:00 00helloworld.py

After the leading dash, there are 3 triplets of symbols. The first triplet
shows user permissions `rw-`. I have read and write permission but not execute.
The next triplets are for group and public. Both have read permission, but not
write or execute. Let's first turn on all permissions for everyone using the
`chmod` command and then list again.

	chmod 777 hello_world.py
	ls -l hello_world.py

Notice that you can now see `rwx` for owner, group, and public. Does it make
sense for _everyone_ to be able to edit your files? Probably not. It also
doesn't make sense for plain text files with your shopping list to have
executable permissions. So turning everything on isn't a good idea.

The `chmod` command has two different syntaxes. The more human readable one
looks like this.

	chmod u-x 00helloworld.py
	ls -l 00helloworld.py

This command says: "change the user (u) to remove (-) the execute (x) permission
from file hello_world.py". You add permissions with +.

	chmod u+x 00helloworld.py
	ls -l 00helloworld.py

The less readable `chmod` format assigns all parameters in octal format
simultaneously. Once you understand how it works, it's much easier.

+ 4 is read permission
+ 2 is write permission
+ 1 is execute permission
+ 0 is no permissions

Every number from 0 to 7 results in a unique set of permission.

| Read | Write | Exec | Sum | Meaning
|:----:|:-----:|:----:|:---:|:--------
|   4  |   0   |   0  |  4  | only reading allowed
|   4  |   2   |   0  |  6  | reading and writing allowed
|   4  |   2   |   1  |  7  | reading, writing, and executing allowed
|   4  |   0   |   1  |  5  | reading and executing allowed
|   0  |   0   |   0  |  0  | nothing allowed

Here are some useful permission sets:

+ 600 your private diary (only you can read and write)
+ 644 your source code (you can read and write, others can read)
+ 755 your programs (like above, but executable)
+ 444 data files (everyone can read, nobody can write)

Let's set the permissions on `00helloworld.py` to the most appropriate set
using the octal format.

	chmod 755 00helloworld.py

### Making hello_world.py Executable ##

Now that your 0hello_world.py program has execute permissions, you can use it
like a Unix program. That is, you don't have to type `python3` before the
program name.

	./hello_world.py

But what's with the `./` before the program name. You don't have to type that
when you run the `ls` command or the `chmod` command, for example. That's
because those programs are in your **executable path** and `00helloworld.py` is
not. We'll fix that in a sec.

### Files on Flash Drives ###

Most flash drives are formatted to be compatible with Windows machines. Each
operating system has a different idea about how to store filesystem metadata
such as permissions. Because of this, most files on flash drives end up with
all permission set. In octal, that would be 777 (read, write, execute) for
owner, group, and public. This is the most permissive setting and can be a
little dangerous. After copying files from a flash drive to your Unix machine,
it's probably a good idea to change the permissions to something more sensible.

### Customizing Your Shell ###

In order to simplify a few things, we need to customize your shell. First, we
have to figure out which shell you're running. Your shell is in your SHELL
environment variable. Here are two ways of seeing that.

	printenv SHELL
	echo $SHELL

If your shell is `/bin/bash` then check if you have a file called `.profile` or
`.bash_profile` or `.bashrc` in your home directory. If you already have one of
those files, edit it with nano. If not, create a `.profile` with nano.

If your shell is `/bin/zsh` then check if you have a file called `.zshrc`. If
it exists, edit it with nano. If not, create it with nano.

Now enter the following 2 lines into the file you're editing.

	alias ls="ls -F"
	export PATH=$PATH:$HOME/Work/bin

The first line makes it so that whenever you use the `ls` command, you're
actually invoking `ls -F` which displays the file type by appending a `*` to
executable files and a `/` to directories.

The second line adds your `Work/bin` directory to the executable path. Now, any
script you put into `Work/bin` can be run like any other program.

To protect yourself from accidentally overwriting or removing files, you might
want to add interactive mode for a few commands.

	alias rm="rm -i"
	alias mv="mv -i"
	alias cp="cp -i"

### PYTHONPATH ###

Just like your shell needs to know where your programs live, Python needs to
know where your libraries live. It's going to be a while before we are writing
our own libraries, but we should set things up for that later. It looks very
similar to the PATH setup you just did.

	export PYTHONPATH=$PYTHONPATH:$HOME/Work/lib

### Finally a Program ###

It's finally time to make `00helloworld.py` work like `ls` and such. Where were
we with what we needed to do?

1. An interpreter directive on the first line (we did this before)
2. Permission to be executed (we did this recently)
3. Located in the executable path

We have a few options here:

1. Move the file from homework to `~/Work/bin`
2. Copy the file from homework to `~/Work/bin`
3. Alias the file frome homework to `~/Work/bin`

We don't want to move the file because then it's no longer in our repo. We also
don't want to copy the file because then we'll have 2 files running around and
edits in one won't be reflected in the other. The best thing is to use an alias
so that the shortcut in `~/Work/bin` points to the original file. While we're
at it, let's change the name of the program from `00helloworld.p` to
`helloworld`.

	cd ~/Work/bin
	ln -s ../homework/00helloworld.py ./helloworld

That's it, you're done. Now you can type `helloworld` in your terminal and the
program runs just like `ls` or any other proper CLI program. Note that you
generally don't need to do this. There's nothing wrong with `python3
filename.py` to invoke your python programs.

## Editors and IDEs ##

It's time to stop using `nano`. While it is useful for very small tasks, it's
not a great programming editor. Most of us are more efficient navigating
documents with a mouse than a keyboard. All of the files you have been editing
with `nano` could have been edited with Atom, BBEdit, Geany, Gedit, Jedit,
Notepad++, Sublime, etc.

Some people prefer programming in an Integrated Development Environment (IDE).
Popular IDEs for Python include IDLE, PyCharm, Spyder and Eclipse. IDEs can
make debugging easier as they automatically place your cursor at lines with
bugs and let you manually inspect variable contents. While IDEs may make your
Python programming more efficient, they separate you from Unix. Since one of
the reasons you are taking this course is to learn some Unix, I don't recommend
using an IDE at this time.

So which programming/text editor should you use? Whatever is installed by
default in your Linux distribution should be fine. I use Geany on Linux, BBEdit
on Mac, and Notepad++ on Windows.

## Useful Unix Commands ##

The `wc` program counts the characters, words, and lines in text files. You
could counts the words in this document, for example.

	wc GUMPY.md

One of the most useful programs is `grep`. This prints out lines that match
specific strings or patterns. For example, if you wanted to print out all the
lines with the word Unix you would do the following:

	grep Unix GUMPY.md

To count how many lines that was, you could either use the `-c` flag to `grep`
or **pipe** the output to `wc`.

	grep -c Unix GUMPY.md
	grep Unix GUMPY.md | wc

When working with tabular data, you will find that `sort` is very useful, as it
let's you sort the lines on different columns.

When monitoring the progress of programs that take a long time to run, you will
find `time` useful for timing how long a program runs and `top` or `htop` for
monitoring how much RAM or other resources a program is taking.

To see how much free space you have on your file system, use the `df` (disk
free) command with the `-h` option to make it more human-readable (try it both
ways).

	df
	df -h

Another useful command is `du` (disk usage) which shows how much space each of
your files and directories uses.

	du
	du -h

## Unix Quick Reference ##

| Token   | Function
|:--------|:-------------------------------------|
| .       | your current directory (see pwd)
| ..      | your parent directory
| ~       | your home directory (also $HOME)
| ^C      | send interrupt signal
| ^D      | send end-of-file character
| tab     | tab-complete names
| *       | wildcard - matches everything
| \|      | pipe output from one command to another
| >       | redirect output to file

| Command   | Example       | Intent                        |
|:----------|:--------------|:------------------------------|
| `cat`     | `cat > f`     | create file f and wait for keyboard (see ^D)
|           | `cat f`       | stream contents of file f to STDOUT
|           | `cat a b > c` | concatenate files a and b into c
| `cd`      | `cd d`        | change to relative directory d
|           | `cd ..`       | go up one directory
|           | `cd /d`       | change to absolute directory d
| `chmod`   | `chmod 644 f` | change permissions for file f in octal format
|           | `chmod u+x f` | change permissions for f the hard way
| `cp`      | `cp f1 f2`    | make a copy of file f1 called f2
| `date`    | `date`        | print the current date
| `df`      | `df -h .`     | display free space on file system
| `du`      | `du -h ~`     | display the sizes of your files
| `git`     | `git add f`   | start tracking file f
|           | `git commit -m "message"` | finished edits, ready to upload
|           | `git push`    | put changes into repository
|           | `git pull`    | retrieve latest documents from repository
|           | `git status`  | check on status of repository
| `grep`    | `grep p f`    | print lines with the letter p in file f
| `gzip`    | `gzip f`      | compress file f
| `gunzip`  | `gunzip f.gz` | uncompress file f.gz
| `head`    | `head f`      | display the first 10 lines of file f
|           | `head -2 f`   | display the first 2 lines of file f
| `history` | `history`     | display the recent commands you typed
| `kill`    | `kill 1023`   | kill process with id 1023
| `less`    | `less f`      | page through a file
| `ln`      | `ln -s f1 f2` | make f2 an alias of f1
| `ls`      | `ls`          | list current directory
|           | `ls -l`       | list with file details
|           | `ls -la`      | also show invisible files
|           | `ls -lta`     | sort by time instead of name
|           | `ls -ltaF`    | also show file type symbols
| `man`     | `man ls`      | read the manual page on ls command
| `mkdir`   | `mkdir d`     | make a directory named d
| `more`    | `more f`      | page through file f (see less)
| `mv`      | `mv foo bar`  | rename file foo as bar
|           | `mv foo ..`   | move file foo to parent directory
| `nano`    | `nano`        | use the nano text file editor
| `pwd`     | `pwd`         | print working directory
| `rm`      | `rm f1 f2`    | remove files f1 and f2
|           | `rm -r d`     | remove directory d and all files beneath
|           | `rm -rf /`    | destroy your computer
| `rmdir`   | `rmdir d`     | remove directory d
| `sort`    | `sort f`      | sort file f alphabetically by first column
|           | `sort -n f`   | sort file f numerically by first column
|           | `sort -k 2 f` | sort file f alphabetically by column 2
| `tail`    | `tail f`      | display the last 10 lines of file f
|           | `tail -f f`   | as above and keep displaying if file is open
| `tar`     | `tar -cf ...` | create a compressed tar-ball (-z to compress)
|           | `tar -xf ...` | decompress a tar-ball (-z if compressed)
| `time`    | `time ...`    | determine how much time a process takes
| `top`     | `top`         | display processes running on your system
| `touch`   | `touch f`     | update file f modification time (create if needed)
| `wc`      | `wc f`        | count the lines, words, and characters in file f
