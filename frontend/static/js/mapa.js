let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 6.2361771, lng: -75.5776548 },
    zoom: 12,
    disableDefaultUI: true,
  });

  const autocompleteOrigen = new google.maps.places.Autocomplete(
    document.getElementById("origen")
  );

  const autocompleteDestino = new google.maps.places.Autocomplete(
    document.getElementById("destino")
  );
}

initMap();

let domain = "http://127.0.0.1:8000";

function buscarRuta() {
  var origen = document.getElementById("origen").value;
  var destino = document.getElementById("destino").value;
  var action = document
    .getElementsByClassName("inputs_button")[0]
    .getAttribute("data-action");

  var data = {
    origen: origen,
    destino: destino,
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
      // Manejar la respuesta del backend
      console.log(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
