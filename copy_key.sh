#!/bin/bash

if [ ! -f ~/.ssh/id_ed25519.pub ]; then
    echo "Публичный SSH-ключ (id_ed25519.pub) не найден в директории ~/.ssh/"
    exit 1
fi

if [ ! -f servers.txt ]; then
    echo "Файл servers.txt не найден в текущей директории."
    exit 1
fi

while IFS= read -r server; do
    echo "Копирование SSH-ключа на сервер: $server"
    ssh-copy-id -i ~/.ssh/id_ed25519_2.pub "root@$server" -p 22154
done < servers.txt

echo "Все ключи были скопированы на серверы из списка."
