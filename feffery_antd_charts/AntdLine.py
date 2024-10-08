# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdLine(Component):
    """An AntdLine component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- data (list of dicts; required)

- meta (optional)

- xField (string; required)

- yField (string; required)

- seriesField (string; optional)

- smooth (boolean; optional)

- stepType (string; optional)

- connectNulls (boolean; optional)

- isStack (boolean; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- lineStyle (dict; optional)

    `lineStyle` is a dict with keys:

    - func (string; optional)

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

- xAxis (optional)

- yAxis (optional)

- width (number; optional)

- height (number; optional)

- autoFit (boolean; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- appendPadding (number | list of numbers; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- limitInPlot (boolean; optional)

- legend (optional)

- label (optional)

- tooltip (optional)

- annotations (optional)

- slider (optional)

- animation (optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (list of dicts; optional)

- recentlyPointClickRecord (dict; optional)

    `recentlyPointClickRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (dict; optional)

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - triggerItemName (boolean | number | string | dict | list; optional)

    - items (list of dicts; optional)

- downloadTrigger (string; default 'download-trigger')

- theme (optional)

- interactions (optional):
    交互功能项配置.

- state (optional):
    状态样式配置.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdLine'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, smooth=Component.UNDEFINED, stepType=Component.UNDEFINED, connectNulls=Component.UNDEFINED, isStack=Component.UNDEFINED, color=Component.UNDEFINED, lineStyle=Component.UNDEFINED, point=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, slider=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyPointClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'smooth', 'stepType', 'connectNulls', 'isStack', 'color', 'lineStyle', 'point', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'slider', 'animation', 'recentlyTooltipChangeRecord', 'recentlyPointClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'smooth', 'stepType', 'connectNulls', 'isStack', 'color', 'lineStyle', 'point', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'slider', 'animation', 'recentlyTooltipChangeRecord', 'recentlyPointClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdLine, self).__init__(**args)
