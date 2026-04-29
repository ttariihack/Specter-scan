import argparse
import asyncio
from specterscan.core.resolver import async_resolve
from specterscan.utils.logger import get_logger

logger = get_logger()

async def run_scan(domain: str, wordlist: str, output: str):
    logger.info(f"Starting scan for {domain} with wordlist {wordlist}")
    results = await async_resolve(domain, wordlist)
    logger.info(f"Found {len(results)} subdomains")
    with open(output, "w") as f:
        for r in results:
            f.write(r + "\n")
    logger.info(f"Results saved to {output}")

def main():
    parser = argparse.ArgumentParser(description="SpecterScan - Modern Subdomain Discovery")
    parser.add_argument("domain", help="Target domain to scan")
    parser.add_argument("-w", "--wordlist", default="specterscan/wordlists/common_10k.txt",
                        help="Path to wordlist file")
    parser.add_argument("-o", "--output", default="results.txt",
                        help="Output file")
    args = parser.parse_args()

    asyncio.run(run_scan(args.domain, args.wordlist, args.output))

if __name__ == "__main__":
    main()
