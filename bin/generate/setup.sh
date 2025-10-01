#!/bin/bash
set -e

#Makes sure dockerfile can reach dir for web files and makes sure dir exists. This is Opensuse generated code
cd "$(dirname "$0")/../.."

#install docker if missing
echo "Checking if Docker is installed..."
if ! command -v docker &> /dev/null; then
        echo "Installing Docker..."
        sudo zypper install -y docker docker-compose docker-compose-switch
fi

# Start and enable Docker
echo "Starting Docker Service..."
if sudo systemctl start docker; then
        echo "Docker Started Successfully."
else
        echo "X Failed to start Docker. Check permissions or logs."
        exit 1
fi

echo "Enabling docker to start on boot."
sudo systemctl enable docker


# Add user to docker group
echo "Adding user to docker group."
sudo usermod -aG docker $USER

cd "$(dirname "$0")/bin//generation"

if ! command -v virtualenv &> /dev/null; then
        echo "Installing virtualenv..."
        sudo zypper install -y python3-virtualenv
fi

virtualenv venv
source venv/bin/activate

echo "Creating Python virtual enviroment..."
if ! command -v python3 &> /dev/null; then
        echo "Python3 not found. Installing..."
        sudo zypper install -y python3 python3-venv python3-devel
fi

#Create python virtual enviroment
python3 -m venv venv
source venv/bin/activate

echo "Upgrading pip tools..."
pip install --upgrade pip setuptools wheel --break-system-packages
pip install --only-binary :all: pyyaml --break-system-packages
 
#echo "Installing dependencies from requirments.txt..." NOT USED ATM
#if ! pip install -r requirements.txt; then
#       echo "Build failed. Installing system build tool."
#       sudo zypper install -t pattern devel_basis
#       pip install --upgrade pip setuptools wheel --break-system-packages
#       pip install -r requirements.txt --break-system-packages
#fi
 

echo "Running Python Scripts"
python3 generate_yaml.py
python3 launch_docker.py
 
echo "Setup Complete"

