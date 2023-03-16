# ML Interpreter

This is a basic machine language interpreter based on the little man computer. It has a slightly increased instruction set allowing for use of a non standard print character instruction.
<br>
XX signifies a memory address.

| ML  | ASM     | Function                                                                        |
| 901 | INP     | Take 1 character of user input                                                  |
| 902 | OUT     | Print the value stored in the accumulator                                       |
| 903 | CHAROUT | Print the ASCII translation of the character stored in the accumulator          |
| 5xx | LDA     | Load location XX in memory the the accumulator                                  |
| 3xx | STA     | Store to location XX in memory from the accumulator                             |
| 1xx | ADD     | Add XX in memory to the accumulator, result is stored in the accumulator        |
| 2xx | SUB     | Subtract XX in memory from the accumulator, result is stored in the accumulator |
| 8xx | BRP     | Branch to XX if the accumulator is positive                                     |
| 7xx | BRZ     | Branch to XX if the accumulator is zero                                         |
| 6xx | BRA     | Branch to XX                                                                    |
| 000 | HALT    | Stop execution                                                                  |

| Name | Register        | Function |
| ACC  | Accumulator     | Stores the result of calculations, is also the target of out and charout |
| PC   | Program Counter | Stores the memory address of the current instruction                     |