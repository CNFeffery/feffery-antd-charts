# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdColumn(Component):
    """An AntdColumn component.


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

- groupField (string; optional)

- isStack (boolean; optional)

- isGroup (boolean; optional)

- isRange (boolean; optional)

- isPercent (boolean; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- slider (optional)

- intervalPadding (number; optional)

- dodgePadding (number; optional)

- minColumnWidth (number; optional)

- maxColumnWidth (number; optional)

- columnStyle (dict; optional)

    `columnStyle` is a dict with keys:

    - func (string; optional)

- columnBackground (dict; optional)

    `columnBackground` is a dict with keys:

    - style (optional)

- columnWidthRatio (number; optional)

- marginRatio (number; optional)

- scrollbar (optional)

- conversionTag (dict; optional)

    `conversionTag` is a dict with keys:

    - size (number; optional)

    - spacing (number; optional)

    - offset (number; optional)

    - arrow (dict; optional)

        `arrow` is a boolean

      Or dict with keys:

        - headSize (number; optional)

    - text (dict; optional)

        `text` is a boolean | dict with keys:

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - style (optional)

- connectedArea (dict; optional)

    `connectedArea` is a dict with keys:

    - trigger (boolean | string; optional) | boolean

- xAxis (optional)

- yAxis (optional)

- width (number; optional)

- height (number; optional)

- autoFit (boolean; optional)

- padding (number | list of numbers | string; optional)

- appendPadding (number | list of numbers | string; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- limitInPlot (boolean; optional)

- legend (optional)

- label (optional)

- tooltip (optional)

- annotations (optional)

- animation (optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (list of dicts; optional)

- recentlyColumnClickRecord (dict; optional)

    `recentlyColumnClickRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (dict; optional)

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - triggerItemName (boolean | number | string | dict | list; optional)

    - items (list of dicts; optional)

- downloadTrigger (string; default 'download-trigger')

- theme (optional)

- pattern (optional):
    配置图形填充贴图样式.

- interactions (optional):
    交互功能项配置.

- state (optional):
    状态样式配置.

- recentlyBarClickRecord (dict; optional)

    `recentlyBarClickRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (dict; optional)

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
    _type = 'AntdColumn'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, seriesField=Component.UNDEFINED, groupField=Component.UNDEFINED, isStack=Component.UNDEFINED, isGroup=Component.UNDEFINED, isRange=Component.UNDEFINED, isPercent=Component.UNDEFINED, color=Component.UNDEFINED, slider=Component.UNDEFINED, intervalPadding=Component.UNDEFINED, dodgePadding=Component.UNDEFINED, minColumnWidth=Component.UNDEFINED, maxColumnWidth=Component.UNDEFINED, columnStyle=Component.UNDEFINED, columnBackground=Component.UNDEFINED, columnWidthRatio=Component.UNDEFINED, marginRatio=Component.UNDEFINED, scrollbar=Component.UNDEFINED, conversionTag=Component.UNDEFINED, connectedArea=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyColumnClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, recentlyBarClickRecord=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'groupField', 'isStack', 'isGroup', 'isRange', 'isPercent', 'color', 'slider', 'intervalPadding', 'dodgePadding', 'minColumnWidth', 'maxColumnWidth', 'columnStyle', 'columnBackground', 'columnWidthRatio', 'marginRatio', 'scrollbar', 'conversionTag', 'connectedArea', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyColumnClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'recentlyBarClickRecord', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'seriesField', 'groupField', 'isStack', 'isGroup', 'isRange', 'isPercent', 'color', 'slider', 'intervalPadding', 'dodgePadding', 'minColumnWidth', 'maxColumnWidth', 'columnStyle', 'columnBackground', 'columnWidthRatio', 'marginRatio', 'scrollbar', 'conversionTag', 'connectedArea', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyColumnClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'recentlyBarClickRecord', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdColumn, self).__init__(**args)
