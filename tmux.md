# tmux

## Notes

```
# create a shared session
tmux -S /tmp/shared new -s shared
sudo chgrp google-sudoers /tmp/shared
sudo chmod 775 /tmp/shared
# ...
tmux -S /tmp/shared attach -t shared
```
