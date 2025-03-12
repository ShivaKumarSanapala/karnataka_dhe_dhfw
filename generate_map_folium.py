import folium

# Create a map centered around Karnataka
karnataka_map = folium.Map(location=[15.3173, 75.7139], zoom_start=7)

# Updated list of cities with new coordinates
cities = {
    "Bangalore Medical College and Research Institute (BMC&RI)": [12.9593833, 77.5747417],
    "Bangalore Medical College and Research Institute, Super Specialty Hospital (SSH) (PMSSY)": [12.9593833, 77.5747417],
    "Indira Gandhi Institute of Child Health (IGICH)": [12.9416, 77.5733],
    "SDS Tuberculosis Research Centre & Rajiv Gandhi Institute of Chest Diseases": [12.9416, 77.5733],
    "Shri Atal Bihari Vajpayee Medical College (SABVMC)": [12.9593833, 77.5747417],
    "Mysore Medical College and Research Institute (MMCRI)": [12.311827, 76.652985],
    "Institute of Nephro Urology (INU), Bengaluru": [12.9416, 77.5733],
    "Institute of Nephro Urology (INU), Mysuru": [12.311827, 76.652985],
    "Gulbarga Institute of Medical Sciences (GIMS)": [17.329127, 76.843539],
    "Belagavi Institute of Medical Sciences (BIMS)": [15.8497, 74.4977],
    "Karnataka Institute of Medical Sciences (KIMS), Hubballi": [15.3647, 75.1239],
    "Vijayanagara Institute of Medical Sciences (VIMS), Ballari": [15.1394, 76.9214],
    "Shimoga Institute of Medical Sciences (SIMS)": [13.9299, 75.5681],
    "Mandya Institute of Medical Sciences (MIMS)": [12.5215, 76.8976],
    "Hassan Institute of Medical Sciences (HIMS)": [13.0057, 76.1025],
    "Bidar Institute of Medical Sciences (BRIMS)": [17.9133, 77.5175],
    "Raichur Institute of Medical Sciences (RIMS)": [16.2135, 77.3566],
    "Gadag Institute of Medical Sciences (GIMS)": [15.4295, 75.6297],
    "Karwar Institute of Medical Sciences (KIMS)": [14.8136, 74.1297],
    "Chikkamagaluru Institute of Medical Sciences (CIMS)": [13.3225, 75.7740],
    "Kodagu Institute of Medical Sciences (KIMS), Madikeri": [12.4260, 75.7382],
    "Koppal Institute of Medical Sciences (KIMS)": [15.3452, 76.1545],
    "Chamarajanagar Institute of Medical Sciences (CIMS)": [11.9236, 76.9405],
    "Dharwad Institute of Mental Health and Neurosciences (DIMHANS)": [15.4589, 75.0078],
    "District Hospital, Haveri": [14.7936, 75.4045],
    "District Hospital, Chikkaballapur": [13.4350, 77.7278],
    "Yadgir Institute of Medical Sciences (YIMS)": [16.7709, 77.1376],
    "H Siddaiah Road Referral Hospital, BBMP (NHM)": [12.9515, 77.5848],
    "Banashankari Referral Hospital, BBMP (NHM)": [12.9250, 77.5440],
    "Ulsoor Referral Hospital, BBMP (NHM)": [12.9843, 77.6190],
    "JJR Nagar Referral Hospital, BBMP (NHM)": [12.9479, 77.5544],
    "Srirampura Referral Hospital, BBMP (NHM)": [12.9982, 77.5693],
    "General Hospital, Doddaballapura (NHM)": [13.2796, 77.5371],
    "MCH H.D Kote": [12.0840, 76.3335],
    "MCH Bannur": [12.3327, 76.8625],
    "General Hospital, T. Narasipura (NHM)": [12.2115, 76.8976],
    "MCH Chikkodi": [16.4297, 74.5859],
    "MCH Nippani": [16.3973, 74.3824],
    "MCH, Davanagere": [14.4645, 75.9213],
    "General Hospital, Sira": [13.7416, 76.9048],
    "District Hospital, Ballari": [15.1394, 76.9214],
    "MCH Hospet": [15.2695, 76.3871],
    "General Hospital, Navalagunda": [15.5753, 75.3530],
    "General Hospital, Kalaghatagi": [15.1838, 75.0080],
    "General Hospital, Thirthahalli": [13.6882, 75.2456],
    "District Hospital, Chitradurga": [14.2265, 76.4005],
    "Chitradurga MCH": [14.2265, 76.4005],
    "General Hospital, Challakere": [14.3180, 76.6512],
    "CHC, Nayakanahatti": [14.5261, 76.6315],
    "General Hospital, Sakaleshapura": [12.9401, 75.7850],
    "General Hospital, Arasikere": [13.3147, 76.2570],
    "General Hospital, Gowribidanuru": [13.6105, 77.5174],
    "General Hospital, Gudibande": [13.6691, 77.6967],
    "General Hospital, Mudigere": [13.1335, 75.6401],
    "General Hospital, Tarikere": [13.7096, 75.8130],
    "General Hospital, Kaduru": [13.5523, 76.0110],
    "General Hospital, N.R. Pura": [13.6093, 75.5154],
    "General Hospital, Biruru": [13.6048, 75.9716],
    "District Hospital, Chikkamagaluru": [13.3225, 75.7740],
    "General Hospital, Aurad": [18.2536, 77.4186],
    "MCH, Kundapur": [13.6202, 74.6909],
    "District Hospital, Karwar": [14.8136, 74.1297],
    "General Hospital, Sirsi": [14.6197, 74.8355],
    "General Hospital, Virajpete": [12.1986, 75.8069],
    "General Hospital, Somavarapete": [12.4416, 75.8492],
    "MCH, Koppal": [15.3452, 76.1545],
    "MCH, Kukanoor": [15.5000, 76.0500],
    "General Hospital, Kollegala": [12.1530, 77.1072]
}

# Add markers for each city with custom styling for popup
for city, coords in cities.items():
    folium.Marker(
        location=coords, 
        popup=folium.Popup(f"<b style='color:blue;'> {city} </b>", max_width=300)
    ).add_to(karnataka_map)

# Save the map to an HTML file
karnataka_map.save("/Users/sanapalas/Desktop/karnataka_cities_map.html")
