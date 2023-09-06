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

