#binRecur.py

"""Performs recursive binary search"""

def merge(l1,l2,l3):
	#merge sorted lists l1 and l2 into l3

	i1, i2, i3 = 0, 0, 0

	n1, n2 = len(l1), len(l2)

	while n1>i1 and n2>i2:	#loop as long as both lists have a value remaining
		if l1[i1] < l2[i2]:	#l1 is greater, populate i3 and advance i1
			l3[i3] = l1[i1]
			i1=i1+1
		else:
			l3[i3] = l2[i2]	#l2 is greater, populate i3 and advance i2
			i2=i2+1
		i3=i3+1			#advance i3

	#one list is complete copy the remainder of the other list

	while i1<n1:
		l3[i3] = l1[i1]
		i3 = i3+1
		i1 = i1+1
	while i2<n2:
		l3[i3] = l2[i2]
		i3=i3+1
		i2=i2+1


def binRecur(nums):

	size = len(nums)

	if size>1:
		mid = size/2
		nums1, nums2 = nums[:mid], nums[mid:]

		binRecur(nums1)
		binRecur(nums2)

		merge(nums1, nums2, nums)

	return nums

