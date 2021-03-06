#!/bin/bash

stall=0
for uuid in $(nova list | grep -E '(ACTIVE|ERROR|BUILD)' | awk '{print $2;}'); do
    nova delete $uuid
    stall=$(($stall+3))
done
sleep $stall

stall=0
for uuid in $(nova list | grep -E '(BLESSED)' | awk '{print $2;}'); do
    nova discard $uuid
    stall=$(($stall+3))
done
sleep $stall

for uuid in $(nova secgroup-list | grep -i 'created by grinder' | awk '{print $2}'); do 
    nova secgroup-delete $uuid;
done
