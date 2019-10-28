#! /bin/bash

urls=(
  https://github.com/mindeng
  https://github.com/mindeng/scripts
)

for i in "${urls[@]}"; do
    curl --header "Range: bytes=10-20" $i > /dev/null || { echo 'failed' ; exit 1; }
done
