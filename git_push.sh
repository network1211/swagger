#!/bin/bash

# Configuration
git_user_id="j.lee@f5.com"
git_repo_id="network1211"
release_note="Minor update"

# Initialize Git repository if not already initialized
if [ ! -d ".git" ]; then
  git init
fi

# Set Git user information if not already set
git config user.email "j.lee@f5.com"
git config user.name "network1211"

# Add and commit changes
git add .
git commit -m "${release_note}"

# Set remote origin and push changes
#git remote add origin https://github.com/${git_user_id}/${git_repo_id}.git
#git push -u origin master
git remote add origin https://${git_user_id}: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@github.com/${git_user_id}/${git_repo_id}.git
git push -u origin master
