function solution(numbers) {

    numbers.sort((a,b) => a-b);
    n = numbers.length;
    var answer = numbers[n-1]*numbers[n-2];
    return answer;
}