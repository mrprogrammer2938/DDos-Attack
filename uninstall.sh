#!/usr/bin/env bash
# This code write by Mr.nope
# DDos-Attacl v1.5.2
if [[ "$(id -u)" -ne 0 ]]; then
  echo "
Please Run This Programm as Root!
"
  exit 1
fi
main() {
      clear
      echo "Uninstalling..."
      sleep 2
      cd .. && rm -r DDos-Attack
      echo ""
      echo "Finish...!"
      echo "
Good Bye :(
"
      exit 1
}
main
