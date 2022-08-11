# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdarea

"""
    ''_antdarea(;kwargs...)

An AntdArea component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `areaStyle` (optional): . areaStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
- `isPercent` (Bool; optional)
- `isStack` (Bool; optional)
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `limitInPlot` (Bool; optional)
- `line` (optional): . line has the following type: lists containing elements 'color', 'style'.
Those elements have the following types:
  - `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (String; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | String; optional)
- `point` (optional): . point has the following type: lists containing elements 'color', 'shape', 'style'.
Those elements have the following types:
  - `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `shape` (optional): . shape has the following type: String | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `renderer` (String; optional)
- `seriesField` (String; optional)
- `slider` (optional)
- `smooth` (Bool; optional)
- `startOnZero` (Bool; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (optional)
- `yField` (String; required)
"""
function ''_antdarea(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :areaStyle, :autoFit, :className, :color, :data, :downloadTrigger, :height, :isPercent, :isStack, :key, :label, :legend, :limitInPlot, :line, :loading_state, :locale, :meta, :padding, :point, :renderer, :seriesField, :slider, :smooth, :startOnZero, :style, :theme, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdarea", "AntdArea", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

