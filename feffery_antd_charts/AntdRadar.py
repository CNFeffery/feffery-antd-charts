# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdRadar(Component):
    """An AntdRadar component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- area (dict; optional)

    `area` is a dict with keys:

    - color (dict; optional)

        `color` is a string

      Or list of strings | dict with keys:

        - func (string; optional)

    - smooth (boolean; optional)

    - style (dict; optional)

        `style` is a dict with keys:

        - func (string; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- endAngle (number; optional)

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

- label (optional)

- legend (optional)

- limitInPlot (boolean; optional)

- lineStyle (dict; optional)

    `lineStyle` is a dict with keys:

    - func (string; optional)

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

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- point (dict; optional)

    `point` is a dict with keys:

    - color (dict; optional)

        `color` is a string

      Or list of strings | dict with keys:

        - func (string; optional)

    - shape (dict; optional)

        `shape` is a string | dict with keys:

        - func (string; optional)

    - style (dict; optional)

        `style` is a dict with keys:

        - func (string; optional)

- radius (number; optional)

- recentlyAreaClickRecord (dict; optional)

    `recentlyAreaClickRecord` is a dict with keys:

    - data (boolean | number | string | dict | list; optional)

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

- seriesField (string; optional)

- smooth (boolean; optional)

- startAngle (number; optional)

- state (optional):
    状态样式配置.

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdRadar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, smooth=Component.UNDEFINED, radius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, color=Component.UNDEFINED, lineStyle=Component.UNDEFINED, point=Component.UNDEFINED, area=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'area', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'endAngle', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'lineStyle', 'loading_state', 'locale', 'meta', 'padding', 'pixelRatio', 'point', 'radius', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'seriesField', 'smooth', 'startAngle', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'area', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'endAngle', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'lineStyle', 'loading_state', 'locale', 'meta', 'padding', 'pixelRatio', 'point', 'radius', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'seriesField', 'smooth', 'startAngle', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdRadar, self).__init__(**args)
