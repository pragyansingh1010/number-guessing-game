# Game State Notes

A round should track the target, valid-guess count, and whether the round has ended. Invalid input should not count as an attempt. After a correct guess, disable further submissions until the player starts a new round. Restart should reset feedback and attempts together.