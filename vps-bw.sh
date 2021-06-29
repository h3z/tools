#!/bin/bash
a=`curl -s "https://justmysocks3.net/members/getbwcounter.php?service=367706&id=3b7af7bb-86a3-4e64-8f20-f2f14d29e658" | jq .bw_counter_b`
used=`bc <<< "scale=2; $a/1024/1024/1024"`
echo $[a/1024/1024/1024/5]% ${used}G
