import pytest
import json
from stonks import main


@pytest.mark.asyncio
async def test_main():
    await main()
    with open('json/top_10_expensive.json') as f:
        top_10_expensive = json.load(f)
    with open('json/top_10_low_pe.json') as f:
        top_10_low_pe = json.load(f)
    with open('json/top_10_growth.json') as f:
        top_10_growth = json.load(f)
    with open('json/top_10_potential_profit.json') as f:
        top_10_potential_profit = json.load(f)
    assert len(top_10_expensive) == 10
    assert len(top_10_low_pe) == 10
    assert len(top_10_growth) == 10
    assert len(top_10_potential_profit) == 10
    assert all(isinstance(company['name'], str) for company in top_10_expensive)
    assert all(isinstance(company['code'], str) for company in top_10_expensive)
    assert all(isinstance(company['price'], float) for company in top_10_expensive)
    assert all(isinstance(company['pe'], float) for company in top_10_low_pe)
    assert all(isinstance(company['growth'], float) for company in top_10_growth)
    assert all(isinstance(company['low'], float) for company in top_10_potential_profit)
    assert all(isinstance(company['high'], float) for company in top_10_potential_profit)
