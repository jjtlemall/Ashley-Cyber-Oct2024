#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.

echo "Enter length of side 1: "
read side1
echo "Enter length of side 2: "
read side2
echo "Enter length of side 3: "
read side3

# Input Format
# Three integers, each on a new line.

if [ $side1 -eq $side2 ] && [ $side2 -eq $side3 ]; then
  echo "EQUILATERAL"
elif [ $side1 -eq $side2 ] || [ $side2 -eq $side3 ] || [ $side1 -eq $side3 ]; then
  echo "ISOCELES"
else
  echo "SCALENE"
fi
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)
