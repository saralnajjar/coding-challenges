/*
Check if s atrinbg reads the same frontwards and backwards.
1. Two pointer: O(n) time, O(1) space
2. Reverse and compare
*/

// Strip non letter or digit items, and lowercase them.
// Walk inward from both ends,m if any pair dont match, not a palindrome.
fun isPalindrome(s: String): Boolean {
    val cleaned = s.filter { it.isLetterOrDigit() }.lowercase()
    var left = 0
    var right = cleaned.length - 1

    while (left<right) {
        if (cleaned[left] != cleaned[right]) return false
        left++
        right--
    }
    return true
}

// "Elegant version": created a reverse copy
fun isPalindromeOneLiner(s: String): Boolean {
    val cleaned = s.filter { it.isLetterOrDigit() }.lowercase()
    return cleaned == cleaned.reversed()
}

fun main() {
    val tests = listOf(
        "hello",
        "Hello, World",
        "racecar",
        "Palindrome",
        "Not a Parlindrome",
        "A man, a plan, a canal: Panama", 
        "nurses run",
        ""
    )

    println("Two ponter approach:")
    for (test in tests) {
        println("   \"$test\" -> ${isPalindrome(test)}")
    }

    println("\nOne liner appreach:")
    for (test in tests) {
        println("   \"$test\" -> ${isPalindromeOneLiner(test)}")
    }
}