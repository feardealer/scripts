#!/bin/bash

DUMP_DIR="/path/to/dir/"

create_traffic_dump() {
    local file_name="traffic_dump_$(date +%Y%m%d_%H%M%S).pcap"
    tcpdump -i any -s 0 -w "$DUMP_DIR/$file_name"
}

mkdir -p "$DUMP_DIR"

while true; do
    create_traffic_dump

    last_dump=$(ls -t "$DUMP_DIR" | head -n1)
    gzip "$DUMP_DIR/$last_dump"
    rm "$DUMP_DIR/$last_dump"

    sleep 3600
done
