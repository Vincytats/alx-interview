#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """Create a list of booleans representing if numbers are prime up to n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def count_primes_up_to_n(n, is_prime):
    """Return the number of primes up to and including n."""
    return sum(is_prime[:n+1])

def isWinner(x, nums):
    """Determine who the winner of the game is after x rounds."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count number of primes up to and including n
        num_of_primes = count_primes_up_to_n(n, is_prime)
        # If the count of primes is odd, Maria wins, otherwise Ben wins
        if num_of_primes % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
