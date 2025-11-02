import pandas as pd
import json
drugI = pd.read_csv("drug-drug-interactions/db_drug_interactions.csv")
#print(drugI.columns)
med = pd.read_csv("250k-medicines-usage-side-effects-and-substitutes/medicine_dataset.csv",low_memory=False)
#print(med.columns)
drugB = pd.read_csv("drug-bank-5110/drugbank_clean.csv",low_memory=False)
#print(drugB.columns)
top_drugs = [
    "Paracetamol","Ibuprofen","Aspirin","Amoxicillin","Azithromycin","Metformin",
    "Prednisolone","Digoxin","Clopidogrel","Omeprazole","Pantoprazole","Losartan",
    "Lisinopril","Tramadol","Gabapentin","Sildenafil","Levothyroxine","Atorvastatin",
    "Rosuvastatin","Alprazolam","Captopril","Busulfan","Clindamycin","Doxycycline","Cetirizine"
]

drugI_filter = drugI[(drugI['Drug 1'].isin(top_drugs)) & (drugI['Drug 2'].isin(top_drugs))]
med_filter = med[med['name'].isin(top_drugs)]
drugB_filter = drugB[drugB['name'].isin(top_drugs)]
kb = {}
for _, row in drugI_filter.iterrows():
    d1 = row['Drug 1']
    d2 = row['Drug 2']
    i = row.get('Interaction Description', "")
    kb.setdefault(d1, {}).setdefault('interactions', {})[d2] = i
    kb.setdefault(d2, {}).setdefault('interactions', {})[d1] = i
for _,row in med_filter.iterrows():
    d = row['name']
    if d in kb:
        side_effects = [row[f'sideEffect{i}'] for i in range(42) if pd.notna(row[f'sideEffect{i}'])]
        uses = [row[f'use{i}'] for i in range(5) if pd.notna(row[f'use{i}'])]
        kb[d] = {
        'side_effects': side_effects,
        'usage': uses,
    }
for _, row in drugB_filter.iterrows():
    d = row['name']
    if d in kb:
        kb[d]['food_interactions'] = row['food-interactions']
        kb[d]['indications'] = row['indication']
medicine_map = {
    "Prednisolone": ["Metrol", "Deltasone", "Predonine"],
    "Digoxin": ["Digox", "Lanoxin"],
    "Busulfan": ["Myleran", "Busilvex"],
    "Ibuprofen": ["Brufen", "Ibugesic", "Advil", "Combiflam"],
    "Rosuvastatin": ["Crestor", "Rosuvast", "Rosuvas"],
    "Doxycycline": ["Doxy 100", "Vibramycin", "Doxytab"],
    "Azithromycin": ["Azithral", "Zithromax", "Azim"],
    "Sildenafil": ["Viagra", "Silagra", "Sildef", "Caverta"],
    "Tramadol": ["Tramacet", "Tramol", "Doreta"],
    "Losartan": ["Losar", "Cozaar"],
    "Pantoprazole": ["Pantocid", "Pantop", "Protonix"],
    "Omeprazole": ["Omez", "Losec", "Omep"],
    "Clopidogrel": ["Plavix", "Clopilet", "Clopitab"],
    "Alprazolam": ["Alprax", "Xanax", "Alzolam"],
    "Levothyroxine": ["Eltroxin", "Thyronorm", "Euthyrox"],
    "Clindamycin": ["Cleocin", "Clindac", "Dalacin"],
    "Lisinopril": ["Lisopril", "Zestril", "Lisir"],
    "Captopril": ["Capoten", "Capozide"],
    "Atorvastatin": ["Lipitor", "Ator", "Cardator"],
    "Gabapentin": ["Neurontin","Gabantin","Gabapin","Gralise","Horizant","Gabarich"],
    "Amoxicillin": ["Amoxil","Augmentin","Novamox","Almox","Mox","Amoxycillin DT"],
    "Cetirizine": ["Zyrtec","Cetzine","Okacet","Cetcip","Reactine","Allercet"],
    "Metformin": ["Glucophage","Glycomet","Gluformin","Obimet","Istamet","Janumet"]
}
for d,b in medicine_map.items():
    if d in kb:
        kb[d]['tablet_brand'] = b

with open("top_kb.json", "w") as f:
    json.dump(kb, f, indent=2)
