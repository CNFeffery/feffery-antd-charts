# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdPie(Component):
    """An AntdPie component.


Keyword arguments:

- id (string; optional)

- angleField (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- colorField (string; optional)

- data (list of dicts; required)

- downloadTrigger (string; default 'download-trigger')

- endAngle (number; optional)

- height (number; optional)

- innerRadius (number; optional)

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

- pattern (optional):
    配置图形填充贴图样式.

- pieStyle (dict; optional)

    `pieStyle` is a dict with keys:

    - func (string; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- radius (number; optional)

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - items (list of dicts; optional)

    - triggerItemName (boolean | number | string | dict | list; optional)

- recentlySectorClickRecord (dict; optional)

    `recentlySectorClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- startAngle (number; optional)

- state (optional):
    状态样式配置.

- statistic (dict; optional)

    `statistic` is a dict with keys:

    - content (dict; optional)

        `content` is a boolean

      Or dict with keys:

        - content (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - offsetX (number; optional)

        - offsetY (number; optional)

        - rotate (number; optional)

        - style (dict; optional)

    - title (dict; optional)

        `title` is a boolean | dict with keys:

        - content (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - offsetX (number; optional)

        - offsetY (number; optional)

        - rotate (number; optional)

        - style (dict; optional) | boolean

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdPie'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, angleField=Component.UNDEFINED, colorField=Component.UNDEFINED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, color=Component.UNDEFINED, statistic=Component.UNDEFINED, pieStyle=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlySectorClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'angleField', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'endAngle', 'height', 'innerRadius', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'pieStyle', 'pixelRatio', 'radius', 'recentlyLegendInfo', 'recentlySectorClickRecord', 'recentlyTooltipChangeRecord', 'renderer', 'startAngle', 'state', 'statistic', 'style', 'theme', 'tooltip', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'angleField', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'data', 'downloadTrigger', 'endAngle', 'height', 'innerRadius', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'pieStyle', 'pixelRatio', 'radius', 'recentlyLegendInfo', 'recentlySectorClickRecord', 'recentlyTooltipChangeRecord', 'renderer', 'startAngle', 'state', 'statistic', 'style', 'theme', 'tooltip', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdPie, self).__init__(**args)
