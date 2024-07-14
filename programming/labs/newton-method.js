function sqrt(x) {
  function abs(n) {
    return n < 0 ? -1 * n : n;
  }

  function square(x) {
    return x * x;
  }

  function isGoodEnough(guess, tolerance = 0.0001) {
    return abs(square(guess) - x) < tolerance;
  }

  function improveGuess(guess, x) {
    return (guess + x / guess) / 2;
  }

  function sqrt_iter(guess, x) {
    if (isGoodEnough(guess)) {
      return guess;
    }
    return sqrt_iter(improveGuess(guess, x), x);
  }
  return sqrt_iter(1, x);
}

console.log(sqrt(25));

console.log(sqrt(9));

console.log(sqrt(2));
