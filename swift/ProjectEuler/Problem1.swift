//
//  Question:
//    If we list all the natural numbers below 10 that are multiples of
//    3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the
//    sum of all the multiples of 3 or 5 below 1000.
//
//  Answer:
//    233168
//

import Foundation

func problem1(max: Int) -> Int {
  let range = Array(1..<max)
  let multiples = range.filter({ $0 % 3 == 0 || $0 % 5 == 0 })
  return multiples.reduce(0, combine: +)
}
