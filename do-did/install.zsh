#!/usr/bin/env zsh

# build the latest versions
pyinstaller --noconfirm --paths ./ installation.py
pyinstaller --noconfirm --paths ./ __init__.py
# move to where the install script expects
cd dist/installation/
# run the installation script
./installation
# add vars to path
source ~/.zshrc
# return to original directory
cd -