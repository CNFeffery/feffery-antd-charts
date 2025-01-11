# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSunburst(Component):
    """An AntdSunburst component.
旭日图组件AntdSunburst

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- style (dict; optional):
    当前组件css样式.

- data (dict; required):
    必填，定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- colorField (string; optional):
    色彩区分字段，默认为根节点的`name`字段.

- rawFields (list of strings; optional):
    声明额外辅助字段.

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

- hierarchyConfig (dict; optional):
    配置层次布局相关参数，具体见在线文档相关说明.

    `hierarchyConfig` is a dict with keys:

    - field (string; optional):
        节点权重字段  默认值：`'value'`.

    - ignoreParentValue (boolean; optional):
        是否忽略父节点实际权重  默认值：`True`.

- drilldown (dict; optional):
    配置下钻交互相关参数，具体见在线文档相关说明.

    `drilldown` is a dict with keys:

    - enabled (boolean; optional):
        是否开启下钻交互  默认值：`True`.

    - breadCrumb (dict; optional):
        配置下钻层级指示面包屑相关参数.

        `breadCrumb` is a dict with keys:

        - rootText (string; optional):
            根节点文案.

        - dividerText (string; optional):
            面包屑分隔符  默认值：`'/'`.

        - textStyle (optional):
            面包屑文字样式.

        - activeTextStyle (optional):
            面包屑激活状态字体样式.

        - position (a value equal to: 'top-left', 'bottom-left'; optional):
            面包屑显示位置，可选项有`'top-left'`、`'bottom-left'`
            默认值：`'bottom-left'`.

- radius (number; optional):
    外半径大小，取值应在`0`到`1`之间  默认值：`0.85`.

- innerRadius (number; optional):
    内半径大小，取值应在`0`到`1`之间  默认值：`0`.

- color (dict; optional):
    控制填充区域颜色，具体见在线文档相关说明.

    `color` is a string | list of strings | dict with keys:

    - func (string; optional):
        js函数体字符串.

- sunburstStyle (dict; optional):
    控制填充区域样式，具体见在线文档相关说明.

    `sunburstStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- reflect (boolean; default False):
    是否进行径向反转  默认值：`False`.

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

    - data (boolean | number | string | dict | list; optional):
        涉及数据信息.

- recentlyAreaClickRecord (dict; optional):
    事件监听属性，用于监听最近一次折点点击事件.

    `recentlyAreaClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (boolean | number | string | dict | list; optional):
        涉及数据信息.

- downloadTrigger (string; default 'download-trigger'):
    对当前组件的`downloadTrigger`值进行更新，可实现主动下载当前图表为`png`格式图片.

- theme (optional):
    配置主题相关参数，具体见在线文档相关说明.

- pattern (optional):
    配置图形填充贴图相关参数，具体见在线文档相关说明.

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
    _type = 'AntdSunburst'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, colorField=Component.UNDEFINED, rawFields=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, hierarchyConfig=Component.UNDEFINED, drilldown=Component.UNDEFINED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, color=Component.UNDEFINED, sunburstStyle=Component.UNDEFINED, reflect=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, annotations=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyTooltipChangeRecord=Component.UNDEFINED, recentlyAreaClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, pattern=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'colorField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'hierarchyConfig', 'drilldown', 'radius', 'innerRadius', 'color', 'sunburstStyle', 'reflect', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'colorField', 'rawFields', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'hierarchyConfig', 'drilldown', 'radius', 'innerRadius', 'color', 'sunburstStyle', 'reflect', 'label', 'tooltip', 'annotations', 'animation', 'recentlyTooltipChangeRecord', 'recentlyAreaClickRecord', 'downloadTrigger', 'theme', 'pattern', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdSunburst, self).__init__(**args)
