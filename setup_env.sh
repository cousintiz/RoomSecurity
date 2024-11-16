!/bin/bash

# Script to create a .env file

# Prompt user for input
echo "Enter API_KEY:"
read -r API_KEY

echo "Enter SENDER_EMAIL:"
read -r SENDER_EMAIL

echo "Enter RECEIVER_EMAIL:"
read -r RECEIVER_EMAIL

echo "Enter PASSWORD:"
read -r PASSWORD

# Create or overwrite the .env file
echo "Creating .env file..."
cat <<EOL > .env
API_KEY=$API_KEY
SENDER_EMAIL=$SENDER_EMAIL
RECEIVER_EMAIL=$RECEIVER_EMAIL
PASSWORD=$PASSWORD
EOL

echo ".env file created successfully!"
