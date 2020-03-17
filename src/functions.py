# Crea el location (long+lat)
def asGeoJSON(lat,lng):
    try:
        lat = float(lat)
        lng = float(lng)
        if not math.isnan(lat) and not math.isnan(lng):
            return {
                "type":"Point",
                "coordinates":[lng,lat]
            }
    except Exception:
        print("Invalid data")
        return None

# Crea el point Geopandas
def asGeo(name):
    return gpd.GeoDataFrame(name, geometry=gpd.points_from_xy(name.longitude, name.latitude))
    

#gCompaniesAtlanta = gpd.GeoDataFrame(companiesAtlanta, geometry=gpd.points_from_xy(companiesAtlanta.longitude, companiesAtlanta.latitude))
#print(f'Tipo: {type(gCompaniesAtlanta)}')
#gCompaniesAtlanta.head()

def geocode(address):
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }


def withGeoQuery(location,maxDistance=3000,minDistance=0,field="location"):
    return {
       field: {
         "$near": {
           "$geometry": location if type(location)==dict else geocode(location),
           "$maxDistance": maxDistance,
           "$minDistance": minDistance
         }
       }
    }

