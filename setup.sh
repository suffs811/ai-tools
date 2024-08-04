#!/bin/bash

echo "[+] downloading dependencies..."
python3 -m pip install openai 2>/dev/null
python3 -m pip install openai_secret_manager 2>/dev/null

echo "[+] updating file names..."
mv priv-ai.py priv-ai 2>/dev/null
mv tool-ai.py tool-ai 2>/dev/null
mv sum-ai.py sum-ai 2>/dev/null

echo "[+] updating file privileges..."
chmod +x priv-ai.py priv-ai 2>/dev/null
chmod +x tool-ai.py tool-ai 2>/dev/null
chmod +x sum-ai.py sum-ai 2>/dev/null

echo "[+] adding tools to PATH..."
cp -p $(pwd)/* /usr/bin 2>/dev/null

echo "[+] complete."
