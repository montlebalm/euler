//
//  Numbers.swift
//  ProjectEuler
//
//  Created by Chris Montrois on 2/13/15.
//  Copyright (c) 2015 Chris Montrois. All rights reserved.
//

import Foundation

/// Generate the square of the given number
/// :param: first The number to be squared.
/// :return: the square of the specified number.
func square(num: Int) -> Int {
  return Int(pow(Double(num), 2))
}

/// Split the given string into an Int array.
/// :param: str The string to be split.
/// :return: an array of Ints.
func stringToDigits(str: String) -> [Int] {
  return Array(str).map({ String($0).toInt()! })
}
