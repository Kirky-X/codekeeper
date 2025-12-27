#!/usr/bin/env python
"""Entry point for CodeKeeper MCP Server."""

import asyncio


def main():
    """Run the MCP Server."""
    from codekeeper.mcp.server import main as server_main

    asyncio.run(server_main())


if __name__ == "__main__":
    main()
