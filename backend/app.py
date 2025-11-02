from flask import Flask,jsonify,request
from flask_cors import CORS
import json
import os
 
app = Flask(__name__)
CORS(app)

with open(os.path.join("data","top_kb.json")) as f:
    kb = json.load(f)
 
def findDrug(tablet_name):
    for drug,info in kb.items():
        tablets_in_kd = info.get("tablet_brand",[])
        print(tablets_in_kd)
        if tablet_name.lower() in [tablet.lower() for tablet in tablets_in_kd]:
            return drug
@app.route('/api/sendInteractions', methods=['POST'])
def sendInteractions():
    data = request.get_json()
    tablets = data.get("tablets",[])

    drugs = []
    for tablet in tablets:
        d = findDrug(tablet)
        if d:
            drugs.append(d)
   
    if len(drugs) < 2:
        return jsonify({"error":"Need at least two tablets"}),400
    
    result = []
    for i in range(len(drugs)):
        drug1 = drugs[i]
        for j in range(i+1,len(drugs)):
            drug2 = drugs[j]
            interaction1 = kb[drug1].get("interactions",{}).get(drug2)  
            interaction2 = kb[drug2].get("interactions",{}).get(drug1)
            interaction = interaction1 or interaction2 or "No known interaction found"
            result.append({
                "drug1":drug1,
                "drug2":drug2,
                "interaction":interaction
            })
    return jsonify({
        "tablets":tablets,
        "drugs":drugs,
        "results":result
    })
@app.route('/api/sendFoodInteractions', methods=['POST'])
def sendFoodInteractions():
    data = request.get_json()
    tablets = data.get("tablets",[])

    drugs = []
    for tablet in tablets:
        d = findDrug(tablet)
        if d:
            drugs.append(d)
   
    if len(drugs) == 0:
        return jsonify({"error":"No valid tablets found"}),400
    
    result = []
    for drug in drugs:
        food_interactions = kb[drug].get("food_interactions","No known food interactions")
        result.append({
            "drug":drug,
            "food_interactions":food_interactions
        })
    return jsonify({
        "tablets":tablets,
        "drugs":drugs,
        "results":result
    })
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
