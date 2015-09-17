function isPrime(x) {
  for(var i = 2; i <= Math.ceil(Math.sqrt(x)); i++) {
    if(x % i === 0) {
      return false;
    }
  }
  return true;
}

function nextPrime(x) {
  x = x + 1;
  while(!isPrime(x)) {
    x++;
  }
  return x;
}

function maxPrime(x) {
  var currentPrime = 2;
  var maxFactor = 2;
  while(x > 1) {
    while(x % currentPrime === 0) {
      x = x / currentPrime;
      maxFactor = currentPrime;
    }
    currentPrime = nextPrime(currentPrime);
  }
  return maxFactor;
}
// function maxPrime(x){ for(var i = Math.ceil(Math.sqrt(x)); i >= 3 ; i--) {if(isPrime(i) && x % i == 0){return i} }}
console.log(maxPrime(600851475143));
