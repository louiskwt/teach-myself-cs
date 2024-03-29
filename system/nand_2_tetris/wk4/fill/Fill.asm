// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Psuedo Code
// Grap the screen address
// Set up the infinite loop
// Check if the data in keyboard address is 0
// if 0 > white; black
(START)
  @SCREEN
  D=A
  @addr
  M=D

  (CHECKKBD)
  @KBD
  D=M
  @BLACKEN
  D;JGT
  @WHITEN
  D;JEQ  

  @CHECKKBD
  0;JMP
      
  (BLACKEN)
  @color
  M=-1 // fill it with black
  @FILL
  0;JMP

  (WHITEN)
  @color
  M=0 // fill it with white
  @FILL
  0;JMP
  
  (FILL)
  @color
  D=M
  @addr
  A=M
  M=D
  
  @addr
  M=M+1
  A=M

  @addr
  D=M+1
  @KBD
  D=A-D // skip to next pixel to fill
  @FILL
  D;JGT   

@START
0;JMP

