/*
Given a list of numbers and a target, find two numbers that add up to the target and return their indices.
*/

fun twoSum(nums: List<Int>, target: Int): Pair<Int, Int>? {
    // Map of value → index for every number we've seen so far
    val seen = mutableMapOf<Int, Int>()

    for ((index, num) in nums.withIndex()) {
        val complement = target - num

        // If we've already seen the number that pairs with this one, we're done
        if (complement in seen) {
            return Pair(seen[complement]!!, index)
        }

        // Otherwise record this number and move on
        seen[num] = index
    }

    // No pair found
    return null
