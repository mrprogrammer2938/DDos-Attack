#!/usr/bin/env bash
# This code write by Mr.nope
if [[ "$id -u" -ne 0 ]]; then
  echo "Please Run This Programm as Root!"
  exit 1
fi

clear
echo "Uninstalling..."
sleep 2
cd .. && rm -r DDos-Attack
echo ""
echo "Uninstalling..., Finish...!"
echo ""
exit 1