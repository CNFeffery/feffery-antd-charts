# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdViolin(Component):
    """An AntdViolin component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- box (boolean; optional):
    是否展示内部箱线图  默认：True.

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

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - items (list of dicts; optional)

    - triggerItemName (boolean | number | string | dict | list; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- recentlyViolinClickRecord (dict; optional)

    `recentlyViolinClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- seriesField (string; optional):
    定义作为分组依据的字段名.

- shape (a value equal to: 'smooth', 'hollow', 'hollow-smooth'; optional):
    小提琴形状，可选的有'smooth'（平滑）、'hollow'（空心）、'hollow-smooth'（平滑、空心）
    默认不设置为非平滑、实心效果.

- state (optional):
    状态样式配置.

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- violinStyle (dict; optional):
    配置小提琴图样式.

    `violinStyle` is a dict with keys:

    - func (string; optional)

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (string; required):
    定义作为y轴数值的字段名."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdViolin'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, box=Component.UNDEFINED, shape=Component.UNDEFINED, violinStyle=Component.UNDEFINED, color=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyViolinClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'box', 'className', 'color', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pixelRatio', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'recentlyViolinClickRecord', 'renderer', 'seriesField', 'shape', 'state', 'style', 'theme', 'tooltip', 'violinStyle', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'box', 'className', 'color', 'data', 'downloadTrigger', 'height', 'interactions', 'key', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pixelRatio', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'recentlyViolinClickRecord', 'renderer', 'seriesField', 'shape', 'state', 'style', 'theme', 'tooltip', 'violinStyle', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdViolin, self).__init__(**args)
