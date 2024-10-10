# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTreemap(Component):
    """An AntdTreemap component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- data (dict; optional)

- meta (optional)

- colorField (string; required)

- rawFields (list of strings; optional)

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

- rectStyle (dict; optional)

    `rectStyle` is a dict with keys:

    - func (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- legend (optional)

- label (optional)

- tooltip (optional)

- annotations (optional)

- animation (optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (list of dicts; optional)

- recentlyAreaClickRecord (dict; optional)

    `recentlyAreaClickRecord` is a dict with keys:

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

- drilldown (dict; optional):
    配置矩形树图下钻功能.

    `drilldown` is a dict with keys:

    - enabled (boolean; optional):
        是否启用矩形树图下钻功能  默认值：`False`.

    - breadCrumb (dict; optional):
        配置下钻层级引导交互面包屑控件.

        `breadCrumb` is a dict with keys:

        - position (a value equal to: 'top-left', 'bottom-left'; optional):
            控件位置，可选项有`'top-left'`、`'bottom-left'`  默认值：`'top-left'`.

        - rootText (string; optional):
            自定义根节点文案内容.

        - dividerText (string; optional):
            自定义层级分割文本内容  默认值：`/`.

        - textStyle (optional):
            设置字体样式.

        - activeTextStyle (optional):
            设置激活状态下的字体样式.

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
    _type = 'AntdTreemap'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, meta=Component.UNDEFINED, colorField=Component.REQUIRED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, rectStyle=Component.UNDEFINED, color=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, drilldown=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'colorField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'rectStyle', 'color', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'drilldown', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'colorField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'rectStyle', 'color', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'drilldown', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['colorField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdTreemap, self).__init__(**args)
