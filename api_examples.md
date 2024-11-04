# API Examples

## TheMovieDB

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/search/tv?query=<title>' \
  --header 'Authorization: Bearer <token>' \
  --header 'accept: application/json' \
    | jq -r '.results[]|[.name,.first_air_date]|@csv' \
    | awk -F '","' '{print $1" ("$2")"}' \
    | tr -d '"' \
    | fzf
```
