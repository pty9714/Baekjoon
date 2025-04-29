function solution(my_string) {
    var answer = 0;
    var arr = my_string.split('');
    for (s of arr){
        if (!isNaN(s)){
            answer+=parseInt(s);
        }
    }
    return answer;
}