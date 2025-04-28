function solution(my_string, letter) {
    var answer = '';
    for(const c in my_string){
        
        if (my_string[c] !=letter){
            answer = answer+my_string[c];
        }
    }
    

    return answer;
}