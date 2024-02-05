# Fummel
![image](https://github.com/heinzfieldmann/Fummel/assets/113355864/384f7108-c1d5-4495-a317-805bd72cf581)

DX7 archive and analysis
(this is a learning project)

Let us archive the open DX7 sysex files. And let us write some fun programs around them!
A machine language network for generating new novel patches for the DX7?

DX7 is an exciting platform since many plugins and many hardware synthesizers are compatible with the DX7 system. 

For example (DX7-compatible platforms):

Hardware: DX7/FS1R/DX200/TX812

Software: Dexed, FM8

Other interesting projects:
https://github.com/mmontag/dx7-synth-js/tree/master


Tech:

First step. Create something that reads  sysex-files scraped from the internet and store the patches in a database. 

Number two: Normalize them for the ML-network.

We could containerize the whole shebang?

To store the presets we could have a denormalized database? Column store in for example sqlite? One row per patch.
