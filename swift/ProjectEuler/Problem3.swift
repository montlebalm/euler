/*
Question:
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143?

Answer:
  6857
*/

import Foundation

func isPrime(num: Int) -> Bool {
  if num < 2 || num % 2 == 0 {
    return false
  }

  if num == 2 {
    return true
  }

  for var i = 3; i < Int(pow(Double(num), 0.5)) + 1; i += 2 {
    if num % i == 0 {
      return false
    }
  }

  return true
}

func problem3(num: Int) -> Int {
  for var i = Int(pow(Double(num), 0.5)) + 1; i > 2; i-- {
    if num % i == 0 && isPrime(i) {
      return i
    }
  }

  return 0
}
