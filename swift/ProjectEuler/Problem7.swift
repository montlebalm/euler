//
//  Question:
//    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
//    see that the 6th prime is 13. What is the 10001st prime number?
//
//  Answer:
//    104743
//

import Foundation

func problem7(targetCount: Int) -> Int {
  var count = 1
  var num = 1

  while count < targetCount {
    // No need to increment by 1 since primes must be odd
    num += 2

    if isPrime(num) {
      count += 1
    }
  }

  return num
}
