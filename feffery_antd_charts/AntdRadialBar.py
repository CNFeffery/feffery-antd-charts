# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdRadialBar(Component):
    """An AntdRadialBar component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- data (list of dicts; required)

- meta (optional)

- xField (string; required)

- yField (string; required)

- colorField (string; optional):
    分组字段名.

- isStack (boolean; optional):
    colorField有定义时，是否开启堆叠功能.

- isGroup (boolean; optional):
    colorField有定义时，是否开启分组功能.

- radius (number; optional):
    外圈半径值，取值应在0到1之间  默认：1.

- innerRadius (number; optional):
    内圈半径值，取值应在0到1之间.

- startAngle (number; optional):
    坐标系起始角度，弧度制.

- endAngle (number; optional):
    坐标系结束角度，弧度制.

- maxAngle (number; optional):
    最大值映射旋转角度，取值应在0到360之间  默认：240.

- type (a value equal to: 'line'; optional):
    特殊的图表类型，可选的有'line'（线形）.

- intervalPadding (number; optional):
    组间柱体像素间距.

- dodgePadding (number; optional):
    组内柱体像素间距.

- minBarWidth (number; optional):
    柱体最小像素宽度.

- maxBarWidth (number; optional):
    柱体最大像素宽度.

- barStyle (dict; optional)

    `barStyle` is a dict with keys:

    - func (string; optional)

- barBackground (dict; optional)

    `barBackground` is a dict with keys:

    - style (optional)

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

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

- recentlyBarClickRecord (dict; optional)

    `recentlyBarClickRecord` is a dict with keys:

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
    _type = 'AntdRadialBar'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, colorField=Component.UNDEFINED, isStack=Component.UNDEFINED, isGroup=Component.UNDEFINED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, maxAngle=Component.UNDEFINED, type=Component.UNDEFINED, intervalPadding=Component.UNDEFINED, dodgePadding=Component.UNDEFINED, minBarWidth=Component.UNDEFINED, maxBarWidth=Component.UNDEFINED, barStyle=Component.UNDEFINED, barBackground=Component.UNDEFINED, color=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyBarClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'isStack', 'isGroup', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'maxAngle', 'type', 'intervalPadding', 'dodgePadding', 'minBarWidth', 'maxBarWidth', 'barStyle', 'barBackground', 'color', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyBarClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'isStack', 'isGroup', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'maxAngle', 'type', 'intervalPadding', 'dodgePadding', 'minBarWidth', 'maxBarWidth', 'barStyle', 'barBackground', 'color', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyBarClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'loading_state']
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
