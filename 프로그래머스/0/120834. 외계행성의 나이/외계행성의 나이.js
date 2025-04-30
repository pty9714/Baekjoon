function solution(age) {
    var answer = '';
    var a = age.toString().split('');
    a.forEach((n) => {
        answer += String.fromCharCode(Number(n) + 97);
    });
    return answer;
}