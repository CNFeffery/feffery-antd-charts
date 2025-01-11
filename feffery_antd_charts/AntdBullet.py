# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdBullet(Component):
    """An AntdBullet component.
子弹图组件AntdBullet

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
    必填，定义绘图所需数据，格式如`[{title: '满意度', ranges: [50, 100], measures: [80],
    target: 85}]`.

- meta (optional):
    以字段为单位，配置图表数据元信息，来定义所涉及数据的类型和展示方式，具体见在线文档相关说明.

- measureField (string; required):
    必填，子弹图长度字段.

- rangeField (string; required):
    必填，子弹图背景条字段.

- targetField (string; required):
    必填，子弹图目标值字段.

- xField (string; optional):
    必填，子弹图分组字段.

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

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    布局方向，可选项有`'horizontal'`、`'vertical'`  默认值：`'horizontal'`.

- color (dict; optional):
    控制子弹图各部分填充颜色，具体见在线文档相关说明.

    `color` is a dict with keys:

    - range (string | list of strings; optional):
        区间背景颜色.

    - measure (string | list of strings; optional):
        实际值颜色.

    - target (string | list of strings; optional):
        目标值颜色.

- size (dict; optional):
    配置子弹图各部分尺寸，具体见在线文档相关说明.

    `size` is a dict with keys:

    - range (dict; optional):
        区间背景像素尺寸.

        `range` is a number

      Or list of numbers | dict with keys:

        - func (string; optional):

            js函数体字符串.

    - measure (dict; optional):
        实际值像素尺寸.

        `measure` is a number | list of numbers | dict with keys:

        - func (string; optional):

            js函数体字符串.

    - target (dict; optional):
        目标值像素尺寸.

        `target` is a number | list of numbers | dict with keys:

        - func (string; optional):

            js函数体字符串.

- bulletStyle (dict; optional):
    控制子弹图各部分样式，具体见在线文档相关说明.

    `bulletStyle` is a dict with keys:

    - range (dict; optional):
        区间背景样式.

        `range` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - measure (dict; optional):
        实际值样式.

        `measure` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - target (dict; optional):
        目标值样式.

        `target` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

- label (dict; optional):
    配置子弹图各部分数值标签，具体见在线文档相关说明.

    `label` is a dict with keys:

    - range (optional):
        区间数值标签.

    - measure (optional):
        实际值标签.

    - target (optional):
        目标值标签.

- tooltip (optional):
    配置信息框相关参数，具体见在线文档相关说明.

- legend (optional):
    配置图例相关参数，具体见在线文档相关说明.

- animation (optional):
    配置动画相关参数，具体见在线文档相关说明.

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
    _type = 'AntdBullet'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, meta=Component.UNDEFINED, measureField=Component.REQUIRED, rangeField=Component.REQUIRED, targetField=Component.REQUIRED, xField=Component.UNDEFINED, xAxis=Component.UNDEFINED, yAxis=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, layout=Component.UNDEFINED, color=Component.UNDEFINED, size=Component.UNDEFINED, bulletStyle=Component.UNDEFINED, label=Component.UNDEFINED, tooltip=Component.UNDEFINED, legend=Component.UNDEFINED, animation=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'meta', 'measureField', 'rangeField', 'targetField', 'xField', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'layout', 'color', 'size', 'bulletStyle', 'label', 'tooltip', 'legend', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'meta', 'measureField', 'rangeField', 'targetField', 'xField', 'xAxis', 'yAxis', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'layout', 'color', 'size', 'bulletStyle', 'label', 'tooltip', 'legend', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data', 'measureField', 'rangeField', 'targetField']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdBullet, self).__init__(**args)
