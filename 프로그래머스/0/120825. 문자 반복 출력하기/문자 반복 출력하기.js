function solution(my_string, n) {
    var answer = '';
    for(var c in my_string){
        for (let i=0; i<n; i++){
            answer += my_string[c];
        }

    }
    return answer;
}