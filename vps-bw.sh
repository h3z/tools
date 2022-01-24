#!/bin/bash
#url="https://justmysocks3.net/members/getbwcounter.php?service=367706&id=4c24d318-ece5-4879-899b-fd4c2bb8c9de"
url="https://justmysocks5.net/members/getbwcounter.php?service=367706&id=4c24d318-ece5-4879-899b-fd4c2bb8c9de"
a=`curl -s ${url} | jq .bw_counter_b`
used=`bc <<< "scale=2; $a/1024/1024/1024" | awk '{printf "%.2f", $0}'`
percent=`bc <<< "scale=2; $used/10" | awk '{printf "%.2f", $0}'`
echo ${percent}%: ${used} GB used out of 1 TB

