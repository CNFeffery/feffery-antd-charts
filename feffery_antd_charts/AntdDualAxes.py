# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDualAxes(Component):
    """An AntdDualAxes component.
双轴图组件AntdDualAxes

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- style (dict; optional):
    当前组件css样式.

- data (list of list of dictss; required):
    必填，定义绘图所需数据.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- xField (string; required):
    必填，图表x轴字段.

- yField (list of strings; required):
    必填，图表y轴字段，格式如`[左轴字段, 右轴字段]`.

- geometryOptions (list of dicts; optional):
    分别配置左右轴相关参数，格式如`[左轴配置, 右轴配置]`，具体见在线文档相关说明.

    `geometryOptions` is a list of dicts with keys:

    - geometry (a value equal to: 'line', 'column'; optional):
        当前轴图表类型，可选项为`'line'`（折线图）、`'column'`（柱状图）.

    - seriesField (string; optional):
        当前轴分组字段.

    - smooth (boolean; optional):
        针对折线图是否渲染为光滑曲线  默认值：`False`.

    - connectNulls (boolean; optional):
        针对折线图中的缺失值片段，是否对空数据段两端进行连线  默认值：`True`.

    - lineStyle (dict; optional):
        控制折线样式，具体见在线文档相关说明.

        `lineStyle` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - point (dict; optional):
        配置折点相关参数，具体见在线文档相关说明.

        `point` is a dict with keys:

        - color (dict; optional):
            配置折点颜色，具体见在线文档相关说明.

            `color` is a string

          Or list of strings

      Or dict with keys:

    - func (string; optional):
        js函数体字符串.

        - shape (dict; optional):
            配置折点形状，具体见在线文档相关说明.

            `shape` is a string | dict with keys:

    - func (string; optional):
        js函数体字符串.

        - style (dict; optional):
            配置折点样式，具体见在线文档相关说明.

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

    - label (optional):
        配置数值标签相关参数，具体见在线文档相关说明.

    - color (dict; optional):
        控制折线颜色，具体见在线文档相关说明.

        `color` is a string | list of strings | dict with keys:

        - func (string; optional):

            js函数体字符串.

    - stepType (string; optional):
        阶梯折线图类型，可选项有`'hv'`、`'vh'`、`'hvh'`、`'vhv'`，其中`'h'`代表水平方向，`'v'`代表竖直方向，譬如`'vh`就代表先竖直再水平. | dict with keys:

    - geometry (a value equal to: 'line', 'column'; optional):
        当前轴图表类型，可选项为`'line'`（折线图）、`'column'`（柱状图）.

    - seriesField (string; optional):
        当前轴分组字段.

    - groupField (string; optional):
        `isGroup=True`时有效，用于针对堆叠分组条形图指定分组字段.

    - isGroup (boolean; optional):
        `seriesField`有效时，是否渲染分组条形图.

    - isStack (boolean; optional):
        `seriesField`有效时，是否渲染堆叠条形图.

    - columnWidthRatio (number; optional):
        柱体宽度比例，取值在`0`到`1`之间.

    - marginRatio (number; optional):
        分组柱体间隔宽度比例，取值在`0`到`1`之间.

    - columnStyle (dict; optional):
        控制柱体填充样式，具体见在线文档相关说明.

        `columnStyle` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - label (optional):
        配置数值标签相关参数，具体见在线文档相关说明.

    - color (dict; optional):
        控制柱体填充颜色，具体见在线文档相关说明.

        `color` is a string | list of strings | dict with keys:

        - func (string; optional):

            js函数体字符串.

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

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- xAxis (optional):
    配置横坐标轴相关参数，具体见在线文档相关说明.

- yAxis (dict with strings as keys and values of type ; optional):
    配置纵坐标轴相关参数，具体见在线文档相关说明.

- annotations (dict with strings as keys and values of type ; optional):
    配置标注相关参数，具体见在线文档相关说明.

- legend (optional):
    配置图例相关参数，具体见在线文档相关说明.

- slider (optional):
    配置缩略轴相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

- recentlyClickRecord (dict; optional):
    事件监听属性，用于监听最近一次数据项点击事件.

    `recentlyClickRecord` is a dict with keys:

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
    _type = 'AntdDualAxes'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, xField=Component.REQUIRED, yField=Component.REQUIRED, geometryOptions=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, tooltip=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, annotations=Component.UNDEFINED, legend=Component.UNDEFINED, slider=Component.UNDEFINED, animation=Component.UNDEFINED, recentlyClickRecord=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'geometryOptions', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'tooltip', 'xAxis', 'yAxis', 'annotations', 'legend', 'slider', 'animation', 'recentlyClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'xField', 'yField', 'geometryOptions', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'tooltip', 'xAxis', 'yAxis', 'annotations', 'legend', 'slider', 'animation', 'recentlyClickRecord', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'xField', 'yField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdDualAxes, self).__init__(**args)
