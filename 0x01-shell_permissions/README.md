20180110 Day 2 - 0x01. Shell, permissions

0-iam_betty
	script executes "su betty" to that changes your user ID to betty

1-who_am_i
	script executes "whoami" that prints the effective userid of the current user

4-empty
	script executes "touch hello" that creates an empty file called hello

2-groups
	script executes "groups" that prints all the groups the current user is part of

3-new_owner
	script executes "chown betty hello" that changes the owner of the file hello to the user betty

5-execute
	script executes "chmod u+x" that adds execute permission to the owner of the file hello

6-multiple_permissions
	script executes "chmod ug+x,o+r hello" that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello

7-everybody
	script executes "chmod ugo+x" that adds execution permission to the owner, the group owner and the other users, to the file hello

8-James_Bond
	script executes "chmod 007 hello" that sets the permission to the file hello as follows:
	Owner: no permission at all
	Group: no permission at all
	Other users: all the permissions

9-John_Doe
	script executes "chmod 753" to set permissions of hello to -rwxr-x-wx

10-mirror_permissions
	script executes "chmod --reference=olleh hello" to that sets the mode of the file hello the same as olleh’s mode.

11-directories_permissions
	script executes "chmod -R ugo+X ./" to change that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

12-directory_permissions
	script executes "mkdir -m 751 dir_holberton" that creates a directory called dir_holberton with permissions 751 in the working directory

13-change_group
	script executes "chgrp holberton hello" that changes the group owner to holberton for the file hello

14-change_owner_and_group
	script executes "chown betty:holberton *" that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory

15-symbolic_link_permissions
	script executes "chown -h betty:holberton _hello" 

16-if_only
	script executes "chown --from=guillaume betty hello" that changes the owner of the file hello to betty only if it is owned by the user guillaume

100-Star_Wars
	script executes "telnet towel.blinkenlights.nl" that will play the StarWars IV episode in the terminal

101-man_holberton
	file executes a copy of holberton example man page using command "man ./101-man_holberton"

