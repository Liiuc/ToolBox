            var machine_type = '{{ machine_type|json_encode()|raw }}';
            mApp.block("#graph_fuel_sweeper", {
                overlayColor: "#575962",
                state: "brand",
                opacity: .1
            });
 
            mApp.block("#graph_materials_spreader", {
                overlayColor: "#575962",
                state: "brand",
                opacity: .1
            });

            $.ajax({
                url:'{{ path('dashboard_graphic') }}',
                type: "POST",
                dataType: "json",
                async: true,
                success: function (data)
                {
                    if(machine_type.includes("Spreader") || machine_type.includes("Sprayer")){
                        spreaderGraph(data['spreader']);
                        mApp.unblock("#graph_materials_spreader");
                    }
                    {# if (machine_type.includes("Sweeper")){
                        sweeperGraph(data['sweeper']);
                        mApp.unblock("#graph_fuel_sweeper");
                    } #}
                },
                error: function (data)
                {
                    console.log("Error loading graphs");
                }
            });
  
            function spreaderGraph(data)
            {
                var dati= JSON.parse(data);
                var materiale= dati['material'];
                var liquido= dati['liquid'];
                var e = [
                    [1, materiale[0]],
                    [2, materiale[1]],
                    [3, materiale[2]],
                    [4, materiale[3]],
                    [5, materiale[4]],
                    [6, materiale[5]],
                    [7, materiale[6]],
                    [8, materiale[7]],
                    [9, materiale[8]],
                    [10, materiale[9]]
                ];
                
                var o = [
                    [1, liquido[0]],
                    [2, liquido[1]],
                    [3, liquido[2]],
                    [4, liquido[3]],
                    [5, liquido[4]],
                    [6, liquido[5]],
                    [7, liquido[6]],
                    [8, liquido[7]],
                    [9, liquido[8]],
                    [10,liquido[9]]
                ];

                $.plot($("#graph_materials_spreader"), [
                    {
                        data: e,
                        label: "Salt(kg)",
                        lines: {
                            lineWidth: 1
                        },
                        shadowSize: 0
                    }, {
                        data: o,
                        label: "Liquid(kg)",
                        lines: {
                            lineWidth: 1
                        },
                        shadowSize: 0
                    }
                ], {
                    series: {
                        lines: {
                            show: !0,
                            lineWidth: 2,
                            fill: !0,
                            fillColor: {
                                colors: [{
                                    opacity: .05
                                }, {
                                    opacity: .01
                                }]
                            }
                        },
                        points: {
                            show: !0,
                            radius: 3,
                            lineWidth: 1
                        },
                        shadowSize: 2
                    },
                    grid: {
                        hoverable: !0,
                        clickable: !0,
                        tickColor: "#eee",
                        borderColor: "#eee",
                        borderWidth: 1
                    },
                    colors: ["#d12610", "#37b7f3", "#52e136"],
                    xaxis: {
                        ticks: 11,
                        tickDecimals: 0,
                        tickColor: "#eee"
                    },
                    yaxis: {
                        ticks: 11,
                        tickDecimals: 0,
                        tickColor: "#eee"
                    }
                });
            }