import folium

# Création de la carte centrée sur Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=11)
# Ajout des points sur la carte
pointsL = {
    "Lycée Madeleine Daniélou": (48.85967762489183, 2.173326743409161), # Neuilly-sur-Seine
    "Lycée St Michel de Picpus": (48.84256762792805, 2.3965336897045333), # 12e arrondissement
    "Lycée Saint-François d'Assise": (48.77894598956109, 2.0405522934840103), # Montigny-le-Bretonneux
    "Lycée Stanislas": (48.84524061529863, 2.3280989608974165), # 6e arrondissement
    "Lycée Louis le Grand": (48.84780646139868, 2.34484483537904), # 5e arrondissement
    "Lycée Henri IV": (48.84629946273005, 2.347573518856156), # 5e arrondissement
    "Lycée Sainte-Marie": (48.88507761900323, 2.281241832178356), # Neuilly-sur-Seine
    "Institution Notre-Dame de Sainte-Croix": (48.88196915966834, 2.2805977814090284), # Neuilly-sur-Seine
    "La Tour Paris - Collège-Lycée": (48.861595252116416, 2.278941003658934) # 16e arrondissement
}
pointsC = {
    "Collège Pierre Alviset": (48.84128087211958, 2.3517182030776738), # Paris 05
    "Collège Pierre de Coubertin": (48.70344610002647, 2.0461705203294764), # Chevreuse
    "Collège Pierre et Marie Curie": (48.8898143607829, 2.1154002726777112), # Le Pecq
    "Collège Rognoni": (48.84827117728773, 2.353253944675279), # Paris 05
    "Collège Pierre-Jean de Berangere": (48.865166503796154, 2.3641596804520795), # Paris 03
    "Collège Le Racinay": (48.63538700877943, 1.8245794708845045), # Rambouillet
    "Collège Les Amandiers": (48.91323742416418, 2.194928865107171), # Carrières Sur Seine
    "Collège Condorcet": (48.88089072350929, 2.3268636536951184), # Paris 08
    "Collège Beaumarchais": (48.864305432600126, 2.366997521543636), # Paris 11
    "Collège Maurive Ravel": (48.7747201236325, 1.816083138822968), # Montfort L'Amaury
    "Collège Le Prieure": (48.94600727318554, 2.149032952545836), # Maisons Laffitte
    "Collège du Bois d'Aulne": (49.012442067466374, 2.1184216328022587), # Conflans Ste Honorine
    "Collège Anne Frank": (48.85205227859802, 2.379485599657913), #  Paris 11
    "Collège Alain Fournier": (48.85784303304381, 2.3839141563275024), # Paris 11 
    "Collège Henri Matisse": (48.85660770523834, 2.4018384663545476), # Paris 20
}

for name, coord in pointsC.items():
    folium.Marker(location=coord, popup=name, icon=folium.Icon(color='red')).add_to(m)
for name, coord in pointsL.items():
    folium.Marker(location=coord, popup=name).add_to(m)

# Affichage de la carte
m.save("carte_lycees_colleges_paris.html")
