function solution(num_list) {
    var answer = [0,0];
    num_list.forEach((e)=>{
        if (e%2 == 0){
            answer[0] +=1;
        }
        else{
            answer[1] +=1;
        }
    })
    return answer;
}