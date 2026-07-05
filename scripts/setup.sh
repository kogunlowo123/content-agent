#!/bin/bash
set -euo pipefail
echo "Setting up Content Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
