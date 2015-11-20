function initialize(aLat, aLong)
{
  var mapCanvas = document.getElementById('map'),
      myLatLng = {lat: aLat, lng: aLong},
      mapOptions = {
          center: new google.maps.LatLng(aLat, aLong),
          zoom: 9,
          mapTypeId: google.maps.MapTypeId.ROADMAP
      }

  var map = new google.maps.Map(mapCanvas, mapOptions),
      marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Nuage Networks !'
    });
}