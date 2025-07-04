- coding: utf-8 -_-
'''
Created on Wednesday Jun 25 20:25:10 2025
Udemy -100 Days of code (Angela Yu)
video -495  Gitignore
Author: JohnC
'''

# *   Git in line commands
control versions in local

: Download git 2.49.0 64 bits (windows)

- Nombre
  $ git config --global user.name "johncoding101"

- Email
  $ git config --global user.email "johncoding101@gmail.com"

- Editor
  $ git config --global core.editor "code --wait" (VS code)

- color
  $ git config --global color.ui true

- Salto de linea (crlf)
  $ git config --global core.autocrlf true

## Create a repo

 $ git ini
   (john MINGW64/name_repo(master))

- Rename a repo
  $ git branch -m main

- Areas
  work (trabajo) - staged(preparacion) - commit (local)

- Add files to staged
  $ git add file1, file2 ...

- Remove files to staged
$ git rm --cached -r .  (file_name or . == all files)

- Status
  $ git status -s (--short)

- Commit
$ git commit -m "my first commit" -a

- Back to (Last modification of the file)
  $ git checkout <filename>

- log
$ git log
$ git log --oneline (id_commits)

- diff (files)
$ git show filename
$ git diff --staged

- diff (commits)
$ git diff id_4427bc1 id_9cc34ab
$ git diff --name-only id1 id2

- Modify commits
$ git commit --amend
$ git reset --soft id_commit
 back to HEAD to area staged , modify --> add --> commit

$ git reset --soft head~1 (one back)
$ git reset --soft head~2 (two back)

$ git reset --hard id_commit
$ git reset --mixed id_commit

- Branch - create
$ git branch name_branch (in main)
$ git switch name_branch

- Delete branch
$ git branch -d name_branch

- Change name
$ git branch -m new_name

- Tree
$ git ls-tree -r --name-only id_commits

- Merge (from main)
$ git merge final_branch
$ git merge --continue

## Git ignore
create a file .gitignore, inside the file # comments
example:
This is a comment # ignore all files like venv  .env  and .history
venv/
.env
.history/

in Python gitignore templetes:
https://github.com/github/gitignore/blob/main/Python.gitignore
files and directories to be ignored

- Global gitignore
c:/misarchivos/code/.gitignore_global
#gitignore global
.history/

$ git config --global core.excludefile c:/misarchivos/code/.gitignore_global

- Alias
example
  $ git log --oneline --all --graph --pretty =
    format:"%C(auto) %h%d%s %C(black) %C(bold) %cr"

  $ git config --global alias.log-mejorado "log --oneline --all --graph --pretty =
    format:'%C(auto) %h%d%s %C(black) %C(bold) %cr' "

- Recover (commit ref)
$ git reflog

- Show the Global Setup
$ git config --global --list

# GitHub
control versions in remote
- Create
Create in remote git_name, create file README.MD
In mi PC(work station):
I have mi project then
$ git pull origin main --rebase (update the changes remote vs PC)
$ git push -u origin main (copy all project from PC to git_name in GitHub)



