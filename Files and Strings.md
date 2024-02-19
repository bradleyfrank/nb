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
