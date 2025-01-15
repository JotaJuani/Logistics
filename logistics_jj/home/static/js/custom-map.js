
        function initMap() {
            if (!coordinates || !coordinates.origin || !coordinates.destination) {
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
            
                // Crear el marcador para el origen
            new google.maps.Marker({
                position: coordinates.origin,
                map: map,
                title: "Origen",
                icon: "http://maps.google.com/mapfiles/ms/icons/green-dot.png", // Marcador verde
            });

            // Crear el marcador para el destino
            new google.maps.Marker({
                position: coordinates.destination,
                map: map,
                title: "Destino",
                icon: "http://maps.google.com/mapfiles/ms/icons/red-dot.png", // Marcador rojo
            });

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

window.initMap = initMap;