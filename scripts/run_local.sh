#!/bin/bash
set -e

echo "========================================="
echo "QRCE Local Development Environment"
echo "========================================="

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check dependencies
echo "Checking dependencies..."

if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed."
    exit 1
fi

if ! command -v cargo &> /dev/null; then
    echo "Cargo is required but not installed."
    exit 1
fi

# Install Python dependencies
echo -e "${BLUE}Installing Python dependencies...${NC}"
pip install -q numpy scipy networkx matplotlib pydantic fastapi uvicorn pytest pytest-cov

# Build Rust platform
echo -e "${BLUE}Building Rust platform...${NC}"
cd platform
cargo build --release
cd ..

# Create log directory
mkdir -p logs

# Start services in background
echo ""
echo -e "${GREEN}Starting QRCE services...${NC}"
echo "-----------------------------------------"

# Start QPU Simulator
echo -e "${YELLOW}[1/3] Starting QPU Simulator on port 9100...${NC}"
python3 -m uvicorn quantum.qpu_server:app --host 0.0.0.0 --port 9100 > logs/qpu.log 2>&1 &
QPU_PID=$!
echo "QPU Simulator PID: $QPU_PID"

# Wait for QPU to start
sleep 2

# Start Python Worker
echo -e "${YELLOW}[2/3] Starting Python Worker on port 9000...${NC}"
python3 -m uvicorn runtime.rpc_server:app --host 0.0.0.0 --port 9000 > logs/worker.log 2>&1 &
WORKER_PID=$!
echo "Worker PID: $WORKER_PID"

# Wait for worker to start
sleep 2

# Start Rust Platform
echo -e "${YELLOW}[3/3] Starting Rust Platform on port 8080...${NC}"
./platform/target/release/qrce-platform > logs/platform.log 2>&1 &
PLATFORM_PID=$!
echo "Platform PID: $PLATFORM_PID"

# Wait for platform to start
sleep 2

# Save PIDs to file for cleanup
echo "$QPU_PID" > logs/qpu.pid
echo "$WORKER_PID" > logs/worker.pid
echo "$PLATFORM_PID" > logs/platform.pid

echo ""
echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}QRCE is running!${NC}"
echo -e "${GREEN}=========================================${NC}"
echo ""
echo "Services:"
echo "  - Platform API:    http://localhost:8080"
echo "  - Python Worker:   http://localhost:9000"
echo "  - QPU Simulator:   http://localhost:9100"
echo ""
echo "Logs:"
echo "  - Platform:  logs/platform.log"
echo "  - Worker:    logs/worker.log"
echo "  - QPU:       logs/qpu.log"
echo ""
echo "To stop all services, run:"
echo "  kill $PLATFORM_PID $WORKER_PID $QPU_PID"
echo ""
echo "Or use: pkill -f 'qrce-platform|uvicorn'"
echo ""

# Keep script running and tail logs
echo "Press Ctrl+C to stop all services and exit"
echo ""

# Trap Ctrl+C to cleanup
trap "echo ''; echo 'Stopping services...'; kill $PLATFORM_PID $WORKER_PID $QPU_PID 2>/dev/null; rm -f logs/*.pid; echo 'All services stopped.'; exit 0" INT

# Tail all logs
tail -f logs/platform.log logs/worker.log logs/qpu.log
