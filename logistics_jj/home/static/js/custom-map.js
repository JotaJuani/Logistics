
<script>
    const coordinates = {{ coordinates|safe }};
    console.log(coordinates);  // Verificar el valor en la consola del navegador
</script>

const coordinates = {{ coordinates|safe }};

        function initMap() {
            if (!coordinates) {
                console.error("No se encontraron coordenadas.");
                return;
            }

            const map = new google.maps.Map(document.getElementById("map"), {
                center: coordinates.origin,
                zoom: 7,
            });

            const directionsService = new google.maps.DirectionsService();
            const directionsRenderer = new google.maps.DirectionsRenderer();
            directionsRenderer.setMap(map);

            const request = {
                origin: coordinates.origin,
                destination: coordinates.destination,
                travelMode: google.maps.TravelMode.DRIVING,
            };

            directionsService.route(request, (result, status) => {
                if (status === google.maps.DirectionsStatus.OK) {
                    directionsRenderer.setDirections(result);
                } else {
                    console.error("Error al calcular la ruta:", status);
                }
            });
        }