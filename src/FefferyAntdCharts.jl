
module FefferyAntdCharts
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1-rc4"

include("jl/''_antdarea.jl")
include("jl/''_antdbar.jl")
include("jl/''_antdchord.jl")
include("jl/''_antdcolumn.jl")
include("jl/''_antdline.jl")
include("jl/''_antdpie.jl")
include("jl/''_antdradar.jl")
include("jl/''_antdscatter.jl")
include("jl/''_antdstock.jl")
include("jl/''_antdsunburst.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "feffery_antd_charts",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "feffery_antd_charts.min.js",
    external_url = "https://unpkg.com/feffery_antd_charts@0.0.1-rc4/feffery_antd_charts/feffery_antd_charts.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "feffery_antd_charts.min.js.map",
    external_url = "https://unpkg.com/feffery_antd_charts@0.0.1-rc4/feffery_antd_charts/feffery_antd_charts.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
