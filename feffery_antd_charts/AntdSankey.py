# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSankey(Component):
    """An AntdSankey component.
桑基图组件AntdSankey

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- style (dict; optional):
    当前组件css样式.

- data (list of dicts; optional):
    必填，定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- sourceField (string; optional):
    来源节点字段.

- targetField (string; optional):
    目标节点字段.

- weightField (string; optional):
    权重字段.

- rawFields (list of strings; optional):
    声明辅助额外字段.

- width (number; optional):
    图表容器像素宽度.

- height (number; optional):
    图表容器像素高度.

- autoFit (boolean; optional):
    图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效  默认值：`True`.

- padding (number | list of numbers | a value equal to: 'auto'; optional):
    画布内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组，或传入`'auto'`开启底层自动计算.

- appendPadding (number | list of numbers; optional):
    画布额外内边距，传入单个数值表示四周边距，也可传入格式如`[上边距，右边距，下边距，左边距]`的数组.

- renderer (a value equal to: 'canvas', 'svg'; optional):
    图表底层渲染方式，可选项有`'canvas'`和`'svg'`  默认值：`'canvas'`.

- pixelRatio (number; optional):
    `renderer='canvas'`时，控制渲染图表图片的像素比  默认值：`1`.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN'):
    图表文案语种，可选项有`'zh-CN'`、`'en-US'`  默认值：`'zh-CN'`.

- limitInPlot (boolean; optional):
    是否对超出绘图区域的几何元素进行裁剪.

- nodeStyle (dict; optional):
    控制填充区域样式，具体见在线文档相关说明.

    `nodeStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- edgeStyle (dict; optional):
    控制轮廓样式，具体见在线文档相关说明.

    `edgeStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- color (dict; optional):
    控制填充区域颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- nodeWidthRatio (number; optional):
    节点宽度比例，取值应在`0`到`1`之间，以画布宽度为单位`1`  默认值：`0.008`.

- nodePaddingRatio (number; optional):
    节点之间间距比例，取值应在`0`到`1`之间，以画布宽度为单位`1`  默认值：`0.01`.

- nodeAlign (a value equal to: 'left', 'right', 'center', 'justify'; optional):
    节点布局方式，可选项有`'left'`、`'right'`、`'center'`、`'justify'`
    默认值：`'justify'`.

- nodeDraggable (boolean; optional):
    节点是否可拖拽调整位置  默认值：`False`.

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

- recentlyTooltipChangeRecord (dict; optional):
    事件监听属性，用于监听最近一次信息框显示事件.

    `recentlyTooltipChangeRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (list of dicts; optional):
        涉及数据信息.

- recentlyAreaClickRecord (dict; optional):
    事件监听属性，用于监听最近一次区域点击事件.

    `recentlyAreaClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

- downloadTrigger (string; default 'download-trigger'):
    对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片.

- theme (optional):
    配置主题相关参数，具体见在线文档相关说明.

- interactions (optional):
    配置交互功能相关参数，具体见在线文档相关说明.

- state (optional):
    配置状态样式相关参数，具体见在线文档相关说明.

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
    _type = 'AntdSankey'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, meta=Component.UNDEFINED, sourceField=Component.UNDEFINED, targetField=Component.UNDEFINED, weightField=Component.UNDEFINED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, nodeStyle=Component.UNDEFINED, edgeStyle=Component.UNDEFINED, color=Component.UNDEFINED, nodeWidthRatio=Component.UNDEFINED, nodePaddingRatio=Component.UNDEFINED, nodeAlign=Component.UNDEFINED, nodeDraggable=Component.UNDEFINED, tooltip=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'sourceField', 'targetField', 'weightField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'nodeStyle', 'edgeStyle', 'color', 'nodeWidthRatio', 'nodePaddingRatio', 'nodeAlign', 'nodeDraggable', 'tooltip', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'sourceField', 'targetField', 'weightField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'nodeStyle', 'edgeStyle', 'color', 'nodeWidthRatio', 'nodePaddingRatio', 'nodeAlign', 'nodeDraggable', 'tooltip', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdSankey, self).__init__(**args)
