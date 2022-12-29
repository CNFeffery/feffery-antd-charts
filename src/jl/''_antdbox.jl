# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdbox

"""
    ''_antdbox(;kwargs...)

An AntdBox component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `autoFit` (Bool; optional)
- `boxStyle` (optional): . boxStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `groupField` (String; optional)
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
- `outliersField` (String; optional)
- `outliersStyle` (optional): . outliersStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `padding` (Real | Array of Reals | String; optional)
- `recentlyBoxClickRecord` (optional): . recentlyBoxClickRecord has the following type: lists containing elements 'timestamp', 'data'.
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
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (optional)
- `yField` (Array of Strings | String; required)
"""
function ''_antdbox(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :boxStyle, :className, :color, :data, :downloadTrigger, :groupField, :height, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :meta, :outliersField, :outliersStyle, :padding, :recentlyBoxClickRecord, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :renderer, :style, :theme, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdbox", "AntdBox", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

