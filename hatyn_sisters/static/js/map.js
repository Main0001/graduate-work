//let polyline = L.polyline([[53.902163761666735, 27.561693187691905], [27.561693187691905, 53.902163761666735]]).addTo(map)

const attribution = '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const map = L.map('map');
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);
let feature = L.geoJSON(markers).bindPopup(function (layer) {
  return `<b>${layer.feature.properties.name}</b><br>${layer.feature.properties.description}<br>Ссылка: <a href="http://127.0.0.1:8000/villages/${layer.feature.properties.village}">http://127.0.0.1:8000/villages/${layer.feature.properties.village}</a>`;
}).addTo(map);

map.fitBounds(feature.getBounds(), { padding: [100, 100] });