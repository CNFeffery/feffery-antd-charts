# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdliquid

"""
    ''_antdliquid(;kwargs...)

An AntdLiquid component.

Keyword arguments:
- `id` (String; optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
- `key` (String; optional)
- `limitInPlot` (Bool; optional)
- `liquidStyle` (optional): . liquidStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `outline` (optional): . outline has the following type: lists containing elements 'border', 'distance', 'style'.
Those elements have the following types:
  - `border` (Real; optional)
  - `distance` (Real; optional)
  - `style` (optional): . style has the following type: lists containing elements 'stroke', 'strokeOpacity'.
Those elements have the following types:
  - `stroke` (String; optional)
  - `strokeOpacity` (Real; optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `percent` (Real; required)
- `radius` (Real; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `shape` (a value equal to: 'circle', 'diamond', 'triangle', 'pin', 'rect'; optional)
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
- `theme` (optional)
- `wave` (optional): . wave has the following type: lists containing elements 'count', 'length'.
Those elements have the following types:
  - `count` (Real; optional)
  - `length` (Real; optional)
- `width` (Real; optional)
"""
function ''_antdliquid(; kwargs...)
        available_props = Symbol[:id, :appendPadding, :autoFit, :className, :color, :downloadTrigger, :height, :key, :limitInPlot, :liquidStyle, :loading_state, :locale, :outline, :padding, :percent, :radius, :renderer, :shape, :statistic, :style, :theme, :wave, :width]
        wild_props = Symbol[]
        return Component("''_antdliquid", "AntdLiquid", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

