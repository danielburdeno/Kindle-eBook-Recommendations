mkdir -p ~/.streamlit/

echo "[theme]
primaryColor='#c5d4c9'
backgroundColor='#c5d4c9'
secondaryBackgroundColor='#e0a69b'
textColor='#000104'
[server]
headless = true
port = $PORT
enableCORS = false
"> ~/.streamlit/config.toml
