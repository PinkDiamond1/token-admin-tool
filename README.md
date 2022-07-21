Token Admin Tool
=======

Install
-------

**Ubuntu/MacOSs**
```
git clone https://github.com/bpx-network/token-admin-tool.git
cd token-admin-tool
python3 -m venv venv
. ./venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install .
```
(If you're on an M1 Mac, make sure you are running an ARM64 native python virtual environment)

**Windows Powershell**
```
git clone https://github.com/bpx-network/token-admin-tool.git
cd token-admin-tool
py -m venv venv
./venv/Scripts/activate
python -m pip install --upgrade pip setuptools wheel
pip install .
```

Lastly this requires a synced, running light wallet
