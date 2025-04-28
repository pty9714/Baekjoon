function solution(n) {
    var answer = 0;
    let arr = [];
    for (let i=1; i<=1000 ; i++){
        arr.push(i*i)
    }
    if (arr.includes(n)){
        answer = 1;
    }
    else{
        answer = 2;
    }
    return answer;
}