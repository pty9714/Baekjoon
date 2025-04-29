function solution(my_string) {
    var answer = '';
    var arr = my_string.split('');
    for (let i=0; i<arr.length; i++){
        arr[i] = arr[i].toLowerCase();
    }
    arr.sort();
    answer = arr.join('');
    return answer;
}