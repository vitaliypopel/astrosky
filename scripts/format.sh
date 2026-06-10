#!/bin/bash

set -e

format_python_code() {
  echo -e "\n${YELLOW}Checking and fixing code...${NO_COLOR}"
  poetry run ruff check --fix

  echo -e "\n${YELLOW}Formatting code...${NO_COLOR}"
  poetry run ruff format .

  echo -e "\n${YELLOW}Sorting imports...${NO_COLOR}"
  poetry run isort .
}

format_core() {
  echo -e "\n${BLUE}Formatting core...${NO_COLOR}"
  cd core

  format_python_code

  cd ..
}

format_api() {
  echo -e "\n${BLUE}Formatting api...${NO_COLOR}"
  cd api

  format_python_code

  cd ..
}

format() {
  format_core
  format_api
}

main() {
  BLUE="\e[1;34m"
  GREEN="\e[1;32m"
  YELLOW="\e[0;33m"
  NO_COLOR="\e[0;0m"

  if [[ " $* " == *" --core "* ]]; then
    format_core
  elif [[ " $* " == *" --api "* ]]; then
    format_api
  else
    format
  fi

  echo -e "\n${GREEN}Code has been successfully formatted!${NO_COLOR}"
}

main "$@"
