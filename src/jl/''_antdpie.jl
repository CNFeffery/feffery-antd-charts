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
- `downloadTrigger` (String; optional)
- `endAngle` (Real; optional)
- `height` (Real; optional)
- `innerRadius` (Real; optional)
- `interactions` (optional): . interactions has the following type: Array of lists containing elements 'type'.
Those elements have the following types:
  - `type` (a value equal to: 'element-active', 'element-selected', 'element-single-selected', 'element-highlight', 'element-highlight-by-color', 'element-highlight-by-x', 'legend-highlight', 'axis-label-highlight', 'pie-statistic-active'; optional)s
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `limitInPlot` (Bool; optional)
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
- `recentlySectorClickRecord` (optional): . recentlySectorClickRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Dict; optional)
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
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
"""
function ''_antdpie(; kwargs...)
        available_props = Symbol[:id, :angleField, :annotations, :appendPadding, :autoFit, :className, :color, :colorField, :data, :downloadTrigger, :endAngle, :height, :innerRadius, :interactions, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :meta, :padding, :pieStyle, :radius, :recentlySectorClickRecord, :renderer, :startAngle, :statistic, :style, :theme, :tooltip, :width]
        wild_props = Symbol[]
        return Component("''_antdpie", "AntdPie", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

