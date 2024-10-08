# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdPie(Component):
    """An AntdPie component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- data (list of dicts; required)

- meta (optional)

- angleField (string; optional)

- colorField (string; optional)

- radius (number; optional)

- innerRadius (number; optional)

- startAngle (number; optional)

- endAngle (number; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- statistic (dict; optional)

    `statistic` is a dict with keys:

    - title (dict; optional)

        `title` is a boolean

      Or dict with keys:

        - style (dict; optional)

        - content (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - rotate (number; optional)

        - offsetX (number; optional)

        - offsetY (number; optional)

    - content (dict; optional)

        `content` is a boolean | dict with keys:

        - style (dict; optional)

        - content (string; optional)

        - formatter (dict; optional)

            `formatter` is a dict with keys:

            - func (string; optional)

        - customHtml (dict; optional)

            `customHtml` is a dict with keys:

            - func (string; optional)

        - rotate (number; optional)

        - offsetX (number; optional)

        - offsetY (number; optional) | boolean

- pieStyle (dict; optional)

    `pieStyle` is a dict with keys:

    - func (string; optional)

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

- downloadTrigger (string; default 'download-trigger')

- theme (optional)

- pattern (optional):
    配置图形填充贴图样式.

- interactions (optional):
    交互功能项配置.

- state (optional):
    状态样式配置.

- animation (optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (list of dicts; optional)

- recentlySectorClickRecord (dict; optional)

    `recentlySectorClickRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (dict; optional)

- recentlyLegendInfo (dict; optional)

    `recentlyLegendInfo` is a dict with keys:

    - triggerItemName (boolean | number | string | dict | list; optional)

    - items (list of dicts; optional)

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
    _type = 'AntdPie'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, angleField=Component.UNDEFINED, colorField=Component.UNDEFINED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, color=Component.UNDEFINED, statistic=Component.UNDEFINED, pieStyle=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlySectorClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'angleField', 'colorField', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'color', 'statistic', 'pieStyle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'animation', 'recentlyTooltipChangeRecord', 'recentlySectorClickRecord', 'recentlyLegendInfo', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'angleField', 'colorField', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'color', 'statistic', 'pieStyle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'animation', 'recentlyTooltipChangeRecord', 'recentlySectorClickRecord', 'recentlyLegendInfo', 'loading_state']
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
