#PrimeNumbers
"""Finds prime numbers up to n using Sieve of Eratosthenes"""

def main(n):

	nums = range(2,n+1)
	prime = []

	while len(nums) > 0:

		test = nums[0]
		prime.append(nums.pop(0))

		for i in nums:

			if i % test == 0:
				nums.remove(i)

	return prime





