#!/bin/bash
for i in `seq 1 44`;
do
  ./p3 $(python -c "print 'a'*$i")
  echo $i
  echo $(python -c "print 'a'*$i")
done
