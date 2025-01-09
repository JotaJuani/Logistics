function initMap() {
    
    if (!locations || locations.length === 0) {
        console.error("No se encontraron ubicaciones para mostrar.");
        return;
    }

    
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: locations[0].lat, lng: locations[0].lng },
        zoom: 4, 
    });

    
    locations.forEach(location => {
        new google.maps.Marker({
            position: { lat: location.lat, lng: location.lng },
            map: map,
            title: location.name,
        });
    });
}