# Space Invaders with Voice

Let's build the Legendary Arcade Space Invaders in Python!

[Play the game now🕹️](https://santhoshkumard11.github.io/pygame-space-invaders/)

[Watch demo video🎬](https://youtu.be/DhoQpftgSNw)

## Setup Environment

### Install all Python packages

`pip install -r requirements.txt`

### Add Azure Speech Service environment variables

- AZURE_COGNITIVE_SERVICE_KEY
- AZURE_COGNITIVE_SERVICE_REGION

## Run the game

### Local Run

`python3 game.py`

### Web - runs on port 8000

`pygbag .\space_invaders`

### Docker

`docker build -t "sandy-inspires-space-invaders" .`

`docker container run -d -p 8000:8000 --name=space-invaders-game sandy-inspires-space-invaders`

![Space Invaders - Arcade Game](https://raw.githubusercontent.com/Santhoshkumard11/pygame-space-invaders/main/images/arcade_game.jpg)

## Inspiration

I stumbled upon this Twitch Streamer with no hands and legs but plays WarZone and to my surprize he is at top zero %. I mean what.
This favorite quote is: `I was born without arms and legs and I will absolutely destroy you on first person shooters.`
Then I realized that games should reach those people too.
I wanted to contribute and help people with disabilities to play games too.
While I was processing this thought and I recently saw this hackathon and that's how space invaders with voice came to life.

![Gaming without hands](https://github.com/Santhoshkumard11/pygame-space-invaders/blob/7d74224cc0a68f25809a2edca776a93933ea58b6/images/nohands-nolegs.png?raw=true)

Image Credits: truly (YouTube Channel)

## What it does

Replicated the Legendary Space Invaders from 1978 which is a shoot 'em up arcade game developed by Tomohiro Nishikado.

The game can be played via any web browser which supports WebAssembly.
In addition to using your keyboard to control the game, now you can use voice commands to do the same actions.

Voice Commands to use - `left, right, left corner, right corner, shoot, rapid fire, start, pause, stop`

> Rapid Fire is command that shoots 100 continues shots at the enemies.

![Gameplay gif](https://github.com/Santhoshkumard11/pygame-space-invaders/blob/7d74224cc0a68f25809a2edca776a93933ea58b6/images/gameplay.gif?raw=true)

## How we built it

- Python - General Programming
- Pygame - Writing Game Logic
- Pygbag - Python WebAssembly for everyone
- asyncio - Tried some asyncio with coroutines between Speech Service and command execution
- WebAssembly - Running Python natively on browser
- GitHub Actions - Convert Python code to WebAssembly and deploy it in GitHub pages
- Azure Cognitive Services (Speech Service) - Speech to Text conversion of the game commands

## Challenges we ran into

- Initially had one module with both game logic and Speech recognition logic both together but it didn't work well as expected so moved it to a different module
- Issues with asyncio on Azure Speech Service, was not returning Coroutine

## Accomplishments that we're proud of

- Got the game working with all the features
- Deployed in GitHub pages with a simple CI/CD

## What we learned

- A great understanding of WebAssembly and it's usefulness
- Game design and writing game logic

## What's next for Space Invaders

- Adding more game logic, I remember after a while one enemy would leave the group and fly over the ship while shooting
- Score calculation and storing it in database to be displayed in a private leaderboard
