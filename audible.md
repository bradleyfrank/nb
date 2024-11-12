# Audible

https://github.com/mkb79/audible-cli

1. create virtualenv
2. `pip install audible-cli`
3. `audible quickstart`
4. `audible library list`
5. `audible download --aax-fallback --asin ASIN`
6. `ffprobe BOOK.aax 2>&1 | grep "file checksum" | awk -F '=' '{print $3}' | xargs > checksum`

## AAX

7. `audible activation-bytes 2>/dev/null > hex`
8. `ffmpeg -activation_bytes "$(cat ./hex)" -i BOOK.aax -vn -c:a copy BOOK.m4b`

## AAXC

7. `key="$(jq -r '.content_license.license_response.key' < BOOK.voucher)"`
8. `iv="$(jq -r '.content_license.license_response.iv' < BOOK.voucher)"`
9. `ffmpeg -y -audible_key "$key" -audible_iv "$iv" -i BOOK.aaxc -c copy -map 0 BOOK.mp4`
