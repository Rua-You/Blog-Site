document.addEventListener("DOMContentLoaded", function(event) {
    const map = L.map('map').setView([0, 0], 3);
    
    UCLA_location = [34.0699, -118.4438]
    USC_location = [34.0224, -118.2851]
    UCSD_location = [32.8812, -117.2344]
    Tufts_location = [42.4085, -71.1183]
    Unimelb_location = [-37.7983, 144.9610]

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    const UCLA_marker = L.marker(UCLA_location).addTo(map);
    const USC_marker = L.marker(USC_location).addTo(map);
    const UCSD_marker = L.marker(UCSD_location).addTo(map);
    const Tufts_marker = L.marker(Tufts_location).addTo(map);
    const Unimelb_marker = L.marker(Unimelb_location).addTo(map);


    UCLA_marker.bindPopup(
        "<b>University of California, Los Angeles</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "<a href=\"/profile/yifan-zhou-2024\">Zhou, Yifan</a>")

    USC_marker.bindPopup(
        "<b>University of Southern California</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "<a href=\"/profile/victor-xu-2024\">Xu, Weihan Victor</a>")

    UCSD_marker.bindPopup(
        "<b>University of California, San Diego</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "<a href=\"/profile/brianna-zhang-2024\">Zhang, Brianna Lin</a>")

    Tufts_marker.bindPopup(
        "<b>Tufts University</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "<a href=\"/profile/jenny-li-2024\">Li, Jia Ling Jenny</a><br>" +
        "<a href=\"/profile/henry-cai-2024\">Cai, Siheng Henry</a>")

    Unimelb_marker.bindPopup(
        "<b>The University of Melbourne</b><br>" + 
        "<b>Alumni Studying Here:</b><br>" +
        "<a href=\"/profile/nicole-he-2024\">He, Xin Ran Nicole</a>")

})