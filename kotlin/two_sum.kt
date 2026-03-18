fun twoSum(nums: List<Int>, target: Int): Pair<Int, Int>? {
    val seen = mutableMapOf<Int, Int>()

    for ((index, num) in nums.withIndex()) {
        val complement = target - num

        if (complement in seen) {
            return Pair(seen[complement]!!, index)
        }

        seen[num] = index
    }

    return null
}

fun main() {
    val tests = listOf(
        Pair(listOf(2, 7, 11, 15), 9),
        Pair(listOf(3, 2, 4), 6),
        Pair(listOf(1, 5, 3, 7), 10),
        Pair(listOf(1, 2, 3), 100)
    )

    for ((nums, target) in tests) {
        val result = twoSum(nums, target)
        if (result != null) {
            val (i, j) = result
            println("$nums, target=$target -> indices ($i, $j): ${nums[i]} + ${nums[j]} = $target")
        } else {
            println("$nums, target=$target -> no solution found")
        }
    }
}