/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    nums = [...new Set(nums)]
    nums = nums.sort((a, b) => b - a)
    console.log(nums)
    if (nums.length>=3){
        return nums[2]
    }
    else{
        return nums[0]
    }
};