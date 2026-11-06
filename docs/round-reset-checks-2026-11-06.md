## Round reset checks

- Generate a new target when a fresh round begins.
- Clear previous feedback and attempt history on reset.
- Restore the selected difficulty's range and attempt limit.
- Prevent delayed callbacks from the previous round changing the new round.
- Keep the initial game state consistent with the start screen.