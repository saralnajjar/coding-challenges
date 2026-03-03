fun pascalsTriangle(n: Int): List<List<Int>> {
    if (n <= 0) return emptyList()

    val triangle = mutableListOf(listOf(1))

    for (i in 1 until n) {
        val row = mutableListOf(1)
        for (j in 1 until i) {
            row.add(triangle[i-1][j-1] + triangle[i-1][j])
        }
        row.add(1)
        triangle.add(row)
    }

    return triangle
}

fun main() {
    print("How many rows? ")
    val n = readLine()?.toIntOrNull() ?: 5
    pascalsTriangle(n).forEach { println(it) }
}