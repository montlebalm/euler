import Foundation

/// Generate the square of the given number
/// :param: first The number to be squared.
/// :return: the square of the specified number.
func square(num: Int) -> Int {
  return Int(pow(Double(num), 2))
}