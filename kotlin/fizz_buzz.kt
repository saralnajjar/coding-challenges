// FizzBuzz: print 1 to n, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz"

fun fizzBuzz(n: Int): List<String> {
    return (1..n).map { i ->
        when {
            i % 15 == 0 -> "FizzBuzz"
            i % 3 == 0  -> "Fizz"
            i % 5 == 0  -> "Buzz"
            else        -> i.toString()
        }
    }
}

fun main() {
    print("Enter n: ")
    val n = readLine()?.toIntOrNull() ?: run {
        println("Invalid input")
        return
    }
    fizzBuzz(n).forEach { println(it) }
}