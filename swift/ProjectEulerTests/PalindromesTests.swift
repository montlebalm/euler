import XCTest
import ProjectEuler

class IsPalindromeTests: XCTestCase {

  func test1IsPalindrome() {
    XCTAssertTrue(isPalindrome(1))
  }

  func test2000002IsPalindrome() {
    XCTAssertTrue(isPalindrome(2000002))
  }

  func test1234IsPalindrome() {
    XCTAssertFalse(isPalindrome(1234))
  }

}
