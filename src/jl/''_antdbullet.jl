# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdbullet

"""
    ''_antdbullet(;kwargs...)

An AntdBullet component.

Keyword arguments:
- `id` (String; optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `bulletStyle` (optional): . bulletStyle has the following type: lists containing elements 'range', 'measure', 'target'.
Those elements have the following types:
  - `range` (optional): . range has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `measure` (optional): . measure has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `target` (optional): . target has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: lists containing elements 'range', 'measure', 'target'.
Those elements have the following types:
  - `range` (String | Array of Strings; optional)
  - `measure` (String | Array of Strings; optional)
  - `target` (String | Array of Strings; optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
- `key` (String; optional)
- `label` (optional): . label has the following type: lists containing elements 'range', 'measure', 'target'.
Those elements have the following types:
  - `range` (optional)
  - `measure` (optional)
  - `target` (optional)
- `layout` (a value equal to: 'horizontal', 'vertical'; optional)
- `legend` (optional)
- `limitInPlot` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `measureField` (String; required)
- `meta` (optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `rangeField` (String; required)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `size` (optional): . size has the following type: lists containing elements 'range', 'measure', 'target'.
Those elements have the following types:
  - `range` (optional): . range has the following type: Real | Array of Reals | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `measure` (optional): . measure has the following type: Real | Array of Reals | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `target` (optional): . target has the following type: Real | Array of Reals | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `style` (Dict; optional)
- `targetField` (String; required)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; optional)
- `yAxis` (optional)
"""
function ''_antdbullet(; kwargs...)
        available_props = Symbol[:id, :appendPadding, :autoFit, :bulletStyle, :className, :color, :data, :downloadTrigger, :height, :key, :label, :layout, :legend, :limitInPlot, :loading_state, :locale, :measureField, :meta, :padding, :rangeField, :renderer, :size, :style, :targetField, :theme, :tooltip, :width, :xAxis, :xField, :yAxis]
        wild_props = Symbol[]
        return Component("''_antdbullet", "AntdBullet", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

