# Space Invaders with Voice

Let's build the Legendary Arcade, Space Invaders with Python!

[Click here to play the game 🕹️](https://santhoshkumard11.github.io/pygame-space-invaders/)

[Click here to watch the demo video🎬](https://youtu.be/DhoQpftgSNw)

![Gameplay gif](https://raw.githubusercontent.com/Santhoshkumard11/pygame-space-invaders/main/images/gameplay.gif)

## Setup Environment

### Install all Python packages

`pip install -r requirements.txt`

### Add Azure Speech Service environment variables

- AZURE_COGNITIVE_SERVICE_KEY
- AZURE_COGNITIVE_SERVICE_REGION

## Run the game

### Local Run

`python3 main.py`

### Web - runs on port 8000

Note: Assuming that you are already inside the code directory

`pygbag .`

### Docker

`docker build -t "sandy-inspires-space-invaders" .`

`docker container run -d -p 8000:8000 --name=space-invaders-game sandy-inspires-space-invaders`

![Space Invaders - Arcade Game](https://raw.githubusercontent.com/Santhoshkumard11/pygame-space-invaders/main/images/arcade_game.jpg)
Image Credits: Wikimedia

## Inspiration

I stumbled upon this Twitch Streamer with no hands and legs but plays Call Of Duty: WarZone and to my surprise, he is in the top zero %. I mean what!!!
This favorite quote is: `I was born without arms and legs and I will absolutely destroy you on first-person shooters.`
Then I realized that games should reach those people too.
I wanted to contribute and help people with disabilities to play games too.
While I was processing this thought and saw this hackathon, that's how space invaders with voice came to life.

![Gaming without hands](https://raw.githubusercontent.com/Santhoshkumard11/pygame-space-invaders/main/images/nohands-nolegs.png?raw=true)

Image Credits: truly (YouTube Channel)

## What it does

Replicated the Legendary Arcade Space Invaders from 1978 which is a shoot 'em up arcade game developed by Tomohiro Nishikado.

The game can be played via any web browser which supports WebAssembly.
In addition to using your keyboard to control the game, now you can use voice commands to do the same actions.

Voice Commands to use - `left, right, left corner, right corner, shoot, rapid fire, start, pause, stop`

Difficulty level can be increased with the `DIFFICULTY_LEVEL`, a value between 1 to 10, number of enemy bullets fired at the ship

> Rapid Fire is a special command that shoots 100 continuous shots at the enemies.

## How we built it

- Python - General Programming
- Pygame - Writing Game Logic
- Pygbag - Python WebAssembly for everyone ( packager + test server )
- asyncio - Tried some asyncio code to await between Speech Service and command executions
- GitHub Actions - Convert Python code to WebAssembly and deploy it in GitHub pages
- Azure Cognitive Services (Speech Service) - Speech to Text conversion of the game commands

## Challenges we ran into

- Initially had one module with both game logic and Speech recognition logic both together but it didn't work well as expected so moved it to a different module
- Issues with asyncio on Azure Speech Service, was not returning Coroutine

## Accomplishments that we're proud of

- Got the game working with almost all the original game features
- Deployed in GitHub pages with a simple CI/CD with Pygbag
- Made a Docker container of the game so its extremely simple to deploy

## What we learned

- A great understanding of WebAssembly and its usefulness
- Game design and writing game logic in Pygame

## What's next for Space Invaders with Voice

- Adding more game logic, I remember after a while one enemy would leave the group and fly over the ship shooting
- Score calculation and storing it in the database to be displayed in a private leaderboard

This was built on top of Lee Robinson's repo.
