from typing import Tuple
from libqtile.bar import Bar
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget import modify
from libqtile.lazy import lazy
from b_theme import Theme, MeasurementsConfig
from qtile_b_widgets import AppName, VisualizerBars


def build_topbar(monitor: Tuple[str, int, int], theme: Theme, measurements: MeasurementsConfig) -> Bar:
    monitor_name, monitor_width, monitor_height = monitor
    colors = theme.colors
    fonts = theme.fonts

    return Bar(
        [
            widget.Image(
                filename='~/.config/qtile/images/launch_icon.png',
                background=colors.black,
                margin_x=2*measurements.margin,
                margin_y=measurements.margin,
                scale=True,
                mouse_callbacks={'Button1': lazy.spawn("rofi -show drun"), },
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.GroupBox(
                font=fonts.font3,
                fontsize=fonts.font3_size,
                highlight_method='block',
                foreground=colors.foreground,
                background=colors.background,
                active=colors.blue,
                inactive=colors.gray,
                block_highlight_text_color=colors.background,
                this_current_screen_border=colors.magenta,
                this_screen_border=colors.magenta,
                other_current_screen_border=colors.green,
                other_screen_border=colors.green,
                urgent_border=colors.background,
                borderwidth=measurements.border_width,
                padding=measurements.padding,
                rounded=True,
                disable_drag=True,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.CurrentLayoutIcon(
                foregoround=colors.magenta,
                background=colors.background,
                padding=measurements.padding,
                scale=0.5,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=measurements.margin*2,
            ),

            widget.TextBox(
                text=" ",
                font=fonts.font4,
                fontsize=fonts.font4_size,
                foreground=colors.background,
                background=colors.yellow,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.CheckUpdates(
                fmt=' {} ',
                distro='Ubuntu',
                display_format='Updates: {updates} ',
                no_update_string='System upto date ',
                colour_have_updates=colors.background,
                colour_no_updates=colors.background,
                background=colors.yellow,
                font=fonts.font5,
                fontsize=fonts.font5_size,
                update_interval=1200,  # in seconds
                padding=0,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.TextBox(
                text='',
                font=fonts.power_font,
                fontsize=fonts.power_font_size,
                foreground=colors.cyan,
                background=colors.yellow,
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.TextBox(
                text='',
                font=fonts.power_font,
                fontsize=fonts.power_font_size,
                foreground=colors.blue,
                background=colors.cyan,
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.TextBox(
                text='',
                font=fonts.power_font,
                fontsize=fonts.power_font_size,
                foreground=colors.magenta,
                background=colors.blue,
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),


            VisualizerBars(
                foreground=colors.background,
                background=colors.magenta,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.TextBox(
                text='',
                font=fonts.power_font,
                fontsize=fonts.power_font_size,
                foreground=colors.red,
                background=colors.magenta,
                padding=0,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            widget.TextBox(
                text=" ",
                font=fonts.font4,
                fontsize=fonts.font4_size,
                foreground=colors.background,
                background=colors.red,
                decorations=[
                     RectDecoration(
                         group=True,
                         use_widget_background=True,
                         radius=4,
                         filled=True,
                         padding_y=0,
                     )
                ],
            ),

            modify(
                AppName,
                default_name='',
                foreground=colors.background,
                background=colors.red,
                font=fonts.font5,
                fontsize=fonts.font5_size,
                fmt=' {}  ',
                format='{name}',
                padding=0,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
            ),

            widget.NetGraph(
                background=colors.background,
                graph_color=colors.blue,
                fill_color=colors.background,
                border_color=colors.background,
                type='line',
                line_width=1,
                border_width=measurements.border_width,
                samples=40,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Net(
                format='{down} ↓↑ {up} ',
                foreground=colors.foreground,
                background=colors.background,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=measurements.margin*2,
            ),

            widget.TextBox(
                text=' ',
                font=fonts.font1,
                fontsize=fonts.font1_size,
                foreground=colors.orange,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Backlight(
                backlight_name='intel_backlight',
                format='{percent:3.0%} ',
                foreground=colors.foreground,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=measurements.margin*2,
            ),

            widget.TextBox(
                text=' ',
                font=fonts.font4,
                fontsize=fonts.font4_size,
                foreground=colors.magenta,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Battery(
                format='{percent:3.0%} ',
                show_short_text=False,
                foreground=colors.foreground,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=measurements.margin*2,
            ),

            widget.TextBox(
                text=' ',
                font=fonts.font4,
                fontsize=fonts.font4_size,
                foreground=colors.green,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Memory(
                format='{MemUsed: .0f}{mm} ',
                foreground=colors.foreground,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=measurements.margin*2,
            ),

            widget.TextBox(
                text=" ",
                font=fonts.font2,
                fontsize=fonts.font2_size,
                foreground=colors.red,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.PulseVolume(
                fmt='{} ',
                foreground=colors.foreground,
                background=colors.background,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        group=True,
                        use_widget_background=True,
                        radius=4,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),

            widget.Spacer(
                background="#000000.00",
                length=measurements.margin*2,
            ),

            widget.Clock(
                format='   %d.%m.%Y |   %H:%M:%S ',
                foreground=colors.background,
                background=colors.yellow,
                padding=measurements.padding,
                decorations=[
                    RectDecoration(
                        use_widget_background=True,
                        radius=10,
                        filled=True,
                        padding_y=0,
                    )
                ],
            ),
        ],
        26,
        margin=[2*measurements.margin, 2*measurements.margin,
                measurements.margin, 2*measurements.margin],
        background="#000000.00",
    )
