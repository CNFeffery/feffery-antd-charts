# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdfunnel

"""
    ''_antdfunnel(;kwargs...)

An AntdFunnel component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `compareField` (String; optional)
- `conversionTag` (optional): . conversionTag has the following type: lists containing elements 'size', 'spacing', 'offset', 'arrow', 'text'.
Those elements have the following types:
  - `size` (Real; optional)
  - `spacing` (Real; optional)
  - `offset` (Real; optional)
  - `arrow` (optional): . arrow has the following type: Bool | lists containing elements 'headSize'.
Those elements have the following types:
  - `headSize` (Real; optional)
  - `text` (optional): . text has the following type: Bool | lists containing elements 'formatter', 'style'.
Those elements have the following types:
  - `formatter` (optional): . formatter has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `style` (optional)
- `data` (Array of Dicts; required)
- `downloadTrigger` (String; optional)
- `dynamicHeight` (Bool; optional)
- `funnelStyle` (optional): . funnelStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `height` (Real; optional)
- `isTransposed` (Bool; optional)
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
- `maxSize` (Real; optional)
- `meta` (optional)
- `minSize` (Real; optional)
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
- `seriesField` (String; optional)
- `shape` (a value equal to: 'funnel', 'pyramid'; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xField` (String; required)
- `yField` (String; required)
"""
function ''_antdfunnel(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :compareField, :conversionTag, :data, :downloadTrigger, :dynamicHeight, :funnelStyle, :height, :isTransposed, :key, :label, :legend, :limitInPlot, :loading_state, :locale, :maxSize, :meta, :minSize, :padding, :recentlyAreaClickRecord, :recentlyLegendInfo, :recentlyTooltipChangeRecord, :renderer, :seriesField, :shape, :style, :theme, :tooltip, :width, :xField, :yField]
        wild_props = Symbol[]
        return Component("''_antdfunnel", "AntdFunnel", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

