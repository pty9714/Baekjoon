function solution(hp) {
    var answer = 0;
    var ant = [5,3,1];
    for (a of ant){
        answer+=parseInt(hp/a);
        hp%=a;
    }
    return answer;
}