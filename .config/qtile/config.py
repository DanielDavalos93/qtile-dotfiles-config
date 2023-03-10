# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension

dispositivo_red = 'wlan0' 
mod = "mod4"
terminal = guess_terminal()
colorBarra = "#282a35"
size_barra = 30
size_iconos = 26
color_fg = "#ffffff"
color_bg = "#182a36"
color_inactivo = "#6272a4"
color_oscuro = "#44475a"
color_claro = "#7fa7f9"
color_urgent = "#ff5555"
color_texto1 = "#b793f9"
color_grupo1 = "#36ab5a"
color_grupo2 = "#b732a9"
color_grupo3 = "#016bff"
color_grupo4 = "#de6551"
color_actualizaciones = "#bc0000"

# definir funciones

def fc_separador():
    return widget.Sep(
            linewidth = 2,
            padding = 1,
            foreground = color_fg,
            background = color_bg
            )

def fc_rect(vColor, tipo):
    if tipo == 0:
        icono = "???"
    else:
        icono = "???" 
    return widget.TextBox(
            text = icono,
            fontsize = size_barra+2.5,
            foreground = vColor,
            background = color_bg,
            padding = -2.5
            )
def fc_icono(icono,color_grupo):
    return widget.TextBox(
            text = icono,
            foreground = color_fg,
            background = color_grupo,
            fontsize = 14
            )

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "p", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Lanzar menu
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"),
    
    # Lanzar explorador
    Key([mod], "n", lazy.spawn("chromium"), desc="Abrir Brave"),
    Key([mod], "f", lazy.spawn("thunar"), desc="Gestor de archivos"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #---    Exit Qtile      ---#
    Key([mod, "shift"], "e", lazy.shutdown()),
    
    # Control de volumen
    
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 5- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 5+ unmute")),

    # Brillo de pantalla
    Key([],"XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([],"XF86MonBrightnessDown",lazy.spawn("brightnessctl set 10%-")),
    Key([mod], "s", lazy.spawn("scrot -e 'mv $f $HOME/Images/Screenshots/'")),          #Must to create the folder ~/Images/Screenshots
    Key([mod, "shift"], "s", lazy.spawn("scrot -s 'mv $f $HOME/Images/Screenshots/'")), #Must to create the folder ~/Images/Screenshots
    Key([], "F1", lazy.spawn("betterlockscreen --lock blur"))
]

key_exensions = Key([mod], 'q', lazy.run_extension(extension.CommandSet(
    commands={
        'reboot': 'reboot',
        'shutdown': 'shutdown',
        'suspend': 'systemctl suspend',
        'lock session': '/home/tokariew/.local/bin/lockme',
        'restart qtile': 'qtile cmd-obj -o cmd -f restart',
        'logout': 'qtile cmd-obj -o cmd -f shutdown',
        },
    dmenu_lines=6))),

keys.extend(key_exensions)

groups = [Group(i) for i in [" ???  "," ??? "," ??? "," ??? "," ??? "," ??? ", " ????  "]]

for i,group in enumerate(groups):
    escritorio = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                escritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                escritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

"""layouts = [
    layout.Columns(
    #   num_columns = 2,
    #    insert_position = 1,
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_focus = '#881111',
        margin = 3,
    #    border_on_single = True,
        ),
    layout.Max(),
    #layout.Spiral()
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    # layout.Bsp(),
    #layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    # layout.VerticalTile(),
    #layout.Zoomy(),
]"""

#---------------------------#
#   WINDOW STYLE IN LAYOUTS #
#---------------------------#

layouts = [
    layout.Columns(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    layout.Max(),
    layout.Bsp(border_focus="#9ccfd8", border_normal="#31748f",
               border_width=1, margin=5),
    layout.MonadWide(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    layout.RatioTile(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    # layout.Matrix(),
]


widget_defaults = dict(
    font="Ubuntu Mono Nerd Font",
    fontsize=13,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    #active="#feefff",
                    rounded=False,
                    highlight_color="#bbcdef",
                    highlight_method="line",
                    #inactive = color_inactivo,
                    margin_x = 0,
                    other_current_screen_border = "#bbcfed",
                    other_screen_border = "#bbcdef",
                    this_sreen_border = color_oscuro,
                    this_current_screen_border = color_oscuro,
                    margin_y = 3,
                    padding_x = 0,
                    padding_y = 6,
                    fontsize = 15,
                    borderwidth=1,
                    disable_drag = True
                ),
                widget.Sep(),
                widget.WindowName(
                    foreground= "#eb6f92",
                    markup=True,
                    font="Ubuntu Mono Nerd Font",
                    fontsize=13,
                    max_chars=63
                ),
                widget.TextBox(
                    text='???',
                    background="#232136",
                    foreground="#f6c177",
                    padding=-3,
                    fontsize=38
                ),
                widget.TextBox(
                    text='??? ',
                    background="#f6c177",
                    foreground="#191724",
                    padding=7
                ),
                widget.CurrentLayout(
                    background="#f6c177",
                    foreground="#191724"
                ),
                widget.TextBox(
                    text='???',
                    background="#f6c177",
                    foreground="#e0def4",
                    padding=-3,
                    fontsize=38
                ),
                widget.ThermalZone(
                    format="??? {temp}??C",
                    fgcolor_normal="#191724",
                    background="#e0def4",
                    zone="/sys/devices/platform/coretemp.0/hwmon/hwmon3/temp1_input"
                ),
                widget.TextBox(
                    text='???',
                    foreground="#bbcdef",
                    background="#e0def4",
                    padding=-3,
                    fontsize=38
                ),
                widget.Memory(
                    format="???{MemUsed: .0f}{mm}",
                    background="#bbcdef",
                    foreground="#191724",
                    interval=1.0
                ),
                widget.TextBox(
                    text='???',
                    background="#bbcdef",
                    foreground="#9ccfd8",
                    padding=-3,
                    fontsize=38
                ),
                widget.Net(
                    interface="wlo1",
                    format="??? {down} ?????? {up}",
                    background="#9ccfd8",
                    foreground="#191724",
                    update_interval=1.0
                ),
                widget.TextBox(
                    text='???',
                    background="#9ccfd8",
                    foreground="#c4a7e7",
                    padding=-3,
                    fontsize=38
                ),
                widget.TextBox(
                    text='???',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M - %d/%m/%Y",
                    update_interval=60.0
                ),
                widget.TextBox(
                    text='???',
                    background="#c4a7e7",
                    foreground="#eb6f92",
                    padding=-3,
                    fontsize=38
                ),
                widget.TextBox(
                    text='???',
                    background="#eb6f92",
                    foreground="#191724",
                    padding=7
                ),
                widget.QuickExit(
                    background = "#eb6f92",
                    foreground="#191724",
                    countdown_format = '{} segundos ',
                    default_text = 'embogue'
                ),
                widget.TextBox(
                    text='???',
                    background="#eb6f92",
                    foreground="#232136",
                    padding=-3,
                    fontsize=38
                ),
                widget.Systray(),
            ],
            25,
            background="#232136",
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="#ffffff",
                    rounded=True,
                    highlight_color="#c4a7e7",
                    highlight_method="line",
                    borderwidth=0
                ),
                widget.WindowName(
                    foreground="#eb6f92",
                    markup=True,
                    font="DaddyTimeMono Nerd Font",
                    fontsize=15,
                ),
                widget.TextBox(
                    text='???',
                    foreground="#e0def4",
                    padding=-3,
                    fontsize=40
                ),
                widget.TextBox(
                    text='??? ',
                    background="#e0def4",
                    foreground="#191724",
                    padding=2
                ),
                widget.CheckUpdates(
                    update_interval=18000,
                    display_format="{updates}",
                    colour_have_updates="#191724",
                    background="#e0def8"
                ),
                widget.TextBox(
                    text='???',
                    background="#e0def4",
                    foreground="#ea9a97",
                    padding=-3,
                    fontsize=38
                ),
                widget.CPU(
                    background="#ea9a97",
                    foreground="191724",
                    format="??? {load_percent}%"
                ),
                widget.TextBox(
                    text='???',
                    background="#ea9a97",
                    foreground="#c4a7e7",
                    padding=-3,
                    fontsize=38
                ),
                widget.TextBox(
                    text='???',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M",
                    update_interval=60.0
                ),
                widget.QuickExit(
                    background = color_grupo4,
                    foreground="#191724",
                    countdown_format = '{} segundos ',
                    default_text = '??? embogue'
                ),
            ],
            25,
            background="#232136",
        ),
    ),

]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus="#9ccfd8",
    border_normal="#31748f"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
