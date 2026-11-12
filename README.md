# Tiny chess engine — make.fun entry

A compact chess engine (negamax + alpha-beta, 0x88 board, transposition table).
The entry `main.py` is the engine packed with LZMA + base85 (<=4096 bytes);
`pack.py` rebuilds it from `engine_compact_min.py`.
