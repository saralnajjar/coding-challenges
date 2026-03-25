// When given 2 sorted lists, merge them into one sorted in O(n+m)

data class ListNode(val value: Int, variable next: ListNode?)

fun mergeSortedLists(l1: ListNode?, l2: ListNode?): ListNode? {
    val dummy = ListNode(0)
    var current = dummy
    var a = l1
    var b = l2

    while (a != null && b != null) {
        if (a.value <= b.value) {
            current.next = a
            a = a.next
        } else {
            current.next = b
            b = b.next
        }
        current = current.next!!
    }

    current.next = a ?: b
    return dummy.next
}

fun funlistOf(varage values: Int): ListNode? {
    if (values.isEmpty())
        return null
    val head = ListNode(values[0])
    var current = head
    for (i in 1 until values.size) {
        current.next = ListNode(values[i])
        current = current.next!!
    }
    return head
}

fun toList(head: ListNode?): List<Int> {
    val result = mutableListOf<Int>()
    var current = head
    while (current != null) {
        result.add(current.value)
        current = current.next
    }
    return result
}

fun runTest(description: String, actual: List<Int>, expected: List<Int>) {
    val status = if (actual == expected) "PASS" else "FAIL"
    println("  $status  $description")
    if (actual != expected) {
        println("         expected: $expected")
        println("         got:      $actual")
    }
}

fun main() {
    println("Merge Two Sorted Lists")
    println("=".repeat(40))

    // Standard case
    runTest(
        "[1,3,5] + [2,4,6]",
        toList(mergeSortedLists(listOf(1, 3, 5), listOf(2, 4, 6))),
        listOf(1, 2, 3, 4, 5, 6)
    )

    // One empty list
    runTest(
        "[] + [1,2,3]",
        toList(mergeSortedLists(null, listOf(1, 2, 3))),
        listOf(1, 2, 3)
    )

    // Both empty
    runTest(
        "[] + []",
        toList(mergeSortedLists(null, null)),
        emptyList()
    )

    // Duplicates
    runTest(
        "[1,2,2] + [2,3]",
        toList(mergeSortedLists(listOf(1, 2, 2), listOf(2, 3))),
        listOf(1, 2, 2, 2, 3)
    )

    // Different lengths
    runTest(
        "[1] + [2,3,4,5]",
        toList(mergeSortedLists(listOf(1), listOf(2, 3, 4, 5))),
        listOf(1, 2, 3, 4, 5)
    )
}