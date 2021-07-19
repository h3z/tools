#!/bin/bash
url="https://justmysocks3.net/members/getbwcounter.php?service=367706&id=3b7af7bb-86a3-4e64-8f20-f2f14d29e658"
a=`curl -s ${url} | jq .bw_counter_b`
used=`bc <<< "scale=2; $a/1024/1024/1024" | awk '{printf "%.2f", $0}'`
percent=`bc <<< "scale=2; $used/5" | awk '{printf "%.2f", $0}'`
echo ${percent}%: ${used} GB used out of 500 GB

