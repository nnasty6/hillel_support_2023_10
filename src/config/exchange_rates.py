import json

import requests
from django.http import JsonResponse
from pydantic import BaseModel, Field

API_KEY = "JKZSOO1M9A4VCFIT"
BASE_URL = "https://www.alphavantage.co"


class AlphavantageCurrencyExchangeRatesRequest(BaseModel):
    currency_from: str
    currency_to: str


class AlphavantageCurrencyExchangeRatesResults(BaseModel):
    currency_from: str = Field(alias="1. From_Currency Code")
    currency_to: str = Field(alias="3. To_Currency Code")
    rate: float = Field(alias="5. Exchange Rate")


class AlphavantageCurrencyExchangeRatesResponse(BaseModel):
    results: AlphavantageCurrencyExchangeRatesResults = Field(
        alias="Realtime Currency Exchange Rate"
    )


def fetch_currency_exchange_rates(
    schema: AlphavantageCurrencyExchangeRatesRequest,
) -> AlphavantageCurrencyExchangeRatesResponse:
    """this function claims the currency exchange rate
    information from external service: Alphavantage
    """

    payload: str = (
        f"/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={schema.currency_from.upper()}&"
        f"to_currency={schema.currency_to.upper()}&"
        f"apikey={API_KEY}"
    )
    url: str = "".join([BASE_URL, payload])

    raw_response: requests.Response = requests.get(url)

    response = AlphavantageCurrencyExchangeRatesResponse(**raw_response.json())

    return response


# def index():
#     return HttpResponse("<h2>Exchange rate</h2>")


def exchange_rates(request) -> JsonResponse:
    currency_from = request.GET.get("currency_from", "gbp")
    currency_to = request.GET.get("currency_to", "uah")
    result: AlphavantageCurrencyExchangeRatesResponse = (
        fetch_currency_exchange_rates(
            schema=AlphavantageCurrencyExchangeRatesRequest(
                currency_from=currency_from,
                currency_to=currency_to,
            )
        )
    )

    headers: dict = {
        # "Content-Type": "application/json", # if httpresponse is used
        "Access-Control-Allow-Origin": "*",
    }

    json_response = JsonResponse(data=result.model_dump(), headers=headers)
    python_data = json.loads(json_response.content)
    save_exchange_rates(request, python_data)

    return JsonResponse(data=result.model_dump(), headers=headers)


def save_exchange_rates(request, json_information):
    if request.method == "GET":
        with open("history.json", "a") as file:
            # for line in json_information:
            json.dump(json_information, file)
            file.write("\n")


def get_information_from_history(request):
    with open("history.json", "r") as file:
        history_information = [json.loads(line) for line in file]

    return JsonResponse(data=history_information, safe=False)
