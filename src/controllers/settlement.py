from client.helpers.requests import get_request, get_results
from flask import jsonify, request
from server.app import app

@app.route('/settlement')
def get():
    print(request.args)

    if len(request.args) != 2:
        return {"error": "Specify merchant and date"}
    
    merchant_id = request.args["merchant"]
    date = request.args["date"]

    transcation_results = get_results(f"https://api-engine-dev.clerq.io/tech_assessment/transactions/?merchant={merchant_id}&updated_at__lte={date}")
    
    settlement_amount = 0
    for transaction in transcation_results:
        settlement_amount += float(transaction["amount"])

    return {"amount": settlement_amount}