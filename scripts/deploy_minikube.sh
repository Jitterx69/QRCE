#!/bin/bash
set -e

echo "========================================="
echo "QRCE Minikube Deployment"
echo "========================================="

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if minikube is installed
if ! command -v minikube &> /dev/null; then
    echo -e "${RED}Minikube is not installed. Please install it first.${NC}"
    echo "Visit: https://minikube.sigs.k8s.io/docs/start/"
    exit 1
fi

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    echo -e "${RED}kubectl is not installed. Please install it first.${NC}"
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Docker is not installed. Please install it first.${NC}"
    exit 1
fi

# Start minikube if not running
echo -e "${BLUE}Checking Minikube status...${NC}"
if ! minikube status &> /dev/null; then
    echo -e "${YELLOW}Starting Minikube...${NC}"
    minikube start --driver=docker --cpus=4 --memory=8192
else
    echo -e "${GREEN}Minikube is already running${NC}"
fi

# Configure Docker to use Minikube's Docker daemon
echo -e "${BLUE}Configuring Docker environment...${NC}"
eval $(minikube docker-env)

# Build Docker images
echo ""
echo -e "${BLUE}Building Docker images...${NC}"
echo "-----------------------------------------"

echo -e "${YELLOW}[1/3] Building Platform image...${NC}"
docker build -f cloud/docker/platform.Dockerfile -t qrce-platform:latest .

echo -e "${YELLOW}[2/3] Building Worker image...${NC}"
docker build -f cloud/docker/worker.Dockerfile -t qrce-worker:latest .

echo -e "${YELLOW}[3/3] Building QPU image...${NC}"
docker build -f cloud/docker/qpu.Dockerfile -t qrce-qpu:latest .

# Create namespace
echo ""
echo -e "${BLUE}Creating Kubernetes resources...${NC}"
echo "-----------------------------------------"

kubectl apply -f cloud/k8s/namespace.yaml

# Deploy services
echo -e "${YELLOW}Deploying Platform...${NC}"
kubectl apply -f cloud/k8s/platform-deployment.yaml

echo -e "${YELLOW}Deploying Worker...${NC}"
kubectl apply -f cloud/k8s/worker-deployment.yaml

echo -e "${YELLOW}Deploying QPU...${NC}"
kubectl apply -f cloud/k8s/qpu-deployment.yaml

echo -e "${YELLOW}Creating Services...${NC}"
kubectl apply -f cloud/k8s/service.yaml

# Deploy observability stack (optional)
if [ -f cloud/k8s/prometheus.yaml ]; then
    echo -e "${YELLOW}Deploying Prometheus...${NC}"
    kubectl apply -f cloud/k8s/prometheus.yaml
fi

if [ -f cloud/k8s/grafana.yaml ]; then
    echo -e "${YELLOW}Deploying Grafana...${NC}"
    kubectl apply -f cloud/k8s/grafana.yaml
fi

# Deploy ingress (optional)
if [ -f cloud/k8s/ingress.yaml ]; then
    echo -e "${YELLOW}Deploying Ingress...${NC}"
    kubectl apply -f cloud/k8s/ingress.yaml
fi

# Wait for deployments to be ready
echo ""
echo -e "${BLUE}Waiting for deployments to be ready...${NC}"
kubectl wait --for=condition=available --timeout=300s \
    deployment/qrce-platform \
    deployment/qrce-worker \
    deployment/qrce-qpu \
    -n qrce

# Get service URLs
echo ""
echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}QRCE deployed successfully!${NC}"
echo -e "${GREEN}=========================================${NC}"
echo ""
echo "Deployments:"
kubectl get deployments -n qrce

echo ""
echo "Pods:"
kubectl get pods -n qrce

echo ""
echo "Services:"
kubectl get services -n qrce

echo ""
echo -e "${BLUE}Access the Platform API:${NC}"
echo "  minikube service qrce-platform -n qrce --url"

echo ""
echo -e "${BLUE}Useful commands:${NC}"
echo "  View logs:        kubectl logs -f deployment/qrce-platform -n qrce"
echo "  Scale workers:    kubectl scale deployment qrce-worker --replicas=3 -n qrce"
echo "  Delete all:       kubectl delete namespace qrce"
echo "  Dashboard:        minikube dashboard"
echo ""
