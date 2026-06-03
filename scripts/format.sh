#!/bin/bash

set -e

setup() {
  BLUE="\e[1;34m"
  GREEN="\e[1;32m"
  YELLOW="\e[0;33m"
  NO_COLOR="\e[0;0m"

  MODE="all"
  if [[ " $* " == *" --core "* ]]; then
    MODE="core"
  elif [[ " $* " == *" --api "* ]]; then
    MODE="api"
  fi

  echo -e "${BLUE}Setup Mode:${NO_COLOR}\t${GREEN}$MODE${NO_COLOR}"
}

format_core() {
  echo -e "\n${BLUE}Formatting core...${NO_COLOR}"
  cd core

  echo -e "\n${YELLOW}Formatting code...${NO_COLOR}"
  poetry run ruff format .

  echo -e "\n${YELLOW}Sorting imports...${NO_COLOR}"
  poetry run isort .

  cd ..
}

format_api() {
  echo -e "\n${BLUE}Formatting api...${NO_COLOR}"
  cd api

  echo -e "\n${YELLOW}Formatting code...${NO_COLOR}"
  poetry run ruff format .

  echo -e "\n${YELLOW}Sorting imports...${NO_COLOR}"
  poetry run isort .

  cd ..
}

format() {
  format_core
  format_api
}

main() {
  setup "$@"

  if [[ "$MODE" == "core" ]]; then
    format_core
  elif [[ "$MODE" == "api" ]]; then
    format_api
  else
    format
  fi

  echo -e "\n${GREEN}Code has been successfully formatted!${NO_COLOR}"
}

main "$@"
