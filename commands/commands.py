# kubectl run <pod name> --image=<image>
# kubectl apply -f <file.yaml>

# kubectl get pods
# kubectl get pods -o wide

# kubectl describe pod <pod name>
# kubectl delete pod <pod name>
# kubectl edit pod <pod name>

# kubectl create -f replicaset-definition.yaml
# kubectl get replicaset

# kubectl delete replicaset <replica-set-name>
# kubectl replace -f replicaset-definition.yaml

# kubectl scale --replica=6 -f replicaset-definition.yaml
# kubectl edit replicaset myapp-replicaset

# kubectl get deployments
# kubectl get pods
# kubectl get all
# kubectl describe deployment myapp-deployment

# kubectl create deployment http-frontend --image=httpd:2.4-alpine --replicas=3
# kubectl rollout status deployment myapp-deployment
# kubectl apply -f deployment-definition.yaml
# kubectl set image deployment myapp-deployment nginx-container=nginx:1.9.1

# kubectl rollout undo deployment myapp-deployment
# kubectl rollout status deployment myapp-deployment
# kubectl delete deployment myapp-deployment

# kubectl rollout history deployment apps/mydeployment
# kubectl create -f deployment.yaml --record

# kubectl edit deployment <deployment-name>

# kubectl create -f service-definition.yaml
# kubectl get services

# minicube service <myapp-service> -url
# kubectl get deployments, services

# kubectl run redis --image=redis123 --dry-run=client -o yaml > redis-definition.yaml
# kubectl create -f redis-definition.yaml

# kubectl edit pod redis
# kubectl apply -f redis-definition.yaml

# kubectl get pod -o yaml > pod-definition.yaml
# kubectl get all
# kubectl get pods --all-namespaces

# kubectl expose pod redis --port=6378 --name redis-service --dry-run=client -o yaml
# kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml

# kubectl expose pod nginx --port=80 --name nginx-service --type=NodePort --dry-run=client -o yaml
# kubectl run httpd --image=http:alpine --port=80 --expose

# kubectl replace --force -f /tmp/pod-def.yaml
# kubectl create configmap  <config-name> --from-file=<path-to-file>

# kubectl get configmaps
# kubectl describe configmaps

# kubectl create secret generic <secret-name> --from-literal=<key>=<value>

# kubectl get secrets

# kubectl create secret generic <secret name> --from-file=<path-to-file>

# kubectl describe secrets
# kubectl get secret app-secret -o yaml

# kubectl describe pod <pod-name> | grep -AS staticmethod

# kubectl create serviceaccount <account-name>
# kubectl get serviceaccount

# kubectl describe secret <token-name>
# kubectl create token <serviceaccountname>

# kubectl taint nodes node-name key=value:taint-effect
# kubectl label nodes <node-name> <label-key>=<label-value>

# kubectl get pods --watch
# kubectl describe node <nodename> | grep -i taints

# kubectl edit pod <pod-name> --namespace <namespace>
# kubectl get pod <pod-name> -o yaml > pod.yaml

# kubectl logs -f <pod-name>
# kubectl logs -f <pod-name> <container-name>

# kubectl top pod
# kubectl get pods --selector <label>=<value>
# kubectl rollout status <deployment>

# kubectl set image <deployment> nginx-container=nginx:1.9.1
# kubectl get replicasets

# kubectl rollout undo <deployment name>
# kubectl rollout status deployment <deployment name>
# kubectl rollout history deployment <deployment name> --revision=3

# kubectl rollout history deployment <deployment-name>
# kubectl get jobs

# kubectl logs <job name>
# kubectl delete <job name>

# kubectl get cronjob
# kubectl get all -A
# kubectl get pods -A
# kubectl get ingress --all-namespaces

# kubectl describe ingress --namespace <app-space>
# kubectl edit ingress --namespace <namespace-name>

# kubectl get ingress -n <namespace>
# kubectl create ingress <ingress-name> -- namespace \
#     <namespace-name> --rule="<path-name>" <service-name>:<port>

# kubectl create namespace <namespace>
# kubectl create configmap <config-name> --namespace <namespace-name>

# kubectl create serviceaccount <serviceaccount-name> --namespace <namespace>

# kubectl get roles -n <namespace>
# kubectl get rolebindings -n <namespace>

# kubectl describe role <role-name> -n <namespace>
# kubectl get persistentvolumeclaim

# kubectl delete persistentvolumeclaim <name>
# kubectl exec webapp -- cat /log/app.log

# kubectl exec <pod-name> -- cat <file>
# kubectl get pvc

# kubectl get pv
# kubectl describe sc <sc-name>

# kubectl get pods \
#     -- server my-kube-playground:6443
#     -- client-key admin.key
#     -- client-certificate admin-crt 
#     -- certificate-authority ca.crt

# kubectl get pods --kubeconfig config
# kubectl config view

# kubectl config use-context pred-user@production
# kubectl get roles
# kubectl get rolebindings

# kubectl auth can-i create deployments
# kubectl auth can-i create deployments --as dev-UserWarning

# kubectl create role developer --namespace=default --verb=list,create,delete --resource=pods

# kubectl create rolebinding dev-user-binding --namespace=default --role=developer --user=dev-user 
# kubectl get pods --selector <label>=<value>

# kubectl get cronjob
    