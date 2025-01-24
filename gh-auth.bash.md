# gh-auth.bash

```sh
# TODO: gh v2.54.0 introduced `--skip-ssh-key` but not all distros are updated yet
GH_BROWSER=false gh auth login --git-protocol ssh --hostname github.com --web
GH_TOKEN="$(gh auth token)"
if ! echo "$GH_TOKEN" | grep --quiet "^gho_"; then
  unset GH_TOKEN
fi
```
