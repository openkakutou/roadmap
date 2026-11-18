---
status: todo
---
# Make openkakutou.github.io explain the project and attract visitors

## Description
https://openkakutou.github.io/ is today a short hand-written list of live apps ("Live now"): it does not say what OpenKakutou is or why it matters. Rework it into a page that explains the project and makes people want to try it or contribute:
- what OpenKakutou is: an open-source fighting-game engine that plays MUGEN 1.0/1.1 and Ikemen GO content (characters, stages, lifebars), runs natively and in the browser, with its own extensions (3D characters, screenpacks, modes);
- why: faithful play of existing community content, portable game folder, tools to view and edit content;
- what is available now (viewers, editors, `game`) and what comes next (the combat milestone);
- fidelity videos: the same match, driven by the same scripted inputs, recorded side by side in Ikemen GO and in OpenKakutou, so visitors can see how faithful the engine is.

## Acceptance Criteria
- [ ] The page explains the project, its goal and its audience in plain words before listing the apps
- [ ] The page is visually attractive and works at phone width
- [ ] A fidelity section shows side-by-side videos (Ikemen GO vs OpenKakutou) of the same scripted match, each naming the characters, stage and the frames identical before the first divergence
- [ ] Every video credits the authors of the characters, stage and lifebar it shows
- [ ] Every linked app still works (links checked)

## Notes
- The repo has no `.vibe/` yet: item 012 (vibe setup and link check) comes first or alongside; decision 018 says to revisit the plain-HTML stack when the page grows.
- The videos are produced by game#052 from the differential test against Ikemen GO (engine#036, game#051, decisions 039 and 042): scripted inputs, fixed seed, no CPU. Until the engine moves characters (engine#039, #041, #028), a video would only show a divergence, so the fidelity section can start with the measured figure and gain videos as parity improves.
- Videos may use any content from the Product Owner's local Ikemen GO collection (Product Owner, 2026-11-18): only the video is published, never the characters or stages themselves. Authors are credited.
