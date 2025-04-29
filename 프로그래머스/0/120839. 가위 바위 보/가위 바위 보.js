function solution(rsp) {
    var answer = '';
    for (c of rsp.split('')){
        if (c==2){
            answer += 0
        }
        else if (c==0){
            answer += 5
        }
        else{
            answer +=2
        }
    }
    return answer;
}