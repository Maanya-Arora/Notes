Missing Semester of CS Education
MIT EDU 
Course Overview + The Shell

OVERVIEW

-computers are great at repeating tasks 
-computer can be used as tool for developing ourselves instead of software development
-combining, learning, and mastering new and old tools
-11 lectures x 1 hour
-highlighting interesting tools and ways to use them
-basics on shell and terminal and then ramping up to tools


THE SHELL

The shell is the primary way you interact with your computer when you want to do more things than what VISUAL INTERFACES allow you to do
-shell we’ll primarily use: bash, on linux, can be found on mac os, and various versions can be downloaded on windows 

HOW DO YOU USE THE SHELL

-on the shell prompt you get to write commands
    -commands are straightforward things that tell the shell to perform an operation, or executing program with arguments
        EX. type “date” in the prompt
        Output:
user@User-Ubuntu:~$ date
Wed Jul 29 12:24:42 PDT 2020
user@User-Ubuntu:~$
echo prints arguments you give it; ie: echo hello returns hello
Arguments are separated by whitespace
If you have more than one word in an argument, group it in quotations so it can stay one argument


HOW DOES THE SHELL KNOW WHAT TO DO?

-the computer has built-in programs that comes with the machine 
-the shell can find the program that is stored in your files
-it finds it using an “environment variable”
    -set when you start the shell
    -sets home directory, PATHS, username, etc
        -echo $PATH shows you all the paths on your device
        -the bash shell will search from programs from these paths                -it will search through each directory for a program that matches the 
command you used
        -on linux and mac, the paths are separated by forward slashes “/”
        -they are a way to name the files on your computer
        - which can tell you where the program is. if you type which echo it will output where the echo file is located
        -ABSOLUTE PATHS are paths that fully determine the location of the file
        -relative paths are relative to where you currently are:
            - “pwd” will show you which directory path you are currently in
            -”cd” (change directory) will change your directory, or current path. 
            -cd /home will change your directory /home (prompt will show this)
            -cd .. = will go to prev. Directory (root) /home ----> /
            -cd ./home = cd into home under current directory
---dot dots can get you back to the root----

-the shell is actually a programming language
-the prompt can not only run a program, you can loops, define functions, etc. 
-programs (by default) will run on current working directory
-what is in the directory: ls shows you files under current directory
-you can ls any directory !! 

cd ~ will take you back to home directory
cd - will take you to the directory you were previously in

ls --help
WILL PRINT A HELP MANUAL FOR THE ARGUMENTS IN SHELL

ls -l WILL...
Use a “long listing format”: it prints the files in the directory but it gives more information on the files

ie. drwxr-xr-x 4 user user   4096 Jul 22 20:08 Desktop

-the d signifies that the item in ? is not a file, but rather a directory 

-the following letters indicate permissions for that file
    -first group of 3 - owner permissions
    -second group - permissions for group
    -third group - permissions for others
“Rwx” - READ permissions - you can read the file; WRITE permissions - you can edit and save the file; EXECUTE permissions - you can run/execute the file;

FOR A DIRECTORY: 
R(ead) permission to see what files are in this directory (list)
W(rite)permission to rename, create, remove files from directory
(e)X(ecute)permission to “search” (are you allowed to enter this directory?) (you must have this permission on all parent directories and the directory itself to CD into it)

“Mv” - rename a file
Change the name 
Or move a file to a new directory 

“Cp” 
copys a file 
Path you want to copy from 
And to 

“Rm” 
Removes a file 
(not recursive, can’t remove a directory)

“Rmdir” removes empty directories 

“Mkdir” creates directories (one word, or put in quotes)

Man - man ls will give manual for ls argument (examples, etc)
^ ctrl l clears terminal, so does clear; q will quit the manual

Cat prints CONTENTS of a file

| = take output of left program and make it input of right program 
Tail = last line of input is printed

“Root user” administrator user - id 0 (can do whatever on your system) SUPER user !! you are *not usually * root

sudo *runs command as if you were root*
--cd/sys
--ls

^kernel parameters through a file system (directories for diff devices)
(you can change computer into blacklight, etc)
--might say PERMISSION DENIED--

# - runs as root 
$ - indicates you are not running anything as root user

Sudo su - lets u be the super user 
Exit - exits from root user

Tee - takes it input and makes it into a file (that you can see) *writes to file and screen** 

Xdg-open : OPENS FILE :) 
*now you dont need to in theory open finder, etc (run straight from shell)

LINK TO DOCS: https://docs.google.com/document/d/1Nck7wlolZ32K04fTTS4h0SCuk_x-_igoG3wP4y2VUxQ/edit





        











