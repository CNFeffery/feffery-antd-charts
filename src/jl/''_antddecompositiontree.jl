# AUTO GENERATED FILE - DO NOT EDIT

export ''_antddecompositiontree

"""
    ''_antddecompositiontree(;kwargs...)

An AntdDecompositionTree component.

Keyword arguments:
- `id` (String; optional)
- `animate` (Bool; optional)
- `autoFit` (Bool; optional)
- `behaviors` (Array of a value equal to: 'drag-canvas', 'scroll-canvas', 'zoom-canvas', 'drag-node's; optional)
- `className` (String; optional)
- `data` (Dict; required)
- `edgeCfg` (optional): . edgeCfg has the following type: lists containing elements 'type', 'label', 'startArrow', 'endArrow', 'edgeStateStyles', 'style'.
Those elements have the following types:
  - `type` (a value equal to: 'line', 'polyline', 'arc', 'quadratic', 'cubic', 'cubic-vertical', 'cubic-horizontal', 'loop'; optional)
  - `label` (optional): . label has the following type: lists containing elements 'style'.
Those elements have the following types:
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `startArrow` (optional): . startArrow has the following type: lists containing elements 'type', 'd', 'path', 'stroke', 'fill'.
Those elements have the following types:
  - `type` (a value equal to: 'vee', 'triangle'; optional)
  - `d` (Real; optional)
  - `path` (String; optional)
  - `stroke` (String; optional)
  - `fill` (String; optional)
  - `endArrow` (optional): . endArrow has the following type: lists containing elements 'fill', 'show'.
Those elements have the following types:
  - `fill` (String; optional)
  - `show` (Bool; optional)
  - `edgeStateStyles` (Dict with Strings as keys and values of type  | Bool; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `height` (Real; optional)
- `key` (String; optional)
- `layout` (optional): . layout has the following type: lists containing elements 'direction', 'type', 'dropCap', 'indent'.
Those elements have the following types:
  - `direction` (a value equal to: 'TB', 'BT', 'LR', 'RL'; optional)
  - `type` (a value equal to: 'indented'; optional)
  - `dropCap` (Bool; optional)
  - `indent` (Real; optional)
- `level` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `markerCfg` (optional): . markerCfg has the following type: lists containing elements 'show', 'collapsed', 'position', 'style'.
Those elements have the following types:
  - `show` (Bool; optional)
  - `collapsed` (Bool; optional)
  - `position` (a value equal to: 'left', 'right', 'top', 'bottom'; optional)
  - `style` (optional) | lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
- `minimapCfg` (optional): . minimapCfg has the following type: lists containing elements 'show', 'viewportClassName', 'type', 'size', 'delegateStyle', 'refresh', 'padding'.
Those elements have the following types:
  - `show` (Bool; optional)
  - `viewportClassName` (String; optional)
  - `type` (a value equal to: 'default', 'keyShape', 'delegate'; optional)
  - `size` (Array of Reals; optional)
  - `delegateStyle` (optional)
  - `refresh` (Bool; optional)
  - `padding` (Real; optional)
- `nodeCfg` (optional): . nodeCfg has the following type: lists containing elements 'type', 'size', 'style', 'label', 'anchorPoints', 'title', 'items', 'padding', 'badge', 'percent', 'autoWidth', 'nodeStateStyles'.
Those elements have the following types:
  - `type` (a value equal to: 'indicator-card'; optional)
  - `size` (Array of Reals; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `label` (optional): . label has the following type: lists containing elements 'style'.
Those elements have the following types:
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `anchorPoints` (Array of Array of Realss; optional)
  - `title` (optional): . title has the following type: lists containing elements 'containerStyle', 'style', 'autoEllipsis'.
Those elements have the following types:
  - `containerStyle` (optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `autoEllipsis` (Bool; optional)
  - `items` (optional): . items has the following type: lists containing elements 'containerStyle', 'style', 'layout', 'sort', 'padding'.
Those elements have the following types:
  - `containerStyle` (optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `layout` (a value equal to: 'bundled', 'flex', 'follow'; optional)
  - `sort` (Bool; optional)
  - `padding` (Real | Array of Reals; optional)
  - `padding` (Real | Array of Reals; optional)
  - `badge` (optional): . badge has the following type: lists containing elements 'position', 'size', 'style'.
Those elements have the following types:
  - `position` (a value equal to: 'left', 'top', 'right', 'bottom'; optional)
  - `size` (Real | Array of Reals; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `percent` (optional): . percent has the following type: lists containing elements 'position', 'size', 'style', 'backgroundStyle'.
Those elements have the following types:
  - `position` (a value equal to: 'top', 'bottom'; optional)
  - `size` (Real; optional)
  - `style` (optional): . style has the following type: lists containing elements 'func'.
Those elements have the following types:
  - `func` (String; optional)
  - `backgroundStyle` (optional)
  - `autoWidth` (Bool; optional)
  - `nodeStateStyles` (Dict with Strings as keys and values of type  | Bool; optional)
- `style` (Dict; optional)
- `width` (Real; optional)
"""
function ''_antddecompositiontree(; kwargs...)
        available_props = Symbol[:id, :animate, :autoFit, :behaviors, :className, :data, :edgeCfg, :height, :key, :layout, :level, :loading_state, :markerCfg, :minimapCfg, :nodeCfg, :style, :width]
        wild_props = Symbol[]
        return Component("''_antddecompositiontree", "AntdDecompositionTree", "feffery_antd_charts", available_props, wild_props; kwargs...)
end

