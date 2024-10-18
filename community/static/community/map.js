document.addEventListener("DOMContentLoaded", function(event) {
    var map = L.map('map').setView([34.0699, -118.4438], 13);
    
    UCLA_location = [34.0699, -118.4438]
    USC_location = [34.0224, -118.2851]
    UCSD_location = [32.8812, -117.2344]
    Tufts_location = [42.4085, -71.1183]
    Unimelb_location = [37.7983, 144.9610]

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    var UCLA_marker = L.marker(UCLA_location).addTo(map);
    var USC_marker = L.marker(USC_location).addTo(map);
    var UCSD_marker = L.marker(UCSD_location).addTo(map);
    var Tufts_marker = L.marker(Tufts_location).addTo(map);
    var Unimelb_marker = L.marker(Unimelb_location).addTo(map);

    UCLA_marker.bindPopup(
        "<b>University of California, Los Angeles</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "Zhou, Yifan")

    USC_marker.bindPopup(
        "<b>University of Southern California</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "Xu, Weihan Victor")

    UCSD_marker.bindPopup(
        "<b>University of California, San Diego</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "Zhang, Brianna Lin")

    Tufts_marker.bindPopup(
        "<b>Tufts University</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "Li, Jia Ling Jenny<br>" +
        "Cai, Siheng Henry")

    Unimelb_marker.bindPopup(
        "<b>The University of Melbourne</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "He, Xin Ran Nicole")

})