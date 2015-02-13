import Foundation

/// Find the least common multiple between two numbers.
/// :param: first The first number to be compared.
/// :param: second The second number to be compared.
/// :return: the least common multiple.
func lcm(first: Int, second: Int) -> Int {
  var multiple = second

  while multiple % first != 0 {
    multiple += second
  }

  return multiple
}

/// Determine whether a number is prime.
/// :param: num The number to be checked.
/// :return: True is the number is prime.
func isPrime(num: Int) -> Bool {
  if num == 2 {
    return true
  }

  if num < 2 || num % 2 == 0 {
    return false
  }

  for var i = 3; i < Int(pow(Double(num), 0.5)) + 1; i += 2 {
    if num % i == 0 {
      return false
    }
  }

  return true
}
