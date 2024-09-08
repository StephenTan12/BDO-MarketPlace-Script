import requests

BDO_URL = "https://api.arsha.io/v2/na/GetWorldMarketSubList"

def fetch_bdo_market_data(request_params: dict[str]) -> dict:
    '''
    Fetch market place data

    @params body_data - category id of the items 
    @returns list of response data
    '''
    response = requests.get(
        url=BDO_URL,
        params=request_params
    )

    res_data = response.json()
    return res_data
