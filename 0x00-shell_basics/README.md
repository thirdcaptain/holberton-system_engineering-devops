20180108 Day 1 - Shell Basics

0-current_working_directory
	 script executes "pwd" command to show absolute path of current working directory

1-listit
	script executes "ls" command to list contents of current directory

2-bring_me_home
	script executes "cd ~" command to change working directory to user's home directory

3-listfiles
	script executes "ls -l" command to display current directory contents in a long format

4-listmorefiles
	script executes "ls -la" command to display current directory contents, including hidden files (starting with .) using the long format.

5-listfilesdigitonly
	script executes "ls -l -n -a" command to Display current directory contents in Long format with user and group IDs displayed numerically And hidden files (starting with .)

6-firstdirectory
	script executes "mkdir /tmp/holberton" command to create a directory named holberton in the /tmp/ directory.

7-movethatfile
	script executes "mv /tmp/betty /tmp/holberton" command to move the file betty from /tmp/ to /tmp/holberton.

8-firstdelete
	script executes "rm /tmp/holberton/betty" command to delete the file "betty" in /tmp/holberton.

9-firstdirdeletion
	script executes "rm -r /tmp/holberton" to delete "holberton" directory in /tmp directory.

10-back
	script executes "cd -" to change the working directory to the previous one.

11-lists
	script executes "ls . -la .. -la /boot -la" so that it lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

12-file_type
	script executes "file /tmp/iamafile" that prints the type of the file named iamafile.

13-symbolic_link
	script executes "ln -s /bin/ls __ls__" to create a symbolic link to /bin/ls, named __ls__.

14-copy_html
	script executes "cp -u *.html .." that that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

15-lets_move
	script executes "mv [[:upper:]]* /tmp/u" that moves all files beginning with an uppercase letter to the directory /tmp/u

16-clean_emacs
	script executes "rm *~" that deletes all files in the current working directory that end with the character ~

17-tree
	script executes "mkdir /welcome/to/holberton -p" that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory

18-commas
	script executes "ls -m -a -p" that lists all the files and directories of the current directory, separated by commas (,).
	Directory names should end with a slash (/)
	Files and directories starting with a dot (.) should be listed
	The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
	Only digits and letters are used to sort; Digits should come first
	You can assume that all the files we will test with will have at least one letter or one digit
	The listing should end with a new line