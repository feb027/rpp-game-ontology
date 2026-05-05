#!/usr/bin/env bash
set -euo pipefail
cd /home/aqua/rpp-game-ontology
exec /home/aqua/rpp-game-ontology/.venv/bin/python -m streamlit run app/main.py \
  --server.address 127.0.0.1 \
  --server.port 8515 \
  --server.headless true \
  --server.baseUrlPath rpp-game \
  --server.enableCORS false \
  --server.enableXsrfProtection false
