// Ex 1.1.1
10; // 10
5 + 3 + 4; // 12
9 - 1; // 8
6 / 2; // 3
2 * 4 + (4 - 6); // 6
const a = 3; 
const b = a + 1;
a + b + a * b;  // 19
a === b;  // false
b > a && b < a * b ? b : a; // 4
a === 4
? 6
: b === 4 ? 6+7+a : 25; // 16

2 + (b > a ? b : a); // 6
(a > b ? a : a < b ? b : -1) * (a + 1); // 16

// ex 1.1.2
(5 + 4 + (2 - (3 - (6 + 4/5)))) / (3 * (6-2) * (2-7))

// ex 1.1.3
function square(x) { return x * x }

function sumLargeSquare(x, y, z) {
  let largest;
  let secondLargest;

  if (x >= y && x >= z) {
    largest = x;
    secondLargest = y > z ? y : z
  };

  if (y >= x && y >= z) {
    largest = y
    secondLargest = x > z ? x : z
  } 
  if (z >= x && z >= y) {
    largest = z
    secondLargest = x > y ? x : y
  }

  return square(largest) + square(secondLargest)
}

// ex1.1.4

function plus(a, b) { return a + b; } 
function minus(a, b) { return a - b; } 

function a_plus_abs_b(a, b) {
  return (b >= 0 ? plus : minus)(a, b);
}

// in a_plus_abs_b, b is first evaluated to determine whether the function of plus or minus should be returned and apply to the argumets (a, b); at the final return, either the plus or mins function is invoked with the arguments of a and b to return the solution.

