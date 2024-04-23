# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdRadialBar(Component):
    """An AntdRadialBar component.


Keyword arguments:

- id (string; optional)

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional)

- autoFit (boolean; optional)

- barBackground (dict; optional)

    `barBackground` is a dict with keys:

    - style (optional)

- barStyle (dict; optional)

    `barStyle` is a dict with keys:

    - func (string; optional)

- className (string; optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- colorField (string; optional):
    分组字段名.

- data (list of dicts; required)

- dodgePadding (number; optional):
    组内柱体像素间距.

- downloadTrigger (string; default 'download-trigger')

- endAngle (number; optional):
    坐标系结束角度，弧度制.

- height (number; optional)

- innerRadius (number; optional):
    内圈半径值，取值应在0到1之间.

- interactions (optional):
    交互功能项配置.

- intervalPadding (number; optional):
    组间柱体像素间距.

- isGroup (boolean; optional):
    colorField有定义时，是否开启分组功能.

- isStack (boolean; optional):
    colorField有定义时，是否开启堆叠功能.

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

- maxAngle (number; optional):
    最大值映射旋转角度，取值应在0到360之间  默认：240.

- maxBarWidth (number; optional):
    柱体最大像素宽度.

- meta (optional)

- minBarWidth (number; optional):
    柱体最小像素宽度.

- padding (number | list of numbers | string; optional)

- pattern (optional):
    配置图形填充贴图样式.

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- radius (number; optional):
    外圈半径值，取值应在0到1之间  默认：1.

- recentlyBarClickRecord (dict; optional)

    `recentlyBarClickRecord` is a dict with keys:

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

- startAngle (number; optional):
    坐标系起始角度，弧度制.

- state (optional):
    状态样式配置.

- style (dict; optional)

- theme (optional)

- tooltip (optional)

- type (a value equal to: 'line'; optional):
    特殊的图表类型，可选的有'line'（线形）.

- width (number; optional)

- xAxis (optional)

- xField (string; required)

- yAxis (optional)

- yField (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdRadialBar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, colorField=Component.UNDEFINED, isStack=Component.UNDEFINED, isGroup=Component.UNDEFINED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, maxAngle=Component.UNDEFINED, type=Component.UNDEFINED, intervalPadding=Component.UNDEFINED, dodgePadding=Component.UNDEFINED, minBarWidth=Component.UNDEFINED, maxBarWidth=Component.UNDEFINED, barStyle=Component.UNDEFINED, barBackground=Component.UNDEFINED, color=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyBarClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'barBackground', 'barStyle', 'className', 'color', 'colorField', 'data', 'dodgePadding', 'downloadTrigger', 'endAngle', 'height', 'innerRadius', 'interactions', 'intervalPadding', 'isGroup', 'isStack', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'maxAngle', 'maxBarWidth', 'meta', 'minBarWidth', 'padding', 'pattern', 'pixelRatio', 'radius', 'recentlyBarClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'startAngle', 'state', 'style', 'theme', 'tooltip', 'type', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'barBackground', 'barStyle', 'className', 'color', 'colorField', 'data', 'dodgePadding', 'downloadTrigger', 'endAngle', 'height', 'innerRadius', 'interactions', 'intervalPadding', 'isGroup', 'isStack', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'maxAngle', 'maxBarWidth', 'meta', 'minBarWidth', 'padding', 'pattern', 'pixelRatio', 'radius', 'recentlyBarClickRecord', 'recentlyLegendInfo', 'recentlyTooltipChangeRecord', 'renderer', 'startAngle', 'state', 'style', 'theme', 'tooltip', 'type', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdRadialBar, self).__init__(**args)
