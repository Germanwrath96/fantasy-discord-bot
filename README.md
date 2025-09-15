# Fantasy Football Discord Bot

This Discord bot integrates with the ESPN Fantasy API to provide live updates, projections, and matchup summaries for your league.

## Features
- Weekly matchups
- Live projections
- Roster updates
- Automated alerts

## Running Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your token:
4. Run the bot: `python bot.py`

## Deploying on Render
- Use a Background Worker
- `Start Command`: `python bot.py`
- Environment variables must be set in the Render dashboard
