# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDualAxes(Component):
    """An AntdDualAxes component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- data (list of list of dictss; required)

- meta (optional)

- xField (string; required)

- yField (list of strings; required)

- geometryOptions (list of dicts; optional)

    `geometryOptions` is a list of dicts with keys:

    - geometry (a value equal to: 'line', 'column'; optional)

    - seriesField (string; optional)

    - smooth (boolean; optional)

    - connectNulls (boolean; optional)

    - lineStyle (dict; optional)

        `lineStyle` is a dict with keys:

        - func (string; optional)

    - point (dict; optional)

        `point` is a dict with keys:

        - color (dict; optional)

            `color` is a string

          Or list of strings

      Or dict with keys:

    - func (string; optional)

        - shape (dict; optional)

            `shape` is a string | dict with keys:

    - func (string; optional)

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - label (optional)

    - color (dict; optional)

        `color` is a string | list of strings | dict with keys:

        - func (string; optional)

    - stepType (string; optional) | dict with keys:

    - geometry (a value equal to: 'line', 'column'; optional)

    - seriesField (string; optional)

    - groupField (string; optional)

    - isGroup (boolean; optional)

    - isStack (boolean; optional)

    - columnWidthRatio (number; optional)

    - marginRatio (number; optional)

    - columnStyle (dict; optional)

        `columnStyle` is a dict with keys:

        - func (string; optional)

    - label (optional)

    - color (dict; optional)

        `color` is a string | list of strings | dict with keys:

        - func (string; optional)

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

- tooltip (optional)

- xAxis (optional)

- yAxis (dict with strings as keys and values of type ; optional)

- annotations (dict with strings as keys and values of type ; optional)

- legend (optional)

- slider (optional)

- animation (optional)

- recentlyClickRecord (dict; optional)

    `recentlyClickRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (dict; optional)

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
    _type = 'AntdDualAxes'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, geometryOptions=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, tooltip=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, annotations=Component.UNDEFINED, legend=Component.UNDEFINED, slider=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'geometryOptions', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'tooltip', 'xAxis', 'yAxis', 'annotations', 'legend', 'slider', 'animation', 'recentlyClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'geometryOptions', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'tooltip', 'xAxis', 'yAxis', 'annotations', 'legend', 'slider', 'animation', 'recentlyClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdDualAxes, self).__init__(**args)
