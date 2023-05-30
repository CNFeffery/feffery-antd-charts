# AUTO GENERATED FILE - DO NOT EDIT

export ''_antddualaxes

"""
    ''_antddualaxes(;kwargs...)

An AntdDualAxes component.

Keyword arguments:
- `id` (String; optional)
- `animation` (Dict | Bool; optional)
- `annotations` (Dict with Strings as keys and values of type ; optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `data` (Array of Array of Dictss; required)
- `downloadTrigger` (String; optional)
- `geometryOptions` (optional): . geometryOptions has the following type: Array of lists containing elements 'geometry', 'seriesField', 'smooth', 'connectNulls', 'lineStyle', 'point', 'label', 'color'.
Those elements have the following types:
  - `geometry` (a value equal to: 'line', 'column'; optional)
  - `seriesField` (String; optional)
  - `smooth` (Bool; optional)
  - `connectNulls` (Bool; optional)
  - `lineStyle` (optional): . lineStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
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
  - `label` (optional)
  - `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional) | lists containing elements 'geometry', 'seriesField', 'groupField', 'isGroup', 'isStack', 'columnWidthRatio', 'marginRatio', 'columnStyle', 'label', 'color'.
Those elements have the following types:
  - `geometry` (a value equal to: 'line', 'column'; optional)
  - `seriesField` (String; optional)
  - `groupField` (String; optional)
  - `isGroup` (Bool; optional)
  - `isStack` (Bool; optional)
  - `columnWidthRatio` (Real; optional)
  - `marginRatio` (Real; optional)
  - `columnStyle` (optional): . columnStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `label` (optional)
  - `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)s
- `height` (Real; optional)
- `key` (String; optional)
- `legend` (optional)
- `limitInPlot` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (Dict with Strings as keys and values of type ; optional)
- `yField` (Array of Strings; required)
"""
function ''_antddualaxes(; kwargs...)
        available_props = Symbol[:id, :animation, :annotations, :appendPadding, :autoFit, :className, :data, :downloadTrigger, :geometryOptions, :height, :key, :legend, :limitInPlot, :loading_state, :locale, :meta, :padding, :renderer, :style, :theme, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antddualaxes", "AntdDualAxes", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

