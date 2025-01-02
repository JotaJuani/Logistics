(async () => {
    // Cargar el mapa de Argentina
    const mapData = await fetch(
        'https://code.highcharts.com/mapdata/countries/ar/ar-all.topo.json'
    ).then(response => response.json());

    // Inicializar el gráfico
    const chart = Highcharts.mapChart('container', {
        title: {
            text: 'Rutas aéreas en Argentina',
            align: 'left'
        },

        legend: {
            align: 'left',
            layout: 'vertical',
            floating: true
        },

        accessibility: {
            point: {
                valueDescriptionFormat: '{xDescription}.'
            }
        },

        mapNavigation: {
            enabled: true
        },

        tooltip: {
            format: '{point.id}{#if point.lat}<br>Lat: {point.lat} Lon ' +
                '{point.lon}{/if}'
        },

        plotOptions: {
            series: {
                marker: {
                    fillColor: '#FFFFFF',
                    lineWidth: 2,
                    lineColor: Highcharts.getOptions().colors[1]
                }
            }
        },

        series: [{
            // Mapa base de Argentina
            mapData,
            name: 'Argentina',
            borderColor: '#707070',
            nullColor: 'rgba(200, 200, 200, 0.3)',
            showInLegend: false
        }, {
            // Especificar ciudades con latitud/longitud
            type: 'mappoint',
            name: 'Ciudades',
            dataLabels: {
                format: '{point.id}'
            },
            data: [
                { id: 'Buenos Aires', lat: -34.603722, lon: -58.381592 },
                { id: 'CABA', lat: -34.603722, lon: -58.381592 }, // Ciudad Autónoma de Buenos Aires
                { id: 'Córdoba', lat: -31.416667, lon: -64.183333 },
                { id: 'Santa Fe', lat: -32.94682, lon: -60.63932 },
                { id: 'Mendoza', lat: -32.889458, lon: -68.845839 },
                { id: 'Bariloche', lat: -41.133472, lon: -71.310277 },
                { id: 'Salta', lat: -24.782932, lon: -65.423197 },
                { id: 'Jujuy', lat: -24.185608, lon: -65.299587 },
                { id: 'Tucumán', lat: -26.808282, lon: -65.217453 },
                { id: 'Misiones', lat: -26.844682, lon: -54.6966 },
                { id: 'Chaco', lat: -27.471195, lon: -59.211995 },
                { id: 'Chubut', lat: -43.615392, lon: -65.115021 },
                { id: 'Corrientes', lat: -27.467346, lon: -58.83943 },
                { id: 'Entre Ríos', lat: -32.062263, lon: -60.722391 },
                { id: 'Formosa', lat: -26.184062, lon: -58.176155 },
                { id: 'La Pampa', lat: -36.616277, lon: -64.185191 },
                { id: 'La Rioja', lat: -29.413947, lon: -66.848742 },
                { id: 'Mendoza', lat: -32.889458, lon: -68.845839 },
                { id: 'Neuquén', lat: -38.951683, lon: -68.059227 },
                { id: 'Río Negro', lat: -41.125303, lon: -71.314145 },
                { id: 'Salta', lat: -24.782932, lon: -65.423197 },
                { id: 'San Juan', lat: -31.536509, lon: -68.327783 },
                { id: 'San Luis', lat: -33.298219, lon: -66.335759 },
                { id: 'Santa Cruz', lat: -49.344431, lon: -68.292404 },
                { id: 'Santiago del Estero', lat: -27.798797, lon: -64.261482 },
                { id: 'Tierra del Fuego', lat: -54.801912, lon: -68.302951 },
                { id: 'Tucumán', lat: -26.808282, lon: -65.217453 }
            ]
        }]
    });

    // Función para generar trayectorias curvas entre dos puntos
    function pointsToPath(fromPoint, toPoint, invertArc) {
        const
            from = chart.mapView.lonLatToProjectedUnits(fromPoint),
            to = chart.mapView.lonLatToProjectedUnits(toPoint),
            curve = 0.05,
            arcPointX = (from.x + to.x) / (invertArc ? 2 + curve : 2 - curve),
            arcPointY = (from.y + to.y) / (invertArc ? 2 + curve : 2 - curve);
        return [
            ['M', from.x, from.y],
            ['Q', arcPointX, arcPointY, to.x, to.y]
        ];
    }

    const bsAsPoint = chart.get('Buenos Aires');

    // Agregar rutas de vuelo
    chart.addSeries({
        name: 'Rutas terrestres desde Buenos Aires',
        type: 'mapline',
        lineWidth: 2,
        color: Highcharts.getOptions().colors[3],
        data: [
            { id: 'BA - Buenos Aires', path: pointsToPath(bsAsPoint, chart.get('Buenos Aires')) },
            { id: 'BA - Catamarca', path: pointsToPath(bsAsPoint, chart.get('Catamarca')) },
            { id: 'BA - Chaco', path: pointsToPath(bsAsPoint, chart.get('Chaco')) },
            { id: 'BA - Chubut', path: pointsToPath(bsAsPoint, chart.get('Chubut')) },
            { id: 'BA - Córdoba', path: pointsToPath(bsAsPoint, chart.get('Córdoba')) },
            { id: 'BA - Corrientes', path: pointsToPath(bsAsPoint, chart.get('Corrientes')) },
            { id: 'BA - Entre Ríos', path: pointsToPath(bsAsPoint, chart.get('Entre Ríos')) },
            { id: 'BA - Formosa', path: pointsToPath(bsAsPoint, chart.get('Formosa')) },
            { id: 'BA - Jujuy', path: pointsToPath(bsAsPoint, chart.get('Jujuy')) },
            { id: 'BA - La Pampa', path: pointsToPath(bsAsPoint, chart.get('La Pampa')) },
            { id: 'BA - La Rioja', path: pointsToPath(bsAsPoint, chart.get('La Rioja')) },
            { id: 'BA - Mendoza', path: pointsToPath(bsAsPoint, chart.get('Mendoza')) },
            { id: 'BA - Misiones', path: pointsToPath(bsAsPoint, chart.get('Misiones')) },
            { id: 'BA - Neuquén', path: pointsToPath(bsAsPoint, chart.get('Neuquén')) },
            { id: 'BA - Río Negro', path: pointsToPath(bsAsPoint, chart.get('Río Negro')) },
            { id: 'BA - Salta', path: pointsToPath(bsAsPoint, chart.get('Salta')) },
            { id: 'BA - San Juan', path: pointsToPath(bsAsPoint, chart.get('San Juan')) },
            { id: 'BA - San Luis', path: pointsToPath(bsAsPoint, chart.get('San Luis')) },
            { id: 'BA - Santa Cruz', path: pointsToPath(bsAsPoint, chart.get('Santa Cruz')) },
            { id: 'BA - Santa Fe', path: pointsToPath(bsAsPoint, chart.get('Santa Fe')) },
            { id: 'BA - Santiago del Estero', path: pointsToPath(bsAsPoint, chart.get('Santiago del Estero')) },
            { id: 'BA - Tucumán', path: pointsToPath(bsAsPoint, chart.get('Tucumán')) }
        ]
    }, true, false);
})();