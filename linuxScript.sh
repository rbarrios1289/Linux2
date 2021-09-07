#!/bin/bash

# add users here
# set permissions




# add users to group
# also check if group exist, if not add also new group

$groupDev = developers
$user = ???

if grep -q $groupDev /etc/group
then
   usermod -a -G $groupDev $user
else
   sudo groupadd $groupDev 
   # adduser Kalle, Fnatte, Tjatte, Katte ??????
fi




# what permissions do "other-group" have?

# get files from features-branch on git

cd 

git clone https://github.com/me2001ru/Linux2.git featuresBranch
git checkout main
cp featuresBranch (git add; git commit; git push)
