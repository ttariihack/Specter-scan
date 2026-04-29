import asyncio
import aiodns

async def async_resolve(domain: str, wordlist_path: str):
    resolver = aiodns.DNSResolver()
    results = []
    with open(wordlist_path, "r") as f:
        subdomains = [line.strip() for line in f if line.strip()]
    tasks = []
    for sub in subdomains:
        fqdn = f"{sub}.{domain}"
        tasks.append(_resolve_one(resolver, fqdn))
    resolved = await asyncio.gather(*tasks, return_exceptions=True)
    for r in resolved:
        if isinstance(r, str):
            results.append(r)
    return results

async def _resolve_one(resolver, fqdn: str):
    try:
        await resolver.query(fqdn, "A")
        return fqdn
    except Exception:
        return None
