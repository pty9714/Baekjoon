function solution(numbers, direction) {

    if (direction == "right"){
        var n = numbers.pop();
        numbers.unshift(n)
    }
    else {
        var n = numbers.shift();
        numbers.push(n)
    }
    return numbers;
}