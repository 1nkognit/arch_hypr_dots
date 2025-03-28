import os

dialog = input('Do you want to install Nvidia GPU drivers? [y/n]: ')
if dialog == '' or dialog.lower() == 'y':
    os.system('sudo pacman -S nvidia nvidia-utils nvidia-settings lib32-nvidia-utils lib32-vulkan-icd-loader')
os.system('sudo pacman -S --needed nwg-look nano hyprland hyprlock flatpak firefox nautilus vim gnome-calculator gnome-text-editor waybar cliphist hyprpaper gnome-disk-utility rofi kitty python-pywal pinta vlc celluloid pavucontrol ttf-jetbrains-mono fastfetch breeze kvantum xdg-desktop-portal xdg-desktop-portal-gtk dunst pipewire pipewire-pulse wireplumber xdg-desktop-portal-hyprland')
os.system('paru -S --needed --skipreview --noconfirm oh-my-posh-git hyprpicker hyprshot-git nwg-look papirus-icon-theme bibata-cursor-theme')
