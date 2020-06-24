# RISCV-Simulator
RISC-V instruction set simulator

CS204 Project Under guidance of T.V. Kalyan Sir

Team - Akshat Goel | Aman Bilaiya | Bolu Sathwik Reddy |  Rohit Tuli  |  Ujjwal Yadav

- HOW TO RUN :-

        On the terminal:-
           python3 MAIN.py
           
        On the GUI:-
           python3 simulator_front_end.py        

- Phase 1 :-
  - Assembly code to machine code conversion 

- Phase 2 :-
  - Implemented data path and control paths to run the Instructions.
  - Implemented all stages i.e. Fetch, Execute, Decode, Memory, Writeback
  - Implemented inter state buffers, memory unit and register files for the same

- Phase 3 :-
  - Implemented pipeline structure with and without data forwarding
  - Implemented -bit predictor for branch instructions

- Functionality to switch between modes :-
  - Non- pipelined
  - Pipelined with stalls
  - Pipelined with Data forwarding
  - Pipelined with 1-bit predictor

GUI :- Python Tkinter
