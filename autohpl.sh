#!/bin/bash
while true
do
	sudo clush -w e[5,8] bash /home/laekov/scripts/fan/localfan_supermicro 100
	sleep 20
	sudo clush -w e[5,8] bash /home/laekov/scripts/fan/localfan_supermicro 10
	./hplit.sh
	./xiu.py
done
