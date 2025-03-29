import os

dialog = input('Do you want to install Nvidia GPU drivers? [Y/n]: ')
if dialog == '' or dialog.lower() == 'y':
    os.system('sudo pacman -Syu nvidia nvidia-utils')
os.system('sudo pacman -S --needed nwg-look go nano hyprland hyprlock flatpak firefox nautilus vim gnome-calculator gnome-text-editor waybar cliphist wl-clipboard hyprpaper gnome-disk-utility rofi kitty python-pywal pinta vlc celluloid pavucontrol ttf-jetbrains-mono ttf-jetbrains-mono-nerd fastfetch xdg-desktop-portal xdg-desktop-portal-gtk dunst pipewire pipewire-pulse wireplumber xdg-desktop-portal-hyprland adwaita-gtk3')
os.system('paru -S --needed --skipreview --noconfirm oh-my-posh-git hyprpicker hyprshot-git nwg-look papirus-icon-theme bibata-cursor-theme')
