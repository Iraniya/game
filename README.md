# Super-Sonic, A single player racing game

## A brief description

Super-Sonic is a single player racing game. The central character of the game is Sonic,
who runs along a mountainous country side along with his competitors. Sonic need to
complete the race by running three laps of the track and based on his speed he gets his
score. He also needs to come ahead of his competitors in order to win. Sonic can be
controlled by the user using keyboard or a joystick. The user can control the throttle of
the run which decides the maximum acceleration of Sonic. The race track consists of
dangerous curves and the player needs to turn swiftly in order to stay on the track. If the
player runs off the track he will be brought back to the track with his acceleration decreased.

# A screenshot of Super Sonic

The opponents have an Artificial Intelligence module embedded in them. Based on the
artificial intelligence, the opponents swerve to the left or right of the track, by going
either to the left or right lane. The opponents also intelligently overtake the first player
and also avoid collisions with the track boundaries. Various parameters of the opponents
like the throttle, acceleration, speed are controlled by the artificial intelligence
component. The game also has sound components associated with each player, so that we get a 3D
experience. To make the gaming experience more enriching, there are game background
music complementing the graphics.

# A screenshot of the demo race using Game AI Environment

The environment consists of a hilly countryside and a road snaking past through the
landscape. The road has very dangerous curves, which the player needs to cross carefully
by tilting and accelerating at the required amount. The road also has a collision detector
which detects when the player moves out of the road. In case a player strays away from
the path, he is brought back to the center.
Game Characters
The game characters include Sonic and three bots. The bots are named 'Tails', 'Rocket
Snail' and 'Balloon'. Sonic is the central character and the first player. The player needs to
control him. The other three characters are controlled by the computer and the
computer decides their lanes, throttle and acceleration.

# Character behaviour

All the players try to defeat the other players. The bots use artificial intelligence to
defeat Sonic who is controlled by the player. Every bot is associated with sounds so that
Sonic can know when the other bots are trying to overtake it. When Sonic gets off the
track the collision tracker checks and brings Sonic back on the track.
Gameplay During the race, the player need to throttle and accelerate to run ahead. The player
needs to turn left or right to stay on the path and avoid the dangerous curves. The score
of the player depends on the distace he has covered. The player needs to complete three
laps in order to complete the race, and also needs to stay ahead of the other three
players. All the other opponent players try to race ahead of the players and the user
needs to prevent that.

# Control of the game are as follows:

Keyboard
W key – Used for the forward motion of the character.
A key –Used to moving Sonic in left direction.
D key – Used for moving Sonic in right direction.
S key – Used for moving Sonic backward.
Controller
Y key – Accelerate Sonic
B key – Stop Sonic
Right key – To move Sonic right side
Left key – To move Sonic left side.

# Game termination and win
The game finishes after the player has completed all the three laps. If the player
completes all the three laps before the other three players, then he wins, else he loses.
Screenshot of the winning screen

# System requirements

Super Sonic is based on Panda3D. So it is cross platform(can run on any platform). To run
the game, there has to be an installation of Panda3D runtime on the platform.
