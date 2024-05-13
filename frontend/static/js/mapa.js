let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 6.2361771, lng: -75.5776548 },
    zoom: 12,
    disableDefaultUI: true,
  });

  var Inputcontainer = document.getElementsByClassName("inputs_container")[0];
  var inputs = Inputcontainer.getElementsByTagName("input");
  [...inputs].forEach((input) => {
    new google.maps.places.Autocomplete(input);
  });
}

initMap();

let domain = "http://127.0.0.1:8000";

async function buscarRuta() {
  var Inputcontainer = document.getElementsByClassName("inputs_container")[0];
  var inputs = Inputcontainer.getElementsByTagName("input");
  var action = document
    .getElementsByClassName("inputs_button")[0]
    .getAttribute("data-action");

  var origen = document.getElementById("origen").value;
  var destinos = [];

  [...inputs].forEach((input) => {
    var place = input.value;
    if (place !== "" && input.id !== "origen") {
      destinos.push(place);
    }
  });

  var data = {
    origen: origen,
    destinos: destinos,
  };

  fetch(domain + action, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      }
      throw new Error("Error al enviar los datos al servidor.");
    })
    .then((data) => {
      trazarRutaEnMapa(data.ruta)
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}



function trazarRutaEnMapa(ruta) {
  var directionsService = new google.maps.DirectionsService();
  var directionsRenderer = new google.maps.DirectionsRenderer();

  directionsRenderer.setMap(map);

  var waypoints = ruta.slice(1, -1).map((waypoint) => ({
    location: waypoint,
    stopover: true,
  }));

  var request = {
    origin: ruta[0],
    destination: ruta[ruta.length - 1],
    waypoints: waypoints,
    travelMode: "DRIVING",
  };

  directionsService.route(request, function (result, status) {
    if (status == "OK") {
      directionsRenderer.setDirections(result);
    } else {
      console.error("Error al trazar la ruta:", status);
    }
  });
}