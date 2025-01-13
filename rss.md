# RSS


How to Configure Newsboat with FreshRSS?

In FreshRSS go to your profile and set an API password under 'External access via API' and see what username you should use.
Create a config file called 'config' in your newsboat config and add:

```
urls-source "freshrss"
freshrss-url "http://<your-IP>:9800/api/greader.php"
freshrss-login "your-username"
freshrss-password "the-api-password"
```
