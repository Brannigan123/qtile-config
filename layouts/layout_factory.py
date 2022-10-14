from typing import List
from libqtile import layout
from libqtile.layout.base import Layout

from b_theme import ColorScheme, MeasurementsConfig
from .layout_behaviour import LayoutBehavior

FLOATING_TYPES: List[str] = ["notification", "toolbar", "splash", "dialog"]


def build_bsp_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.Bsp(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
        ratio=behaviour.aspect_ratio,
        grow_amount=behaviour.grow_amount,
        border_on_single=behaviour.border_on_single,
        margin_on_single=measurements.margin if behaviour.margin_on_single else 0,
        fair=behaviour.fair,
    )


def build_spiral_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.Spiral(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
        ratio=behaviour.windows_ratio,
        ratio_increment=behaviour.ratio_increment,
    )


def build_ratio_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.RatioTile(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
        ratio=behaviour.aspect_ratio,
        ratio_increment=behaviour.ratio_increment,
    )


def build_floating_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.Floating(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
        fullscreen_border_width=measurements.border_width,
    )


def build_monadtall_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.MonadTall(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
        ratio=behaviour.windows_ratio,
        change_ratio=behaviour.ratio_increment,
        single_border_width=measurements.border_width if behaviour.border_on_single else None,
        single_margin=measurements.margin if behaviour.margin_on_single else None,
    )


def build_monadwide_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.MonadWide(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
        ratio=behaviour.windows_ratio,
        change_ratio=behaviour.ratio_increment,
        single_border_width=measurements.border_width if behaviour.border_on_single else None,
        single_margin=measurements.margin if behaviour.margin_on_single else None,
    )


def build_monad3col_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.MonadThreeCol(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
        ratio=behaviour.windows_ratio,
        change_ratio=behaviour.ratio_increment,
        single_border_width=measurements.border_width if behaviour.border_on_single else None,
        single_margin=measurements.margin if behaviour.margin_on_single else None,
    )


def build_matrix_layout(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> Layout:
    return layout.Matrix(
        border_focus=colors.green,
        border_normal=colors.gray,
        border_width=measurements.border_width,
        margin=measurements.margin,
    )


def build_layouts(colors: ColorScheme, measurements: MeasurementsConfig, behaviour: LayoutBehavior) -> 'List[Layout]':
    return [
        build_bsp_layout(colors, measurements, behaviour),
        build_spiral_layout(colors, measurements, behaviour),
        build_ratio_layout(colors, measurements, behaviour),
        build_floating_layout(colors, measurements, behaviour),
        build_monadtall_layout(colors, measurements, behaviour),
        build_monadwide_layout(colors, measurements, behaviour),
        build_monad3col_layout(colors, measurements, behaviour),
        build_matrix_layout(colors, measurements, behaviour),
    ]
