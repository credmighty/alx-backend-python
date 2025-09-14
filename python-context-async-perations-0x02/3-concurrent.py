#!/usr/bin/python3
import asyncio
import aiosqlite # type: ignore

DB_NAME = "users.db"

async def async_fetch_users():
    """Fetch all users from the database asynchronously"""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM user_data") as cursor:
            rows = await cursor.fetchall()
            print("All Users:", rows)
            return rows


async def async_fetch_older_users():
    """Fetch users older than 40 from the database asynchronously"""
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM user_data WHERE age > 40") as cursor:
            rows = await cursor.fetchall()
            print("Users older than 40:", rows)
            return rows


async def fetch_concurrently():
    """Run both queries concurrently"""
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return results


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
