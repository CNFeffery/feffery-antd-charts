# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdscatter

"""
    ''_antdscatter(;kwargs...)

An AntdScatter component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `colorField` (String; optional)
- `data` (Array of Dicts; required)
- `height` (Real; optional)
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (String; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | String; optional)
- `pointStyle` (optional): . pointStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `quadrant` (optional): . quadrant has the following type: lists containing elements 'xBaseline', 'yBaseline', 'lineStyle', 'regionStyle', 'labels'.
Those elements have the following types:
  - `xBaseline` (Real; optional)
  - `yBaseline` (Real; optional)
  - `lineStyle` (optional)
  - `regionStyle` (Array; optional)
  - `labels` (optional): . labels has the following type: Array of lists containing elements 'content', 'position', 'style'.
Those elements have the following types:
  - `content` (String; optional)
  - `position` (Array of Reals; optional)
  - `style` (optional)s
- `regressionLine` (optional): . regressionLine has the following type: lists containing elements 'type', 'style', 'algorithm', 'top'.
Those elements have the following types:
  - `type` (a value equal to: 'exp', 'linear', 'loess', 'log', 'poly', 'pow', 'quad'; optional)
  - `style` (optional)
  - `algorithm` (optional): . algorithm has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `top` (Bool; optional)
- `renderer` (String; optional)
- `shape` (optional): . shape has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `shapeField` (String; optional)
- `shapeLegend` (optional)
- `size` (optional): . size has the following type: Real | Array of Reals | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `sizeField` (String; optional)
- `sizeLegend` (optional)
- `style` (Dict; optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (optional)
- `yField` (String; required)
"""
function ''_antdscatter(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :color, :colorField, :data, :height, :key, :label, :legend, :loading_state, :locale, :meta, :padding, :pointStyle, :quadrant, :regressionLine, :renderer, :shape, :shapeField, :shapeLegend, :size, :sizeField, :sizeLegend, :style, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdscatter", "AntdScatter", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

