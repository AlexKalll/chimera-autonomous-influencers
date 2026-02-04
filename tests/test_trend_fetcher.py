import pytest


def test_trend_data_schema():
    # This test asserts that trend data matches the API contract in specs/technical.md
    # It should fail initially because the fetcher is not implemented.
    from src.perception import fetch_trends

    data = fetch_trends("mcp://news/trends")
    assert "trending_topics" in data
    assert isinstance(data["trending_topics"], list)
