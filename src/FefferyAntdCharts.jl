
module FefferyAntdCharts
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/''_fefferyantdcharts.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "feffery_antd_charts",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "feffery_antd_charts.min.js",
    external_url = "https://unpkg.com/feffery_antd_charts@0.0.1/feffery_antd_charts/feffery_antd_charts.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "feffery_antd_charts.min.js.map",
    external_url = "https://unpkg.com/feffery_antd_charts@0.0.1/feffery_antd_charts/feffery_antd_charts.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
