import streamlit as st
from streamlit_folium import st_folium
import folium
from geopy.geocoders import Nominatim
import psycopg2
from psycopg2.extras import RealDictCursor
import pygame

geolocator = Nominatim(user_agent="location-reporter")

pygame.mixer.init()

sound_path = "lmao.mp3"  

def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",  
            database="utek",  
            user="postgres",  
            password="" #Connect to DB with your own password, make your own table  
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

def add_location_to_db(name, address, latitude, longitude, severity, category):
    try:
        conn = connect_db()
        if conn:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO reported_locations (name, address, latitude, longitude, severity, category)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (name, address, latitude, longitude, severity, category),
            )
            conn.commit()
            cur.close()
            conn.close()

            # Play sound after successful submission
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

            st.success("Location added successfully!")
    except Exception as e:
        st.error(f"Error saving location: {e}")

def fetch_locations_from_db():
    try:
        conn = connect_db()
        if conn:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute("SELECT * FROM reported_locations")
            locations = cur.fetchall()
            cur.close()
            conn.close()
            return locations
        else:
            return []
    except Exception as e:
        st.error(f"Error fetching locations: {e}")
        return []

def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            st.error("Address not found. Please try again.")
            return None, None
    except Exception as e:
        st.error(f"Error geocoding address: {e}")
        return None, None

st.title("Hurricane Damage Reporter")

hurricane_data = {
    "name": "Hurricane Alpha",
    "latitude": 27.8,
    "longitude": -82.3,
    "severity": 9,
}

st.markdown("## Report Hurricane Damage")
with st.form("location_form"):
    name = st.text_input("Name", help="Enter a name for this location (e.g., 'Flooded Area').")
    address = st.text_input("Address", help="Enter the address of the location.")
    severity = st.slider("Severity", 1, 10, 5, help="Rate the severity of the damage (1: Low, 10: High).")
    category = st.selectbox("Category", ["Flood", "Fire", "Wind Damage", "Other"], help="Select the type of damage.")
    submitted = st.form_submit_button("Submit Report")
    
    if submitted:
        if name and address:
            lat, lon = geocode_address(address)
            if lat is not None and lon is not None:
                add_location_to_db(name, address, lat, lon, severity, category)
            else:
                st.error("Could not determine coordinates for the address.")
        else:
            st.error("Please provide all required fields.")

st.markdown("## Reported Locations")
locations = fetch_locations_from_db()
m = folium.Map(location=[27.6648, -81.5158], zoom_start=6)
folium.Marker(
    location=[hurricane_data["latitude"], hurricane_data["longitude"]],
    popup=f"Hurricane {hurricane_data['name']} (Severity: {hurricane_data['severity']})",
    icon=folium.Icon(color="red"),
).add_to(m)

for loc in locations:
    popup_text = f"""
    <b>Name:</b> {loc['name']}<br>
    <b>Address:</b> {loc['address']}<br>
    <b>Severity:</b> {loc['severity']}<br>
    <b>Category:</b> {loc['category']}
    """
    folium.Marker(
        location=[loc["latitude"], loc["longitude"]],
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.Icon(color="red" if loc["severity"] > 7 else "orange" if loc["severity"] > 4 else "green"),
    ).add_to(m)

st_folium(m, height=500, width=700)

st.markdown("### Funny Hurricane Warning")
st.markdown(
    """
    ```
    ┌( ಠ‿ಠ)┘
    I have played these games before.
    ```
    """
)
