import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { LatLngExpression } from "leaflet";

import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";
import "leaflet-defaulticon-compatibility";

// TODO: must accept an array of [lat, lon]
interface MapProps {
    positions: LatLngExpression;
    zoom?: number;
}

const defaults = {
    zoom: 13,
};

// TODO: get actual theme mode and switch between maps png
// light: https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
// dark: https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png

const Map = ({ zoom = defaults.zoom, positions }: MapProps) => {
    return (
        <MapContainer
            center={positions}
            zoom={zoom}
            scrollWheelZoom={false}
            style={{ height: "100%", width: "100%" }}>
            <TileLayer
                url="https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png"
                attribution='&copy; <a href="https://carto.com/">CARTO</a>'
            />
            <Marker position={positions}>
                <Popup>{`Puerto`}</Popup>
            </Marker>
        </MapContainer>
    );
};

export default Map;
