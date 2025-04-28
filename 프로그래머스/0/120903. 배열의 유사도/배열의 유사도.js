function solution(s1, s2) {
    var answer = 0;
    s1.forEach((element1)=>{
        s2.forEach((element2)=>{
            if(element1==element2){
                answer +=1;
            }
        })
    })
    return answer;
}