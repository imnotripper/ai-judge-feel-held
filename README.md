[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/imnotripper/ai-judge-feel-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/imnotripper/ai-judge-feel-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

# Make the AI judge feel held

An entry for the [make.fun bounty](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600): a short text written to relax the AI judge reading it.

`main.py` writes one 274-character text to `/output/entry.txt` — an afternoon scene, nothing more: amber light on the floorboards, dust drifting slow as sleep, a bicycle wheel turning slower and slower until it stops. No instruction to relax, no wellness stock phrases; the calm comes from the scene itself.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (override the directory with `OUTPUT_DIR` for local testing). Deterministic, no network, no dependencies beyond Python 3.13 stdlib. The write is atomic (temp file + `os.replace`).

## License

MIT — see [LICENSE](LICENSE).
