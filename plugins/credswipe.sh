#!/bin/bash

clear
echo "Swipe your card"
while [ 1 ]
do

    read data

    if [ "$data" = "" ]
    then 
        echo "Exiting"
        exit 0
    fi
	echo ""
	echo ""
    num="$(echo "$data"|cut -d\B -f2|cut -d\^ -f1)"
    name="$(echo "$data"|cut -d\^ -f2)"
    lname="$(echo "$name"|cut -d\/ -f1)"
    fname="$(echo "$name"|cut -d\/ -f2)"
    exdate="$(echo "$data"|cut -d\^ -f3)"
    exdate="${exdate:0:2}/${exdate:2:2}"

    echo "Card Number: $num"
    echo "Card Holder: $fname $lname"
    echo "Experation Date: $exdate"
    echo "----------------------------"
done
