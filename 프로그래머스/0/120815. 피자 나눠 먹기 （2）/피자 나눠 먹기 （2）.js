function solution(n) {
    
    let lcm = 1;
   
    while(true){
      if((lcm % n == 0) && (lcm % 6 == 0)){
        break;
      }
      lcm++;
    }
    console.log(lcm);
    
    return lcm/6;
}