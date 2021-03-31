#!/bin/bash
i=1
while [ $i -le 20 ]; do
cd Config$i
make
msub submit.sh
cd ..
i=$((i+1))
done