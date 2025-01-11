# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdGauge(Component):
    """An AntdGauge component.
仪表盘组件AntdGauge

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string; optional):
    当前组件css类名.

- style (dict; optional):
    当前组件css样式.

- percent (number; required):
    当前仪表盘实际值，取值应在`0`到`1`之间.

- radius (number; default 0.95):
    仪表盘相对画布的外环半径尺寸，取值应在`0`到`1`之间  默认值：`0.95`.

- innerRadius (number; optional):
    仪表盘相对画布的内环半径大小，取值应在`0`到`1`之间  默认值：`0.9`.

- startAngle (number; optional):
    仪表盘开始角度，弧度制  默认值：`(-7 / 6) * π`.

- endAngle (number; optional):
    仪表盘终止角度，弧度制  默认值：`(1 / 6) * π`.

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

- range (dict; optional):
    配置仪表盘辅助圆弧，具体见在线文档相关说明.

    `range` is a dict with keys:

    - ticks (list of numbers; optional):
        辅助圆弧显示刻度值数组.

    - color (string | list of strings; optional):
        辅助圆弧背景色，传入数组时表示渐变色.

    - width (number; optional):
        辅助圆弧像素宽度.

- type (a value equal to: 'meter'; optional):
    仪表盘类型，可选项有`'meter'`.

- meter (dict; optional):
    针对`type='meter'`的仪表盘进行配置.

    `meter` is a dict with keys:

    - steps (number; optional):
        仪表盘总步数  默认值：`50`.

    - stepRatio (number; optional):
        分步刻度与对应间距的宽度比例关系  默认值：`0.5`.

- gaugeStyle (dict; optional):
    控制仪表盘样式，具体见在线文档相关说明.

    `gaugeStyle` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

- axis (optional):
    配置坐标轴相关参数，具体见在线文档相关说明.

- indicator (dict; optional):
    配置仪表盘指示器，具体见在线文档相关说明.

    `indicator` is a dict with keys:

    - pointer (dict; optional):
        配置指示器指针.

        `pointer` is a dict with keys:

        - style (optional):
            配置指示器指针样式.

    - pin (dict; optional):
        配置指示器圆盘.

        `pin` is a dict with keys:

        - style (optional):
            配置指示器圆盘样式.

    - shape (a value equal to: 'default', 'cursor', 'ring-cursor', 'simple'; optional):
        指示器指针类型，可选项有`'default'`、`'cursor'`、`'ring-cursor'`、`'simple'`.

- statistic (dict; optional):
    配置仪表盘中心统计内容，具体见在线文档相关说明.

    `statistic` is a boolean | dict with keys:

    - title (dict; optional):
        配置统计内容标题，设置为`False`时将隐藏标题.

        `title` is a boolean

      Or dict with keys:

        - style (dict; optional):

            统计内容标题样式.

        - content (string; optional):

            配置统计内容标题文本.

        - formatter (dict; optional):

            格式化统计内容标题文本函数.

            `formatter` is a dict with keys:

            - func (string; optional):

                js函数体字符串.

        - customHtml (dict; optional):

            配置统计内容标题原始html文本内容.

            `customHtml` is a dict with keys:

            - func (string; optional):

                js函数体字符串.

        - rotate (number; optional):

            标题旋转角度.

        - offsetX (number; optional):

            标题水平像素偏移.

        - offsetY (number; optional):

            标题竖直像素偏移.

    - content (dict; optional):
        配置统计内容，设置为`False`时将隐藏内容.

        `content` is a boolean | dict with keys:

        - style (dict; optional):

            统计内容样式.

        - content (string; optional):

            配置统计内容文本.

        - formatter (dict; optional):

            格式化统计内容文本函数.

            `formatter` is a dict with keys:

            - func (string; optional):

                js函数体字符串.

        - customHtml (dict; optional):

            配置统计内容原始html文本内容.

            `customHtml` is a dict with keys:

            - func (string; optional):

                js函数体字符串.

        - rotate (number; optional):

            标题旋转角度.

        - offsetX (number; optional):

            标题水平像素偏移.

        - offsetY (number; optional):

            标题竖直像素偏移.

    - style (optional):
        统计内容样式.

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
    _type = 'AntdGauge'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, percent=Component.REQUIRED, radius=Component.UNDEFINED, innerRadius=Component.UNDEFINED, startAngle=Component.UNDEFINED, endAngle=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, padding=Component.UNDEFINED, appendPadding=Component.UNDEFINED, renderer=Component.UNDEFINED, pixelRatio=Component.UNDEFINED, locale=Component.UNDEFINED, limitInPlot=Component.UNDEFINED, range=Component.UNDEFINED, type=Component.UNDEFINED, meter=Component.UNDEFINED, gaugeStyle=Component.UNDEFINED, axis=Component.UNDEFINED, indicator=Component.UNDEFINED, statistic=Component.UNDEFINED, animation=Component.UNDEFINED, downloadTrigger=Component.UNDEFINED, theme=Component.UNDEFINED, interactions=Component.UNDEFINED, state=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'percent', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'range', 'type', 'meter', 'gaugeStyle', 'axis', 'indicator', 'statistic', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'percent', 'radius', 'innerRadius', 'startAngle', 'endAngle', 'width', 'height', 'autoFit', 'padding', 'appendPadding', 'renderer', 'pixelRatio', 'locale', 'limitInPlot', 'range', 'type', 'meter', 'gaugeStyle', 'axis', 'indicator', 'statistic', 'animation', 'downloadTrigger', 'theme', 'interactions', 'state', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['percent']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdGauge, self).__init__(**args)
