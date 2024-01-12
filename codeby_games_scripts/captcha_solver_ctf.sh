#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Использование: $0 <base64-строка>"
    exit 1
fi

base64_input=$1

decoded_string=$(echo "$base64_input" | base64 -d)
result=$((decoded_string))

echo "'$decoded_string' = $result"

