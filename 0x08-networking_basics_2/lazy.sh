#!/bin/bash

echo "Enter file name:"
read -e file_name # `-e` option to enable line editing

git add "$file_name"

echo "Enter Your Commit Message:"
read -e commit_msg

git commit -m "$commit_msg"

git push
