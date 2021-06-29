#!/bin/bash
a=`curl -s "https://justmysocks3.net/members/getbwcounter.php?service=367706&id=5afe44ae-a620-44a2-8e7a-9e01257f68c5" | jq .bw_counter_b`
used=`bc <<< "scale=2; $a/1024/1024/1024"`
echo $[a/1024/1024/1024/5]% ${used}G
