# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdHeatmap(Component):
    """An AntdHeatmap component.


Keyword arguments:

- id (string; optional):
    组件id.

- animation (optional)

- annotations (optional)

- appendPadding (number | list of numbers | string; optional):
    定义在padding基础上额外的像素填充间距.

- autoFit (boolean; optional):
    图表是否自适应容器宽高，当设置为True时，width与height参数将失效  默认：True.

- className (string; optional):
    css类名.

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- colorField (string; optional):
    定义作为色彩映射依据的字段.

- coordinate (dict; optional):
    配置坐标系相关参数.

    `coordinate` is a dict with keys:

    - cfg (dict; optional):
        坐标系配置项，作用于极坐标系.

        `cfg` is a dict with keys:

        - endAngle (number; optional):
            配置结束弧度.

        - innerRadius (number; optional):
            配置极坐标系内半径，取值在0到1之间.

        - radius (number; optional):
            配置极坐标系半径，取值在0到1之间.

        - startAngle (number; optional):
            配置起始弧度.

    - type (a value equal to: 'cartesian', 'polar', 'helix', 'theta'; optional):
        坐标系类型，可选的有'cartesian'（笛卡尔坐标系）、'polar'（极坐标系）、'helix'（螺旋坐标系）、'theta'（角度映射坐标系）.

- data (list of dicts; required):
    必填，用于定义绘图所需数据.

- downloadTrigger (string; default 'download-trigger')

- heatmapStyle (dict; optional)

    `heatmapStyle` is a dict with keys:

    - func (string; optional)

- height (number; optional):
    定义图表容器像素高度  默认：400.

- interactions (optional):
    交互功能项配置.

- key (string; optional):
    辅助强制刷新.

- label (optional)

- legend (optional)

- limitInPlot (boolean; optional):
    是否对超出绘图区域的几何元素进行裁剪.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN'):
    设置语言，可选的有'zh-CN'与'en-US'.

- meta (optional):
    字段预处理元信息.

- padding (number | list of numbers | string; optional):
    定义图表四个方向的空白间距值，可以为单个数字譬如16，也可以为四个数字构成的数组，  按顺序代表上-右-下-左分别的像素间距.

- pattern (optional):
    配置图形填充贴图样式.

- recentlyGridClickRecord (dict; optional)

    `recentlyGridClickRecord` is a dict with keys:

    - data (dict; optional)

    - timestamp (number; optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - data (list of dicts; optional)

    - timestamp (number; optional)

- reflect (a value equal to: 'x', 'y'; optional):
    配置坐标轴映射，可选的有'x'、'y'.

- renderer (a value equal to: 'canvas', 'svg'; optional):
    图表渲染模式，可选的有'canvas'、'svg'  默认：'canvas'.

- shape (a value equal to: 'rect', 'square', 'circle'; optional):
    设置热力网格形状，可选的有'rect'、'square'、'square'.

- sizeField (string; optional):
    定义作为尺寸映射依据的字段.

- sizeRatio (number; optional):
    热力网格中图形的尺寸比例，当shape或sizeField定义时有效.

- state (optional):
    状态样式配置.

- style (dict; optional):
    css样式.

- theme (optional)

- tooltip (optional)

- width (number; optional):
    定义图表容器像素宽度  默认：400.

- xAxis (optional)

- xField (string; required):
    定义作为x轴的字段名.

- yAxis (optional)

- yField (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdHeatmap'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, colorField=Component.UNDEFINED, sizeField=Component.UNDEFINED, reflect=Component.UNDEFINED, color=Component.UNDEFINED, shape=Component.UNDEFINED, coordinate=Component.UNDEFINED, sizeRatio=Component.UNDEFINED, heatmapStyle=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, pattern=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyGridClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'coordinate', 'data', 'downloadTrigger', 'heatmapStyle', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'recentlyGridClickRecord', 'recentlyTooltipChangeRecord', 'reflect', 'renderer', 'shape', 'sizeField', 'sizeRatio', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animation', 'annotations', 'appendPadding', 'autoFit', 'className', 'color', 'colorField', 'coordinate', 'data', 'downloadTrigger', 'heatmapStyle', 'height', 'interactions', 'key', 'label', 'legend', 'limitInPlot', 'loading_state', 'locale', 'meta', 'padding', 'pattern', 'recentlyGridClickRecord', 'recentlyTooltipChangeRecord', 'reflect', 'renderer', 'shape', 'sizeField', 'sizeRatio', 'state', 'style', 'theme', 'tooltip', 'width', 'xAxis', 'xField', 'yAxis', 'yField']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdHeatmap, self).__init__(**args)
