
set /p commit_str=

git pull origin master

git add --all

git commit -m "%commit_str%"

git push origin master
