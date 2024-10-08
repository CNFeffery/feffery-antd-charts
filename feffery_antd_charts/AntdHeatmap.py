# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdHeatmap(Component):
    """An AntdHeatmap component.


Keyword arguments:

- id (string; optional):
    组件id.

- key (string; optional):
    辅助强制刷新.

- className (string; optional):
    css类名.

- style (dict; optional):
    css样式.

- data (list of dicts; required):
    必填，用于定义绘图所需数据.

- meta (optional):
    字段预处理元信息.

- xField (string; required):
    定义作为x轴的字段名.

- yField (string; required)

- colorField (string; optional):
    定义作为色彩映射依据的字段.

- sizeField (string; optional):
    定义作为尺寸映射依据的字段.

- reflect (a value equal to: 'x', 'y'; optional):
    配置坐标轴映射，可选的有'x'、'y'.

- color (dict; optional)

    `color` is a string | list of strings | dict with keys:

    - func (string; optional)

- shape (a value equal to: 'rect', 'square', 'circle'; optional):
    设置热力网格形状，可选的有'rect'、'square'、'square'.

- coordinate (dict; optional):
    配置坐标系相关参数.

    `coordinate` is a dict with keys:

    - type (a value equal to: 'cartesian', 'polar', 'helix', 'theta'; optional):
        坐标系类型，可选的有'cartesian'（笛卡尔坐标系）、'polar'（极坐标系）、'helix'（螺旋坐标系）、'theta'（角度映射坐标系）.

    - cfg (dict; optional):
        坐标系配置项，作用于极坐标系.

        `cfg` is a dict with keys:

        - startAngle (number; optional):
            配置起始弧度.

        - endAngle (number; optional):
            配置结束弧度.

        - radius (number; optional):
            配置极坐标系半径，取值在0到1之间.

        - innerRadius (number; optional):
            配置极坐标系内半径，取值在0到1之间.

- sizeRatio (number; optional):
    热力网格中图形的尺寸比例，当shape或sizeField定义时有效.

- heatmapStyle (dict; optional)

    `heatmapStyle` is a dict with keys:

    - func (string; optional)

- xAxis (optional)

- yAxis (optional)

- width (number; optional):
    定义图表容器像素宽度  默认：400.

- height (number; optional):
    定义图表容器像素高度  默认：400.

- autoFit (boolean; optional):
    图表是否自适应容器宽高，当设置为True时，width与height参数将失效  默认：True.

- padding (number | list of numbers | string; optional):
    定义图表四个方向的空白间距值，可以为单个数字譬如16，也可以为四个数字构成的数组，  按顺序代表上-右-下-左分别的像素间距.

- appendPadding (number | list of numbers | string; optional):
    定义在padding基础上额外的像素填充间距.

- renderer (a value equal to: 'canvas', 'svg'; optional):
    图表渲染模式，可选的有'canvas'、'svg'  默认：'canvas'.

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN'):
    设置语言，可选的有'zh-CN'与'en-US'.

- limitInPlot (boolean; optional):
    是否对超出绘图区域的几何元素进行裁剪.

- legend (optional)

- label (optional)

- tooltip (optional)

- annotations (optional)

- pattern (optional):
    配置图形填充贴图样式.

- animation (optional)

- recentlyTooltipChangeRecord (dict; optional)

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (list of dicts; optional)

- recentlyGridClickRecord (dict; optional)

    `recentlyGridClickRecord` is a dict with keys:

    - timestamp (number; optional)

    - data (dict; optional)

- downloadTrigger (string; default 'download-trigger')

- theme (optional)

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
    _type = 'AntdHeatmap'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, colorField=Component.UNDEFINED, sizeField=Component.UNDEFINED, reflect=Component.UNDEFINED, color=Component.UNDEFINED, shape=Component.UNDEFINED, coordinate=Component.UNDEFINED, sizeRatio=Component.UNDEFINED, heatmapStyle=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, pattern=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyGridClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'sizeField', 'reflect', 'color', 'shape', 'coordinate', 'sizeRatio', 'heatmapStyle', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'pattern', 'animation', 'recentlyTooltipChangeRecord', 'recentlyGridClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'sizeField', 'reflect', 'color', 'shape', 'coordinate', 'sizeRatio', 'heatmapStyle', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'pattern', 'animation', 'recentlyTooltipChangeRecord', 'recentlyGridClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
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
