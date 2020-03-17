# Learn Git

## Check Git Version

```
!git --version
```
## Commonly Used Terminal Command (for Windows)
`dir` lists all the files and folders under the current folder
```
!dir
```
`cd` displays the name of the the current directory or changes the current folder
```
# change to the my_project folder
!cd my_project
```
`mkdir` creates a directory (folder) or subdirectory (subfolder)
```
# create a folder named myproject
!mkdir myproject
```
`copy` copies a file from one location to another
```
# Copy a file named MyFile.txt from a Desktop folder to a Ducuments folder
!copy ~/Desktop/MyFile.txt ~/Documents
```
`move` moves a file from one folder to another.
The `move` command can also rename files.
```
# Moves a file named Myfile.txt from Desktop to a folder on a backup disk
!move ~/Desktop/MyFile.txt /Volumes/Backup/MyFolder

# Renamed a MyFile.txt to MyFile-old.txt
!move ~/Desktop/MyFile.txt ~/Desktop/MyFile-old.txt
```
`del` deletes one or more files
```
# deletes a file named MyFile.txt under myfolder
!del ~/myfolder/MyFile.txt
```
`cls` clears the screen
```
!cls
```
## Set Up Git
To start using git, the first thing to do is set up user name and user email. (Only needs to set up one time)
```
!git config --global user.name "Eric Juo"
!git config --global user.email "xxx@gmail.com"
```
After enter the command, check the current setting:
```
!git config --list
user.name=Eric Juo
user.email=xxx@gmail.com
```
## First Time To Git
`git init` initiates Git to control the current directory
```
!cd learn-git    # change to learn-git folder
!git init        # initiate git for the current directory
Initialized empty Git repository in /Desktop/learn-bioinformatics/.git/
```
`git status` checks the status of git
```
!git status
On branch master

No commits yet  

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        Rosalind/
        learn-git/

nothing added to commit but untracked files present (use "git add" to track)
```
`git add` adds files for git to track. Parameter `--all` includes all the files and folders (any file under subfolders as well).
```
!git add --all
```
`git commit` saves the sanppets of files into git. Parameter `-m` is necessary and important, which leaves a message for the current commit.
```
!git commit -m "Commit for the first time"
```
`git log` reads the log of git. Parameter `--oneline` and `--graphic` could help to streamline the result on the screen.
```
!git log --oneline --graphic
* fa7fa4b (HEAD -> master) Commit for the first time
```
`git rm --cached` untrack files from git
```
!git rm --cached ./learn-git/learn-git.md
rm 'learn-git/learn-git.md'
```
## Permanently Untrack a file by Git
Create a file named `.gitignore`, then Git will ignore the files lised in the .gitignore file.
```
# ignore a file
myfile.txt

# ignore everything under project folder
project/*
```
