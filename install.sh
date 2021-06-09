#!/usr/bin/bash
# This code write by Mr.nope
printf '\033]2;Installing\a'
clear
echo ""
echo "Installing... "
sleep 1
echo "   ____  ____   __   ____     __  ____  ____  __    ___  __ _ "
echo "  (    \(    \ /  \ / ___)   / _\(_  _)(_  _)/ _\  / __)(  / )"
echo "   ) D ( ) D ((  O )\___ \  /    \ )(    )( /    \( (__  )  ( "
echo "  (____/(____/ \__/ (____/  \_/\_/(__)  (__)\_/\_/ \___)(__\_)"
echo "   Version: 1.3.0"
echo ""
sleep 1
sudo apt install python
sudo apt install python-pip
pip install --upgrade pip
chmod +x DDos.py
cd Update && chmod +x update && cd ..
pip install requirments.txt
echo ""
echo "finish..., Installing...!"
echo ""
echo "usage: python DDos.py"
echo ""
exit 1
