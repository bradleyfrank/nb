# File Conversions

## Tags

#pdf #documents #pictures

## Notes

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
