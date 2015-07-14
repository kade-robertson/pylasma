# Syntax

There are only a few keywords available in LindenMASM which you will need to implement.

1. `STT` - Begins every LindenMASM file.
2. `AXI $` - Sets the axiom (initial state) of the system.
 * `$` is a series of commands/variables/constants, ranging from the built-ins plus any user-defined functions.
3. `DEG $` - Sets the degree of which all turns will follow, default is 90.
4. `MOV $` - Sets the move distance of which all position adjustments will follow, default is 10.
5. `INC $` - Sets the number of iterations the generation should go through, default is 0.
6. `SET $ #` - Sets a constant `$` to a specified command `#`
 * `$` should be a character that is not one of `[]+-`.
 * `#` will either be a 0 or a 1, where a 0 corresponds to the constant being one that draws forward, and a 1 corresponds to the constant being one that moves fowards.
7. `RPL $ #` - On every iteration, variable/constant `$` will be replaced with the command/variable/constant string `#`.
 * `$` will be a letter between A and Z, inclusive, and uppercase. It does not need to be `SET` to be replaced.
 * `#` is a string of commands/variables/constants that `$` should be replaced with.
8. `END` - Ends every LindenMASM file.

Each keyword should be placed on a new line. Every file should start with `STT` and end with `END`.

# Commands

These are the builtin commands you can use in the axiom, or any replacement.

1. `+` - Rotates the pointer to the right `DEG` degrees.
2. `-` - Rotates the pointer to the left `DEG` degrees.
3. `[` - Saves the pointer's coordinates and heading to a list.
4. `]` - Pops the last value of a list and sets the pointer's coordinates and heading to that.

# Example

Check out the `linden-test.lasm` file for an example.
