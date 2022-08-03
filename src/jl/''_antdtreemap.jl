# AUTO GENERATED FILE - DO NOT EDIT

export ''_antdtreemap

"""
    ''_antdtreemap(;kwargs...)

An AntdTreemap component.

Keyword arguments:
- `id` (String; optional)
- `annotations` (optional)
- `appendPadding` (Real | Array of Reals; optional)
- `autoFit` (Bool; optional)
- `className` (String; optional)
- `color` (optional): . color has the following type: String | Array of Strings | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `colorField` (String; required)
- `data` (Array of Dicts; optional)
- `downloadTrigger` (String; optional)
- `height` (Real; optional)
- `key` (String; optional)
- `label` (optional)
- `legend` (optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `locale` (a value equal to: 'zh-CN', 'en-US'; optional)
- `meta` (optional)
- `padding` (Real | Array of Reals | a value equal to: 'auto'; optional)
- `rawFields` (Array of Strings; optional)
- `rectStyle` (optional): . rectStyle has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `renderer` (a value equal to: 'canvas', 'svg'; optional)
- `style` (Dict; optional)
- `theme` (optional)
- `tooltip` (optional)
- `width` (Real; optional)
"""
function ''_antdtreemap(; kwargs...)
        available_props = Symbol[:id, :annotations, :appendPadding, :autoFit, :className, :color, :colorField, :data, :downloadTrigger, :height, :key, :label, :legend, :loading_state, :locale, :meta, :padding, :rawFields, :rectStyle, :renderer, :style, :theme, :tooltip, :width]
        wild_props = Symbol[]
        return Component("''_antdtreemap", "AntdTreemap", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

