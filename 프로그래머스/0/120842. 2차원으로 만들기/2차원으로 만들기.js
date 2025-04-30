function solution(num_list, n) {
    var answer = [];
    for (let i=0; i<num_list.length/n; i++){
        answer.push([])
    }
    var cnt = 0;
    for (let i=0; i<num_list.length/n; i++){
        for (let j=0; j<n; j++){
            answer[i].push(num_list[cnt]);
            cnt +=1
        } 
             
    }
    return answer;
}