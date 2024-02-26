# K8s

## Tags

#kubernetes #k8s

## Notes

```sh
kubectl get pods -selector=app=<app>
kubectl patch pod <pod> -p '{"metadata":{"finalizers":null}}'   # remove finalizer
kubectl delete --wait=false pod <pod> --grace-period=<seconds>  # terminate gracefully
kubectl delete --grace-period=1 pod <pod>                       # terminate immediately
kubectl delete --grace-period=0 pod <pod> --force=true          # terminate forced
kubectl scale --replicas=3 deployment <deployment>              # scale deployment replicas
kubectl rollout history deployment <deployment> [--revision=<num>]
kubectl cordon <node>    # schedule
kubectl uncordon <node>  # unschedule
kubectl get secret <secret> -o json \
  | jq -r '.data."tls.crt"' \
  | base64 --decode \
  | openssl x509 -noout -enddate  # verify certificate
kubectl proxy --port=8001 && curl http://localhost:8001/api/v1/namespace/default/pods  # proxy
kubectl port-forward <pod> <port>  # port-forward
kubectl top <pods|nodes> --sort-by=<memory|cpu>
```

Get pods by node:

```sh
kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=<node>
```
