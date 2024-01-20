// TODO: Count Prime Numbers Between `1 to The Given Number`

var countPrimes = (n) => {
    var count = 0
    for (var i = 2; i <= n; i++) {
        if (isPrime(i)) {
            //console.log(i)
            count++
        }
    }
    console.log(`Number of primes till ${n} are ${count}`)

}

var isPrime = (n) => {
    for (var i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false
    }
    return true
}

countPrimes(10)