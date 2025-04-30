function solution(my_string) {
    var answer = '';
    var str = my_string.split('')
    for (let i=0; i<str.length; i++){
        for (let j=i+1; j<str.length; j++){
            if (str[i]==str[j]){
                str[j] = ''
            }
        }
    }
    answer = str.join('');
    return answer;
}