# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdcolumn

"""
    ''_antdcolumn(;kwargs...)

An AntdColumn component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals | String; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `columnBackground` (optional): . columnBackground has the following type: lists containing elements 'style'.
Those elements have the following types:
  - `style` (optional)
- `columnStyle` (optional): . columnStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `columnWidthRatio` (Real; optional)
- `connectedArea` (optional): . connectedArea has the following type: lists containing elements 'trigger'.
Those elements have the following types:
  - `trigger` (Bool | String; optional) | Bool
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
- `dodgePadding` (Real; optional)
- `groupField` (String; optional)
- `height` (Real; optional)
- `intervalPadding` (Real; optional)
- `isGroup` (Bool; optional)
- `isPercent` (Bool; optional)
- `isRange` (Bool; optional)
- `isStack` (Bool; optional)
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (String; optional)
- `marginRatio` (Real; optional)
- `maxColumnWidth` (Real; optional)
- `meta` (optional)
- `minColumnWidth` (Real; optional)
- `padding` (Real | Array of Reals | String; optional)
- `renderer` (String; optional)
- `scrollbar` (optional)
- `seriesField` (String; optional)
- `slider` (optional)
- `style` (Dict; optional)
- `tooltip` (optional)
- `width` (Real; optional)
- `xAxis` (optional)
- `xField` (String; required)
- `yAxis` (optional)
- `yField` (String; required)
"""
function ''_antdcolumn(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :color, :columnBackground, :columnStyle, :columnWidthRatio, :connectedArea, :conversionTag, :data, :dodgePadding, :groupField, :height, :intervalPadding, :isGroup, :isPercent, :isRange, :isStack, :key, :label, :legend, :loading_state, :locale, :marginRatio, :maxColumnWidth, :meta, :minColumnWidth, :padding, :renderer, :scrollbar, :seriesField, :slider, :style, :tooltip, :width, :xAxis, :xField, :yAxis, :yField]
        wild_props = Symbol[]
        return Component("''_antdcolumn", "AntdColumn", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

