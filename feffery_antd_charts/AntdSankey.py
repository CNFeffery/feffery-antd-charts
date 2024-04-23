# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSankey(Component):
    """An AntdSankey component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- appendPadding (number | list of numbers; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- data (list of dicts; optional)

- downloadTrigger (string; default 'download-trigger')

- edgeStyle (dict; optional)

    `edgeStyle` is a dict with keys:

    - func (string; optional)

- height (number; optional)

- interactions (optional):
    交互功能项配置.

- key (string; optional)

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

- nodeAlign (a value equal to: 'left', 'right', 'center', 'justify'; optional)

- nodeDraggable (boolean; optional)

- nodePaddingRatio (number; optional)

- nodeStyle (dict; optional)

    `nodeStyle` is a dict with keys:

    - func (string; optional)

- nodeWidthRatio (number; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- rawFields (list of strings; optional)

- recentlyAreaClickRecord (dict; optional)

    `recentlyAreaClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- sourceField (string; optional)

- state (optional):
    状态样式配置.

- style (dict; optional)

- targetField (string; optional)

- theme (optional)

- weightField (string; optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdSankey'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, meta=Component.UNDEFINED, sourceField=Component.UNDEFINED, targetField=Component.UNDEFINED, weightField=Component.UNDEFINED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, nodeStyle=Component.UNDEFINED, edgeStyle=Component.UNDEFINED, color=Component.UNDEFINED, nodeWidthRatio=Component.UNDEFINED, nodePaddingRatio=Component.UNDEFINED, nodeAlign=Component.UNDEFINED, nodeDraggable=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'appendPadding', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'edgeStyle', 'height', 'interactions', 'key', 'limitInPlot', 'loading_state', 'locale', 'meta', 'nodeAlign', 'nodeDraggable', 'nodePaddingRatio', 'nodeStyle', 'nodeWidthRatio', 'padding', 'pixelRatio', 'rawFields', 'recentlyAreaClickRecord', 'recentlyTooltipChangeRecord', 'renderer', 'sourceField', 'state', 'style', 'targetField', 'theme', 'weightField', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'appendPadding', 'autoFit', 'className', 'color', 'data', 'downloadTrigger', 'edgeStyle', 'height', 'interactions', 'key', 'limitInPlot', 'loading_state', 'locale', 'meta', 'nodeAlign', 'nodeDraggable', 'nodePaddingRatio', 'nodeStyle', 'nodeWidthRatio', 'padding', 'pixelRatio', 'rawFields', 'recentlyAreaClickRecord', 'recentlyTooltipChangeRecord', 'renderer', 'sourceField', 'state', 'style', 'targetField', 'theme', 'weightField', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdSankey, self).__init__(**args)
