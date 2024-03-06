# macOS

## Tags

#apple #mac #filesystem

## Notes

```sh
# system information
systemstats
system_profiler
sw_vers

# set hostname
sudo scutil --set HostName "hostname.local"
sudo scutil --set LocalHostName "hostname"
sudo scutil --set ComputerName "hostname"
sudo dscacheutil -flushcache

sudo nvram AutoBoot=%00  # disable auto-boot on keypress
pmset -g batt | grep -E 'InternalBattery' | cut -f2 | awk -F\; '{print $1$2}'  # get battery
osascript -e 'tell application "Safari" to add reading list item "<url>"'
sudo softwareupdate -aiR  # install macOS updates and reboot
printf "%s ALL=(ALL) NOPASSWD: ALL\n" "$(id -un)" \
  | sudo VISUAL="tee" visudo -f /etc/sudoers.d/nopasswd  # add entries to '/etc/sudoers.d'
```

Erase and format flash drives:

```sh
diskutil list
diskutil eraseDisk free NAME /dev/diskN
diskutil addPartition /dev/diskN APFSX NAME SIZE[%]
diskutil mount /dev/diskNsX
```

### Homebrew

```sh
brew bundle dump  # write a Brewfile
brew bundle cleanup --force  # uninstall all dependencies not listed in Brewfile
brew info alacritty --cask --json=v2 | jq -r '.casks[].version'   # get cask version
brew info toilet --json=v2 | jq -r '.formulae[].versions.stable'  # get formulae version
brew info google-cloud-sdk --json=v2 \
  | jq -r '.casks[].installed,.formulae[].installed[].version'    # get install status
```
