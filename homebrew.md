# Homebrew

## Create a Tap

```sh
brew tap homebrew/core --force
brew tap hashicorp/tap/terraform

brew extract homebrew/core/istioctl --version 1.18.2 oreillymedia/orm
brew extract homebrew/core/helm --version 3.11.1 oreillymedia/orm
brew extract hashicorp/tap/terraform --version 1.5.7 oreillymedia/orm
brew extract hashicorp/tap/vault --version 1.10.3 oreillymedia/orm
brew extract hashicorp/tap/packer --version 1.10.1 oreillymedia/orm

for f in Formula/*.rb; do /usr/bin/sed -i '' -E "s/([a-zA-Z]+)AT[0-9]+/\1/" "$f"; done
for f in Formula/*.rb; do
  name="$(/usr/bin/grep -Eo "class\s[a-zA-Z]+" "$f" | /usr/bin/awk '{print $2}' | tr '[:upper:]' '[:lower:]')"
  mv "$f" "Formula/${name}.rb"
done
```

