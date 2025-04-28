function solution(array, height) {
    var answer = 0;
    array.forEach((element) =>{
        if (element>height){
            answer +=1 
        }
    })
    return answer;
}