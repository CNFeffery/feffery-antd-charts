# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdVenn(Component):
    """An AntdVenn component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- blendMode (a value equal to: 'multiply', 'normal', 'darken', 'lighten', 'screen', 'overlay', 'burn', 'dodge'; optional):
    交集区域颜色混合方式，可选项有'multiply'、'normal'、'darken'、'lighten'、'screen'、'overlay'、'burn'、'dodge'.

- className (string; optional)

- color (dict; optional):
    配置图形颜色.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

- label (optional)

- legend (optional)

- limitInPlot (boolean; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- meta (optional)

- padding (number | list of numbers | string; optional)

- pointStyle (dict; optional):
    配置集合圆形样式.

    `pointStyle` is a dict with keys:

    - func (string; optional)

- recentlyCircleClickRecord (dict; optional)

    `recentlyCircleClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - items (list of dicts; optional)

    - triggerItemName (boolean | number | string | dict | list; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- setsField (string; optional):
    定义集合对应字段.

- sizeField (string; optional):
    定义圆形大小映射字段.

- state (optional):
    状态样式配置.

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdVenn'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, setsField=Component.UNDEFINED, sizeField=Component.UNDEFINED, blendMode=Component.UNDEFINED, pointStyle=Component.UNDEFINED, color=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyCircleClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'appendPadding', 'autoFit', 'blendMode', 'className', 'color', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pointStyle', 'recentlyCircleClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'setsField', 'sizeField', 'state', 'style', 'theme', 'tooltip', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'appendPadding', 'autoFit', 'blendMode', 'className', 'color', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pointStyle', 'recentlyCircleClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'setsField', 'sizeField', 'state', 'style', 'theme', 'tooltip', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdVenn, self).__init__(**args)
