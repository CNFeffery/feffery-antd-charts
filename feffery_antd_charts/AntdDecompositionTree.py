# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDecompositionTree(Component):
    """An AntdDecompositionTree component.
指标拆解图组件AntdDecompositionTree

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

- width (number; optional):
    图表容器像素宽度.

- height (number; optional):
    图表容器像素高度.

- autoFit (boolean; optional):
    图表是否自适应所在父容器宽高，当`autoFit=True`时，`width`和`height`参数将失效  默认值：`True`.

- nodeCfg (dict; optional):
    配置节点相关参数，具体见在线文档相关说明.

    `nodeCfg` is a dict with keys:

    - type (a value equal to: 'indicator-card'; optional):
        节点类型，可选项有`'indicator-card'`.

    - size (list of numbers; optional):
        节点像素尺寸范围  默认值：`[120, 40]`.

    - style (dict; optional):
        节点样式.

        `style` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

    - label (dict; optional):
        节点文本样式.

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

    - anchorPoints (list of list of numberss; optional):
        边相对于节点的锚点位置  默认值：`[[0.5, 0], [0.5, 1]]`.

    - title (dict; optional):
        配置节点标题.

        `title` is a dict with keys:

        - containerStyle (optional):
            标题容器样式.

        - style (dict; optional):
            标题样式.

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

        - autoEllipsis (boolean; optional):
            文本是否超出范围后自动隐藏.

    - items (dict; optional):
        配置节点内容.

        `items` is a dict with keys:

        - containerStyle (optional):
            节点内容容器样式.

        - style (dict; optional):
            节点内容样式.

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

        - layout (a value equal to: 'bundled', 'flex', 'follow'; optional):
            布局方式，可选项有`'bundled'`、`'flex'`、`'follow'`  默认值：`'bundled'`.

        - sort (boolean; optional):
            是否按照节点顺序渲染.

        - padding (number | list of numbers; optional):
            节点内容容器填充.

    - padding (number | list of numbers; optional):
        文本填充.

    - badge (dict; optional):
        配置节点标记.

        `badge` is a dict with keys:

        - position (a value equal to: 'left', 'top', 'right', 'bottom'; optional):
            标记位置，可选项有`'left'`、`'top'`、`'right'`、`'bottom'`.

        - size (number | list of numbers; optional):
            标记尺寸.

        - style (dict; optional):
            标记样式.

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

    - percent (dict; optional):
        配置节点占比内容.

        `percent` is a dict with keys:

        - position (a value equal to: 'top', 'bottom'; optional):
            占比内容位置，可选项有`'top'`、`'bottom'`.

        - size (number; optional):
            占比内容背景像素高度.

        - style (dict; optional):
            占比内容样式.

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

        - backgroundStyle (optional):
            占比内容背景样式.

    - autoWidth (boolean; optional):
        是否动态调整节点宽度.

    - nodeStateStyles (dict with strings as keys and values of type  | boolean; optional):
        配置节点不同状态下的样式，可用的状态有`'hover'`.

- edgeCfg (dict; optional):
    配置边相关参数，具体见在线文档相关说明.

    `edgeCfg` is a dict with keys:

    - type (a value equal to: 'line', 'polyline', 'arc', 'quadratic', 'cubic', 'cubic-vertical', 'cubic-horizontal', 'loop'; optional):
        边类型，可选项有`'line'`、`'polyline'`、`'arc'`、`'quadratic'`、`'cubic'`、`'cubic-vertical'`、`'cubic-horizontal'`、`'loop'`
        默认值：`'cubic-horizontal'`.

    - label (dict; optional):
        边文本样式.

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional):
        js函数体字符串.

    - startArrow (dict; optional):
        配置边开始箭头.

        `startArrow` is a dict with keys:

        - type (a value equal to: 'vee', 'triangle'; optional):
            箭头类型，可选项有`'vee'`、`'triangle'`.

        - d (number; optional):
            像素偏移量.

        - path (string; optional):
            绘制路径.

        - stroke (string; optional):
            描边色.

        - fill (string; optional):
            填充色.

    - endArrow (dict; optional):
        配置边结束箭头.

        `endArrow` is a dict with keys:

        - fill (string; optional):
            填充色.

        - show (boolean; optional):
            是否展示结束箭头.

    - edgeStateStyles (dict with strings as keys and values of type  | boolean; optional):
        配置边不同状态下的样式，可用的状态有`'hover'`.

    - style (dict; optional):
        边样式.

        `style` is a dict with keys:

        - func (string; optional):

            js函数体字符串.

- level (number; optional):
    默认展开层级  默认值：`100`.

- behaviors (list of a value equal to: 'drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node', 'click-select's; optional):
    配置要启用的交互模式，支持多选，可选项有`'drag-canvas'`、`'scroll-canvas'`、`'zoom-canvas'`、`'drag-node'`、`'click-select'`
    默认值：`['drag-canvas', 'zoom-canvas']`.

- markerCfg (dict; optional):
    配置标记相关参数，具体见在线文档.

    `markerCfg` is a dict with keys:

    - show (boolean; optional):
        是否展示标记.

    - collapsed (boolean; optional):
        是否显示为折叠状态.

    - position (a value equal to: 'left', 'right', 'top', 'bottom'; optional):
        标记位置，可选项有`'left'`、`'right'`、`'top'`、`'bottom'`.

    - style (optional):
        标记样式.

      Or dict with keys:

    - func (string; optional):
        js函数体字符串.

- animate (boolean; optional):
    是否启用动画效果  默认值：`True`.

- minimapCfg (dict; optional):
    配置迷你图相关参数，具体见在线文档.

    `minimapCfg` is a dict with keys:

    - show (boolean; optional):
        是否展示迷你图  默认值：`False`.

    - viewportClassName (string; optional):
        迷你图css类名.

    - type (a value equal to: 'default', 'keyShape', 'delegate'; optional):
        迷你图类型，可选项有`'default'`、`'keyShape'`、`'delegate'`.

    - size (list of numbers; optional):
        配置迷你图像素尺寸，格式如`[宽度, 高度]`.

    - padding (number; optional):
        内填充像素尺寸.

- layout (dict; optional):
    配置布局相关参数，具体见在线文档.

    `layout` is a dict with keys:

    - direction (a value equal to: 'TB', 'BT', 'LR', 'RL'; optional):
        布局方式，可选项有`'TB'`、`'BT'`、`'LR'`、`'RL'`.

    - type (a value equal to: 'indented'; optional):
        布局类型，可选项有`'indented'`.

    - indent (number; optional):
        缩进像素宽度.

- recentlyNodeClickRecord (dict; optional):
    事件监听属性，用于监听最近一次节点点击事件.

    `recentlyNodeClickRecord` is a dict with keys:

    - timestamp (number; optional):
        事件时间戳.

    - data (dict; optional):
        涉及数据信息.

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
    _type = 'AntdDecompositionTree'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, nodeCfg=Component.UNDEFINED, edgeCfg=Component.UNDEFINED, level=Component.UNDEFINED, behaviors=Component.UNDEFINED, markerCfg=Component.UNDEFINED, animate=Component.UNDEFINED, minimapCfg=Component.UNDEFINED, layout=Component.UNDEFINED, recentlyNodeClickRecord=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'className', 'style', 'data', 'width', 'height', 'autoFit', 'nodeCfg', 'edgeCfg', 'level', 'behaviors', 'markerCfg', 'animate', 'minimapCfg', 'layout', 'recentlyNodeClickRecord', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'className', 'style', 'data', 'width', 'height', 'autoFit', 'nodeCfg', 'edgeCfg', 'level', 'behaviors', 'markerCfg', 'animate', 'minimapCfg', 'layout', 'recentlyNodeClickRecord', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(AntdDecompositionTree, self).__init__(**args)
