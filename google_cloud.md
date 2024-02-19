# Google Cloud

#gcloud

## Notes

```sh
# get configs
gcloud projects describe $(gcloud config list --format 'value(core.project)') --format 'value(name)'
gcloud projects describe $(gcloud config get-value project) --format 'value(name)'
gcloud info --format='value(config.paths.active_config_path)'
gcloud info --format='value(config.paths.sdk_root)'
gcloud config configurations list --filter='is_active=True' --format='value(name)'

# service accounts
gcloud iam service-accounts update {{ sa }} \
  --display-name "..." --description "..."  # update the description and the display name
gcloud iam service-accounts get-iam-policy {{ sa }}  # check the IAM policy for sa
gcloud iam service-accounts add-iam-policy-binding {{ sa }} \
  --member {{ email }} --role roles/{{ role }}  # add a user to the policy
```
