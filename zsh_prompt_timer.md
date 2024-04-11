# Zsh prompt timer

```zsh
preexec() {
  timer=$(print -P %D{%s%3.})
}


_precmd_timer() {
  local elapsed duration_ms duration_s ms s m h

  now="$(print -P %D{%s%3.})"
  duration_ms="$(($now - $timer))"
  duration_s="$((duration_ms / 1000))"
  ms="$((duration_ms % 1000))"
  s="$((duration_s % 60))"
  m="$(((duration_s / 60) % 60))"
  h="$((duration_s / 3600))"

  if   [[ $h -gt 0 ]]; then elapsed="${h}h${m}m${s}s"
  elif [[ $m -gt 0 ]]; then elapsed="${m}m${s}.$(printf $(($ms / 100)))s"
  elif [[ $s -gt 9 ]]; then elapsed="${s}.$(printf %02d $(($ms / 10)))s"
  elif [[ $s -gt 0 ]]; then elapsed="${s}.$(printf %03d $ms)s"
  else elapsed="${ms}ms"
  fi

  print -P "$elapsed"
}


precmd()
  ...
  if [[ -n $timer ]]; then
    elapsed="$(_precmd_timer)"
    prompt_segments[timer]=" [${bold}${yellow}${elapsed}${reset}]"
    unset timer
  fi
  ...
```
