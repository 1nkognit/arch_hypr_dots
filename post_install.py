import os
import subprocess
import pathlib

file_dir = pathlib.Path(__file__).parent.resolve()
home = os.getenv("HOME")

rule_content = '''
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.udisks2.filesystem-mount" ||
        action.id == "org.freedesktop.udisks2.filesystem-mount-system" ||
        action.id == "org.freedesktop.udisks2.encrypted-unlock") {
        return polkit.Result.YES;
    }
});
'''

waybar_css = f'{home}/.config/waybar/style.css'
hyprpaper_conf = f'{home}/.config/hypr/hyprpaper.conf'
hyprlock_conf = f'{home}/.config/hypr/hyprlock.conf'
udisks_rules = '/etc/polkit-1/rules.d/50-udisks.rules'



# Waybar config
if not os.access(waybar_css, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {waybar_css} && chmod 644 {waybar_css}')

file = open(waybar_css, 'rb')
content = file.read().decode()
file.close()
file = open(waybar_css, 'wb')
file.write(content.replace('$HOME',home).encode())
file.close()



# Walpaper set

image = f'{home}/wallpapers/wallpaper.jpg'

os.system(f'wal -i {image}')

if not os.access(hyprpaper_conf, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {hyprpaper_conf} && chmod 644 {hyprpaper_conf}')

file = open(hyprpaper_conf,'wb')
file.write(f'preload = {image}\nwallpaper = ,{image}'.encode())
file.close()



# Hyprlock wallpaper

if not os.access(hyprpaper_conf, os.R_OK | os.W_OK):
    os.system(f'sudo chown $USER:$USER {hyprlock_conf} && chmod 644 {hyprlock_conf}')

file = open(hyprlock_conf,'rb')
content = file.read().decode()
file.close()

hypr_config = ''

for line in content.split('\n'):
    if line.startswith('$wallpaper'):
        hypr_config += f'$wallpaper = {image}\n'
    else:
        hypr_config += f'{line}\n'
	    
file = open(hyprlock_conf,'wb')
content = file.write(hypr_config.encode())
file.close()


try:
    subprocess.run(
        ["sudo", "tee", "/etc/polkit-1/rules.d/50-udisks.rules"],
        input=rule_content,
        text=True,
        check=True
    )
    
    subprocess.run(["sudo", "systemctl", "restart", "polkit"], check=True)
except:
    pass

os.system('systemctl --user enable --now pipewire pipewire-pulse wireplumber')
