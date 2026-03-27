#!/bin/bash

echo "Räume auf..."
kubectl delete namespace k8s-demo --ignore-not-found
kubectl create namespace k8s-demo

echo "Erstelle ConfigMaps..."
kubectl create configmap victim-code --from-file=victim.py -n k8s-demo
kubectl create configmap control-code --from-file=control.py -n k8s-demo

echo "Deploye..."
kubectl apply -f manifests.yaml

echo "Warte bis alles läuft..."
kubectl wait --for=condition=ready pod --all -n k8s-demo --timeout=120s

echo "Starte Tunnels... (Ctrl+C zum Beenden)"

# Cleanup Funktion für Ctrl+C
trap 'kill $(jobs -p)' EXIT

# Die magischen Endlosschleifen, die den Disconnect überleben
(while true; do kubectl port-forward svc/victim-1 4000:8080 -n k8s-demo > /dev/null 2>&1; sleep 1; done) &
(while true; do kubectl port-forward svc/victim-2 4001:8080 -n k8s-demo > /dev/null 2>&1; sleep 1; done) &
(while true; do kubectl port-forward svc/victim-3 4002:8080 -n k8s-demo > /dev/null 2>&1; sleep 1; done) &
(while true; do kubectl port-forward svc/control 6969:8080 -n k8s-demo > /dev/null 2>&1; sleep 1; done)

wait
