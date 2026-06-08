import json
import requests

def load_company_data():

    try:

        requests.get(
            "https://www.sec.gov",
            timeout=5
        )

        raise Exception(
            "Using synthetic governance mapping"
        )

    except Exception:

        with open(
            "app/mock_data/board_data.json",
            "r"
        ) as f:

            companies = json.load(f)

        for company in companies:

            company["data_source"] = (
                "synthetic_fallback"
            )

        return companies