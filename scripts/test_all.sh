#!/bin/bash
set -e

echo "========================================="
echo "QRCE Test Suite"
echo "========================================="

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo -e "${RED}pytest not found. Installing...${NC}"
    pip install pytest
fi

# Run Python tests
echo ""
echo "Running Python tests..."
echo "-----------------------------------------"

# Test engine layer
echo "Testing Layer 1: Classical Reflexive Core..."
pytest engine/tests/ -v

# Test quantum layer
echo ""
echo "Testing Layer 2: Quantum Reflexive Core..."
pytest quantum/tests/ -v

# Test control layer
echo ""
echo "Testing Layer 3: Ethical & Computability Control..."
pytest control/tests/ -v

# Test runtime layer
echo ""
echo "Testing Layer 4: Runtime & Experiment System..."
pytest runtime/tests/ -v

# Run all tests with coverage
echo ""
echo "Running full test suite with coverage..."
echo "-----------------------------------------"
pytest engine/tests/ quantum/tests/ control/tests/ runtime/tests/ \
    --cov=engine --cov=quantum --cov=control --cov=runtime \
    --cov-report=term-missing \
    --cov-report=html:coverage_report

echo ""
echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}All Python tests passed!${NC}"
echo -e "${GREEN}=========================================${NC}"

# Run Rust tests (if cargo is available)
if command -v cargo &> /dev/null; then
    echo ""
    echo "Running Rust tests..."
    echo "-----------------------------------------"
    cd platform
    cargo test --all
    cd ..
    echo -e "${GREEN}All Rust tests passed!${NC}"
else
    echo -e "${RED}Cargo not found. Skipping Rust tests.${NC}"
fi

echo ""
echo "Coverage report generated at: coverage_report/index.html"
echo ""
