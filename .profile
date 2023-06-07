#!/bin/zsh

setxkbmap latam &
#wpa_supplicant -B -i eno1 -c /etc/wpa_supplicant/wpa_supplicant.conf &
redshift -l -34:-58 -t 6000:3000 &
#dunst --config ~/.config/dunst/dunstrc &
volumeicon &
cbatticon -u 5 &
feh --bg-fill --randomize ~/Imágenes/Wallpaper/* &
#picom --config ~/.config/picom/picom.conf &
#plank &
nm-applet &
exec xfce4-power-manager --daemon &
exec xfce4-screensaver &
exec xfce4-notifyd &
