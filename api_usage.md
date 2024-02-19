# API Usage

## Tags

#git #github

## Notes

```sh
gh api search/repositories\?q=org:<org>+language:<language>
gh api search/issues\?q=repo:<org>/<repo>+is:pr+is:merged
gh api search/issues\?q=repo:<org>/<repo>+is:pr+is:merged+merged:\>=<YYYY-MM-DD>
gh api search/repositories\?q=org:<org>+language:<language> | jq ' .items | .[] | .name'
gh api -X PATCH /repos/<org>/<repo> -f archived=true

# GET GitHub Gist
curl --fail --silent \
  --header "Accept: application/vnd.github.v3+json" \
  --header "Authorization: token <token>" \
  https://api.github.com/gists/<id>

# PATCH GitHub Gist
curl --fail --silent \
  --header "Accept: application/vnd.github.v3+json" \
  --header "Authorization: token <token>" \
  --request PATCH https://api.github.com/gists/<id> \
  --data "{\"files\": { \"filename\": { \"content\": \"...\" }}}"

# POST GitHub Gist
curl --fail --silent \
  --header "Accept: application/vnd.github.v3+json" \
  --header "Authorization: token <token>" \
  --request POST https://api.github.com/gists \
  --data "{\"files\": { \"cmarks\": { \"content\": \"...\" }}}"
```
