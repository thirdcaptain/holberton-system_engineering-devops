#0x02-shell_redirections
20180112 - Day 4 0x02. Shell, I/O Redirections and filters

0-hello_world
	script executes "echo "Hello, World" to print hello world

1-confused_smiley
	script executes "echo "\"(Ôo)'"" that displays a confused smiley "(Ôo)'.

2-hellofile
	script executes "cat /etc/passwd" that displays the content of the /etc/passwd file

3-twofiles
	script executes "cat /etc/passwd /etc/hosts" that displays the content of /etc/passwd and /etc/hosts

4-lastlines
	script executes "tail -10 /etc/passwd" that displays the last 10 lines of /etc/passwd

5-firstlines
	script executes "head -10 /etc/passwd" that displays the first 10 lines of /etc/passwd

6-third_line
	script executes "head -3 iacta | tail -1" that displays the third line of the file iacta

8-cwd_state
	script executes "ls -la > ls_cwd_content" that writes into the file ls_cwd_content the result of the command ls -la

7-file
	script executes "echo "Holberton School" > "\\*\\\\'\"Holberton School\"\\'\\\\*$\\?\\*\\*\\*\\*\\*:)"" that creates a file named exactly \*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:) containing the text Holberton School ending by a new line

9-duplicate_last_line
	script executes "tail -1 iacta >> iacta" that duplicates the last line of the file iacta

10-no_more_js
	script executes "find . -name "*.js" -type f -delete" that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders

11-directories
	script executes "find . ! -path . -type d | wc -l"  that counts the number of directories and sub-directories in the current directory

12-newest_files
	script executes "ls -t1p | grep -v / | head -10" that displays the 10 newest files in the current directory

13-unique
	script executes "sort | uniq -u" that takes a list of words as input and prints only words that appear exactly once.

14-findthatword 
	script executes "grep root /etc/passwd" that Display lines containing the pattern “root” from the file /etc/passwd

15-countthatword
	script executes "grep bin /etc/passwd | wc -l" that Display the number of lines that contain the pattern “bin” in the file /etc/passwd

16-whatsnext
	script executes "grep -A 3 root /etc/passwd" that Display lines containing the pattern “root” and 3 lines after them in the file

17-hidethisword
	script executes "grep -v bin /etc/passwd" that Display all the lines in the file /etc/passwd that do not contain the pattern “bin”

18-letteronly
	script executes "grep ^[A-Za-z] /etc/ssh/sshd_config" that Display all lines of the file /etc/ssh/sshd_config starting with a letter

cat 19-AZ
	script executes "tr "A" "Z" | tr "c" "e"" that replace all characters A and c from input to Z and e respectively

20-hiago
	script executes "tr -d "C" | tr -d "c"" that removes all letters c and C from input

21-reverse
	script executes "rev" that reverse its input

22-users_and_homes
	script executes "sort /etc/passwd | cut -d ':' -f 1,6" that displays all users and their home directories, sorted by users

100-empty_casks
	script executes "find -empty -printf "%f\n"" that finds all empty files and directories in the current directory and all sub-directories