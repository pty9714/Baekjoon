function solution(order) {
    var answer = 0;
    while (order>0){
        let digit = order % 10;
        if (digit !== 0 && digit % 3 === 0) {
            answer += 1;
        }
        order = parseInt(order/10);
    }
    return answer;
}