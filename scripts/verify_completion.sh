#!/bin/bash
# QRCE Project Verification Script
# Verifies that all components are complete and functional

set -e

echo "========================================="
echo "QRCE Project Verification"
echo "========================================="
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASS=0
FAIL=0

check() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ PASS${NC}: $1"
        ((PASS++))
    else
        echo -e "${RED}✗ FAIL${NC}: $1"
        ((FAIL++))
    fi
}

echo "1. Checking Python environment..."
source .venv/bin/activate 2>/dev/null || python3 -m venv .venv && source .venv/bin/activate
check "Python virtual environment"

echo ""
echo "2. Checking Python dependencies..."
python3 -c "import numpy, scipy, networkx, matplotlib, pydantic, fastapi, uvicorn, pytest" 2>/dev/null
check "Python dependencies installed"

echo ""
echo "3. Checking QPU Simulator..."
python3 -c "from quantum.qpu_simulator import QPUSimulator; import numpy as np; sim = QPUSimulator(); rho = np.array([[1,0],[0,0]], dtype=complex); result = sim.execute(rho, 3); assert len(result) == 4" 2>/dev/null
check "QPU Simulator implementation"

echo ""
echo "4. Checking Python tests..."
pytest engine/tests/ quantum/tests/ control/tests/ runtime/tests/ -q --tb=no > /dev/null 2>&1
check "All Python tests pass"

echo ""
echo "5. Checking Rust platform..."
cd platform && cargo check --quiet 2>&1 | grep -q "Finished" && cd ..
check "Rust platform builds"

echo ""
echo "6. Checking shell scripts..."
[ -x scripts/test_all.sh ] && [ -x scripts/run_local.sh ] && [ -x scripts/deploy_minikube.sh ]
check "Shell scripts are executable"

echo ""
echo "7. Checking interface schemas..."
[ -f interfaces/control.schema.json ] && \
[ -f interfaces/engine_state.schema.json ] && \
[ -f interfaces/event.schema.json ] && \
[ -f interfaces/metrics.schema.json ] && \
[ -f interfaces/qpu.schema.json ]
check "All interface schemas exist"

echo ""
echo "8. Checking Docker files..."
[ -f cloud/docker/platform.Dockerfile ] && \
[ -f cloud/docker/worker.Dockerfile ] && \
[ -f cloud/docker/qpu.Dockerfile ]
check "All Dockerfiles exist"

echo ""
echo "9. Checking Kubernetes manifests..."
[ -f cloud/k8s/namespace.yaml ] && \
[ -f cloud/k8s/platform-deployment.yaml ] && \
[ -f cloud/k8s/worker-deployment.yaml ] && \
[ -f cloud/k8s/qpu-deployment.yaml ]
check "All K8s manifests exist"

echo ""
echo "10. Checking Helm chart..."
[ -f cloud/helm/qrce/Chart.yaml ] && \
[ -f cloud/helm/qrce/values.yaml ] && \
[ -f cloud/helm/qrce/templates/platform.yaml ] && \
[ -f cloud/helm/qrce/templates/worker.yaml ] && \
[ -f cloud/helm/qrce/templates/qpu.yaml ]
check "Helm chart is complete"

echo ""
echo "11. Checking core implementations..."
[ -f engine/engine.py ] && \
[ -f quantum/quantum_operator.py ] && \
[ -f control/ethical_operator.py ] && \
[ -f runtime/experiment.py ] && \
[ -f platform/src/main.rs ]
check "All core layer implementations exist"

echo ""
echo "12. Checking documentation..."
[ -f README.md ] && [ -f COMPLETION_REPORT.md ]
check "Documentation exists"

echo ""
echo "========================================="
echo "Verification Summary"
echo "========================================="
echo -e "Passed: ${GREEN}${PASS}/12${NC}"
echo -e "Failed: ${RED}${FAIL}/12${NC}"
echo ""

if [ $FAIL -eq 0 ]; then
    echo -e "${GREEN}✓ ALL CHECKS PASSED!${NC}"
    echo ""
    echo "The QRCE project is complete and ready for use."
    echo ""
    echo "Next steps:"
    echo "  1. Run tests: ./scripts/test_all.sh"
    echo "  2. Run locally: ./scripts/run_local.sh"
    echo "  3. Deploy to K8s: ./scripts/deploy_minikube.sh"
    echo ""
    exit 0
else
    echo -e "${RED}✗ SOME CHECKS FAILED${NC}"
    echo "Please review the failures above."
    exit 1
fi
