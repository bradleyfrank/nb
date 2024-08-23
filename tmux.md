# tmux

## Notes

### Create a shared session

```sh
tmux -S /tmp/shared new -s shared
sudo chgrp google-sudoers /tmp/shared
sudo chmod 775 /tmp/shared
# ...
tmux -S /tmp/shared attach -t shared
```

### Move a window from one session to another

```sh
move() {
  local session_name window_name session_index session_window \
    window_to_move target_session target_index
  local -A tmux_windows

  # Create a list of each window in every session
  while read -r session_name; do
    while read -r window_name; do
      session_index="$(awk -F ':' '{print $1}' <<< "$window_name")"
      session_window="$(awk -F ':' '{print $2}' <<< "$window_name")"
      tmux_windows["${session_name}: ${session_window}"]="${session_name}:${session_index}"
    done < <(tmux list-windows -F "#{window_index}:#{window_name}" -t "$session_name")
  done < <(tmux list-sessions -F "#{session_name}")

  [[ ${#tmux_windows[@]} -eq 0 ]] && return 1

  while read -r window_to_move; do
    target_session="$(_select_session)"
    target_index="$(tmux list-windows -F "#{window_index}" -t "$target_session" | tail -n1)"
    tmux move-window \
      -s "${tmux_windows["$window_to_move"]}" -t "${target_session}:${target_index}" -da
  done < <(printf "%s\n" "${!tmux_windows[@]}" | sort | fzf-tmux -p --multi)
}
```
