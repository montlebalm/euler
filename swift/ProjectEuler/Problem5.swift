/*
Question:
  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer:
  232792560
*/

import Foundation

func lcm(a: Int, b: Int) -> Int {
  var pairLcm = b

  while pairLcm % a != 0 {
    pairLcm += b
  }

  return pairLcm
}

func problem5(divisors: [Int]) -> Int {
  var smallestLcm = 1

  for (i, num) in enumerate(divisors) {
    if i + 1 < countElements(divisors) {
      let pairLcm = lcm(num, divisors[i + 1])
      smallestLcm = lcm(pairLcm, smallestLcm)
    }
  }

  return smallestLcm
}
