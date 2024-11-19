# Digital Ocean

```sh
# create a reserved IP address
doctl compute fip create --region nyc1

# get list of public images
doctl compute image list --public --output json \
  | jq -j '.[] | select(.type == "base") | .distribution," ",.name,"\t",.slug,"\t",.id,"\n"' \
  | sort \
  | fzf --with-nth 1 -d "\t" \
  | awk -F '\t' '{print $3}' \
  | xargs -I {} doctl compute image get {} --format Slug --no-header
```
