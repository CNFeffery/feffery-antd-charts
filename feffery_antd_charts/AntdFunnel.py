# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdFunnel(Component):
    """An AntdFunnel component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- className (string; optional)

- compareField (string; optional)

- conversionTag (dict; optional)

    `conversionTag` is a boolean | dict with keys:

    - formatter (dict; optional)

        `formatter` is a dict with keys:

        - func (string; optional)

    - offsetX (number; optional)

    - offsetY (number; optional)

    - style (optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- dynamicHeight (boolean; optional)

- funnelStyle (dict; optional)

    `funnelStyle` is a dict with keys:

    - func (string; optional)

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- isTransposed (boolean; optional)

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

- maxSize (number; optional)

- meta (optional)

- minSize (number; optional)

- padding (number | list of numbers | string; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- recentlyAreaClickRecord (dict; optional)

    `recentlyAreaClickRecord` is a dict with keys:

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

- seriesField (string; optional)

- shape (a value equal to: 'funnel', 'pyramid'; optional)

- state (optional):
    状态样式配置.

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)

- xField (string; required)

- yField (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdFunnel'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, compareField=Component.UNDEFINED, seriesField=Component.UNDEFINED, isTransposed=Component.UNDEFINED, shape=Component.UNDEFINED, dynamicHeight=Component.UNDEFINED, maxSize=Component.UNDEFINED, minSize=Component.UNDEFINED, funnelStyle=Component.UNDEFINED, conversionTag=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'compareField', 'conversionTag', 'data', 'downloadTrigger', 'dynamicHeight', 'funnelStyle', 'height', 'interactions', 'isTransposed', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'maxSize', 'meta', 'minSize', 'padding', 'pixelRatio', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'seriesField', 'shape', 'state', 'style', 'theme', 'tooltip', 'width', 'xField', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'compareField', 'conversionTag', 'data', 'downloadTrigger', 'dynamicHeight', 'funnelStyle', 'height', 'interactions', 'isTransposed', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'maxSize', 'meta', 'minSize', 'padding', 'pixelRatio', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'seriesField', 'shape', 'state', 'style', 'theme', 'tooltip', 'width', 'xField', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdFunnel, self).__init__(**args)
