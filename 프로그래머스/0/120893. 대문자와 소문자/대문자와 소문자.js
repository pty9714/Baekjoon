function solution(my_string) {
    var answer = '';
    for (c of my_string){
        if (c === c.toLowerCase()){
            answer += c.toUpperCase();
        }
        else {
            answer += c.toLowerCase();
        }
    }
    return answer;
}