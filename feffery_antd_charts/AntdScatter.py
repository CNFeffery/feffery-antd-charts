# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdScatter(Component):
    """An AntdScatter component.
散点图组件AntdScatter

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- style (dict; optional):
    当前组件css样式.

- data (list of dicts; required):
    必填，定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- xField (string; required):
    必填，图表x轴字段.

- yField (string; required):
    必填，图表y轴字段.

- colorField (string; optional):
    颜色映射字段.

- sizeField (string; optional):
    尺寸映射字段.

- shapeField (string; optional):
    形状映射字段.

- color (dict; optional):
    控制散点颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- size (dict; optional):
    控制散点尺寸，具体见在线文档相关说明.

    `size` is a number | list of numbers | dict with keys:

    - func (string; optional):
        js函数体字符串.

- shape (dict; optional):
    控制散点形状，具体见在线文档相关说明.

    `shape` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- pointStyle (dict; optional):
    控制散点样式，具体见在线文档相关说明.

    `pointStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- shapeLegend (optional):
    是否为散点形状渲染图例.

- sizeLegend (optional):
    是否为散点尺寸渲染图例.

- quadrant (dict; optional):
    配置象限相关参数，具体见在线文档相关说明.

    `quadrant` is a dict with keys:

    - xBaseline (number; optional):
        横轴基准分割线位置  默认值：`0`.

    - yBaseline (number; optional):
        纵轴基准分割线位置  默认值：`0`.

    - lineStyle (optional):
        配置分割线样式.

    - regionStyle (list; optional):
        配置象限样式，支持传入格式如`[左上, 右上, 右下, 左下]`格式的参数分别配置四个象限的样式.

    - labels (list of dicts; optional):
        配置各象限文字标注，格式如`[左上, 右上, 右下, 左下]`.

        `labels` is a list of dicts with keys:

        - content (string; optional):

            标注文字内容.

        - position (list of numbers; optional):

            标注坐标位置，格式如`[x, y]`.

        - style (optional):

            标注文字样式.

- regressionLine (dict; optional):
    配置回归线相关参数，具体见在线文档相关说明.

    `regressionLine` is a dict with keys:

    - type (a value equal to: 'exp', 'linear', 'loess', 'log', 'poly', 'pow', 'quad'; optional):
        回归线类型，可选项有`'exp'`、`'linear'`、`'loess'`、`'log'`、`'poly'`、`'pow'`、`'quad'`.

    - style (optional):
        回归线样式.

    - algorithm (dict; optional):
        自定义回归线数值映射算法.

        `algorithm` is a dict with keys:

        - func (string; optional):
            js函数体字符串.

    - top (boolean; optional):
        回归线是否置于顶层显示.

- xAxis (optional):
    配置横坐标轴相关参数，具体见在线文档相关说明.

- yAxis (optional):
    配置纵坐标轴相关参数，具体见在线文档相关说明.

- width (number; optional):
    图表容器像素宽度.

- height (number; optional):
    图表容器像素高度.

- autoFit (boolean; optional):
    图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效  默认值：`True`.

- padding (number | list of numbers | string; optional):
    画布内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组，或传入`'auto'`开启底层自动计算.

- appendPadding (number | list of numbers | string; optional):
    画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组.

- renderer (a value equal to: 'canvas', 'svg'; optional):
    图表底层渲染方式，可选项有`'canvas'`和`'svg'`  默认值：`'canvas'`.

- pixelRatio (number; optional):
    `renderer='canvas'`时，控制渲染图表图片的像素比  默认值：`1`.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN'):
    图表文案语种，可选项有`'zh-CN'`、`'en-US'`  默认值：`'zh-CN'`.

- limitInPlot (boolean; optional):
    是否对超出绘图区域的几何元素进行裁剪.

- legend (optional):
    配置图例相关参数，具体见在线文档相关说明.

- label (optional):
    配置数值标签相关参数，具体见在线文档相关说明.

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- annotations (optional):
    配置标注相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

- recentlyTooltipChangeRecord (dict; optional):
    事件监听属性，用于监听最近一次信息框显示事件.

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (list of dicts; optional):
        涉及数据信息.

- recentlyPointClickRecord (dict; optional):
    事件监听属性，用于监听最近一次散点点击事件.

    `recentlyPointClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- recentlyPointDoubleClickRecord (dict; optional):
    事件监听属性，用于监听最近一次散点双击事件.

    `recentlyPointDoubleClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- recentlyLegendInfo (dict; optional):
    事件监听属性，用于监听最近一次图例点击事件.

    `recentlyLegendInfo` is a dict with keys:

    - triggerItemName (boolean | number | string | dict | list; optional):
        被点击图例项名称.

    - items (list of dicts; optional):
        当前各图例项信息.

- downloadTrigger (string; default 'download-trigger'):
    对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片.

- theme (optional):
    配置主题相关参数，具体见在线文档相关说明.

- interactions (optional):
    配置交互功能相关参数，具体见在线文档相关说明.

- state (optional):
    配置状态样式相关参数，具体见在线文档相关说明.

- brush (optional):
    配置刷选相关功能，具体见在线文档相关说明.

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
    _type = 'AntdScatter'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, colorField=Component.UNDEFINED, sizeField=Component.UNDEFINED, shapeField=Component.UNDEFINED, color=Component.UNDEFINED, size=Component.UNDEFINED, shape=Component.UNDEFINED, pointStyle=Component.UNDEFINED, shapeLegend=Component.UNDEFINED, sizeLegend=Component.UNDEFINED, quadrant=Component.UNDEFINED, regressionLine=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, legend=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyPointClickRecord=Component.UNDEFINED, recentlyPointDoubleClickRecord=Component.UNDEFINED, recentlyLegendInfo=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, brush=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'sizeField', 'shapeField', 'color', 'size', 'shape', 'pointStyle', 'shapeLegend', 'sizeLegend', 'quadrant', 'regressionLine', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyPointClickRecord', 'recentlyPointDoubleClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state', 'brush', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'colorField', 'sizeField', 'shapeField', 'color', 'size', 'shape', 'pointStyle', 'shapeLegend', 'sizeLegend', 'quadrant', 'regressionLine', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'legend', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyPointClickRecord', 'recentlyPointDoubleClickRecord', 'recentlyLegendInfo', 'downloadTrigger', 'theme', 'interactions', 'state', 'brush', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdScatter, self).__init__(**args)
