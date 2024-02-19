# Git

## Tags

#git #github

## Notes

```sh
# clone by tag
git clone -b <tagname> <repository> .

# logs and searching
git log --full-history -- /path/to/file  # search for file changes
git log --all --grep='Build 0051'  # search the commit log (across all branches) for the given text
git grep 'Build 0051' $(git rev-list --all)  # search the content of commits

# find and retrieve a deleted file
file=/path/to/file
git checkout $(git rev-list -n 1 HEAD -- "$file")~1 -- "$file"

# find commiter and show commit
git log --format='%h %ae' | grep {{ email }} | awk '{print $1}' | xargs git show

# branching
git push --delete <remote_name> <branch_name>  # delete remote branch
git branch -d <branch_name>  # delete local branch
git branch –m <new_name>  # rename local branch
git push origin -u <new_name>  # rename remote branch
git push origin --delete <old_name>  # delete old branch

# comparing
git diff --staged  # diff files already staged
git diff --stat  # diff summary
git diff --check  # check for conflicts and whitespace errors

# fixups
git reset --hard [HEAD|<hash>]  # forget all the changes, clean start
git reset <hash>  # edit, re-stage and re-commit files
git reset --soft <hash>  # re-commit past commits, as one big commit

# submodules
git clone --recursive --jobs {{ int }} {{ repo }}  # clone repo w/ submodules (synchronously)
git submodule update --init  # load submodules in a previously cloned repo
git submodule update --init --recursive  # for nested submodules
git submodule update --init --recursive --jobs 8  # " " " (synchronously)
git submodule update --remote  # pull all changes in submodules
git submodule add <repo>  # add a child repository to a parent repository
git submodule init  # initialize an existing Git submodule
git submodule update  # update the commit of the submodule to the latest commit
```

### Commit Signing

```sh
ssh-keygen -t rsa -b 4096 -C "me@email.com"
git config --global user.name "Name"
git config --global user.email "me@email.com"
git config --global user.signingkey "$(cat ~/.ssh/id_rsa.pub)"
git config --global commit.gpgsign true
git config --global gpg.format ssh
git config --global gpg.ssh.allowedSignersFile "$HOME/.ssh/allowed_signers"
printf "<email> %s" "$(awk '{print $1" "$2}' /path/to/public/key)" >> ~/.ssh/allowed_signers
```
