#! /bin/bash

set -euo pipefail

kubectl apply -f storage_account_secret.yaml
kubectl apply -f hello_world_1.yaml
kubectl apply -f hello_world_2.yaml
