#!/bin/bash

DEVICE=$2

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root." 1>&2
   exit 1
fi

while read line; do

    echo "$line" | cryptsetup luksOpen "$DEVICE" encrypted 2>/dev/null

    # success
    if [[ $? -eq 0 ]]; then
        cryptsetup luksClose encrypted
        echo "Passphrase: $line"
        exit 0
    fi

done < "$1"

echo "Passphrase not contained in word list."
exit 1
