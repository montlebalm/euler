//
//  Question:
//    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
//    which, a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. There
//    exists exactly one Pythagorean triplet for which a + b + c = 1000. Find
//    the product abc.
//
//  Answer:
//    31875000
//
//  Resources:
//    http://www.mathsisfun.com/numbers/pythagorean-triples.html
//

import Foundation

private func a(first: Int, second: Int) -> Int {
  return square(first) - square(second)
}

private func b(first: Int, second: Int) -> Int {
  return first * second * 2
}

private func c(first: Int, second: Int) -> Int {
  return square(first) + square(second)
}

func problem9(sum: Int) -> Int {
  var total = 0
  var ctr: (m: Int, n: Int) = (1, 2)

  while total != sum {
    if total > sum {
      ctr.m += 1
      ctr.n = ctr.m
    }

    ctr.n += 1
    total = a(ctr.m, ctr.n) + b(ctr.m, ctr.n) + c(ctr.m, ctr.n)
  }

  return a(ctr.m, ctr.n) * b(ctr.m, ctr.n) * c(ctr.m, ctr.n)
}
