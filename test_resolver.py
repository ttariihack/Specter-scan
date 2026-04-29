import asyncio
import pytest
from specterscan.core.resolver import async_resolve

@pytest.mark.asyncio
async def test_resolver_runs(tmp_path):
    wordlist = tmp_path / "wordlist.txt"
    wordlist.write_text("www\nmail\n")
    results = await async_resolve("example.com", str(wordlist))
    assert isinstance(results, list)
