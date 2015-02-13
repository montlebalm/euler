//
//  Question:
//    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
//    factor of the number 600851475143?
//
//  Answer:
//    6857
//

import Foundation

func problem3(num: Int) -> Int {
  let startNum = Int(pow(Double(num), 0.5)) + 1

  for var i = startNum; i > 2; i-- {
    if num % i == 0 && isPrime(i) {
      return i
    }
  }

  return 0
}
