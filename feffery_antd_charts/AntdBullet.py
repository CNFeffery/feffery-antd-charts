# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdBullet(Component):
    """An AntdBullet component.


Keyword arguments:

- id (string; optional)

- key (string; optional)

- className (string; optional)

- style (dict; optional)

- data (list of dicts; required)

- meta (optional)

- measureField (string; required)

- rangeField (string; required)

- targetField (string; required)

- xField (string; optional)

- xAxis (optional)

- yAxis (optional)

- width (number; optional)

- height (number; optional)

- autoFit (boolean; optional)

- padding (number | list of numbers | a value equal to: 'auto'; optional)

- appendPadding (number | list of numbers; optional)

- renderer (a value equal to: 'canvas', 'svg'; optional)

- pixelRatio (number; optional):
    canvas模式下，控制渲染图表图片的像素比  默认：1.

- locale (a value equal to: 'zh-CN', 'en-US'; default 'zh-CN')

- limitInPlot (boolean; optional)

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal')

- color (dict; optional)

    `color` is a dict with keys:

    - range (string | list of strings; optional)

    - measure (string | list of strings; optional)

    - target (string | list of strings; optional)

- size (dict; optional)

    `size` is a dict with keys:

    - range (dict; optional)

        `range` is a number

      Or list of numbers | dict with keys:

        - func (string; optional)

    - measure (dict; optional)

        `measure` is a number | list of numbers | dict with keys:

        - func (string; optional)

    - target (dict; optional)

        `target` is a number | list of numbers | dict with keys:

        - func (string; optional)

- bulletStyle (dict; optional)

    `bulletStyle` is a dict with keys:

    - range (dict; optional)

        `range` is a dict with keys:

        - func (string; optional)

    - measure (dict; optional)

        `measure` is a dict with keys:

        - func (string; optional)

    - target (dict; optional)

        `target` is a dict with keys:

        - func (string; optional)

- label (dict; optional)

    `label` is a dict with keys:

    - range (optional)

    - measure (optional)

    - target (optional)

- tooltip (optional)

- legend (optional)

- animation (optional)

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
