<html>
<head>
	<title>My first chart using FusionCharts Suite XT</title>
	<script type="text/javascript" src="https://cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
	<script type="text/javascript" src="https://cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
	<script type="text/javascript">
		FusionCharts.ready(function(){
			var chartObj = new FusionCharts({
    type: 'multilevelpie',
    renderAt: 'chart-container',

    width: '500',
    height: '500',
    dataFormat: 'json',
    dataSource: {
        "chart": {
            "caption": "Antibodies Database",
            "subcaption": "Antibody Result",
            "showPlotBorder": "1",
            "piefillalpha": "60",
            "pieborderthickness": "2",
            "hoverfillcolor": "#CCCCCC",
            "piebordercolor": "#FFFFFF",
            "hoverfillcolor": "#CCCCCC",
            "numberprefix": "$",
            "plottooltext": "$label, $$valueK, $percentValue",
            //Theme
            "theme": "fusion"
        },
        "category": [{
            "label": "Identifier",
            "color": "#ffffff",
            "value": "150",
            "category": [{
                "label": "Antibody Source",
                "color": "#f8bd19",
                "value": "25",
                "tooltext": "Antibody Source, $$valueK, $percentValue",
                "category": [{
                    "label": "Antibody Type",
                    "color": "#33ccff",
                    "value": "100",
                    "tooltext": "Antibody Type, $$valueK, $percentValue"
                }]
            }, {
                "label": "Antibody Nature",
                "color": "#33ccff",
                "value": "25",
                "category": [{
                    "label": "Purpose of Mutations",
                    "color": "#ccff66",
                    "value": "100",
                    "tooltext": "Antibody Type, $$valueK, $percentValue"
                }]
                
            }, {
                "label": "Fusion with",
                "color": "#ffcccc",
                "value": "25",
                "tooltext": "Fusion with, $$valueK, $percentValue",
                "category": [{
                    "label": "CDRs Source",
                    "color": "#f8bd19",
                    "value": "100",
                    "tooltext": "Antibody Type, $$valueK, $percentValue"
                }]

                
            }, {
                "label": "ID",
                "color": "#ccff66",
                "value": "25",
                "category": [{
                    "label": "Sequence",
                    "color": "#ffcccc",
                    "value": "100",
                    "tooltext": "Antibody Type, $$valueK, $percentValue"
                }]
                
            }]
        }]
    }
}
);
			chartObj.render();
		});
	</script>
	</head>
	<body>
		<div id="chart-container">FusionCharts XT will load here!</div>
	</body>
</html>