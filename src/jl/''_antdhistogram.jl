# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdhistogram

"""
    ''_antdhistogram(;kwargs...)

An AntdHistogram component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `autoFit` (Bool; optional)
- `binField` (String; required)
- `binNumber` (Real; optional)
- `binWidth` (Real; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `columnStyle` (optional): . columnStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
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
- `recentlyAreaClickRecord` (optional): . recentlyAreaClickRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Dict; optional)
- `recentlyLegendInfo` (optional): . recentlyLegendInfo has the following type: lists containing elements 'triggerItemName', 'items'.
Those elements have the following types:
  - `triggerItemName` (Bool | Real | String | Dict | Array; optional)
  - `items` (Array of Dicts; optional)
- `recentlyTooltipChangeRecord` (optional): . recentlyTooltipChangeRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Array of Dicts; optional)
- `renderer` (String; optional)
- `stackField` (String; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `yAxis` (optional)
"""
function ''_antdhistogram(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :binField, :binNumber, :binWidth, :className, :color, :columnStyle, :data, :downloadTrigger, :height, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :meta, :padding, :recentlyAreaClickRecord, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :renderer, :stackField, :style, :theme, :tooltip, :width, :xAxis, :yAxis]
        wild_props = Symbol[]
        return Component("''_antdhistogram", "AntdHistogram", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

