# K8s Self-Healing Demo (The Bare Minimum)

## Purpose
To be honest: The architecture of this application is s*ht. It is not a production-grade setup, ignores platform engineering best practices, and runs on a rudimentary Docker Desktop cluster. 

The sole purpose and intent of this project is the isolated proof of a core Kubernetes concept: **Self-healing and the automatic restoration of the desired state (Reconciliation Loop).**

## The Components
The setup consists of four microservices:
* **3x Victim Pods (Ports 4000, 4001, 4002):** Dumb Flask containers. They merely display their current K8s pod name and wait for their termination.
* **1x Control Panel (Port 6969):** A simple UI to send targeted kill signals (SIGTERM) to the individual pods.

## How to run
The startup script deploys the manifests, ConfigMaps, and enforces persistent port-forwards to localhost to bypass the tunnel collapsing when a pod dies.

```bash
chmod +x start.sh
./start.sh
```

## Cleanup / Teardown
To stop the application, simply press Ctrl+C in your terminal to kill the active port-forwards.

Since all resources are cleanly isolated within their own namespace, you can completely remove the deployments, services, and ConfigMaps from your cluster with a single command:

```bash
kubectl delete namespace k8s-demo
```
