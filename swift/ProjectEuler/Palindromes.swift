import Foundation

/// Determine whether the given number is a palindrome.
/// :param: num The number to be checked.
/// :return: True if the number is a palindrome.
func isPalindrome(num: Int) -> Bool {
  let str = String(num)
  return equal(str, reverse(str))
}
