/**
 * @param {number[]} nums
 * @return {number[][]}
 */
function threeSum(nums) {
  const triplets = [];
  const sorted = nums.sort((a, b) => a - b);

  for (let i = 0; i < sorted.length - 2 || sorted[i] > 0; i++) {
    if (sorted[i - 1] === sorted[i]) continue;
    let left = i + 1;
    let right = sorted.length - 1;
    while (right > left) {
      const sum = sorted[i] + sorted[left] + sorted[right];
      if (sum > 0) right--;
      else if (sum < 0) left++;
      else if (sum === 0) {
        triplets.push([sorted[i], sorted[left], sorted[right]]);
        while (right > left && sorted[right] === sorted[right - 1]) right--;
        while (right > left && sorted[left] === sorted[left + 1]) left++;
        right--;
        left++;
      }
    }
  }

  return triplets;
}
