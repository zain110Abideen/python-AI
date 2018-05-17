import csv

def mapWithMarker(api, lat, long, zoom, title, path):
    try:

        f = open(path,'w')

        htmlCode = """<!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <style>
           #map {
            height: 400px;
            width: 50%;
            border: 1px solid black;
            margin: 10px;

           }

           #sig {
            width: 50%;
            border: 1px solid black;
            padding: 15px;
            margin: 10px;
           }
        </style>
      </head>
      <body>
        <div id="map"></div>
        <div id="sig">
          <h4>Zain-ul-Abideen Maps</h4>
          <p>Powered by 1ten Development Team</p>
          <a href="https://1tenhost.com/" target="_blank"><button type="button" class="btn btn-success">Visit Our Side</button></a>
        </div>
        <script>
          function initMap() {
            var uluru = {lat: """+lat+""", lng: """+long+"""};
            var map = new google.maps.Map(document.getElementById('map'), {
              zoom: """+zoom+""",
              center: uluru
              
            });
            var marker = new google.maps.Marker({
              position: uluru,
              map: map,
              title: '"""+title+"""'
            });
          }
        </script>
        <script async defer
        src="https://maps.googleapis.com/maps/api/js?key="""+api+"""&callback=initMap">
        </script>
      </body>
    </html>"""

        f.write(htmlCode)
        f.close()
        print('File Created')

    except:
        print("ERROR..!!\nSome thing went Wrong. \nMay be Wrong path is define OR Parameters not fill correctly.")

#mapWithMarker('AIzaSyCrQS1-U09_8Mm6TpZM8oQsDFzddmvp8po', '24.795129', '67.049817', '12', 'zain', 'simpelMap.html')






def mapWithMultipleMarker(csvFile, js, api, lats, longs, zoom, path):

    i = 0
    name = []
    lat = []
    long = []
    javaCode = ""
    strt = "var markers =[\n"
    end = "];"

    js_created = False
    
    try:
        with open(csvFile) as f:
            reader = csv.reader(f)
            for row in reader:
                i+=1
                a = row[0]
                b = row[1]
                c = row[2]
                if i>1:
                    name.append(a)
                    lat.append(b)
                    long.append(c)

        f = open(js,'w')
        for i in range(len(name)):
            javaCode += '{"title": "'+name[i]+'", "lat": "'+lat[i]+'", "long": "'+long[i]+'"},\n'

        final = strt+""+javaCode+""+end
        f.write(final)
        f.close()
        print('Java Files Created')
        js_created = True
    except:
        print("ERROR..!!\nSome thing went Wrong. \nMay be Wrong path is define OR Parameters not fill correctly.")


    if js_created == True:
        f = open(path,'w')
        htmlCode = """<!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script type="text/javascript" src='"""+js+"""'></script>
        <style>
           #map {
            height: 400px;
            width: 50%;
            border: 1px solid black;
            margin: 10px;

           }

           #sig {
            width: 50%;
            border: 1px solid black;
            padding: 15px;
            margin: 10px;
           }
        </style>
      </head>
      <body>
        <div id="map"></div>
        <div id="sig">
          <h4>Zain-ul-Abideen Maps</h4>
          <p>Powered by 1ten Development Team</p>
          <a href="https://1tenhost.com/" target="_blank"><button type="button" class="btn btn-success">Visit Our Side</button></a>
        </div>
        <script>
          function initMap() {
            var uluru = {lat: """+str(lats)+""", lng: """+str(longs)+"""};
            var map = new google.maps.Map(document.getElementById('map'), {
              zoom: """+str(zoom)+""",
              center: uluru
            });
            
            for (var i = 0; i < markers.length; i++) {
              data = markers[i];
              var myLatlng = new google.maps.LatLng(data.lat, data.long);

              var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                title: data.title
              });
            }
          }
        </script>
        <script async defer
        src="https://maps.googleapis.com/maps/api/js?key="""+str(api)+"""&callback=initMap">
        </script>
      </body>
    </html>"""
        f.write(htmlCode)
        f.close()
        print('File Created')
            
    else:
        print("java file not creaeted")
    


#mapWithMultipleMarker("example.csv", "marker.js", 'AIzaSyCrQS1-U09_8Mm6TpZM8oQsDFzddmvp8po', '24.795129', '67.049817', '12', 'multipleMarker.html')
