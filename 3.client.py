import asyncio
from acp_sdk.client import Client
from colorama import Fore 

async def run_finance_workflow() -> None:
    async with Client(base_url="http://localhost:4242") as hospital:
        run1 = await hospital.run_sync(
            agent="stock_agent", input="What was IBMs EBITDA?"
        )
        content = run1.output[0].parts[0].content
        print(Fore.LIGHTMAGENTA_EX+ content + Fore.RESET)

if __name__ == "__main__":
    asyncio.run(run_finance_workflow())