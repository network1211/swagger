#!/bin/bash

# Configuration
git_user_id="network1211"
git_repo_id="swagger"
release_note="Minor update"
branch_name="new-branch"

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

# Remove existing remote origin if it exists
git remote remove origin

# Set remote origin and push changes using a Personal Access Token (PAT)
# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual PAT
git remote add origin https://network1211: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@github.com/network1211/swagger.git
git push -u origin master

# Create a new branch and push
git checkout -b ${branch_name}
git push -u origin ${branch_name}
