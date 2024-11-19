# ID3v2 scripting

# MISC
eyeD3 -A "Season 5" -a "Mission To Zyxx" -N 21 -d 1 -D 1 -G comedy -Y 2019 --composer "Brendan Ryan" --add-image ../Season_05.jpg:FRONT_COVER *.mp3 --recording-date "" --v2

# TRACK NO
for i in *.mp3; do eyeD3 -n "$(cut -c 2-3 <<< $i)" "$i"; done

# TITLES
for i in *.mp3; do t="$(eyeD3 "$i" | grep '^title' | sed -rn 's/title:\s[0-9]{3}:\s(.*)$/\1/p')"; eyeD3 "$i" -t "$t"; done

for i in *.mp3; do j="$(cut -c 2-3 <<< "$i")"; eyeD3 "$i" -t "$(sed -n "${j}p" titles)"; done

# DESCRIPTIONS
for i in *.mp3; do desc="$(eyeD3 "$i" | grep '^Comment' -A1 | grep -v '^Comment')"; eyeD3 "$i" --remove-all-comments --add-comment "${desc}:Synopsis"; done

for i in *.mp3; do j="$(cut -c 2-3 <<< "$i")"; eyeD3 "$i" --add-comment "$(sed -n "${j}p" desc):Synopsis"; done
