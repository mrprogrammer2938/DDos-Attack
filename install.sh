#!/usr/bin/bash
# This code write by (Mr.nope)
# installing DDosAttack package!
clear
time 1
echo ""
echo "   installing... "
time 2
echo "   ____  ____   __   ____     __  ____  ____  __    ___  __ _ "
echo "  (    \(    \ /  \ / ___)   / _\(_  _)(_  _)/ _\  / __)(  / )"
echo "   ) D ( ) D ((  O )\___ \  /    \ )(    )( /    \( (__  )  ( "
echo "  (____/(____/ \__/ (____/  \_/\_/(__)  (__)\_/\_/ \___)(__\_)"
echo ""
time 1
sudo apt install python
sudo apt install python-pip
pip install --upgrade pip
chmod +x ddosattack.py
pip install requirments.txt
echo ""
echo "finish!"
echo ""
echo "usage: "
echo "      python ddosattack.py"
echo ""
