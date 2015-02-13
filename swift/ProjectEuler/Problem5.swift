//
//  Question:
//    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
//
//  Answer:
//    232792560
//

import Foundation

func problem5(divisors: [Int]) -> Int {
  var smallestLcm = 1

  for (i, num) in enumerate(divisors) {
    if i + 1 < divisors.count {
      let pairLcm = lcm(num, divisors[i + 1])
      smallestLcm = lcm(pairLcm, smallestLcm)
    }
  }

  return smallestLcm
}
