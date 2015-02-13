//
//  Question:
//    A palindromic number reads the same both ways. The largest palindrome
//    made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the
//    largest palindrome made from the product of two 3-digit numbers.
//
//  Answer:
//    906609
//

import Foundation

func problem4(digits: Double) -> Int {
  let highest = Int(pow(10.0, digits) - 1)
  let lowest = Int(pow(10.0, digits - 1))
  var nums: (a: Int, b: Int) = (highest, highest)
  var palindrome = 0

  while nums.a >= lowest && nums.b >= lowest {
    nums.a -= 1
    let product = nums.a * nums.b

    if product > palindrome && isPalindrome(product) {
      palindrome = product
    }

    if nums.a == lowest {
      nums.b -= 1
      nums.a = highest
    }
  }

  return palindrome
}
