function solution(numbers) {
    var answer = 0;
    numbers.sort((a,b) => a-b);
    var i = numbers[0] * numbers[1];
    var j = numbers[numbers.length-1]*numbers[numbers.length-2];
    answer = Math.max(i,j)
    return answer;
}