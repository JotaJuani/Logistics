function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: locations[0].lat, lng: locations[0].lng }, // Centrar en el punto de partida
        zoom: 8, // Nivel de zoom
    });

    locations.forEach(location => {
        new google.maps.Marker({
            position: { lat: location.lat, lng: location.lng },
            map: map,
            title: location.name,
        });
    });
}

    const locations = {{ locations|safe }};
    locations.forEach(location => {
        new google.maps.Marker({
            position: { lat: location.lat, lng: location.lng },
            map: map,
            title: location.name
        });
    });
}
