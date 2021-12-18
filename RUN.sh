pip3 show cx-freeze 2>/dev/null || pip3 install cx-freeze
apt install patchelf
python3 setup.py build

## Only available on windows?
# python3 setup.py bdist_msi
