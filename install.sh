script_dir=$(dirname "$(realpath "$0")")

echo "~~~INSTALL SCRIPT~~~"
echo "    Installing python"
sudo pacman -S python --noconfirm
python "$script_dir/install_packages.py"
echo "    Packages installed"
echo ""
echo "    Installing configs"
python "$script_dir/install_homefiles.py"
echo "    Configs installed"
echo ""
echo "    Post-installing"
python "$script_dir/post_install.py"
