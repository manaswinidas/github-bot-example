import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
   async with aiohttp.ClientSession() as session:
       gh = GitHubAPI(session, "mariatta", oauth_token=os.getenv("GH_AUTH"))
       await gh.post('/repos/manaswinidas/github-ci/issues',
             data={
                 'title': 'We got a problem',
                 'body': 'Use more emoji!',
             })

loop = asyncio.get_event_loop()
loop.run_until_complete(main())