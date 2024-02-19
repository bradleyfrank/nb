# Video Transcoding

## Notes

```sh
sudo docker pull ntodd/video-transcoding
sudo docker run -itv "$PWD":/data ntodd/video-transcoding
transcode-video --scan ./
transcode-video --encoder x265 -o movie.mkv ./  # transcode feature title to h265 mkv
transcode-video --encoder x265 --title <title> -o title.mkv ./  # transcode a title to h265 mkv

flac -cd "$f" | lame -b 192 - "${f%.*}.mp3"     # flac to mp3
ffmpeg -i "$f" -b:a 192K -vn "${f%.*}.mp3"      # mp4 to mp3
ffmpeg -i "$f" -c:a alac "${f%.*}.m4a"          # flac to m4a
ffmpeg -i "$f" -f flac "${f%.*}.flac" -vsync 0  # m4a to flac
ffmpeg -i input.mpg output.mp4                  # mpg to mp4
ffmpeg -i input.mp4 -vcodec libx264 -crf {18..24} output.mp4
ffmpeg -i input.mp4 -vcodec libx265 -crf {24..30} output.mp4
ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i "$f" -c copy \
  -bsf:a aac_adtstoasc "${f%.*}.mp4"            # m3u8 to mp4

makemkvcon backup --decrypt disc:0 /path/to/folder  # rip blu-ray as decrypted backup
makemkvcon mkv disc:0 all /path/to/folder           # rip blu-ray as mkv
makemkvcon mkv iso:/path/to/file.iso all /path/to/output                 # convert ISO to mkv
mkvmerge -o outfile.mkv infile_01.mp4 \+ infile_02.mp4 \+ infile_03.mp4  # merge mp4/mkv files

# rip multiple videos simultaneously
parallel --line-buffer --jobs 8 -a /path/to/list youtube-dl ...
```
