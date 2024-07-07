# File Conversions

## Tags

#pdf #documents #pictures #json #diff

## Document and Image Conversion

```sh
pandoc file.md -f gfm -t dokuwiki -o file.wiki  # convert GitHub Markdown to DokuWiki format
qpdf --password="PASSWORD" --decrypt input.pdf output.pdf  # remove password from PDF
pdftk /path/to/input.pdf input_pw PROMPT output /path/to/output.pdf  # remove password from PDF
openssl enc -aes-256-cbc -salt -in /path/to/input -out /path/to/output  # encrypt file
openssl enc -d -aes-256-cbc -in /path/to/input -out /path/to/output  # decrypt file
soffice --headless --convert-to docx --outdir /tmp /path/to/doc  # convert doc to docx
libreoffice --headless --convert-to epub /path/to/odt  # convert odt to epub
convert /path/to/file -resize 50% /path/to/output  # resize image by 50%
convert -coalesce file.gif out.png  # extract gif images
heif-convert "$f" ${f/%.HEIC/.JPG}  # convert HEIC images
ffmpeg -i "$f" "${f%.webp}.jpg"  # convert webp images
```

## Renaming

```sh
for i in {1..20}; do ep="$(printf "S02E%02d\n" "$i")"; mv "./${ep}.mkv" "./${ep}.$(awk "NR == $i" episodes.txt).mkv"; done
```

## Comparing

```sh
fdupes --recurse --reverse --delete --noprompt .  # delete old duplicate images
diff -Nur oldfile newfile > patchfile  # produce a patch file
diff -q directory-1/ directory-2/  # compare two directories

# compare two files
vimdiff file1 file2
code --diff file1 file2
sdiff -s file1 file2
comm -12 < (sort file1) < (sort file2)
```

## Manipulation

```sh
jq -Rsa '.' < file.json  # escapes alll newlines and slashes
index_name="${indexes[$i]%$'\n'}"  # removes newlines from the array value
```

## Substitution

```sh
${vcs_info_msg_0_/(#s):(#e)/}  # remove stand-alone color (i.e. '^:$')
```

## Matching

```sh
paste file1 file2 > file3  # merge line-by-line
awk 'NR>1 {print $1}'  # skip first line in output
awk '/PATTERN/{f="newfile"++i;}{print > f;}'  # split a file at every PATTERN
awk '/PATTERN/{f="newfile"++i;next}{print > f;}'  # split file at every PATTERN but omit PATTERN
awk 'NR%n==1{f="newfile"++i;}{print > f}'  # split a file on every Nth line
awk '!x[$0]++'  # find non-adjacent unique lines
awk -vFS=. -vOFS=. '{$NF++;print}'  # increment version number
sed -i '1s/^/<added text> \n/'  # insert at top of file
sed -n '/PATTERN/,$p'  # print all lines, inclusively, from search string
sed '/PATTERN/q'  # print all lines up to the match
sed '$!N; /^\(.*\)\n\1$/!P; D'  # delete all consecutive duplicate lines from a file
sed ':a;N;$!ba;s/\n/\\n/g'  # replace newlines with '\n'
```
