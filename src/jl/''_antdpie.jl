# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdpie

"""
    ''_antdpie(;kwargs...)

An AntdPie component.

Keyword arguments:
- `id` (String; optional)
- `angleField` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `colorField` (String; optional)
- `data` (Array of Dicts; required)
- `endAngle` (Real; optional)
- `height` (Real; optional)
- `innerRadius` (Real; optional)
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
- `pieStyle` (optional): . pieStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `radius` (Real; optional)
- `renderer` (String; optional)
- `startAngle` (Real; optional)
- `statistic` (optional): . statistic has the following type: lists containing elements 'title', 'content'.
Those elements have the following types:
  - `title` (optional): . title has the following type: Bool | lists containing elements 'style', 'content', 'formatter', 'rotate', 'offsetX', 'offsetY'.
Those elements have the following types:
  - `style` (Dict; optional)
  - `content` (String; optional)
  - `formatter` (optional): . formatter has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `rotate` (Real; optional)
  - `offsetX` (Real; optional)
  - `offsetY` (Real; optional)
  - `content` (optional): . content has the following type: Bool | lists containing elements 'style', 'content', 'formatter', 'rotate', 'offsetX', 'offsetY'.
Those elements have the following types:
  - `style` (Dict; optional)
  - `content` (String; optional)
  - `formatter` (optional): . formatter has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `rotate` (Real; optional)
  - `offsetX` (Real; optional)
  - `offsetY` (Real; optional)
- `style` (Dict; optional)
- `tooltip` (optional)
- `width` (Real; optional)
"""
function ''_antdpie(; kwargs...)
        available_props = Symbol[:id, :angleField, :annotations, :appendPadding, :autoFit, :className, :color, :colorField, :data, :endAngle, :height, :innerRadius, :key, :label, :legend, :loading_state, :locale, :meta, :padding, :pieStyle, :radius, :renderer, :startAngle, :statistic, :style, :tooltip, :width]
        wild_props = Symbol[]
        return Component("''_antdpie", "AntdPie", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

