function solution(n, numlist) {
    var answer = [];
    for (s of numlist){
        if (s%n == 0){
            answer.push(s);
        }
    }
    return answer;
}