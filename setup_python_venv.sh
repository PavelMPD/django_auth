sudo apt-get -y update
sudo apt-get -y install python-dev
sudo apt-get -y install python-virtualenv
sudo apt-get -y update

virtualenv .venv

. .venv/bin/activate

pip install -r requirements.txt
