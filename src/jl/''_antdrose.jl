# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdrose

"""
    ''_antdrose(;kwargs...)

An AntdRose component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `endAngle` (Real; optional)
- `height` (Real; optional)
- `innerRadius` (Real; optional)
- `isGroup` (Bool; optional)
- `isStack` (Bool; optional)
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
- `radius` (Real; optional)
- `recentlyAreaClickRecord` (optional): . recentlyAreaClickRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Bool | Real | String | Dict | Array; optional)
- `recentlyLegendInfo` (optional): . recentlyLegendInfo has the following type: lists containing elements 'triggerItemName', 'items'.
Those elements have the following types:
  - `triggerItemName` (Bool | Real | String | Dict | Array; optional)
  - `items` (Array of Dicts; optional)
- `recentlyTooltipChangeRecord` (optional): . recentlyTooltipChangeRecord has the following type: lists containing elements 'timestamp', 'data'.
Those elements have the following types:
  - `timestamp` (Real; optional)
  - `data` (Array of Dicts; optional)
- `renderer` (String; optional)
- `sectorStyle` (optional): . sectorStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `seriesField` (String; optional)
- `startAngle` (Real; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; optional)
- `yAxis` (optional)
- `yField` (String; optional)
"""
function ''_antdrose(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :color, :data, :downloadTrigger, :endAngle, :height, :innerRadius, :isGroup, :isStack, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :meta, :padding, :radius, :recentlyAreaClickRecord, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :renderer, :sectorStyle, :seriesField, :startAngle, :style, :theme, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdrose", "AntdRose", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

