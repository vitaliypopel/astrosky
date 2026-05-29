#!/bin/bash

BLUE="\e[1;34m"
GREEN="\e[1;32m"
YELLOW="\e[1;33m"
NO_COLOR="\e[0;0m"

echo -e "${BLUE}Formatting code...${NO_COLOR}"
poetry run ruff format . >/dev/null 2>&1

echo -e "${YELLOW}Sorting imports...${NO_COLOR}"
poetry run isort . >/dev/null 2>&1

echo -e "${GREEN}Code has been successfully formatted!${NO_COLOR}"
