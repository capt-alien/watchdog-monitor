#!/bin/bash

SERVICE_NAME=watchdog.service
SERVICE_PATH=/etc/systemd/system/$SERVICE_NAME
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
USER_NAME=$(whoami)

echo "🔧 Setting up Watchdog Monitor..."

# 1. Copy the service file
echo "➡️ Copying systemd service file to $SERVICE_PATH"
sudo cp "$SCRIPT_DIR/$SERVICE_NAME" "$SERVICE_PATH"

# 2. Replace 'alien' with actual user if needed
sudo sed -i "s/^User=.*/User=$USER_NAME/" "$SERVICE_PATH"

# 3. Create log files and set permissions
echo "📂 Creating log files..."
mkdir -p "$SCRIPT_DIR/logs"
touch "$SCRIPT_DIR/watchdog.out" "$SCRIPT_DIR/watchdog.err"
chmod 644 "$SCRIPT_DIR"/*.out "$SCRIPT_DIR"/*.err

# 4. Prompt to create the .env file
ENV_FILE=/etc/watchdog.env
if [ ! -f "$ENV_FILE" ]; then
    echo "🔐 Creating $ENV_FILE"
    sudo bash -c "echo 'EMAIL_PASSWORD=your_password_here' > $ENV_FILE"
    sudo chmod 600 "$ENV_FILE"
    echo "⚠️ Please update the EMAIL_PASSWORD in $ENV_FILE"
fi

# 5. Reload systemd, enable and start the service
echo "🔁 Reloading systemd..."
sudo systemctl daemon-reload

echo "🚀 Enabling and starting watchdog.service..."
sudo systemctl enable watchdog.service
sudo systemctl restart watchdog.service

echo "✅ Setup complete. Use 'sudo systemctl status watchdog.service' to verify."