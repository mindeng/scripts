#! /bin/sh

while IFS=' ' read -r col1 col2
do
    if cmp -s $col1 $col2; then
        rm $col2
        echo deleted $col2
    fi
done <"${1:-/dev/stdin}"    # read from file or stdin
