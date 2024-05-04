# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDecompositionTree(Component):
    """An AntdDecompositionTree component.


Keyword arguments:

- id (string; optional)

- animate (boolean; optional)

- autoFit (boolean; optional)

- behaviors (list of a value equal to: 'drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node', 'click-select's; optional)

- className (string; optional)

- data (dict; required)

- edgeCfg (dict; optional)

    `edgeCfg` is a dict with keys:

    - edgeStateStyles (dict with strings as keys and values of type  | boolean; optional)

    - endArrow (dict; optional)

        `endArrow` is a dict with keys:

        - fill (string; optional)

        - show (boolean; optional)

    - label (dict; optional)

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - startArrow (dict; optional)

        `startArrow` is a dict with keys:

        - d (number; optional)

        - fill (string; optional)

        - path (string; optional)

        - stroke (string; optional)

        - type (a value equal to: 'vee', 'triangle'; optional)

    - style (dict; optional)

        `style` is a dict with keys:

        - func (string; optional)

    - type (a value equal to: 'line', 'polyline', 'arc', 'quadratic', 'cubic', 'cubic-vertical', 'cubic-horizontal', 'loop'; optional)

- height (number; optional)

- key (string; optional)

- layout (dict; optional)

    `layout` is a dict with keys:

    - direction (a value equal to: 'TB', 'BT', 'LR', 'RL'; optional)

    - dropCap (boolean; optional)

    - indent (number; optional)

    - type (a value equal to: 'indented'; optional)

- level (number; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- markerCfg (dict; optional)

    `markerCfg` is a dict with keys:

    - collapsed (boolean; optional)

    - position (a value equal to: 'left', 'right', 'top', 'bottom'; optional)

    - show (boolean; optional)

    - style (optional)

      Or dict with keys:

    - func (string; optional)

- minimapCfg (dict; optional)

    `minimapCfg` is a dict with keys:

    - delegateStyle (optional)

    - padding (number; optional)

    - refresh (boolean; optional)

    - show (boolean; optional)

    - size (list of numbers; optional)

    - type (a value equal to: 'default', 'keyShape', 'delegate'; optional)

    - viewportClassName (string; optional)

- nodeCfg (dict; optional)

    `nodeCfg` is a dict with keys:

    - anchorPoints (list of list of numberss; optional)

    - autoWidth (boolean; optional)

    - badge (dict; optional)

        `badge` is a dict with keys:

        - position (a value equal to: 'left', 'top', 'right', 'bottom'; optional)

        - size (number | list of numbers; optional)

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - items (dict; optional)

        `items` is a dict with keys:

        - containerStyle (optional)

        - layout (a value equal to: 'bundled', 'flex', 'follow'; optional)

        - padding (number | list of numbers; optional)

        - sort (boolean; optional)

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - label (dict; optional)

        `label` is a dict with keys:

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - nodeStateStyles (dict with strings as keys and values of type  | boolean; optional)

    - padding (number | list of numbers; optional)

    - percent (dict; optional)

        `percent` is a dict with keys:

        - backgroundStyle (optional)

        - position (a value equal to: 'top', 'bottom'; optional)

        - size (number; optional)

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - size (list of numbers; optional)

    - style (dict; optional)

        `style` is a dict with keys:

        - func (string; optional)

    - title (dict; optional)

        `title` is a dict with keys:

        - autoEllipsis (boolean; optional)

        - containerStyle (optional)

        - style (dict; optional)

            `style` is a dict with keys:

    - func (string; optional)

    - type (a value equal to: 'indicator-card'; optional)

- recentlyNodeClickRecord (dict; optional):
    节点点击事件监听.

    `recentlyNodeClickRecord` is a dict with keys:

    - data (dict; optional):
        事件对应节点信息，点击空白处时为空.

    - timestamp (number; optional):
        事件触发时间戳.

- style (dict; optional)

- width (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_charts'
    _type = 'AntdDecompositionTree'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.REQUIRED, width=Component.UNDEFINED, height=Component.UNDEFINED, autoFit=Component.UNDEFINED, nodeCfg=Component.UNDEFINED, edgeCfg=Component.UNDEFINED, level=Component.UNDEFINED, behaviors=Component.UNDEFINED, markerCfg=Component.UNDEFINED, animate=Component.UNDEFINED, minimapCfg=Component.UNDEFINED, layout=Component.UNDEFINED, recentlyNodeClickRecord=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animate', 'autoFit', 'behaviors', 'className', 'data', 'edgeCfg', 'height', 'key', 'layout', 'level', 'loading_state', 'markerCfg', 'minimapCfg', 'nodeCfg', 'recentlyNodeClickRecord', 'style', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animate', 'autoFit', 'behaviors', 'className', 'data', 'edgeCfg', 'height', 'key', 'layout', 'level', 'loading_state', 'markerCfg', 'minimapCfg', 'nodeCfg', 'recentlyNodeClickRecord', 'style', 'width']
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
